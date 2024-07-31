from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_metadata_update_request_metadata import (
        CSSCMSDataModelModelsMetadataUpdateRequestMetadata,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsMetadataUpdateRequest")


@_attrs_define
class CSSCMSDataModelModelsMetadataUpdateRequest:
    """
    Attributes:
        metadata (CSSCMSDataModelModelsMetadataUpdateRequestMetadata):
        certificate_id (Union[Unset, int]):
    """

    metadata: "CSSCMSDataModelModelsMetadataUpdateRequestMetadata"
    certificate_id: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metadata = self.metadata.to_dict()

        certificate_id = self.certificate_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "metadata": metadata,
            }
        )
        if certificate_id is not UNSET:
            field_dict["certificateId"] = certificate_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_metadata_update_request_metadata import (
            CSSCMSDataModelModelsMetadataUpdateRequestMetadata,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        metadata = CSSCMSDataModelModelsMetadataUpdateRequestMetadata.from_dict(d.pop("metadata"))

        certificate_id = d.pop("certificateId", UNSET)

        csscms_data_model_models_metadata_update_request = cls(
            metadata=metadata,
            certificate_id=certificate_id,
        )

        return csscms_data_model_models_metadata_update_request
