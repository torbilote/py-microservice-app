from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_serializer

config = ConfigDict(extra="forbid", strict=True)


class Name(BaseModel):
    model_config = config

    first: str
    last: str


class Address(BaseModel):
    model_config = config

    city: str


class Sale(BaseModel):
    model_config = config

    date: datetime
    value: int

    @field_serializer("date")
    def serialize_datetime(self, date: datetime, _info) -> str:
        return date.strftime("%Y-%m-%d %H:%M:%S")


class Record(BaseModel):
    model_config = config

    name: Name
    address: Address
    sale: Sale
