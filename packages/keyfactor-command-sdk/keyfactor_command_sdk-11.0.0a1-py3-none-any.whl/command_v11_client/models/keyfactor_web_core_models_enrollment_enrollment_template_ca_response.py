from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyfactor_web_core_models_enrollment_enrollment_ca import KeyfactorWebCoreModelsEnrollmentEnrollmentCA
    from ..models.keyfactor_web_core_models_enrollment_enrollment_template import (
        KeyfactorWebCoreModelsEnrollmentEnrollmentTemplate,
    )


T = TypeVar("T", bound="KeyfactorWebCoreModelsEnrollmentEnrollmentTemplateCAResponse")


@_attrs_define
class KeyfactorWebCoreModelsEnrollmentEnrollmentTemplateCAResponse:
    """
    Attributes:
        templates (Union[Unset, None, List['KeyfactorWebCoreModelsEnrollmentEnrollmentTemplate']]):
        standalone_c_as (Union[Unset, None, List['KeyfactorWebCoreModelsEnrollmentEnrollmentCA']]):
    """

    templates: Union[Unset, None, List["KeyfactorWebCoreModelsEnrollmentEnrollmentTemplate"]] = UNSET
    standalone_c_as: Union[Unset, None, List["KeyfactorWebCoreModelsEnrollmentEnrollmentCA"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        templates: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            if self.templates is None:
                templates = None
            else:
                templates = []
                for templates_item_data in self.templates:
                    templates_item = templates_item_data.to_dict()

                    templates.append(templates_item)

        standalone_c_as: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.standalone_c_as, Unset):
            if self.standalone_c_as is None:
                standalone_c_as = None
            else:
                standalone_c_as = []
                for standalone_c_as_item_data in self.standalone_c_as:
                    standalone_c_as_item = standalone_c_as_item_data.to_dict()

                    standalone_c_as.append(standalone_c_as_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if templates is not UNSET:
            field_dict["templates"] = templates
        if standalone_c_as is not UNSET:
            field_dict["standaloneCAs"] = standalone_c_as

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyfactor_web_core_models_enrollment_enrollment_ca import (
            KeyfactorWebCoreModelsEnrollmentEnrollmentCA,
        )
        from ..models.keyfactor_web_core_models_enrollment_enrollment_template import (
            KeyfactorWebCoreModelsEnrollmentEnrollmentTemplate,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        templates = []
        _templates = d.pop("templates", UNSET)
        for templates_item_data in _templates or []:
            templates_item = KeyfactorWebCoreModelsEnrollmentEnrollmentTemplate.from_dict(templates_item_data)

            templates.append(templates_item)

        standalone_c_as = []
        _standalone_c_as = d.pop("standaloneCAs", UNSET)
        for standalone_c_as_item_data in _standalone_c_as or []:
            standalone_c_as_item = KeyfactorWebCoreModelsEnrollmentEnrollmentCA.from_dict(standalone_c_as_item_data)

            standalone_c_as.append(standalone_c_as_item)

        keyfactor_web_core_models_enrollment_enrollment_template_ca_response = cls(
            templates=templates,
            standalone_c_as=standalone_c_as,
        )

        return keyfactor_web_core_models_enrollment_enrollment_template_ca_response
