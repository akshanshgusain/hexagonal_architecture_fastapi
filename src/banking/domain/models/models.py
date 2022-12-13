import datetime
import uuid
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Customers:
    name: str
    city: str
    zipcode: str
    date_of_birth: datetime.date
    status: int
    customer_id: Optional[str] = None

    @classmethod
    def from_dict(cls, dict_):
        return cls(**dict_)

    def to_dict(self):
        return asdict(self)

    def __eq__(self, other):
        if not isinstance(other, Customers):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


def customer_factory(
        name: str,
        city: str,
        zipcode: str,
        date_of_birth: datetime.date,
) -> Customers:
    customer = Customers(
        name=name,
        city=city,
        zipcode=zipcode,
        date_of_birth=date_of_birth,
        status=1,
    )
    return customer
