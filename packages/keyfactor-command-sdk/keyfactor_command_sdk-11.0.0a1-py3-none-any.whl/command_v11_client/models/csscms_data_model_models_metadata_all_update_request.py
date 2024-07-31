from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_metadata_single_update_request import (
        CSSCMSDataModelModelsMetadataSingleUpdateRequest,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsMetadataAllUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsMetadataAllUpdateRequest:
    """
    Attributes:
        metadata (List['CSSCMSDataModelModelsMetadataSingleUpdateRequest']):
        query (Union[Unset, None, str]):
        certificate_ids (Union[Unset, None, List[int]]):
    """

    metadata: List["CSSCMSDataModelModelsMetadataSingleUpdateRequest"]
    query: Union[Unset, None, str] = UNSET
    certificate_ids: Union[Unset, None, List[int]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metadata = []
        for metadata_item_data in self.metadata:
            metadata_item = metadata_item_data.to_dict()

            metadata.append(metadata_item)

        query = self.query
        certificate_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.certificate_ids, Unset):
            if self.certificate_ids is None:
                certificate_ids = None
            else:
                certificate_ids = self.certificate_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "metadata": metadata,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if certificate_ids is not UNSET:
            field_dict["certificateIds"] = certificate_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_metadata_single_update_request import (
            CSSCMSDataModelModelsMetadataSingleUpdateRequest,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        metadata = []
        _metadata = d.pop("metadata")
        for metadata_item_data in _metadata:
            metadata_item = CSSCMSDataModelModelsMetadataSingleUpdateRequest.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        query = d.pop("query", UNSET)

        certificate_ids = cast(List[int], d.pop("certificateIds", UNSET))

        csscms_data_model_models_metadata_all_update_request = cls(
            metadata=metadata,
            query=query,
            certificate_ids=certificate_ids,
        )

        return csscms_data_model_models_metadata_all_update_request
