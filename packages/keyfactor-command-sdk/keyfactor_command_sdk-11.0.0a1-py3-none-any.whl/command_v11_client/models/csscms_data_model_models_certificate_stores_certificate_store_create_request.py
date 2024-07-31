from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStoresCertificateStoreCreateRequest")


@_attrs_define
class CSSCMSDataModelModelsCertificateStoresCertificateStoreCreateRequest:
    """
    Attributes:
        container_id (Union[Unset, None, int]):
        client_machine (Union[Unset, None, str]):
        storepath (Union[Unset, None, str]):
        cert_store_type (Union[Unset, int]):
        create_if_missing (Union[Unset, bool]):
        properties (Union[Unset, None, str]):
        agent_id (Union[Unset, None, str]):
        agent_assigned (Union[Unset, bool]):
        inventory_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        password (Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]):
    """

    container_id: Union[Unset, None, int] = UNSET
    client_machine: Union[Unset, None, str] = UNSET
    storepath: Union[Unset, None, str] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    create_if_missing: Union[Unset, bool] = UNSET
    properties: Union[Unset, None, str] = UNSET
    agent_id: Union[Unset, None, str] = UNSET
    agent_assigned: Union[Unset, bool] = UNSET
    inventory_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    password: Union[Unset, "CSSCMSDataModelModelsKeyfactorAPISecret"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        container_id = self.container_id
        client_machine = self.client_machine
        storepath = self.storepath
        cert_store_type = self.cert_store_type
        create_if_missing = self.create_if_missing
        properties = self.properties
        agent_id = self.agent_id
        agent_assigned = self.agent_assigned
        inventory_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_schedule, Unset):
            inventory_schedule = self.inventory_schedule.to_dict()

        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if storepath is not UNSET:
            field_dict["storepath"] = storepath
        if cert_store_type is not UNSET:
            field_dict["certStoreType"] = cert_store_type
        if create_if_missing is not UNSET:
            field_dict["createIfMissing"] = create_if_missing
        if properties is not UNSET:
            field_dict["properties"] = properties
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if agent_assigned is not UNSET:
            field_dict["agentAssigned"] = agent_assigned
        if inventory_schedule is not UNSET:
            field_dict["inventorySchedule"] = inventory_schedule
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_api_secret import CSSCMSDataModelModelsKeyfactorAPISecret
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        container_id = d.pop("containerId", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        storepath = d.pop("storepath", UNSET)

        cert_store_type = d.pop("certStoreType", UNSET)

        create_if_missing = d.pop("createIfMissing", UNSET)

        properties = d.pop("properties", UNSET)

        agent_id = d.pop("agentId", UNSET)

        agent_assigned = d.pop("agentAssigned", UNSET)

        _inventory_schedule = d.pop("inventorySchedule", UNSET)
        inventory_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_inventory_schedule, Unset):
            inventory_schedule = UNSET
        else:
            inventory_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_inventory_schedule)

        _password = d.pop("password", UNSET)
        password: Union[Unset, CSSCMSDataModelModelsKeyfactorAPISecret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = CSSCMSDataModelModelsKeyfactorAPISecret.from_dict(_password)

        csscms_data_model_models_certificate_stores_certificate_store_create_request = cls(
            container_id=container_id,
            client_machine=client_machine,
            storepath=storepath,
            cert_store_type=cert_store_type,
            create_if_missing=create_if_missing,
            properties=properties,
            agent_id=agent_id,
            agent_assigned=agent_assigned,
            inventory_schedule=inventory_schedule,
            password=password,
        )

        return csscms_data_model_models_certificate_stores_certificate_store_create_request
