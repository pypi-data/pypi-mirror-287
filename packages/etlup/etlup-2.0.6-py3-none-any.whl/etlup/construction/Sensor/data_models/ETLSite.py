from pydantic import BaseModel, Field, AliasChoices, model_validator
from typing import Literal, Union, List, Optional

class ETLSiteV0(BaseModel):
    etl_leakage_current_uA: Union[None,float] = Field(validation_alias=AliasChoices('etl_leakage_current_uA','ETL Leakage Current [uA]'))
    etl_breakdown_voltage_V: Union[None,float] = Field(validation_alias=AliasChoices('etl_breakdown_voltage_V','ETL Breakdown Voltage [V]'))
    etl_category: Union[None,Literal["BAD", "GOOD", "MEDIUM"]] = Field(validation_alias=AliasChoices('etl_category','ETL Category'))
    etl_gain_category: Union[None,Literal["A", "B", "C"]] = Field(validation_alias=AliasChoices('etl_gain_category','ETL Gain Category'))

    current: Union[None,List[float]] = Field(validation_alias=AliasChoices('current','Current'))
    voltage: Union[None,List[float]] = Field(validation_alias=AliasChoices('voltage','Voltage'))

    interpad_resistance_GOhm: Optional[float] = None #not required can be None
    vgl_V: Optional[List[float]] = None
    current_stability: Optional[float] = None

    @model_validator(mode='after')
    def same_lengths(self):
        if len(self.current) != len(self.voltage):
            raise ValueError(f'Current and voltage arrays should have the same lengths. Length of Current, Length of Voltage = ({len(self.current)}, {len(self.voltage)})')
        return self