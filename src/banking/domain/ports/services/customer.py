from abc import ABC, abstractmethod
from typing import Union

from src.banking.domain.ports.repositories.customer import CustomerRepository
from src.banking.domain.ports.common.responses import *
from src.banking.domain.ports.schemas.customers import CustomersRequestDto


class CustomerService(ABC):
    def __init__(self, customer_repository: CustomerRepository):
        self.customer_repository: CustomerRepository = customer_repository

    @abstractmethod
    def get_all_customers(self) -> ResponseSuccess:
        raise NotImplementedError

    @abstractmethod
    def get_customer(self, customer_id: str) -> ResponseSuccess:
        raise NotImplementedError

    @abstractmethod
    def create_customer(self, customer: CustomersRequestDto) -> Union[ResponseFailure, ResponseSuccess]:
        raise NotImplementedError
