from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.csscms_data_model_models_report_parameters import CSSCMSDataModelModelsReportParameters
    from ..models.csscms_data_model_models_report_schedule import CSSCMSDataModelModelsReportSchedule


T = TypeVar("T", bound="CSSCMSDataModelModelsReport")


@_attrs_define
class CSSCMSDataModelModelsReport:
    """
    Attributes:
        id (Union[Unset, int]):
        scheduled (Union[Unset, None, int]):
        display_name (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        report_path (Union[Unset, None, str]):
        version_number (Union[Unset, None, str]):
        categories (Union[Unset, None, str]):
        short_name (Union[Unset, None, str]):
        in_navigator (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
        remove_duplicates (Union[Unset, bool]):
        uses_collection (Union[Unset, bool]):
        report_parameter (Union[Unset, None, List['CSSCMSDataModelModelsReportParameters']]):
        schedules (Union[Unset, None, List['CSSCMSDataModelModelsReportSchedule']]):
        accepted_schedule_formats (Union[Unset, None, List[str]]):
    """

    id: Union[Unset, int] = UNSET
    scheduled: Union[Unset, None, int] = UNSET
    display_name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    report_path: Union[Unset, None, str] = UNSET
    version_number: Union[Unset, None, str] = UNSET
    categories: Union[Unset, None, str] = UNSET
    short_name: Union[Unset, None, str] = UNSET
    in_navigator: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    remove_duplicates: Union[Unset, bool] = UNSET
    uses_collection: Union[Unset, bool] = UNSET
    report_parameter: Union[Unset, None, List["CSSCMSDataModelModelsReportParameters"]] = UNSET
    schedules: Union[Unset, None, List["CSSCMSDataModelModelsReportSchedule"]] = UNSET
    accepted_schedule_formats: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        scheduled = self.scheduled
        display_name = self.display_name
        description = self.description
        report_path = self.report_path
        version_number = self.version_number
        categories = self.categories
        short_name = self.short_name
        in_navigator = self.in_navigator
        favorite = self.favorite
        remove_duplicates = self.remove_duplicates
        uses_collection = self.uses_collection
        report_parameter: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_parameter, Unset):
            if self.report_parameter is None:
                report_parameter = None
            else:
                report_parameter = []
                for report_parameter_item_data in self.report_parameter:
                    report_parameter_item = report_parameter_item_data.to_dict()

                    report_parameter.append(report_parameter_item)

        schedules: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            if self.schedules is None:
                schedules = None
            else:
                schedules = []
                for schedules_item_data in self.schedules:
                    schedules_item = schedules_item_data.to_dict()

                    schedules.append(schedules_item)

        accepted_schedule_formats: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.accepted_schedule_formats, Unset):
            if self.accepted_schedule_formats is None:
                accepted_schedule_formats = None
            else:
                accepted_schedule_formats = self.accepted_schedule_formats

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if scheduled is not UNSET:
            field_dict["scheduled"] = scheduled
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if report_path is not UNSET:
            field_dict["reportPath"] = report_path
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number
        if categories is not UNSET:
            field_dict["categories"] = categories
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if in_navigator is not UNSET:
            field_dict["inNavigator"] = in_navigator
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if remove_duplicates is not UNSET:
            field_dict["removeDuplicates"] = remove_duplicates
        if uses_collection is not UNSET:
            field_dict["usesCollection"] = uses_collection
        if report_parameter is not UNSET:
            field_dict["reportParameter"] = report_parameter
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if accepted_schedule_formats is not UNSET:
            field_dict["acceptedScheduleFormats"] = accepted_schedule_formats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.csscms_data_model_models_report_parameters import CSSCMSDataModelModelsReportParameters
        from ..models.csscms_data_model_models_report_schedule import CSSCMSDataModelModelsReportSchedule

        d = {x[0].lower()+x[1:]:src_dict[x] for x in src_dict.keys()}
        id = d.pop("id", UNSET)

        scheduled = d.pop("scheduled", UNSET)

        display_name = d.pop("displayName", UNSET)

        description = d.pop("description", UNSET)

        report_path = d.pop("reportPath", UNSET)

        version_number = d.pop("versionNumber", UNSET)

        categories = d.pop("categories", UNSET)

        short_name = d.pop("shortName", UNSET)

        in_navigator = d.pop("inNavigator", UNSET)

        favorite = d.pop("favorite", UNSET)

        remove_duplicates = d.pop("removeDuplicates", UNSET)

        uses_collection = d.pop("usesCollection", UNSET)

        report_parameter = []
        _report_parameter = d.pop("reportParameter", UNSET)
        for report_parameter_item_data in _report_parameter or []:
            report_parameter_item = CSSCMSDataModelModelsReportParameters.from_dict(report_parameter_item_data)

            report_parameter.append(report_parameter_item)

        schedules = []
        _schedules = d.pop("schedules", UNSET)
        for schedules_item_data in _schedules or []:
            schedules_item = CSSCMSDataModelModelsReportSchedule.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        accepted_schedule_formats = cast(List[str], d.pop("acceptedScheduleFormats", UNSET))

        csscms_data_model_models_report = cls(
            id=id,
            scheduled=scheduled,
            display_name=display_name,
            description=description,
            report_path=report_path,
            version_number=version_number,
            categories=categories,
            short_name=short_name,
            in_navigator=in_navigator,
            favorite=favorite,
            remove_duplicates=remove_duplicates,
            uses_collection=uses_collection,
            report_parameter=report_parameter,
            schedules=schedules,
            accepted_schedule_formats=accepted_schedule_formats,
        )

        return csscms_data_model_models_report
