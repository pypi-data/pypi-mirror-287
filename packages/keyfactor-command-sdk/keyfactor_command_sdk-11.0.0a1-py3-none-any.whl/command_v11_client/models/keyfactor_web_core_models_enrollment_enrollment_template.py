from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_extended_key_usage import CSSCMSDataModelModelsExtendedKeyUsage
    from ..models.csscms_data_model_models_templates_template_enrollment_field import (
        CSSCMSDataModelModelsTemplatesTemplateEnrollmentField,
    )
    from ..models.csscms_data_model_models_templates_template_metadata_field import (
        CSSCMSDataModelModelsTemplatesTemplateMetadataField,
    )
    from ..models.csscms_data_model_models_templates_template_regex import CSSCMSDataModelModelsTemplatesTemplateRegex
    from ..models.keyfactor_web_core_models_enrollment_enrollment_ca import KeyfactorWebCoreModelsEnrollmentEnrollmentCA
    from ..models.keyfactor_web_core_models_enrollment_enrollment_template_policy import (
        KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy,
    )


T = TypeVar("T", bound="KeyfactorWebCoreModelsEnrollmentEnrollmentTemplate")


@_attrs_define
class KeyfactorWebCoreModelsEnrollmentEnrollmentTemplate:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, None, str]):
        display_name (Union[Unset, None, str]):
        forest (Union[Unset, None, str]):
        requires_approval (Union[Unset, bool]):
        rfc_enforcement (Union[Unset, bool]):
        c_as (Union[Unset, None, List['KeyfactorWebCoreModelsEnrollmentEnrollmentCA']]):
        enrollment_fields (Union[Unset, None, List['CSSCMSDataModelModelsTemplatesTemplateEnrollmentField']]):
        metadata_fields (Union[Unset, None, List['CSSCMSDataModelModelsTemplatesTemplateMetadataField']]):
        regexes (Union[Unset, None, List['CSSCMSDataModelModelsTemplatesTemplateRegex']]):
        extended_key_usages (Union[Unset, None, List['CSSCMSDataModelModelsExtendedKeyUsage']]):
        enrollment_template_policy (Union[Unset, KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy]):
        key_size (Union[Unset, None, str]):
        key_type (Union[Unset, None, str]):
        curve (Union[Unset, None, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, None, str] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    forest: Union[Unset, None, str] = UNSET
    requires_approval: Union[Unset, bool] = UNSET
    rfc_enforcement: Union[Unset, bool] = UNSET
    c_as: Union[Unset, None, List["KeyfactorWebCoreModelsEnrollmentEnrollmentCA"]] = UNSET
    enrollment_fields: Union[Unset, None, List["CSSCMSDataModelModelsTemplatesTemplateEnrollmentField"]] = UNSET
    metadata_fields: Union[Unset, None, List["CSSCMSDataModelModelsTemplatesTemplateMetadataField"]] = UNSET
    regexes: Union[Unset, None, List["CSSCMSDataModelModelsTemplatesTemplateRegex"]] = UNSET
    extended_key_usages: Union[Unset, None, List["CSSCMSDataModelModelsExtendedKeyUsage"]] = UNSET
    enrollment_template_policy: Union[Unset, "KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy"] = UNSET
    key_size: Union[Unset, None, str] = UNSET
    key_type: Union[Unset, None, str] = UNSET
    curve: Union[Unset, None, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        display_name = self.display_name
        forest = self.forest
        requires_approval = self.requires_approval
        rfc_enforcement = self.rfc_enforcement
        c_as: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.c_as, Unset):
            if self.c_as is None:
                c_as = None
            else:
                c_as = []
                for c_as_item_data in self.c_as:
                    c_as_item = c_as_item_data.to_dict()

                    c_as.append(c_as_item)

        enrollment_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enrollment_fields, Unset):
            if self.enrollment_fields is None:
                enrollment_fields = None
            else:
                enrollment_fields = []
                for enrollment_fields_item_data in self.enrollment_fields:
                    enrollment_fields_item = enrollment_fields_item_data.to_dict()

                    enrollment_fields.append(enrollment_fields_item)

        metadata_fields: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata_fields, Unset):
            if self.metadata_fields is None:
                metadata_fields = None
            else:
                metadata_fields = []
                for metadata_fields_item_data in self.metadata_fields:
                    metadata_fields_item = metadata_fields_item_data.to_dict()

                    metadata_fields.append(metadata_fields_item)

        regexes: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.regexes, Unset):
            if self.regexes is None:
                regexes = None
            else:
                regexes = []
                for regexes_item_data in self.regexes:
                    regexes_item = regexes_item_data.to_dict()

                    regexes.append(regexes_item)

        extended_key_usages: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extended_key_usages, Unset):
            if self.extended_key_usages is None:
                extended_key_usages = None
            else:
                extended_key_usages = []
                for extended_key_usages_item_data in self.extended_key_usages:
                    extended_key_usages_item = extended_key_usages_item_data.to_dict()

                    extended_key_usages.append(extended_key_usages_item)

        enrollment_template_policy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_template_policy, Unset):
            enrollment_template_policy = self.enrollment_template_policy.to_dict()

        key_size = self.key_size
        key_type = self.key_type
        curve = self.curve

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if forest is not UNSET:
            field_dict["forest"] = forest
        if requires_approval is not UNSET:
            field_dict["requiresApproval"] = requires_approval
        if rfc_enforcement is not UNSET:
            field_dict["rfcEnforcement"] = rfc_enforcement
        if c_as is not UNSET:
            field_dict["cAs"] = c_as
        if enrollment_fields is not UNSET:
            field_dict["enrollmentFields"] = enrollment_fields
        if metadata_fields is not UNSET:
            field_dict["metadataFields"] = metadata_fields
        if regexes is not UNSET:
            field_dict["regexes"] = regexes
        if extended_key_usages is not UNSET:
            field_dict["extendedKeyUsages"] = extended_key_usages
        if enrollment_template_policy is not UNSET:
            field_dict["enrollmentTemplatePolicy"] = enrollment_template_policy
        if key_size is not UNSET:
            field_dict["keySize"] = key_size
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if curve is not UNSET:
            field_dict["curve"] = curve

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_extended_key_usage import CSSCMSDataModelModelsExtendedKeyUsage
        from ..models.csscms_data_model_models_templates_template_enrollment_field import (
            CSSCMSDataModelModelsTemplatesTemplateEnrollmentField,
        )
        from ..models.csscms_data_model_models_templates_template_metadata_field import (
            CSSCMSDataModelModelsTemplatesTemplateMetadataField,
        )
        from ..models.csscms_data_model_models_templates_template_regex import (
            CSSCMSDataModelModelsTemplatesTemplateRegex,
        )
        from ..models.keyfactor_web_core_models_enrollment_enrollment_ca import (
            KeyfactorWebCoreModelsEnrollmentEnrollmentCA,
        )
        from ..models.keyfactor_web_core_models_enrollment_enrollment_template_policy import (
            KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy,
        )

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        forest = d.pop("forest", UNSET)

        requires_approval = d.pop("requiresApproval", UNSET)

        rfc_enforcement = d.pop("rfcEnforcement", UNSET)

        c_as = []
        _c_as = d.pop("cAs", UNSET)
        for c_as_item_data in _c_as or []:
            c_as_item = KeyfactorWebCoreModelsEnrollmentEnrollmentCA.from_dict(c_as_item_data)

            c_as.append(c_as_item)

        enrollment_fields = []
        _enrollment_fields = d.pop("enrollmentFields", UNSET)
        for enrollment_fields_item_data in _enrollment_fields or []:
            enrollment_fields_item = CSSCMSDataModelModelsTemplatesTemplateEnrollmentField.from_dict(
                enrollment_fields_item_data
            )

            enrollment_fields.append(enrollment_fields_item)

        metadata_fields = []
        _metadata_fields = d.pop("metadataFields", UNSET)
        for metadata_fields_item_data in _metadata_fields or []:
            metadata_fields_item = CSSCMSDataModelModelsTemplatesTemplateMetadataField.from_dict(
                metadata_fields_item_data
            )

            metadata_fields.append(metadata_fields_item)

        regexes = []
        _regexes = d.pop("regexes", UNSET)
        for regexes_item_data in _regexes or []:
            regexes_item = CSSCMSDataModelModelsTemplatesTemplateRegex.from_dict(regexes_item_data)

            regexes.append(regexes_item)

        extended_key_usages = []
        _extended_key_usages = d.pop("extendedKeyUsages", UNSET)
        for extended_key_usages_item_data in _extended_key_usages or []:
            extended_key_usages_item = CSSCMSDataModelModelsExtendedKeyUsage.from_dict(extended_key_usages_item_data)

            extended_key_usages.append(extended_key_usages_item)

        _enrollment_template_policy = d.pop("enrollmentTemplatePolicy", UNSET)
        enrollment_template_policy: Union[Unset, KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy]
        if isinstance(_enrollment_template_policy, Unset):
            enrollment_template_policy = UNSET
        else:
            enrollment_template_policy = KeyfactorWebCoreModelsEnrollmentEnrollmentTemplatePolicy.from_dict(
                _enrollment_template_policy
            )

        key_size = d.pop("keySize", UNSET)

        key_type = d.pop("keyType", UNSET)

        curve = d.pop("curve", UNSET)

        keyfactor_web_core_models_enrollment_enrollment_template = cls(
            id=id,
            name=name,
            display_name=display_name,
            forest=forest,
            requires_approval=requires_approval,
            rfc_enforcement=rfc_enforcement,
            c_as=c_as,
            enrollment_fields=enrollment_fields,
            metadata_fields=metadata_fields,
            regexes=regexes,
            extended_key_usages=extended_key_usages,
            enrollment_template_policy=enrollment_template_policy,
            key_size=key_size,
            key_type=key_type,
            curve=curve,
        )

        return keyfactor_web_core_models_enrollment_enrollment_template
