import datetime
from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.keyfactor_auditing_enums_audit_log_level import KeyfactorAuditingEnumsAuditLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorAuditingQueryingAuditLogEntry")


@_attrs_define
class KeyfactorAuditingQueryingAuditLogEntry:
    """
    Attributes:
        id (Union[Unset, int]):
        timestamp (Union[Unset, datetime.datetime]):
        message (Union[Unset, None, str]):
        signature (Union[Unset, None, str]):
        category (Union[Unset, int]):
        operation (Union[Unset, int]):
        level (Union[Unset, KeyfactorAuditingEnumsAuditLogLevel]):
        user (Union[Unset, None, str]):
        entity_type (Union[Unset, None, str]):
        audit_identifier (Union[Unset, None, str]):
        immutable_identifier (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    message: Union[Unset, None, str] = UNSET
    signature: Union[Unset, None, str] = UNSET
    category: Union[Unset, int] = UNSET
    operation: Union[Unset, int] = UNSET
    level: Union[Unset, KeyfactorAuditingEnumsAuditLogLevel] = UNSET
    user: Union[Unset, None, str] = UNSET
    entity_type: Union[Unset, None, str] = UNSET
    audit_identifier: Union[Unset, None, str] = UNSET
    immutable_identifier: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()[:-6]+'Z'

        message = self.message
        signature = self.signature
        category = self.category
        operation = self.operation
        level: Union[Unset, int] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        user = self.user
        entity_type = self.entity_type
        audit_identifier = self.audit_identifier
        immutable_identifier = self.immutable_identifier

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if message is not UNSET:
            field_dict["message"] = message
        if signature is not UNSET:
            field_dict["signature"] = signature
        if category is not UNSET:
            field_dict["category"] = category
        if operation is not UNSET:
            field_dict["operation"] = operation
        if level is not UNSET:
            field_dict["level"] = level
        if user is not UNSET:
            field_dict["user"] = user
        if entity_type is not UNSET:
            field_dict["entityType"] = entity_type
        if audit_identifier is not UNSET:
            field_dict["auditIdentifier"] = audit_identifier
        if immutable_identifier is not UNSET:
            field_dict["immutableIdentifier"] = immutable_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        message = d.pop("message", UNSET)

        signature = d.pop("signature", UNSET)

        category = d.pop("category", UNSET)

        operation = d.pop("operation", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, KeyfactorAuditingEnumsAuditLogLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = KeyfactorAuditingEnumsAuditLogLevel(_level)

        user = d.pop("user", UNSET)

        entity_type = d.pop("entityType", UNSET)

        audit_identifier = d.pop("auditIdentifier", UNSET)

        immutable_identifier = d.pop("immutableIdentifier", UNSET)

        keyfactor_auditing_querying_audit_log_entry = cls(
            id=id,
            timestamp=timestamp,
            message=message,
            signature=signature,
            category=category,
            operation=operation,
            level=level,
            user=user,
            entity_type=entity_type,
            audit_identifier=audit_identifier,
            immutable_identifier=immutable_identifier,
        )

        return keyfactor_auditing_querying_audit_log_entry
