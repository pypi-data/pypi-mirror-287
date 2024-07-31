from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionFavoriteRequest")


@_attrs_define
class KeyfactorWebKeyfactorApiModelsCertificateCollectionsCertificateCollectionFavoriteRequest:
    """
    Attributes:
        show_in_navigator (bool):
    """

    show_in_navigator: bool

    def to_dict(self) -> Dict[str, Any]:
        show_in_navigator = self.show_in_navigator

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "showInNavigator": show_in_navigator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        show_in_navigator = d.pop("showInNavigator")

        keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_favorite_request = cls(
            show_in_navigator=show_in_navigator,
        )

        return keyfactor_web_keyfactor_api_models_certificate_collections_certificate_collection_favorite_request
