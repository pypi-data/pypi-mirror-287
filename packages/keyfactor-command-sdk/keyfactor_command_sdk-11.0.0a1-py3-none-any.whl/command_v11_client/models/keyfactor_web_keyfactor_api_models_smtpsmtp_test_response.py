from typing import Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsSMTPSMTPTestResponse")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsSMTPSMTPTestResponse:
    """
    Attributes:
        host (Union[Unset, None, str]):
        id (Union[Unset, int]):
        port (Union[Unset, int]):
        relay_authentication_type (Union[Unset, int]):
        relay_username (Union[Unset, None, str]):
        sender_account (Union[Unset, None, str]):
        sender_name (Union[Unset, None, str]):
        test_recipient (Union[Unset, None, str]):
        use_ssl (Union[Unset, bool]):
    """

    host: Union[Unset, None, str] = UNSET
    id: Union[Unset, int] = UNSET
    port: Union[Unset, int] = UNSET
    relay_authentication_type: Union[Unset, int] = UNSET
    relay_username: Union[Unset, None, str] = UNSET
    sender_account: Union[Unset, None, str] = UNSET
    sender_name: Union[Unset, None, str] = UNSET
    test_recipient: Union[Unset, None, str] = UNSET
    use_ssl: Union[Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        id = self.id
        port = self.port
        relay_authentication_type = self.relay_authentication_type
        relay_username = self.relay_username
        sender_account = self.sender_account
        sender_name = self.sender_name
        test_recipient = self.test_recipient
        use_ssl = self.use_ssl

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if id is not UNSET:
            field_dict["id"] = id
        if port is not UNSET:
            field_dict["port"] = port
        if relay_authentication_type is not UNSET:
            field_dict["relayAuthenticationType"] = relay_authentication_type
        if relay_username is not UNSET:
            field_dict["relayUsername"] = relay_username
        if sender_account is not UNSET:
            field_dict["senderAccount"] = sender_account
        if sender_name is not UNSET:
            field_dict["senderName"] = sender_name
        if test_recipient is not UNSET:
            field_dict["testRecipient"] = test_recipient
        if use_ssl is not UNSET:
            field_dict["useSSL"] = use_ssl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        host = d.pop("host", UNSET)

        id = d.pop("id", UNSET)

        port = d.pop("port", UNSET)

        relay_authentication_type = d.pop("relayAuthenticationType", UNSET)

        relay_username = d.pop("relayUsername", UNSET)

        sender_account = d.pop("senderAccount", UNSET)

        sender_name = d.pop("senderName", UNSET)

        test_recipient = d.pop("testRecipient", UNSET)

        use_ssl = d.pop("useSSL", UNSET)

        keyfactor_web_keyfactor_api_models_smtpsmtp_test_response = cls(
            host=host,
            id=id,
            port=port,
            relay_authentication_type=relay_authentication_type,
            relay_username=relay_username,
            sender_account=sender_account,
            sender_name=sender_name,
            test_recipient=test_recipient,
            use_ssl=use_ssl,
        )

        return keyfactor_web_keyfactor_api_models_smtpsmtp_test_response
