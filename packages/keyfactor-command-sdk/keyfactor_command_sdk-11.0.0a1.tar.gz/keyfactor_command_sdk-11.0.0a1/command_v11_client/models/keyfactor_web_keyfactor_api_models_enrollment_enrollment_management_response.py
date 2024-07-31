from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsEnrollmentEnrollmentManagementResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsEnrollmentEnrollmentManagementResponse:
    """
    Attributes:
        successful_stores (Union[Unset, None, List[str]]):
        failed_stores (Union[Unset, None, List[str]]):
    """

    successful_stores: Union[Unset, None, List[str]] = UNSET
    failed_stores: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        successful_stores: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.successful_stores, Unset):
            if self.successful_stores is None:
                successful_stores = None
            else:
                successful_stores = self.successful_stores

        failed_stores: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.failed_stores, Unset):
            if self.failed_stores is None:
                failed_stores = None
            else:
                failed_stores = self.failed_stores

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if successful_stores is not UNSET:
            field_dict["successfulStores"] = successful_stores
        if failed_stores is not UNSET:
            field_dict["failedStores"] = failed_stores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        successful_stores = cast(List[str], d.pop("successfulStores", UNSET))

        failed_stores = cast(List[str], d.pop("failedStores", UNSET))

        keyfactor_web_keyfactor_api_models_enrollment_enrollment_management_response = cls(
            successful_stores=successful_stores,
            failed_stores=failed_stores,
        )

        return keyfactor_web_keyfactor_api_models_enrollment_enrollment_management_response
