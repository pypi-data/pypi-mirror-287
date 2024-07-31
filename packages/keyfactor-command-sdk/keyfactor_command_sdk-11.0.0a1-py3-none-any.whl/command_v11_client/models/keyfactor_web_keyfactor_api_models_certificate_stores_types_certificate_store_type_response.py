from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.csscms_core_enums_cert_store_private_key import CSSCMSCoreEnumsCertStorePrivateKey
from ..models.keyfactor_orchestrators_common_enums_cert_store_custom_alias import (
    KeyfactorOrchestratorsCommonEnumsCertStoreCustomAlias,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_cert_store_type_password_options import (
        CSSCMSDataModelModelsCertStoreTypePasswordOptions,
    )
    from ..models.csscms_data_model_models_cert_store_type_supported_operations import (
        CSSCMSDataModelModelsCertStoreTypeSupportedOperations,
    )
    from ..models.csscms_data_model_models_certificate_store_type_property import (
        CSSCMSDataModelModelsCertificateStoreTypeProperty,
    )
    from ..models.csscms_data_model_models_certificate_store_types_certificate_store_type_entry_parameter import (
        CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter,
    )


T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateStoresTypesCertificateStoreTypeResponse:
    """
    Attributes:
        name (Union[Unset, None, str]):
        short_name (Union[Unset, None, str]):
        capability (Union[Unset, None, str]):
        store_type (Union[Unset, None, int]):
        import_type (Union[Unset, None, int]):
        local_store (Union[Unset, bool]):
        supported_operations (Union[Unset, CSSCMSDataModelModelsCertStoreTypeSupportedOperations]):
        properties (Union[Unset, None, List['CSSCMSDataModelModelsCertificateStoreTypeProperty']]):
        entry_parameters (Union[Unset, None,
            List['CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter']]):
        password_options (Union[Unset, CSSCMSDataModelModelsCertStoreTypePasswordOptions]):
        store_path_type (Union[Unset, None, str]):
        store_path_value (Union[Unset, None, str]):
        private_key_allowed (Union[Unset, CSSCMSCoreEnumsCertStorePrivateKey]):
        job_properties (Union[Unset, None, List[str]]):
        server_required (Union[Unset, bool]):
        power_shell (Union[Unset, bool]):
        blueprint_allowed (Union[Unset, bool]):
        custom_alias_allowed (Union[Unset, KeyfactorOrchestratorsCommonEnumsCertStoreCustomAlias]):
        server_registration (Union[Unset, None, int]):
        inventory_endpoint (Union[Unset, None, str]):
        inventory_job_type (Union[Unset, str]):
        management_job_type (Union[Unset, None, str]):
        discovery_job_type (Union[Unset, None, str]):
        enrollment_job_type (Union[Unset, None, str]):
    """

    name: Union[Unset, None, str] = UNSET
    short_name: Union[Unset, None, str] = UNSET
    capability: Union[Unset, None, str] = UNSET
    store_type: Union[Unset, None, int] = UNSET
    import_type: Union[Unset, None, int] = UNSET
    local_store: Union[Unset, bool] = UNSET
    supported_operations: Union[Unset, "CSSCMSDataModelModelsCertStoreTypeSupportedOperations"] = UNSET
    properties: Union[Unset, None, List["CSSCMSDataModelModelsCertificateStoreTypeProperty"]] = UNSET
    entry_parameters: Union[
        Unset, None, List["CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter"]
    ] = UNSET
    password_options: Union[Unset, "CSSCMSDataModelModelsCertStoreTypePasswordOptions"] = UNSET
    store_path_type: Union[Unset, None, str] = UNSET
    store_path_value: Union[Unset, None, str] = UNSET
    private_key_allowed: Union[Unset, CSSCMSCoreEnumsCertStorePrivateKey] = UNSET
    job_properties: Union[Unset, None, List[str]] = UNSET
    server_required: Union[Unset, bool] = UNSET
    power_shell: Union[Unset, bool] = UNSET
    blueprint_allowed: Union[Unset, bool] = UNSET
    custom_alias_allowed: Union[Unset, KeyfactorOrchestratorsCommonEnumsCertStoreCustomAlias] = UNSET
    server_registration: Union[Unset, None, int] = UNSET
    inventory_endpoint: Union[Unset, None, str] = UNSET
    inventory_job_type: Union[Unset, str] = UNSET
    management_job_type: Union[Unset, None, str] = UNSET
    discovery_job_type: Union[Unset, None, str] = UNSET
    enrollment_job_type: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        short_name = self.short_name
        capability = self.capability
        store_type = self.store_type
        import_type = self.import_type
        local_store = self.local_store
        supported_operations: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supported_operations, Unset):
            supported_operations = self.supported_operations.to_dict()

        properties: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            if self.properties is None:
                properties = None
            else:
                properties = []
                for properties_item_data in self.properties:
                    properties_item = properties_item_data.to_dict()

                    properties.append(properties_item)

        entry_parameters: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entry_parameters, Unset):
            if self.entry_parameters is None:
                entry_parameters = None
            else:
                entry_parameters = []
                for entry_parameters_item_data in self.entry_parameters:
                    entry_parameters_item = entry_parameters_item_data.to_dict()

                    entry_parameters.append(entry_parameters_item)

        password_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password_options, Unset):
            password_options = self.password_options.to_dict()

        store_path_type = self.store_path_type
        store_path_value = self.store_path_value
        private_key_allowed: Union[Unset, int] = UNSET
        if not isinstance(self.private_key_allowed, Unset):
            private_key_allowed = self.private_key_allowed.value

        job_properties: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.job_properties, Unset):
            if self.job_properties is None:
                job_properties = None
            else:
                job_properties = self.job_properties

        server_required = self.server_required
        power_shell = self.power_shell
        blueprint_allowed = self.blueprint_allowed
        custom_alias_allowed: Union[Unset, int] = UNSET
        if not isinstance(self.custom_alias_allowed, Unset):
            custom_alias_allowed = self.custom_alias_allowed.value

        server_registration = self.server_registration
        inventory_endpoint = self.inventory_endpoint
        inventory_job_type = self.inventory_job_type
        management_job_type = self.management_job_type
        discovery_job_type = self.discovery_job_type
        enrollment_job_type = self.enrollment_job_type

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if capability is not UNSET:
            field_dict["capability"] = capability
        if store_type is not UNSET:
            field_dict["storeType"] = store_type
        if import_type is not UNSET:
            field_dict["importType"] = import_type
        if local_store is not UNSET:
            field_dict["localStore"] = local_store
        if supported_operations is not UNSET:
            field_dict["supportedOperations"] = supported_operations
        if properties is not UNSET:
            field_dict["properties"] = properties
        if entry_parameters is not UNSET:
            field_dict["entryParameters"] = entry_parameters
        if password_options is not UNSET:
            field_dict["passwordOptions"] = password_options
        if store_path_type is not UNSET:
            field_dict["storePathType"] = store_path_type
        if store_path_value is not UNSET:
            field_dict["storePathValue"] = store_path_value
        if private_key_allowed is not UNSET:
            field_dict["privateKeyAllowed"] = private_key_allowed
        if job_properties is not UNSET:
            field_dict["jobProperties"] = job_properties
        if server_required is not UNSET:
            field_dict["serverRequired"] = server_required
        if power_shell is not UNSET:
            field_dict["powerShell"] = power_shell
        if blueprint_allowed is not UNSET:
            field_dict["blueprintAllowed"] = blueprint_allowed
        if custom_alias_allowed is not UNSET:
            field_dict["customAliasAllowed"] = custom_alias_allowed
        if server_registration is not UNSET:
            field_dict["serverRegistration"] = server_registration
        if inventory_endpoint is not UNSET:
            field_dict["inventoryEndpoint"] = inventory_endpoint
        if inventory_job_type is not UNSET:
            field_dict["inventoryJobType"] = inventory_job_type
        if management_job_type is not UNSET:
            field_dict["managementJobType"] = management_job_type
        if discovery_job_type is not UNSET:
            field_dict["discoveryJobType"] = discovery_job_type
        if enrollment_job_type is not UNSET:
            field_dict["enrollmentJobType"] = enrollment_job_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_cert_store_type_password_options import (
            CSSCMSDataModelModelsCertStoreTypePasswordOptions,
        )
        from ..models.csscms_data_model_models_cert_store_type_supported_operations import (
            CSSCMSDataModelModelsCertStoreTypeSupportedOperations,
        )
        from ..models.csscms_data_model_models_certificate_store_type_property import (
            CSSCMSDataModelModelsCertificateStoreTypeProperty,
        )
        from ..models.csscms_data_model_models_certificate_store_types_certificate_store_type_entry_parameter import (
            CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        name = d.pop("name", UNSET)

        short_name = d.pop("shortName", UNSET)

        capability = d.pop("capability", UNSET)

        store_type = d.pop("storeType", UNSET)

        import_type = d.pop("importType", UNSET)

        local_store = d.pop("localStore", UNSET)

        _supported_operations = d.pop("supportedOperations", UNSET)
        supported_operations: Union[Unset, CSSCMSDataModelModelsCertStoreTypeSupportedOperations]
        if isinstance(_supported_operations, Unset):
            supported_operations = UNSET
        else:
            supported_operations = CSSCMSDataModelModelsCertStoreTypeSupportedOperations.from_dict(
                _supported_operations
            )

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = CSSCMSDataModelModelsCertificateStoreTypeProperty.from_dict(properties_item_data)

            properties.append(properties_item)

        entry_parameters = []
        _entry_parameters = d.pop("entryParameters", UNSET)
        for entry_parameters_item_data in _entry_parameters or []:
            entry_parameters_item = (
                CSSCMSDataModelModelsCertificateStoreTypesCertificateStoreTypeEntryParameter.from_dict(
                    entry_parameters_item_data
                )
            )

            entry_parameters.append(entry_parameters_item)

        _password_options = d.pop("passwordOptions", UNSET)
        password_options: Union[Unset, CSSCMSDataModelModelsCertStoreTypePasswordOptions]
        if isinstance(_password_options, Unset):
            password_options = UNSET
        else:
            password_options = CSSCMSDataModelModelsCertStoreTypePasswordOptions.from_dict(_password_options)

        store_path_type = d.pop("storePathType", UNSET)

        store_path_value = d.pop("storePathValue", UNSET)

        _private_key_allowed = d.pop("privateKeyAllowed", UNSET)
        private_key_allowed: Union[Unset, CSSCMSCoreEnumsCertStorePrivateKey]
        if isinstance(_private_key_allowed, Unset):
            private_key_allowed = UNSET
        else:
            private_key_allowed = CSSCMSCoreEnumsCertStorePrivateKey(_private_key_allowed)

        job_properties = cast(List[str], d.pop("jobProperties", UNSET))

        server_required = d.pop("serverRequired", UNSET)

        power_shell = d.pop("powerShell", UNSET)

        blueprint_allowed = d.pop("blueprintAllowed", UNSET)

        _custom_alias_allowed = d.pop("customAliasAllowed", UNSET)
        custom_alias_allowed: Union[Unset, KeyfactorOrchestratorsCommonEnumsCertStoreCustomAlias]
        if isinstance(_custom_alias_allowed, Unset):
            custom_alias_allowed = UNSET
        else:
            custom_alias_allowed = KeyfactorOrchestratorsCommonEnumsCertStoreCustomAlias(_custom_alias_allowed)

        server_registration = d.pop("serverRegistration", UNSET)

        inventory_endpoint = d.pop("inventoryEndpoint", UNSET)

        inventory_job_type = d.pop("inventoryJobType", UNSET)

        management_job_type = d.pop("managementJobType", UNSET)

        discovery_job_type = d.pop("discoveryJobType", UNSET)

        enrollment_job_type = d.pop("enrollmentJobType", UNSET)

        keyfactor_web_keyfactor_api_models_certificate_stores_types_certificate_store_type_response = cls(
            name=name,
            short_name=short_name,
            capability=capability,
            store_type=store_type,
            import_type=import_type,
            local_store=local_store,
            supported_operations=supported_operations,
            properties=properties,
            entry_parameters=entry_parameters,
            password_options=password_options,
            store_path_type=store_path_type,
            store_path_value=store_path_value,
            private_key_allowed=private_key_allowed,
            job_properties=job_properties,
            server_required=server_required,
            power_shell=power_shell,
            blueprint_allowed=blueprint_allowed,
            custom_alias_allowed=custom_alias_allowed,
            server_registration=server_registration,
            inventory_endpoint=inventory_endpoint,
            inventory_job_type=inventory_job_type,
            management_job_type=management_job_type,
            discovery_job_type=discovery_job_type,
            enrollment_job_type=enrollment_job_type,
        )

        return keyfactor_web_keyfactor_api_models_certificate_stores_types_certificate_store_type_response
