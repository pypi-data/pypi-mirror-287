from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.measurement_type_enum import MeasurementTypeEnum






T = TypeVar("T", bound="TrixelMapUpdate")


@_attrs_define
class TrixelMapUpdate:
    """ Schema for updating the sensor count for a measurement type in a trixel.

        Attributes:
            trixel_id (int): A valid Trixel ID.
            type (MeasurementTypeEnum): Supported measurement types.
            sensor_count (int):
     """

    trixel_id: int
    type: MeasurementTypeEnum
    sensor_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        trixel_id = self.trixel_id

        type = self.type.value

        sensor_count = self.sensor_count


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "trixel_id": trixel_id,
            "type_": type,
            "sensor_count": sensor_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trixel_id = d.pop("trixel_id")

        type = MeasurementTypeEnum(d.pop("type_"))




        sensor_count = d.pop("sensor_count")

        trixel_map_update = cls(
            trixel_id=trixel_id,
            type=type,
            sensor_count=sensor_count,
        )


        trixel_map_update.additional_properties = d
        return trixel_map_update

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
