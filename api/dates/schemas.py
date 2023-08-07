from pydantic import BaseModel


class DateCreate(BaseModel):
    month: int
    day: int


class DateResponse(BaseModel):
    id: int
    month: str
    day: int
    fact: str


class PopularMonth(BaseModel):
    id: int
    month: str
    days_checked: int
