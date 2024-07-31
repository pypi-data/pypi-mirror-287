from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret_parameters import (
        CSSCMSDataModelModelsKeyfactorAPISecretParameters,
    )


T = TypeVar("T", bound="CSSCMSDataModelModelsKeyfactorAPISecret")


@_attrs_define
class CSSCMSDataModelModelsKeyfactorAPISecret:
    """
    Attributes:
        secret_value (Union[Unset, None, str]):
        parameters (Union[Unset, None, CSSCMSDataModelModelsKeyfactorAPISecretParameters]):
        provider (Union[Unset, None, int]):
        has_value (Union[Unset, bool]):
    """

    secret_value: Union[Unset, None, str] = UNSET
    parameters: Union[Unset, None, "CSSCMSDataModelModelsKeyfactorAPISecretParameters"] = UNSET
    provider: Union[Unset, None, int] = UNSET
    has_value: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        secret_value = self.secret_value
        parameters: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict() if self.parameters else None

        provider = self.provider
        has_value = self.has_value

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if secret_value is not UNSET:
            field_dict["secretValue"] = secret_value
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if provider is not UNSET:
            field_dict["provider"] = provider
        if has_value is not UNSET:
            field_dict["hasValue"] = has_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret_parameters import (
            CSSCMSDataModelModelsKeyfactorAPISecretParameters,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        secret_value = d.pop("secretValue", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, None, CSSCMSDataModelModelsKeyfactorAPISecretParameters]
        if _parameters is None:
            parameters = None
        elif isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = CSSCMSDataModelModelsKeyfactorAPISecretParameters.from_dict(_parameters)

        provider = d.pop("provider", UNSET)

        has_value = d.pop("hasValue", UNSET)

        csscms_data_model_models_keyfactor_api_secret = cls(
            secret_value=secret_value,
            parameters=parameters,
            provider=provider,
            has_value=has_value,
        )

        return csscms_data_model_models_keyfactor_api_secret
