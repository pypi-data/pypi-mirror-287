from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_keyfactor_secret import CSSCMSDataModelModelsKeyfactorSecret
    from ..models.csscms_data_model_models_reenrollment_status import CSSCMSDataModelModelsReenrollmentStatus
    from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsCertificateStore")


@_attrs_define
class CSSCMSDataModelModelsCertificateStore:
    """
    Attributes:
        id (Union[Unset, str]):
        display_name (Union[Unset, None, str]):
        container_id (Union[Unset, None, int]):
        client_machine (Union[Unset, None, str]):
        storepath (Union[Unset, None, str]):
        cert_store_inventory_job_id (Union[Unset, None, str]):
        cert_store_type (Union[Unset, int]):
        approved (Union[Unset, bool]):
        create_if_missing (Union[Unset, bool]):
        properties (Union[Unset, None, str]):
        agent_id (Union[Unset, None, str]):
        agent_assigned (Union[Unset, bool]):
        container_name (Union[Unset, None, str]):
        inventory_schedule (Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]):
        reenrollment_status (Union[Unset, CSSCMSDataModelModelsReenrollmentStatus]):
        set_new_password_allowed (Union[Unset, bool]):
        password (Union[Unset, CSSCMSDataModelModelsKeyfactorSecret]):
    """

    id: Union[Unset, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    container_id: Union[Unset, None, int] = UNSET
    client_machine: Union[Unset, None, str] = UNSET
    storepath: Union[Unset, None, str] = UNSET
    cert_store_inventory_job_id: Union[Unset, None, str] = UNSET
    cert_store_type: Union[Unset, int] = UNSET
    approved: Union[Unset, bool] = UNSET
    create_if_missing: Union[Unset, bool] = UNSET
    properties: Union[Unset, None, str] = UNSET
    agent_id: Union[Unset, None, str] = UNSET
    agent_assigned: Union[Unset, bool] = UNSET
    container_name: Union[Unset, None, str] = UNSET
    inventory_schedule: Union[Unset, "KeyfactorCommonSchedulingKeyfactorSchedule"] = UNSET
    reenrollment_status: Union[Unset, "CSSCMSDataModelModelsReenrollmentStatus"] = UNSET
    set_new_password_allowed: Union[Unset, bool] = UNSET
    password: Union[Unset, "CSSCMSDataModelModelsKeyfactorSecret"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        display_name = self.display_name
        container_id = self.container_id
        client_machine = self.client_machine
        storepath = self.storepath
        cert_store_inventory_job_id = self.cert_store_inventory_job_id
        cert_store_type = self.cert_store_type
        approved = self.approved
        create_if_missing = self.create_if_missing
        properties = self.properties
        agent_id = self.agent_id
        agent_assigned = self.agent_assigned
        container_name = self.container_name
        inventory_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.inventory_schedule, Unset):
            inventory_schedule = self.inventory_schedule.to_dict()

        reenrollment_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reenrollment_status, Unset):
            reenrollment_status = self.reenrollment_status.to_dict()

        set_new_password_allowed = self.set_new_password_allowed
        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if container_id is not UNSET:
            field_dict["containerId"] = container_id
        if client_machine is not UNSET:
            field_dict["clientMachine"] = client_machine
        if storepath is not UNSET:
            field_dict["storepath"] = storepath
        if cert_store_inventory_job_id is not UNSET:
            field_dict["certStoreInventoryJobId"] = cert_store_inventory_job_id
        if cert_store_type is not UNSET:
            field_dict["certStoreType"] = cert_store_type
        if approved is not UNSET:
            field_dict["approved"] = approved
        if create_if_missing is not UNSET:
            field_dict["createIfMissing"] = create_if_missing
        if properties is not UNSET:
            field_dict["properties"] = properties
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if agent_assigned is not UNSET:
            field_dict["agentAssigned"] = agent_assigned
        if container_name is not UNSET:
            field_dict["containerName"] = container_name
        if inventory_schedule is not UNSET:
            field_dict["inventorySchedule"] = inventory_schedule
        if reenrollment_status is not UNSET:
            field_dict["reenrollmentStatus"] = reenrollment_status
        if set_new_password_allowed is not UNSET:
            field_dict["setNewPasswordAllowed"] = set_new_password_allowed
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_keyfactor_secret import CSSCMSDataModelModelsKeyfactorSecret
        from ..models.csscms_data_model_models_reenrollment_status import CSSCMSDataModelModelsReenrollmentStatus
        from ..models.keyfactor_common_scheduling_keyfactor_schedule import KeyfactorCommonSchedulingKeyfactorSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        display_name = d.pop("displayName", UNSET)

        container_id = d.pop("containerId", UNSET)

        client_machine = d.pop("clientMachine", UNSET)

        storepath = d.pop("storepath", UNSET)

        cert_store_inventory_job_id = d.pop("certStoreInventoryJobId", UNSET)

        cert_store_type = d.pop("certStoreType", UNSET)

        approved = d.pop("approved", UNSET)

        create_if_missing = d.pop("createIfMissing", UNSET)

        properties = d.pop("properties", UNSET)

        agent_id = d.pop("agentId", UNSET)

        agent_assigned = d.pop("agentAssigned", UNSET)

        container_name = d.pop("containerName", UNSET)

        _inventory_schedule = d.pop("inventorySchedule", UNSET)
        inventory_schedule: Union[Unset, KeyfactorCommonSchedulingKeyfactorSchedule]
        if isinstance(_inventory_schedule, Unset):
            inventory_schedule = UNSET
        else:
            inventory_schedule = KeyfactorCommonSchedulingKeyfactorSchedule.from_dict(_inventory_schedule)

        _reenrollment_status = d.pop("reenrollmentStatus", UNSET)
        reenrollment_status: Union[Unset, CSSCMSDataModelModelsReenrollmentStatus]
        if isinstance(_reenrollment_status, Unset):
            reenrollment_status = UNSET
        else:
            reenrollment_status = CSSCMSDataModelModelsReenrollmentStatus.from_dict(_reenrollment_status)

        set_new_password_allowed = d.pop("setNewPasswordAllowed", UNSET)

        _password = d.pop("password", UNSET)
        password: Union[Unset, CSSCMSDataModelModelsKeyfactorSecret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = CSSCMSDataModelModelsKeyfactorSecret.from_dict(_password)

        csscms_data_model_models_certificate_store = cls(
            id=id,
            display_name=display_name,
            container_id=container_id,
            client_machine=client_machine,
            storepath=storepath,
            cert_store_inventory_job_id=cert_store_inventory_job_id,
            cert_store_type=cert_store_type,
            approved=approved,
            create_if_missing=create_if_missing,
            properties=properties,
            agent_id=agent_id,
            agent_assigned=agent_assigned,
            container_name=container_name,
            inventory_schedule=inventory_schedule,
            reenrollment_status=reenrollment_status,
            set_new_password_allowed=set_new_password_allowed,
            password=password,
        )

        return csscms_data_model_models_certificate_store
