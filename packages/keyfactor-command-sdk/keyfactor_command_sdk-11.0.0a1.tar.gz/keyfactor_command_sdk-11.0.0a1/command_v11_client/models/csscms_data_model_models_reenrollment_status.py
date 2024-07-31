from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_certificate_store_types_certificate_store_type_entry_parameter import (
        CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsReenrollmentStatus")


@_attrs_define
class CSSCMSDataModelModelsReenrollmentStatus:
    """
    Attributes:
        data (Union[Unset, bool]):
        agent_id (Union[Unset, None, str]):
        message (Union[Unset, None, str]):
        job_properties (Union[Unset, None, str]):
        custom_alias_allowed (Union[Unset, int]):
        entry_parameters (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter']]):
    """

    data: Union[Unset, bool] = UNSET
    agent_id: Union[Unset, None, str] = UNSET
    message: Union[Unset, None, str] = UNSET
    job_properties: Union[Unset, None, str] = UNSET
    custom_alias_allowed: Union[Unset, int] = UNSET
    entry_parameters: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter"]
    ] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        data = self.data
        agent_id = self.agent_id
        message = self.message
        job_properties = self.job_properties
        custom_alias_allowed = self.custom_alias_allowed
        entry_parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry_parameters, Unset):
            if self.entry_parameters is None:
                entry_parameters = None
            else:
                entry_parameters = []
                for entry_parameters_item_data in self.entry_parameters:
                    entry_parameters_item = entry_parameters_item_data.to_dict()

                    entry_parameters.append(entry_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if message is not UNSET:
            field_dict["message"] = message
        if job_properties is not UNSET:
            field_dict["jobProperties"] = job_properties
        if custom_alias_allowed is not UNSET:
            field_dict["customAliasAllowed"] = custom_alias_allowed
        if entry_parameters is not UNSET:
            field_dict["entryParameters"] = entry_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_certificate_store_types_certificate_store_type_entry_parameter import (
            CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        data = d.pop("data", UNSET)

        agent_id = d.pop("agentId", UNSET)

        message = d.pop("message", UNSET)

        job_properties = d.pop("jobProperties", UNSET)

        custom_alias_allowed = d.pop("customAliasAllowed", UNSET)

        entry_parameters = []
        _entry_parameters = d.pop("entryParameters", UNSET)
        for entry_parameters_item_data in _entry_parameters or []:
            entry_parameters_item = (
                CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter.from_dict(
                    entry_parameters_item_data
                )
            )

            entry_parameters.append(entry_parameters_item)

        csscms_data_model_models_reenrollment_status = cls(
            data=data,
            agent_id=agent_id,
            message=message,
            job_properties=job_properties,
            custom_alias_allowed=custom_alias_allowed,
            entry_parameters=entry_parameters,
        )

        return csscms_data_model_models_reenrollment_status
