import re
from pydantic import BaseModel, field_validator

formats = {
    "OLT": r"^[A-Z][A-Z]F-([A-Z0-9]{10}|[A-Z0-9]{10}-[1-9]{1})$",
    "OTB": r"^CA2-[A-Z0-9]{10}-[A-Z]{1,2}[0-9]{1,2}-T[0-9]{1,2}$",
    "CA1": r"^CA1-[A-Z0-9]{10}-[A-Z]{1,2}$",
    "CA2": r"^CA2-[A-Z0-9]{10}-[A-Z]{1,2}[0-9]{1,2}$",
    "FTSBS": r"^P[0-9]{1,2}-[A-Z0-9]{8,10}$",
    "CPE": r"^P[0-9]{1,2}-[A-Za-z0-9\-]+$",
}


class Device(BaseModel):
    device_name: str
    device_type: str

    @field_validator("*")
    def str_strip(cls, value: str) -> str:
        return value.strip()

    @field_validator("device_type")
    def device_type_validation(cls, value: str) -> str:
        if value.upper() not in formats.keys():
            raise ValueError("Invalid Device Type")
        return value.upper()

    def get_device_format(self) -> bool:
        result = re.fullmatch(formats.get(self.device_type), self.device_name)
        if result is not None:
            return True
        return False
