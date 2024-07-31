from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsMonitoringOCSPParametersRequest:
    """
    Attributes:
        certificate_contents (Union[Unset, None, str]):
        certificate_authority_id (Union[Unset, None, int]):
        authority_name (Union[Unset, None, str]):
        authority_name_id (Union[Unset, None, str]):
        authority_key_id (Union[Unset, None, str]):
        sample_serial_number (Union[Unset, None, str]):
        file_name (Union[Unset, None, str]):
    """

    certificate_contents: Union[Unset, None, str] = UNSET
    certificate_authority_id: Union[Unset, None, int] = UNSET
    authority_name: Union[Unset, None, str] = UNSET
    authority_name_id: Union[Unset, None, str] = UNSET
    authority_key_id: Union[Unset, None, str] = UNSET
    sample_serial_number: Union[Unset, None, str] = UNSET
    file_name: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        certificate_contents = self.certificate_contents
        certificate_authority_id = self.certificate_authority_id
        authority_name = self.authority_name
        authority_name_id = self.authority_name_id
        authority_key_id = self.authority_key_id
        sample_serial_number = self.sample_serial_number
        file_name = self.file_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if certificate_contents is not UNSET:
            field_dict["certificateContents"] = certificate_contents
        if certificate_authority_id is not UNSET:
            field_dict["certificateAuthorityId"] = certificate_authority_id
        if authority_name is not UNSET:
            field_dict["authorityName"] = authority_name
        if authority_name_id is not UNSET:
            field_dict["authorityNameId"] = authority_name_id
        if authority_key_id is not UNSET:
            field_dict["authorityKeyId"] = authority_key_id
        if sample_serial_number is not UNSET:
            field_dict["sampleSerialNumber"] = sample_serial_number
        if file_name is not UNSET:
            field_dict["fileName"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        certificate_contents = d.pop("certificateContents", UNSET)

        certificate_authority_id = d.pop("certificateAuthorityId", UNSET)

        authority_name = d.pop("authorityName", UNSET)

        authority_name_id = d.pop("authorityNameId", UNSET)

        authority_key_id = d.pop("authorityKeyId", UNSET)

        sample_serial_number = d.pop("sampleSerialNumber", UNSET)

        file_name = d.pop("fileName", UNSET)

        keyfactor_web_keyfactor_api_models_monitoring_ocsp_parameters_request = cls(
            certificate_contents=certificate_contents,
            certificate_authority_id=certificate_authority_id,
            authority_name=authority_name,
            authority_name_id=authority_name_id,
            authority_key_id=authority_key_id,
            sample_serial_number=sample_serial_number,
            file_name=file_name,
        )

        return keyfactor_web_keyfactor_api_models_monitoring_ocsp_parameters_request
