"""
---
title: "Objects - Ontology Labels"
slug: "sdk-ref-objects-ont-labels"
hidden: false
metadata:
  title: "Objects - Ontology Labels"
  description: "Encord SDK Objects - Ontology Labels."
category: "64e481b57b6027003f20aaa0"
---
"""

from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Type, Union

from encord.client import EncordClientProject
from encord.client import LabelRow as OrmLabelRow
from encord.constants.enums import DataType
from encord.exceptions import LabelRowError, WrongProjectTypeError
from encord.http.bundle import Bundle, BundleResultHandler, BundleResultMapper, bundled_operation
from encord.http.limits import (
    LABEL_ROW_BUNDLE_CREATE_LIMIT,
    LABEL_ROW_BUNDLE_GET_LIMIT,
)
from encord.objects.attributes import Attribute
from encord.objects.bundled_operations import (
    BundledCreateRowsPayload,
    BundledGetRowsPayload,
    BundledSaveRowsPayload,
    BundledSetPriorityPayload,
    BundledWorkflowCompletePayload,
    BundledWorkflowReopenPayload,
)
from encord.objects.classification import Classification
from encord.objects.classification_instance import ClassificationInstance
from encord.objects.constants import (  # pylint: disable=unused-import # for backward compatibility
    DATETIME_LONG_STRING_FORMAT,
    DEFAULT_CONFIDENCE,
    DEFAULT_MANUAL_ANNOTATION,
)
from encord.objects.coordinates import (
    BitmaskCoordinates,
    BoundingBoxCoordinates,
    Coordinates,
    PointCoordinate,
    PolygonCoordinates,
    PolylineCoordinates,
    RotatableBoundingBoxCoordinates,
    SkeletonCoordinates,
)
from encord.objects.frames import Frames, frames_class_to_frames_list, frames_to_ranges
from encord.objects.metadata import DICOMSeriesMetadata, DICOMSliceMetadata
from encord.objects.ontology_object import Object
from encord.objects.ontology_object_instance import ObjectInstance
from encord.objects.ontology_structure import OntologyStructure
from encord.objects.utils import _lower_snake_case
from encord.ontology import Ontology
from encord.orm.label_row import (
    AnnotationTaskStatus,
    LabelRowMetadata,
    LabelStatus,
    WorkflowGraphNode,
)

log = logging.getLogger(__name__)

OntologyTypes = Union[Type[Object], Type[Classification]]
OntologyClasses = Union[Object, Classification]


class LabelRowV2:
    """
    This class represents a single label row. It is corresponding to exactly one data row within a project. It holds all
    the labels for that data row.

    You can access a many metadata fields with this class directly. If you want to read or write labels you will need to
    call :meth:`.initialise_labels()` first. To upload your added labels call :meth:`.save()`.
    """

    def __init__(
        self,
        label_row_metadata: LabelRowMetadata,
        project_client: EncordClientProject,
        ontology: Ontology,
    ) -> None:
        self._project_client = project_client
        self._ontology = ontology

        self._label_row_read_only_data: LabelRowV2.LabelRowReadOnlyData = self._parse_label_row_metadata(
            label_row_metadata
        )

        self._is_labelling_initialised = False

        self._frame_to_hashes: defaultdict[int, Set[str]] = defaultdict(set)
        # ^ frames to object and classification hashes

        self._metadata: Optional[DICOMSeriesMetadata] = None
        self._frame_metadata: defaultdict[int, Optional[DICOMSliceMetadata]] = defaultdict(lambda: None)

        self._classifications_to_frames: defaultdict[Classification, Set[int]] = defaultdict(set)

        self._objects_map: Dict[str, ObjectInstance] = dict()
        self._classifications_map: Dict[str, ClassificationInstance] = dict()
        # ^ conveniently a dict is ordered in Python. Use this to our advantage to keep the labels in order
        # at least at the final objects_index/classifications_index level.

    @property
    def label_hash(self) -> Optional[str]:
        return self._label_row_read_only_data.label_hash

    @property
    def branch_name(self) -> str:
        return self._label_row_read_only_data.branch_name

    @property
    def data_hash(self) -> str:
        return self._label_row_read_only_data.data_hash

    @property
    def dataset_hash(self) -> str:
        return self._label_row_read_only_data.dataset_hash

    @property
    def dataset_title(self) -> str:
        return self._label_row_read_only_data.dataset_title

    @property
    def data_title(self) -> str:
        return self._label_row_read_only_data.data_title

    @property
    def data_type(self) -> DataType:
        return self._label_row_read_only_data.data_type

    @property
    def file_type(self) -> str | None:
        return self._label_row_read_only_data.file_type

    @property
    def client_metadata(self) -> dict | None:
        return self._label_row_read_only_data.client_metadata

    @property
    def label_status(self) -> LabelStatus:
        """
        Returns the current labeling status for the label row.

        **Note**: This method is not supported for workflow-based projects. Please see our
        :ref:`workflow documentation <tutorials/workflows:Workflows>`
        for more details.
        """

        if self.__is_tms2_project:
            raise WrongProjectTypeError(
                '"label_status" property returns incorrect results for workflow-based projects.\
             Please use "workflow_graph_node" property instead.'
            )

        return self._label_row_read_only_data.label_status

    @property
    def annotation_task_status(self) -> AnnotationTaskStatus:
        """
        Returns the current annotation task status for the label row.

        **Note**: This method is not supported for workflow-based projects. Please see our
        :ref:`workflow documentation <tutorials/workflows:Workflows>`
        for more details.
        """
        if self.__is_tms2_project:
            raise WrongProjectTypeError(
                '"annotation_task_status" property returns incorrect results for workflow-based projects.\
             Please use "workflow_graph_node" property instead.'
            )

        assert self._label_row_read_only_data.annotation_task_status is not None  # Never None for Workflow projects

        return self._label_row_read_only_data.annotation_task_status

    @property
    def workflow_graph_node(self) -> Optional[WorkflowGraphNode]:
        return self._label_row_read_only_data.workflow_graph_node

    @property
    def is_shadow_data(self) -> bool:
        return self._label_row_read_only_data.is_shadow_data

    @property
    def created_at(self) -> Optional[datetime]:
        """The creation date of the label row. None if the label row was not yet created."""
        return self._label_row_read_only_data.created_at

    @property
    def last_edited_at(self) -> Optional[datetime]:
        """The time the label row was updated last as a whole. None if the label row was not yet created."""
        return self._label_row_read_only_data.last_edited_at

    @property
    def number_of_frames(self) -> int:
        return self._label_row_read_only_data.number_of_frames

    @property
    def duration(self) -> Optional[float]:
        """Only a value for Video data types."""
        return self._label_row_read_only_data.duration

    @property
    def fps(self) -> Optional[float]:
        """Only a value for Video data types."""
        return self._label_row_read_only_data.fps

    @property
    def data_link(self) -> Optional[str]:
        """
        The data link in either your cloud storage or the encord storage to the underlying object. This will be `None`
        for DICOM series or image groups that have been created without performance optimisations, as there is no
        single underlying file for these data types.

        This property will contain signed url if :meth:`.initialise_labels` was called with `include_signed_url=True`.
        """
        return self._label_row_read_only_data.data_link

    @property
    def width(self) -> Optional[int]:
        """
        This is `None` for image groups without performance optimisation, as there is no single underlying width
        for this data type.
        """
        return self._label_row_read_only_data.width

    @property
    def height(self) -> Optional[int]:
        """
        This is `None` for image groups without performance optimisation, as there is no single underlying width
        for this data type.
        """
        return self._label_row_read_only_data.height

    @property
    def priority(self) -> Optional[float]:
        """
        Get workflow priority for the task associated with the data unit.

        This property only works for workflow-based project.

        It is None for label rows in "complete" state.
        """
        if not self.__is_tms2_project:
            raise WrongProjectTypeError('"priority" property only works with workflow-based projects.')

        return self._label_row_read_only_data.priority

    @property
    def is_valid(self) -> bool:
        """
        For labels uploaded via the SDK, a check is run to ensure that the labels are valid.
        This property returns `True` if the labels have correct structure and match the project ontology.

        If it is `False`, then loading the labels via `LabelRowV2` will raise an error, and the label editor
        will not be able to load the labels.

        You can call :meth`.get_validation_errors` to get the validation error messages.
        """
        return self._label_row_read_only_data.is_valid

    @property
    def ontology_structure(self) -> OntologyStructure:
        """Get the corresponding ontology structure"""
        return self._ontology.structure

    @property
    def is_labelling_initialised(self) -> bool:
        """
        Whether you can start labelling or not. If this is `False`, call the member :meth:`.initialise_labels()` to
        read or write specific ObjectInstances or ClassificationInstances.
        """
        return self._is_labelling_initialised

    @property
    def __is_tms2_project(self) -> bool:
        return self.workflow_graph_node is not None

    def initialise_labels(
        self,
        include_object_feature_hashes: Optional[Set[str]] = None,
        include_classification_feature_hashes: Optional[Set[str]] = None,
        include_reviews: bool = False,
        overwrite: bool = False,
        bundle: Optional[Bundle] = None,
        *,
        include_signed_url: bool = False,
    ) -> None:
        """
        Call this function to download or export labels stored on the Encord server, as well as to perform any other
        reading or writing operations. If you only want to inspect a subset of labels, you can filter them.
        Please note that if you filter the labels, and upload them later, you will effectively delete all the labels
        that were previously filtered.

        If the label was not yet in progress, this will set the label status to `LabelStatus.LABEL_IN_PROGRESS`.

        You can call this function at any point to overwrite the current labels stored in this class with the most
        up to date labels stored in the Encord servers. This would only matter if you manipulate the labels while
        someone else is working on the labels as well. You would need to supply the `overwrite` parameter to `True`

        Args:
            include_object_feature_hashes: If None all the objects will be included. Otherwise, only objects labels
                will be included of which the feature_hash has been added. WARNING: it is only recommended to use
                this filter if you are reading (not writing) the labels. If you are requesting a subset of objects and
                later, save the label, you will effectively delete all the object instances that are stored in the
                Encord platform, which were not included in this filtered subset.
            include_classification_feature_hashes: If None all the classifications will be included. Otherwise, only
                classification labels will be included of which the feature_hash has been added. WARNING: it is only
                recommended to use this filter if you are reading (not writing) the labels. If you are requesting a
                subset of classifications and later, save the label, you will effectively delete all the
                classification instances that are stored in the Encord platform, which were not included in this
                filtered subset.
            include_reviews: Whether to request read only information about the reviews of the label row.
            overwrite: If the label row was already initialised, you need to set this flag to `True` to overwrite the
                current labels with the labels stored in the Encord server. If this is `False` and the label row was
                already initialised, this function will throw an error.
            bundle: If not passed, initialisation is performed independently. If passed, it will be delayed and
                initialised along with other objects in the same bundle.
            include_signed_url: if set to true, :attr:`.data_link` property will contain signed url.
                See documentation for :attr:`.data_link` for more details.
        """
        if self.is_labelling_initialised and not overwrite:
            raise LabelRowError(
                "You are trying to re-initialise a label row that has already been initialised. This would overwrite "
                "current labels. If this is your intend, set the `overwrite` flag to `True`."
            )

        if not self.label_hash:
            # If label_hash is None, it means we need to explicitly create the label row first
            bundled_operation(
                bundle,
                operation=self._project_client.create_label_rows,
                payload=BundledCreateRowsPayload(
                    uids=[self.data_hash],
                    get_signed_url=include_signed_url,
                ),
                result_mapper=BundleResultMapper[OrmLabelRow](
                    result_mapping_predicate=lambda r: r["data_hash"],
                    result_handler=BundleResultHandler(predicate=self.data_hash, handler=self.from_labels_dict),
                ),
                limit=LABEL_ROW_BUNDLE_CREATE_LIMIT,
            )
        else:
            bundled_operation(
                bundle,
                operation=self._project_client.get_label_rows,
                payload=BundledGetRowsPayload(
                    uids=[self.label_hash],
                    get_signed_url=include_signed_url,
                    include_object_feature_hashes=include_object_feature_hashes,
                    include_classification_feature_hashes=include_classification_feature_hashes,
                    include_reviews=include_reviews,
                ),
                result_mapper=BundleResultMapper[OrmLabelRow](
                    result_mapping_predicate=lambda r: r["label_hash"],
                    result_handler=BundleResultHandler(predicate=self.label_hash, handler=self.from_labels_dict),
                ),
                limit=LABEL_ROW_BUNDLE_GET_LIMIT,
            )

    def from_labels_dict(self, label_row_dict: dict) -> None:
        """
        If you have a label row dictionary in the same format that the Encord servers produce, you can initialise the
        LabelRow from that directly. In most cases you should prefer using the `initialise_labels` method.

        This function also initialises the label row.

        Calling this function will reset all the labels that are currently stored within this class.

        Args:
            label_row_dict: The dictionary of all labels as expected by the Encord format.
        """
        self._is_labelling_initialised = True

        self._label_row_read_only_data = self._parse_label_row_dict(label_row_dict)
        self._frame_to_hashes = defaultdict(set)
        self._classifications_to_frames = defaultdict(set)

        self._metadata = None
        self._frame_metadata = defaultdict(lambda: None)

        self._objects_map = dict()
        self._classifications_map = dict()
        self._parse_labels_from_dict(label_row_dict)

    def get_image_hash(self, frame_number: int) -> Optional[str]:
        """
        Get the corresponding image hash of the frame number. Return `None` if the frame number is out of bounds.
        Raise an error if this function is used for non-image data types.
        """
        self._check_labelling_is_initalised()

        if self.data_type not in (DataType.IMAGE, DataType.IMG_GROUP):
            raise LabelRowError("This function is only supported for label rows of image or image group data types.")

        return self._label_row_read_only_data.frame_to_image_hash.get(frame_number)

    def get_frame_number(self, image_hash: str) -> Optional[int]:
        """
        Get the corresponding image hash of the frame number. Return `None` if the image hash was not found with an
        associated frame number.
        Raise an error if this function is used for non-image data types.
        """
        self._check_labelling_is_initalised()

        if self.data_type not in (DataType.IMAGE, DataType.IMG_GROUP):
            raise LabelRowError("This function is only supported for label rows of image or image group data types.")
        return self._label_row_read_only_data.image_hash_to_frame[image_hash]

    def save(self, bundle: Optional[Bundle] = None, validate_before_saving: bool = False) -> None:
        """
        Upload the created labels with the Encord server. This will overwrite any labels that someone has created
        in the platform in the meantime.

        Args:
            bundle: if not passed, save is executed immediately. If passed, it is executed as a part of the bundle
            validate_before_saving: enable stricter server-side integrity checks. Boolean, `False` by default.

        """
        self._check_labelling_is_initalised()
        assert self.label_hash is not None  # Checked earlier, assert is just to silence mypy

        bundled_operation(
            bundle,
            self._project_client.save_label_rows,
            payload=BundledSaveRowsPayload(
                uids=[self.label_hash], payload=[self.to_encord_dict()], validate_before_saving=validate_before_saving
            ),
        )

    @property
    def metadata(self) -> Optional[DICOMSeriesMetadata]:
        """
        Metadata for the given data type.
        Currently only supported for DICOM, and will return `None` for other formats.

        Label row needs to be initialised before using this property
        """
        self._check_labelling_is_initalised()
        return self._metadata

    def get_frame_view(self, frame: Union[int, str] = 0) -> FrameView:
        """
        Args:
            frame: Either the frame number or the image hash if the data type is an image or image group.
                Defaults to the first frame.
        """
        self._check_labelling_is_initalised()
        if isinstance(frame, str):
            frame_num = self.get_frame_number(frame)
            if frame_num is None:
                raise LabelRowError(f"Image hash {frame} not found in the label row")
        else:
            frame_num = frame

        return self.FrameView(self, self._label_row_read_only_data, frame_num)

    def _get_frame_metadata_list(self) -> List[LabelRowReadOnlyDataImagesDataEntry]:
        if self._label_row_read_only_data.data_type in [DataType.IMAGE, DataType.VIDEO]:
            return [
                self.LabelRowReadOnlyDataImagesDataEntry(
                    index=0,
                    title=self._label_row_read_only_data.data_title,
                    file_type=self._label_row_read_only_data.file_type or "",
                    height=self._label_row_read_only_data.height or 0,
                    width=self._label_row_read_only_data.width or 0,
                    image_hash=self._label_row_read_only_data.data_hash,
                )
            ]

        images_data = self._label_row_read_only_data.images_data
        if images_data is None:
            raise LabelRowError("Image data is not present in the label row")
        return images_data

    def get_frame_metadata(self, frame: Union[int, str] = 0) -> FrameViewMetadata:
        """
        Get image group metadata for frame or image hash.
        """
        images_data = self._get_frame_metadata_list()
        if isinstance(frame, str):
            data_meta = None
            for data in images_data:
                if data.image_hash == frame:
                    data_meta = data
                    break
            if data_meta is None:
                raise LabelRowError(f"Image hash {frame} not found in the label row")
        else:
            data_meta = None
            for data in images_data:
                if data.index == frame:
                    data_meta = data
                    break
            if data_meta is None:
                raise LabelRowError(f"Frame {frame} not found in the label row")

        return self.FrameViewMetadata(data_meta)

    def get_frames_metadata(self) -> List[FrameViewMetadata]:
        """
        Get image metadata for image group if requested.
        """
        views = []

        images_data = self._get_frame_metadata_list()

        for data in images_data:
            views.append(self.FrameViewMetadata(data))
        return views

    def get_frame_views(self) -> List[FrameView]:
        """
        Returns:
            A list of frame views in order of available frames.
        """
        self._check_labelling_is_initalised()
        ret = []
        for frame in range(self.number_of_frames):
            ret.append(self.get_frame_view(frame))
        return ret

    def get_object_instances(
        self, filter_ontology_object: Optional[Object] = None, filter_frames: Optional[Frames] = None
    ) -> List[ObjectInstance]:
        """
        Args:
            filter_ontology_object:
                Optionally filter by a specific ontology object.
            filter_frames:
                Optionally filter by specific frames.

        Returns:
            All the `ObjectInstance`s that match the filter.
        """
        self._check_labelling_is_initalised()

        ret: List[ObjectInstance] = list()

        if filter_frames is not None:
            filtered_frames_list = frames_class_to_frames_list(filter_frames)
        else:
            filtered_frames_list = list()

        for object_ in self._objects_map.values():
            # filter by ontology object
            if not (
                filter_ontology_object is None
                or object_.ontology_item.feature_node_hash == filter_ontology_object.feature_node_hash
            ):
                continue

            # filter by frame
            if filter_frames is None:
                append = True
            else:
                append = False
            for frame in filtered_frames_list:
                hashes = self._frame_to_hashes.get(frame, set())
                if object_.object_hash in hashes:
                    append = True
                    break

            if append:
                ret.append(object_)

        return ret

    def add_object_instance(self, object_instance: ObjectInstance, force: bool = True) -> None:
        """
        Add an object instance to the label row. If the object instance already exists, it overwrites the current instance

        Args:
            object_instance: The object instance to add.
            force: overwrites current objects, otherwise this will replace the current object.
        """
        self._check_labelling_is_initalised()

        object_instance.is_valid()

        if object_instance.is_assigned_to_label_row():
            raise LabelRowError(
                "The supplied ObjectInstance is already part of a LabelRowV2. You can only add a ObjectInstance to one "
                "LabelRowV2. You can do a ObjectInstance.copy() to create an identical ObjectInstance which is not part of "
                "any LabelRowV2."
            )

        object_hash = object_instance.object_hash
        if object_hash in self._objects_map and not force:
            raise LabelRowError(
                "The supplied ObjectInstance was already previously added. (the object_hash is the same)."
            )
        elif object_hash in self._objects_map and force:
            self._objects_map.pop(object_hash)

        self._objects_map[object_hash] = object_instance
        object_instance._parent = self

        frames = set(_frame_views_to_frame_numbers(object_instance.get_annotations()))
        self._add_to_frame_to_hashes_map(object_instance, frames)

    def add_classification_instance(self, classification_instance: ClassificationInstance, force: bool = False) -> None:
        """
        Add a classification instance to the label row.

        Args:
            classification_instance: The object instance to add.
            force: overwrites current objects, otherwise this will replace the current object.
        """
        self._check_labelling_is_initalised()

        classification_instance.is_valid()

        if classification_instance.is_assigned_to_label_row():
            raise LabelRowError(
                "Provided ClassificationInstance object is already attached to a different LabelRowV2 object. "
                "You can only add a ClassificationInstance to one label row. "
                "You can do a ClassificationInstance.copy() to create an identical ClassificationInstance which is not part of any label row."
            )

        classification_hash = classification_instance.classification_hash
        frames = set(_frame_views_to_frame_numbers(classification_instance.get_annotations()))
        already_present_frames = self._is_classification_already_present(
            classification_instance.ontology_item,
            frames,
        )
        if classification_hash in self._classifications_map and not force:
            raise LabelRowError(
                f"A ClassificationInstance for classification hash '{classification_hash}' already exists on the label row object. "
                f"Pass 'force=True' to override it."
            )

        if already_present_frames and not force:
            raise LabelRowError(
                f"A ClassificationInstance '{classification_hash}' was already added and has overlapping frames. "
                f"Overlapping frames that were found are `{frames_to_ranges(already_present_frames)}`. "
                f"Make sure that you only add classifications which are on frames where the same type of "
                f"classification does not yet exist."
            )

        if classification_hash in self._classifications_map and force:
            self._classifications_map.pop(classification_hash)

        self._classifications_map[classification_hash] = classification_instance
        classification_instance._parent = self

        self._classifications_to_frames[classification_instance.ontology_item].update(frames)
        self._add_to_frame_to_hashes_map(classification_instance, frames)

    def remove_classification(self, classification_instance: ClassificationInstance):
        """Remove a classification instance from a label row."""
        self._check_labelling_is_initalised()

        classification_hash = classification_instance.classification_hash
        self._classifications_map.pop(classification_hash)
        all_frames = self._classifications_to_frames[classification_instance.ontology_item]
        actual_frames = _frame_views_to_frame_numbers(classification_instance.get_annotations())
        for actual_frame in actual_frames:
            all_frames.remove(actual_frame)

    def add_to_single_frame_to_hashes_map(
        self, label_item: Union[ObjectInstance, ClassificationInstance], frame: int
    ) -> None:
        """This is an internal function, it is not meant to be called by the SDK user."""
        self._check_labelling_is_initalised()

        if isinstance(label_item, ObjectInstance):
            self._frame_to_hashes[frame].add(label_item.object_hash)
        elif isinstance(label_item, ClassificationInstance):
            self._frame_to_hashes[frame].add(label_item.classification_hash)
        else:
            raise NotImplementedError(f"Got an unexpected label item class `{type(label_item)}`")

    def get_classification_instances(
        self, filter_ontology_classification: Optional[Classification] = None, filter_frames: Optional[Frames] = None
    ) -> List[ClassificationInstance]:
        """
        Args:
            filter_ontology_classification:
                Optionally filter by a specific ontology classification.
            filter_frames:
                Optionally filter by specific frames.

        Returns:
            All the `ObjectInstance`s that match the filter.
        """
        self._check_labelling_is_initalised()

        ret: List[ClassificationInstance] = list()

        if filter_frames is not None:
            filtered_frames_list = frames_class_to_frames_list(filter_frames)
        else:
            filtered_frames_list = list()

        for classification in self._classifications_map.values():
            # filter by ontology object
            if not (
                filter_ontology_classification is None
                or classification.ontology_item.feature_node_hash == filter_ontology_classification.feature_node_hash
            ):
                continue

            # filter by frame
            if filter_frames is None:
                append = True
            else:
                append = False
            for frame in filtered_frames_list:
                hashes = self._frame_to_hashes.get(frame, set())
                if classification.classification_hash in hashes:
                    append = True
                    break

            if append:
                ret.append(classification)
        return ret

    def remove_object(self, object_instance: ObjectInstance):
        """Remove an object instance from a label row."""
        self._check_labelling_is_initalised()

        self._objects_map.pop(object_instance.object_hash)
        self._remove_from_frame_to_hashes_map(
            _frame_views_to_frame_numbers(object_instance.get_annotations()), object_instance.object_hash
        )
        object_instance._parent = None

    def to_encord_dict(self) -> Dict[str, Any]:
        """
        This is an internal helper function. Likely this should not be used by a user. To upload labels use the
        :meth:`.save()` function.
        """
        self._check_labelling_is_initalised()

        ret: Dict[str, Any] = {}
        read_only_data = self._label_row_read_only_data

        ret["label_hash"] = read_only_data.label_hash
        ret["branch_name"] = read_only_data.branch_name
        ret["created_at"] = read_only_data.created_at
        ret["last_edited_at"] = read_only_data.last_edited_at
        ret["data_hash"] = read_only_data.data_hash
        ret["dataset_hash"] = read_only_data.dataset_hash
        ret["dataset_title"] = read_only_data.dataset_title
        ret["data_title"] = read_only_data.data_title
        ret["data_type"] = read_only_data.data_type.value
        ret["annotation_task_status"] = read_only_data.annotation_task_status
        ret["is_shadow_data"] = read_only_data.is_shadow_data
        ret["object_answers"] = self._to_object_answers()
        ret["classification_answers"] = self._to_classification_answers()
        ret["object_actions"] = self._to_object_actions()
        ret["label_status"] = read_only_data.label_status.value
        ret["data_units"] = self._to_encord_data_units()

        return ret

    def workflow_reopen(self, bundle: Optional[Bundle] = None) -> None:
        """
        A label row is returned to the first annotation stage for re-labeling.
        No data will be lost during this call.

        This method is only relevant for the projects that use the :ref:`Workflow <tutorials/workflows:Workflows>`
        feature, and will raise an error for pre-workflow projects.
        """
        if self.label_hash is None:
            # Label has not yet moved from the initial state, nothing to do
            return

        bundled_operation(
            bundle,
            self._project_client.workflow_reopen,
            payload=BundledWorkflowReopenPayload(label_hashes=[self.label_hash]),
        )

    def workflow_complete(self, bundle: Optional[Bundle] = None) -> None:
        """
         A label row is moved to the final workflow node, marking it as 'Complete'.

         This method can be called only for labels for which :meth:`.initialise_labels()` was called at least ance, and
         consequentially the "label_hash" field is not `None`.
        Please note that labels need not be initialised every time the workflow_complete() method is called.

         This method is only relevant for the projects that use the :ref:`Workflow <tutorials/workflows:Workflows>`
         feature, and will raise an error for projects that don't use Workflows.
        """
        if self.label_hash is None:
            raise LabelRowError(
                "For this operation you will need to initialise labelling first. Call the .initialise_labels() "
                "to do so first."
            )

        bundled_operation(
            bundle,
            self._project_client.workflow_complete,
            payload=BundledWorkflowCompletePayload(label_hashes=[self.label_hash]),
        )

    def set_priority(self, priority: float, bundle: Optional[Bundle] = None) -> None:
        """
        Set priority for task in workflow project.

        Args:
            priority: float value from 0.0 to 1.0, where 1.0 is the highest priority
            bundle: optional parameter. If passed, the method will be executed in a deferred way as part of the bundle.
        """
        if not self.__is_tms2_project:
            raise WrongProjectTypeError("Setting priority only possible for workflow-based projects")

        bundled_operation(
            bundle,
            self._project_client.workflow_set_priority,
            payload=BundledSetPriorityPayload(priorities=[(self.data_hash, priority)]),
        )

    def get_validation_errors(self) -> List[str] | None:
        """
        Get validation errors for the label row (list of error messages).

        If the label row is valid, this will return `None`.
        """
        if not self.label_hash or self.is_valid:
            return None

        return self._project_client.get_label_validation_errors(self.label_hash)

    class FrameViewMetadata:
        """
        This class can be used to inspect what metadata for a frame view
        """

        def __init__(self, images_data: LabelRowV2.LabelRowReadOnlyDataImagesDataEntry):
            self._image_data = images_data

        @property
        def title(self) -> str:
            return self._image_data.title

        @property
        def file_type(self) -> str:
            return self._image_data.file_type

        @property
        def width(self) -> int:
            return self._image_data.width

        @property
        def height(self) -> int:
            return self._image_data.height

        @property
        def image_hash(self) -> str:
            return self._image_data.image_hash

        @property
        def frame_number(self) -> int:
            return self._image_data.index

    class FrameView:
        """
        This class can be used to inspect what object/classification instances are on a given frame or
        what metadata, such as a image file size, is on a given frame.
        """

        def __init__(
            self, label_row: LabelRowV2, label_row_read_only_data: LabelRowV2.LabelRowReadOnlyData, frame: int
        ):
            self._label_row = label_row
            self._label_row_read_only_data = label_row_read_only_data
            self._frame = frame

        @property
        def image_hash(self) -> str:
            if self._label_row.data_type not in [DataType.IMAGE, DataType.IMG_GROUP]:
                raise LabelRowError("Image hash can only be retrieved for DataType.IMAGE or DataType.IMG_GROUP")
            return self._frame_level_data().image_hash

        @property
        def image_title(self) -> str:
            if self._label_row.data_type not in [DataType.IMAGE, DataType.IMG_GROUP]:
                raise LabelRowError("Image title can only be retrieved for DataType.IMAGE or DataType.IMG_GROUP")
            return self._frame_level_data().image_title

        @property
        def file_type(self) -> str:
            if self._label_row.data_type not in [DataType.IMAGE, DataType.IMG_GROUP]:
                raise LabelRowError("File type can only be retrieved for DataType.IMAGE or DataType.IMG_GROUP")
            return self._frame_level_data().file_type

        @property
        def frame(self) -> int:
            return self._frame

        @property
        def width(self) -> int:
            if self._label_row.data_type in [DataType.IMG_GROUP]:
                return self._frame_level_data().width
            elif self._label_row_read_only_data.width is not None:
                return self._label_row_read_only_data.width
            else:
                raise LabelRowError(f"Width is expected but not set for the data type {self._label_row.data_type}")

        @property
        def height(self) -> int:
            if self._label_row.data_type in [DataType.IMG_GROUP]:
                return self._frame_level_data().height
            elif self._label_row_read_only_data.height is not None:
                return self._label_row_read_only_data.height
            else:
                raise LabelRowError(f"Height is expected but not set for the data type {self._label_row.data_type}")

        @property
        def data_link(self) -> Optional[str]:
            if self._label_row.data_type not in [DataType.IMAGE, DataType.IMG_GROUP]:
                raise LabelRowError("Data link can only be retrieved for DataType.IMAGE or DataType.IMG_GROUP")
            return self._frame_level_data().data_link

        @property
        def metadata(self) -> Optional[DICOMSliceMetadata]:
            """
            Annotation metadata.
            Particular format depends on the data type.
            Currently only supported for DICOM, and will return `None` for other formats.
            """
            return self._label_row._frame_metadata[self._frame]

        def add_object_instance(
            self,
            object_instance: ObjectInstance,
            coordinates: Coordinates,
            *,
            overwrite: bool = False,
            created_at: Optional[datetime] = None,
            created_by: Optional[str] = None,
            last_edited_at: Optional[datetime] = None,
            last_edited_by: Optional[str] = None,
            confidence: Optional[float] = None,
            manual_annotation: Optional[bool] = None,
        ) -> None:
            label_row = object_instance.is_assigned_to_label_row()
            if label_row and self._label_row != label_row:
                raise LabelRowError(
                    "This object instance is already assigned to a different label row. It can not be "
                    "added to multiple label rows at once."
                )

            object_instance.set_for_frames(
                coordinates,
                self._frame,
                overwrite=overwrite,
                created_at=created_at,
                created_by=created_by,
                last_edited_at=last_edited_at,
                last_edited_by=last_edited_by,
                confidence=confidence,
                manual_annotation=manual_annotation,
            )

            if not label_row:
                self._label_row.add_object_instance(object_instance)

        def add_classification_instance(
            self,
            classification_instance: ClassificationInstance,
            *,
            overwrite: bool = False,
            created_at: Optional[datetime] = None,
            created_by: Optional[str] = None,
            confidence: float = DEFAULT_CONFIDENCE,
            manual_annotation: bool = DEFAULT_MANUAL_ANNOTATION,
            last_edited_at: Optional[datetime] = None,
            last_edited_by: Optional[str] = None,
        ) -> None:
            if created_at is None:
                created_at = datetime.now()

            if last_edited_at is None:
                last_edited_at = datetime.now()

            label_row = classification_instance.is_assigned_to_label_row()
            if label_row and self._label_row != label_row:
                raise LabelRowError(
                    "This object instance is already assigned to a different label row. It can not be "
                    "added to multiple label rows at once."
                )

            classification_instance.set_for_frames(
                self._frame,
                overwrite=overwrite,
                created_at=created_at,
                created_by=created_by,
                confidence=confidence,
                manual_annotation=manual_annotation,
                last_edited_at=last_edited_at,
                last_edited_by=last_edited_by,
            )

            if not label_row:
                self._label_row.add_classification_instance(classification_instance)

        def get_object_instances(self, filter_ontology_object: Optional[Object] = None) -> List[ObjectInstance]:
            """
            Args:
                filter_ontology_object:
                    Optionally filter by a specific ontology object.

            Returns:
                All the `ObjectInstance`s that match the filter.
            """
            return self._label_row.get_object_instances(
                filter_ontology_object=filter_ontology_object, filter_frames=self._frame
            )

        def get_classification_instances(
            self, filter_ontology_classification: Optional[Classification] = None
        ) -> List[ClassificationInstance]:
            """
            Args:
                filter_ontology_classification:
                    Optionally filter by a specific ontology object.

            Returns:
                All the `ObjectInstance`s that match the filter.
            """
            return self._label_row.get_classification_instances(
                filter_ontology_classification=filter_ontology_classification, filter_frames=self._frame
            )

        def _frame_level_data(self) -> LabelRowV2.FrameLevelImageGroupData:
            return self._label_row_read_only_data.frame_level_data[self._frame]

        def __repr__(self):
            return f"FrameView(label_row={self._label_row}, frame={self._frame})"

    @dataclass(frozen=True)
    class FrameLevelImageGroupData:
        """This is an internal helper class. A user should not directly interact with it."""

        image_hash: str
        image_title: str
        file_type: str
        frame_number: int
        width: int
        height: int
        data_link: Optional[str] = None

    @dataclass(frozen=True)
    class LabelRowReadOnlyDataImagesDataEntry:
        index: int
        title: str
        file_type: str
        height: int
        width: int
        image_hash: str

    @dataclass(frozen=True)
    class LabelRowReadOnlyData:
        """This is an internal helper class. A user should not directly interact with it."""

        label_hash: Optional[str]
        """This is None if the label row does not have any labels and was not initialised for labelling."""
        created_at: Optional[datetime]
        """This is None if the label row does not have any labels and was not initialised for labelling."""
        last_edited_at: Optional[datetime]
        """This is None if the label row does not have any labels and was not initialised for labelling."""
        data_hash: str
        data_type: DataType
        label_status: LabelStatus
        annotation_task_status: Optional[AnnotationTaskStatus]
        workflow_graph_node: Optional[WorkflowGraphNode]
        is_shadow_data: bool
        number_of_frames: int
        duration: Optional[float]
        fps: Optional[float]
        dataset_hash: str
        dataset_title: str
        data_title: str
        width: Optional[int]
        height: Optional[int]
        data_link: Optional[str]
        priority: Optional[float]
        file_type: Optional[str]
        client_metadata: Optional[dict]
        images_data: Optional[List[LabelRowV2.LabelRowReadOnlyDataImagesDataEntry]]
        branch_name: str
        frame_level_data: Dict[int, LabelRowV2.FrameLevelImageGroupData] = field(default_factory=dict)
        image_hash_to_frame: Dict[str, int] = field(default_factory=dict)
        frame_to_image_hash: Dict[int, str] = field(default_factory=dict)
        is_valid: bool = field(default=True)

    def _to_object_answers(self) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}
        for obj in self._objects_map.values():
            all_static_answers = self._get_all_static_answers(obj)
            ret[obj.object_hash] = {
                "classifications": list(reversed(all_static_answers)),
                "objectHash": obj.object_hash,
            }
        return ret

    def _to_object_actions(self) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}
        for obj in self._objects_map.values():
            all_static_answers = self._dynamic_answers_to_encord_dict(obj)
            if len(all_static_answers) == 0:
                continue
            ret[obj.object_hash] = {
                "actions": list(reversed(all_static_answers)),
                "objectHash": obj.object_hash,
            }
        return ret

    def _to_classification_answers(self) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}
        for classification in self._classifications_map.values():
            all_static_answers = classification.get_all_static_answers()
            classifications = [answer.to_encord_dict() for answer in all_static_answers if answer.is_answered()]
            ret[classification.classification_hash] = {
                "classifications": list(reversed(classifications)),
                "classificationHash": classification.classification_hash,
            }
        return ret

    @staticmethod
    def _get_all_static_answers(object_instance: ObjectInstance) -> List[Dict[str, Any]]:
        """Essentially convert to the JSON format of all the static answers."""
        ret = []
        for answer in object_instance._get_all_static_answers():
            d_opt = answer.to_encord_dict()
            if d_opt is not None:
                ret.append(d_opt)
        return ret

    @staticmethod
    def _dynamic_answers_to_encord_dict(object_instance: ObjectInstance) -> List[Dict[str, Any]]:
        ret = []
        for answer, ranges in object_instance._get_all_dynamic_answers():
            d_opt = answer.to_encord_dict(ranges)
            if d_opt is not None:
                ret.append(d_opt)
        return ret

    def _to_encord_data_units(self) -> Dict[str, Any]:
        frame_level_data = self._label_row_read_only_data.frame_level_data
        return {value.image_hash: self._to_encord_data_unit(value) for value in frame_level_data.values()}

    def _to_encord_data_unit(self, frame_level_data: FrameLevelImageGroupData) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}

        data_type = self._label_row_read_only_data.data_type
        if data_type == DataType.IMG_GROUP:
            data_sequence: Union[str, int] = str(frame_level_data.frame_number)
        elif data_type in (DataType.VIDEO, DataType.DICOM, DataType.IMAGE):
            data_sequence = frame_level_data.frame_number
        else:
            raise NotImplementedError(f"The data type {data_type} is not implemented yet.")

        ret["data_hash"] = frame_level_data.image_hash
        ret["data_title"] = frame_level_data.image_title

        if data_type != DataType.DICOM:
            ret["data_link"] = frame_level_data.data_link

        ret["data_type"] = frame_level_data.file_type
        ret["data_sequence"] = data_sequence
        ret["width"] = frame_level_data.width
        ret["height"] = frame_level_data.height
        ret["labels"] = self._to_encord_labels(frame_level_data)

        if self._label_row_read_only_data.duration is not None:
            ret["data_duration"] = self._label_row_read_only_data.duration
        if self._label_row_read_only_data.fps is not None:
            ret["data_fps"] = self._label_row_read_only_data.fps

        return ret

    def _to_encord_labels(self, frame_level_data: FrameLevelImageGroupData) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}
        data_type = self._label_row_read_only_data.data_type

        if data_type in [DataType.IMAGE, DataType.IMG_GROUP]:
            frame = frame_level_data.frame_number
            ret.update(self._to_encord_label(frame))

        elif data_type in [DataType.VIDEO, DataType.DICOM]:
            for frame in self._frame_to_hashes.keys():
                ret[str(frame)] = self._to_encord_label(frame)

        return ret

    def _to_encord_label(self, frame: int) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}

        ret["objects"] = self._to_encord_objects_list(frame)
        ret["classifications"] = self._to_encord_classifications_list(frame)

        return ret

    def _to_encord_objects_list(self, frame: int) -> list:
        # Get objects for frame
        ret: List[dict] = []

        objects = self.get_object_instances(filter_frames=frame)
        for object_ in objects:
            encord_object = self._to_encord_object(object_, frame)
            ret.append(encord_object)
        return ret

    def _to_encord_object(
        self,
        object_: ObjectInstance,
        frame: int,
    ) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}

        object_instance_annotation = object_.get_annotation(frame)
        coordinates = object_instance_annotation.coordinates
        ontology_hash = object_.ontology_item.feature_node_hash
        ontology_object = self._ontology.structure.get_child_by_hash(ontology_hash, type_=Object)

        ret["name"] = ontology_object.name
        ret["color"] = ontology_object.color
        ret["shape"] = ontology_object.shape.value
        ret["value"] = _lower_snake_case(ontology_object.name)
        ret["createdAt"] = object_instance_annotation.created_at.strftime(DATETIME_LONG_STRING_FORMAT)
        ret["createdBy"] = object_instance_annotation.created_by
        ret["confidence"] = object_instance_annotation.confidence
        ret["objectHash"] = object_.object_hash
        ret["featureHash"] = ontology_object.feature_node_hash
        ret["manualAnnotation"] = object_instance_annotation.manual_annotation

        if object_instance_annotation.last_edited_at is not None:
            ret["lastEditedAt"] = object_instance_annotation.last_edited_at.strftime(DATETIME_LONG_STRING_FORMAT)
        if object_instance_annotation.last_edited_by is not None:
            ret["lastEditedBy"] = object_instance_annotation.last_edited_by
        if object_instance_annotation.is_deleted is not None:
            ret["isDeleted"] = object_instance_annotation.is_deleted

        self._add_coordinates_to_encord_object(coordinates, frame, ret)

        return ret

    def _add_coordinates_to_encord_object(
        self, coordinates: Coordinates, frame: int, encord_object: Dict[str, Any]
    ) -> None:
        if isinstance(coordinates, BoundingBoxCoordinates):
            encord_object["boundingBox"] = coordinates.to_dict()
        elif isinstance(coordinates, RotatableBoundingBoxCoordinates):
            encord_object["rotatableBoundingBox"] = coordinates.to_dict()
        elif isinstance(coordinates, PolygonCoordinates):
            encord_object["polygon"] = coordinates.to_dict()
        elif isinstance(coordinates, PolylineCoordinates):
            encord_object["polyline"] = coordinates.to_dict()
        elif isinstance(coordinates, PointCoordinate):
            encord_object["point"] = coordinates.to_dict()
        elif isinstance(coordinates, BitmaskCoordinates):
            frame_view = self.get_frame_view(frame)
            if not (
                frame_view.height == coordinates._encoded_bitmask.height
                and frame_view.width == coordinates._encoded_bitmask.width
            ):
                raise ValueError("Bitmask dimensions don't match the media dimensions")
            encord_object["bitmask"] = coordinates.to_dict()
        elif isinstance(coordinates, SkeletonCoordinates):
            encord_object["skeleton"] = coordinates.to_dict()
        else:
            raise NotImplementedError(f"adding coordinatees for this type not yet implemented {type(coordinates)}")

    def _to_encord_classifications_list(self, frame: int) -> list:
        ret: List[Dict[str, Any]] = []

        classifications = self.get_classification_instances(filter_frames=frame)
        for classification in classifications:
            encord_classification = self._to_encord_classification(classification, frame)
            ret.append(encord_classification)

        return ret

    def _to_encord_classification(self, classification: ClassificationInstance, frame: int) -> Dict[str, Any]:
        ret: Dict[str, Any] = {}

        annotation = classification.get_annotation(frame)
        classification_feature_hash = classification.ontology_item.feature_node_hash
        ontology_classification = self._ontology.structure.get_child_by_hash(
            classification_feature_hash, type_=Classification
        )
        attribute_hash = classification.ontology_item.attributes[0].feature_node_hash
        ontology_attribute = self._ontology.structure.get_child_by_hash(attribute_hash, type_=Attribute)

        ret["name"] = ontology_attribute.name
        ret["value"] = _lower_snake_case(ontology_attribute.name)
        ret["createdAt"] = annotation.created_at.strftime(DATETIME_LONG_STRING_FORMAT)
        ret["createdBy"] = annotation.created_by
        ret["confidence"] = annotation.confidence
        ret["featureHash"] = ontology_classification.feature_node_hash
        ret["classificationHash"] = classification.classification_hash
        ret["manualAnnotation"] = annotation.manual_annotation

        if annotation.last_edited_at is not None:
            ret["lastEditedAt"] = annotation.last_edited_at.strftime(DATETIME_LONG_STRING_FORMAT)
        if annotation.last_edited_by is not None:
            ret["lastEditedBy"] = annotation.last_edited_by

        return ret

    def _is_classification_already_present(self, classification: Classification, frames: Iterable[int]) -> Set[int]:
        present_frames = self._classifications_to_frames.get(classification, set())
        return present_frames.intersection(frames)

    def _add_frames_to_classification(self, classification: Classification, frames: Iterable[int]) -> None:
        self._classifications_to_frames[classification].update(frames)

    def _remove_frames_from_classification(self, classification: Classification, frames: Iterable[int]) -> None:
        present_frames = self._classifications_to_frames.get(classification, set())
        for frame in frames:
            present_frames.remove(frame)

    def _add_to_frame_to_hashes_map(
        self, label_item: Union[ObjectInstance, ClassificationInstance], frames: Iterable[int]
    ) -> None:
        for frame in frames:
            self.add_to_single_frame_to_hashes_map(label_item, frame)

    def _remove_from_frame_to_hashes_map(self, frames: Iterable[int], item_hash: str):
        for frame in frames:
            self._frame_to_hashes[frame].remove(item_hash)

    def _parse_label_row_metadata(self, label_row_metadata: LabelRowMetadata) -> LabelRowV2.LabelRowReadOnlyData:
        data_type = DataType.from_upper_case_string(label_row_metadata.data_type)

        return LabelRowV2.LabelRowReadOnlyData(
            label_hash=label_row_metadata.label_hash,
            branch_name=label_row_metadata.branch_name,
            data_hash=label_row_metadata.data_hash,
            data_title=label_row_metadata.data_title,
            dataset_hash=label_row_metadata.dataset_hash,
            dataset_title=label_row_metadata.dataset_title,
            data_type=data_type,
            data_link=label_row_metadata.data_link,
            label_status=label_row_metadata.label_status,
            annotation_task_status=label_row_metadata.annotation_task_status,
            workflow_graph_node=label_row_metadata.workflow_graph_node,
            is_shadow_data=label_row_metadata.is_shadow_data,
            created_at=label_row_metadata.created_at,
            last_edited_at=label_row_metadata.last_edited_at,
            duration=label_row_metadata.duration,
            fps=label_row_metadata.frames_per_second,
            number_of_frames=label_row_metadata.number_of_frames,
            width=label_row_metadata.width,
            height=label_row_metadata.height,
            priority=label_row_metadata.priority,
            images_data=None
            if label_row_metadata.images_data is None
            else [LabelRowV2.LabelRowReadOnlyDataImagesDataEntry(**data) for data in label_row_metadata.images_data],
            client_metadata=label_row_metadata.client_metadata,
            file_type=label_row_metadata.file_type,
            is_valid=label_row_metadata.is_valid,
        )

    def _parse_label_row_dict(self, label_row_dict: dict) -> LabelRowReadOnlyData:
        frame_level_data = self._parse_image_group_frame_level_data(label_row_dict["data_units"])
        image_hash_to_frame = {item.image_hash: item.frame_number for item in frame_level_data.values()}
        frame_to_image_hash = {item.frame_number: item.image_hash for item in frame_level_data.values()}
        data_type = DataType(label_row_dict["data_type"])

        if data_type == DataType.VIDEO:
            video_dict = list(label_row_dict["data_units"].values())[0]
            data_link = video_dict["data_link"]
            # Dimensions should be always there
            # But we have some older entries that don't have them
            # So setting them to None for now until the format is not guaranteed to be enforced
            height = video_dict.get("height")
            width = video_dict.get("width")

        elif data_type == DataType.DICOM:
            dicom_dict = list(label_row_dict["data_units"].values())[0]
            data_link = None
            height = dicom_dict["height"]
            width = dicom_dict["width"]

        elif data_type == DataType.IMAGE:
            image_dict = list(label_row_dict["data_units"].values())[0]
            data_link = image_dict["data_link"]
            # Dimensions should be always there
            # But we have some older entries that don't have them
            # So setting them to None for now until the format is not guaranteed to be enforced
            height = image_dict.get("height")
            width = image_dict.get("width")

        elif data_type == DataType.IMG_GROUP:
            data_link = None
            height = None
            width = None

        else:
            raise NotImplementedError(f"The data type {data_type} is not implemented yet.")

        return LabelRowV2.LabelRowReadOnlyData(
            label_hash=label_row_dict["label_hash"],
            branch_name=label_row_dict["branch_name"],
            dataset_hash=label_row_dict["dataset_hash"],
            dataset_title=label_row_dict["dataset_title"],
            data_title=label_row_dict["data_title"],
            data_hash=label_row_dict["data_hash"],
            data_type=data_type,
            label_status=LabelStatus(label_row_dict["label_status"]),
            annotation_task_status=label_row_dict.get("annotation_task_status"),
            workflow_graph_node=label_row_dict.get(
                "workflow_graph_node", self._label_row_read_only_data.workflow_graph_node
            ),
            is_shadow_data=self.is_shadow_data,
            created_at=label_row_dict["created_at"],
            last_edited_at=label_row_dict["last_edited_at"],
            frame_level_data=frame_level_data,
            image_hash_to_frame=image_hash_to_frame,
            frame_to_image_hash=frame_to_image_hash,
            duration=self.duration,
            fps=self.fps,
            number_of_frames=self.number_of_frames,
            data_link=data_link,
            height=height,
            width=width,
            priority=label_row_dict.get("priority", self._label_row_read_only_data.priority),
            client_metadata=label_row_dict.get("client_metadata", self._label_row_read_only_data.client_metadata),
            images_data=label_row_dict.get("images_data", self._label_row_read_only_data.images_data),
            file_type=label_row_dict.get("file_type", None),
            is_valid=bool(label_row_dict.get("is_valid", True)),
        )

    def _parse_labels_from_dict(self, label_row_dict: dict):
        classification_answers = label_row_dict["classification_answers"]

        for data_unit in label_row_dict["data_units"].values():
            data_type = DataType(label_row_dict["data_type"])
            if data_type in {DataType.IMG_GROUP, DataType.IMAGE}:
                frame = int(data_unit["data_sequence"])
                self._add_object_instances_from_objects(data_unit["labels"].get("objects", []), frame)
                self._add_classification_instances_from_classifications(
                    data_unit["labels"].get("classifications", []),
                    classification_answers,
                    frame,
                )
            elif data_type in {DataType.VIDEO, DataType.DICOM}:
                for frame, frame_data in data_unit["labels"].items():
                    frame_num = int(frame)
                    self._add_object_instances_from_objects(frame_data["objects"], frame_num)
                    self._add_classification_instances_from_classifications(
                        frame_data["classifications"], classification_answers, frame_num
                    )
                    self._add_frame_metadata(frame_num, frame_data.get("metadata"))
            else:
                raise NotImplementedError(f"Got an unexpected data type `{data_type}`")

            self._add_data_unit_metadata(data_type, data_unit.get("metadata"))

        self._add_objects_answers(label_row_dict)
        self._add_action_answers(label_row_dict)

    def _add_frame_metadata(self, frame: int, metadata: Optional[Dict[str, str]]):
        if metadata is not None:
            self._frame_metadata[frame] = DICOMSliceMetadata.from_dict(metadata)
        else:
            self._frame_metadata[frame] = None

    def _add_data_unit_metadata(self, data_type: DataType, metadata: Optional[Dict[str, str]]) -> None:
        if metadata is None:
            self._metadata = None
            return

        if data_type == DataType.DICOM:
            self._metadata = DICOMSeriesMetadata.from_dict(metadata)
        else:
            log.warning(
                f"Unexpected metadata for the data type: {data_type}. Please update the Encord SDK to the latest version."
            )

    def _add_object_instances_from_objects(
        self,
        objects_list: List[dict],
        frame: int,
    ) -> None:
        for frame_object_label in objects_list:
            object_hash = frame_object_label["objectHash"]
            if object_hash not in self._objects_map:
                object_instance = self._create_new_object_instance(frame_object_label, frame)
                self.add_object_instance(object_instance)
            else:
                self._add_coordinates_to_object_instance(frame_object_label, frame)

    def _add_objects_answers(self, label_row_dict: dict):
        for answer in label_row_dict["object_answers"].values():
            object_hash = answer["objectHash"]
            # In cases when we had an object, added some attributes for this object, and then removed the object,
            # in some label rows we still have such "orphaned" answers.
            # To avoid parser errors, we're omitting attributes for the object that is not in label rows.
            if object_instance := self._objects_map.get(object_hash):
                answer_list = answer["classifications"]
                object_instance.set_answer_from_list(answer_list)

    def _add_action_answers(self, label_row_dict: dict):
        for answer in label_row_dict["object_actions"].values():
            object_hash = answer["objectHash"]
            object_instance = self._objects_map[object_hash]

            answer_list = answer["actions"]
            object_instance.set_answer_from_list(answer_list)

    def _create_new_object_instance(self, frame_object_label: dict, frame: int) -> ObjectInstance:
        ontology = self._ontology.structure
        feature_hash = frame_object_label["featureHash"]
        object_hash = frame_object_label["objectHash"]

        label_class = ontology.get_child_by_hash(feature_hash, type_=Object)
        object_instance = ObjectInstance(label_class, object_hash=object_hash)

        coordinates = self._get_coordinates(frame_object_label)
        object_frame_instance_info = ObjectInstance.FrameInfo.from_dict(frame_object_label)

        object_instance.set_for_frames(
            coordinates=coordinates,
            frames=frame,
            created_at=object_frame_instance_info.created_at,
            created_by=object_frame_instance_info.created_by,
            last_edited_at=object_frame_instance_info.last_edited_at,
            last_edited_by=object_frame_instance_info.last_edited_by,
            confidence=object_frame_instance_info.confidence,
            manual_annotation=object_frame_instance_info.manual_annotation,
            reviews=object_frame_instance_info.reviews,
            is_deleted=object_frame_instance_info.is_deleted,
        )
        return object_instance

    def _add_coordinates_to_object_instance(
        self,
        frame_object_label: dict,
        frame: int = 0,
    ) -> None:
        object_hash = frame_object_label["objectHash"]
        object_instance = self._objects_map[object_hash]

        coordinates = self._get_coordinates(frame_object_label)
        object_frame_instance_info = ObjectInstance.FrameInfo.from_dict(frame_object_label)

        object_instance.set_for_frames(
            coordinates=coordinates,
            frames=frame,
            created_at=object_frame_instance_info.created_at,
            created_by=object_frame_instance_info.created_by,
            last_edited_at=object_frame_instance_info.last_edited_at,
            last_edited_by=object_frame_instance_info.last_edited_by,
            confidence=object_frame_instance_info.confidence,
            manual_annotation=object_frame_instance_info.manual_annotation,
            reviews=object_frame_instance_info.reviews,
            is_deleted=object_frame_instance_info.is_deleted,
        )

    def _get_coordinates(self, frame_object_label: dict) -> Coordinates:
        if "boundingBox" in frame_object_label:
            return BoundingBoxCoordinates.from_dict(frame_object_label)
        if "rotatableBoundingBox" in frame_object_label:
            return RotatableBoundingBoxCoordinates.from_dict(frame_object_label)
        elif "polygon" in frame_object_label:
            return PolygonCoordinates.from_dict(frame_object_label)
        elif "point" in frame_object_label:
            return PointCoordinate.from_dict(frame_object_label)
        elif "polyline" in frame_object_label:
            return PolylineCoordinates.from_dict(frame_object_label)
        elif "skeleton" in frame_object_label:
            skeleton_frame_object_label = {
                "name": frame_object_label["name"],
                "values": list(frame_object_label["skeleton"].values()),
            }
            return SkeletonCoordinates.from_dict(skeleton_frame_object_label)
        elif "bitmask" in frame_object_label:
            return BitmaskCoordinates.from_dict(frame_object_label)
        else:
            raise NotImplementedError(f"Getting coordinates for `{frame_object_label}` is not supported yet.")

    def _add_classification_instances_from_classifications(
        self, classifications_list: List[dict], classification_answers: dict, frame: int
    ):
        for frame_classification_label in classifications_list:
            classification_hash = frame_classification_label["classificationHash"]
            if classification_hash in self._classifications_map:
                self._add_frames_to_classification_instance(frame_classification_label, frame)
            elif classification_instance := self._create_new_classification_instance(
                frame_classification_label, frame, classification_answers
            ):
                self.add_classification_instance(classification_instance)

    def _parse_image_group_frame_level_data(self, label_row_data_units: dict) -> Dict[int, FrameLevelImageGroupData]:
        frame_level_data: Dict[int, LabelRowV2.FrameLevelImageGroupData] = {}
        for payload in label_row_data_units.values():
            frame_number = int(payload["data_sequence"])
            frame_level_image_group_data = self.FrameLevelImageGroupData(
                image_hash=payload["data_hash"],
                image_title=payload["data_title"],
                data_link=payload.get("data_link"),
                file_type=payload["data_type"],
                frame_number=frame_number,
                # Dimensions should be always there
                # But we have some older entries that don't have them
                # So setting them to 0 for now until the format is not guaranteed to be enforced
                width=payload.get("width", 0),
                height=payload.get("height", 0),
            )
            frame_level_data[frame_number] = frame_level_image_group_data
        return frame_level_data

    def _create_new_classification_instance(
        self, frame_classification_label: dict, frame: int, classification_answers: dict
    ) -> Optional[ClassificationInstance]:
        feature_hash = frame_classification_label["featureHash"]
        classification_hash = frame_classification_label["classificationHash"]

        label_class = self._ontology.structure.get_child_by_hash(feature_hash, type_=Classification)
        classification_instance = ClassificationInstance(label_class, classification_hash=classification_hash)

        frame_view = ClassificationInstance.FrameData.from_dict(frame_classification_label)
        classification_instance.set_for_frames(
            frame,
            created_at=frame_view.created_at,
            created_by=frame_view.created_by,
            confidence=frame_view.confidence,
            manual_annotation=frame_view.manual_annotation,
            last_edited_at=frame_view.last_edited_at,
            last_edited_by=frame_view.last_edited_by,
            reviews=frame_view.reviews,
            overwrite=True,  # Always overwrite during label row dict parsing, as older dicts known to have duplicates
        )

        # For some older label rows we might have a classification entry, but without an assigned answer.
        # These cases are equivalent to not having classifications at all, so just ignoring them
        if classification_answer := classification_answers.get(classification_hash):
            answers_dict = classification_answer["classifications"]
            self._add_static_answers_from_dict(classification_instance, answers_dict)
            return classification_instance

        return None

    def _add_static_answers_from_dict(
        self, classification_instance: ClassificationInstance, answers_list: List[dict]
    ) -> None:
        classification_instance.set_answer_from_list(answers_list)

    def _add_frames_to_classification_instance(self, frame_classification_label: dict, frame: int) -> None:
        object_hash = frame_classification_label["classificationHash"]
        classification_instance = self._classifications_map[object_hash]
        frame_view = ClassificationInstance.FrameData.from_dict(frame_classification_label)
        classification_instance.set_frame_data(frame_view, frame)

    def _check_labelling_is_initalised(self):
        if not self.is_labelling_initialised:
            raise LabelRowError(
                "For this operation you will need to initialise labelling first. Call the `.initialise_labels()` "
                "to do so first."
            )

    def __repr__(self) -> str:
        return f"LabelRowV2(label_hash={self.label_hash}, data_hash={self.data_hash}, data_title={self.data_title})"


def _frame_views_to_frame_numbers(
    frame_views: Sequence[Union[ObjectInstance.Annotation, ClassificationInstance.Annotation, LabelRowV2.FrameView]],
) -> List[int]:
    return [frame_view.frame for frame_view in frame_views]
