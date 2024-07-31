from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_revocation_suspended_revocation_response import (
        CSSCMSDataModelModelsRevocationSuspendedRevocationResponse,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsRevocationRevocationResponse")


@_attrs_define
class CSSCMSDataModelModelsRevocationRevocationResponse:
    """
    Attributes:
        revoked_ids (Union[Unset, None, List[int]]):
        suspended_certs (Union[Unset, None, List['CSSCMSDataModelModelsRevocationSuspendedRevocationResponse']]):
    """

    revoked_ids: Union[Unset, None, List[int]] = UNSET
    suspended_certs: Union[Unset, None, List["CSSCMSDataModelModelsRevocationSuspendedRevocationResponse"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        revoked_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.revoked_ids, Unset):
            if self.revoked_ids is None:
                revoked_ids = None
            else:
                revoked_ids = self.revoked_ids

        suspended_certs: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.suspended_certs, Unset):
            if self.suspended_certs is None:
                suspended_certs = None
            else:
                suspended_certs = []
                for suspended_certs_item_data in self.suspended_certs:
                    suspended_certs_item = suspended_certs_item_data.to_dict()

                    suspended_certs.append(suspended_certs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if revoked_ids is not UNSET:
            field_dict["revokedIds"] = revoked_ids
        if suspended_certs is not UNSET:
            field_dict["suspendedCerts"] = suspended_certs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_revocation_suspended_revocation_response import (
            CSSCMSDataModelModelsRevocationSuspendedRevocationResponse,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        revoked_ids = cast(List[int], d.pop("revokedIds", UNSET))

        suspended_certs = []
        _suspended_certs = d.pop("suspendedCerts", UNSET)
        for suspended_certs_item_data in _suspended_certs or []:
            suspended_certs_item = CSSCMSDataModelModelsRevocationSuspendedRevocationResponse.from_dict(
                suspended_certs_item_data
            )

            suspended_certs.append(suspended_certs_item)

        csscms_data_model_models_revocation_revocation_response = cls(
            revoked_ids=revoked_ids,
            suspended_certs=suspended_certs,
        )

        return csscms_data_model_models_revocation_revocation_response
