from pydantic import BaseModel, Field, AliasChoices, model_validator
from typing import Literal, Union, List, Optional

class VendorV0(BaseModel):
    vendor_leakage_current_uA: Union[None,float] = Field(validation_alias=AliasChoices('vendor_leakage_current_uA','Vendor Leakage Current [uA]'))
    vendor_breakdown_voltage_V: Union[None,float] = Field(validation_alias=AliasChoices('vendor_breakdown_voltage_V','Vendor Breakdown Voltage [V]'))
    vendor_category: Union[None,Literal["BAD", "GOOD", "MEDIUM"]] = Field(validation_alias=AliasChoices('vendor_category','Vendor Category'))
    vendor_gain_category: Union[None,Literal["A", "B", "C"]] = Field(validation_alias=AliasChoices('vendor_gain_category','Vendor Gain Category'))

    current: Union[None,List[float]] = Field(validation_alias=AliasChoices('current','Current'))
    voltage: Union[None,List[float]] = Field(validation_alias=AliasChoices('voltage','Voltage'))

    @model_validator(mode='after')
    def same_lengths(self):
        if len(self.current) != len(self.voltage):
            raise ValueError(f'Current and voltage arrays should have the same lengths. Length of Current, Length of Voltage = ({len(self.current)}, {len(self.voltage)})')
        return self