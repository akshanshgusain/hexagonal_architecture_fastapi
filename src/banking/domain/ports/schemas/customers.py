from typing import Optional

from pydantic import BaseModel
import datetime


class CustomersResponseDto(BaseModel):
    customer_id: Optional[str] = None
    name: Optional[str] = None
    city: Optional[str] = None
    zipcode: Optional[str] = None
    date_of_birth: Optional[datetime.date] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True


class CustomersRequestDto(BaseModel):
    name: str
    city: str
    zipcode: str
    date_of_birth: datetime.date

    class Config:
        orm_mode = True
