from typing import Union
from xmlrpc.client import SYSTEM_ERROR

from src.banking.adapters.repositories.customer import SqlAlchemyCustomerRepository
from src.banking.domain.models.models import Customers, customer_factory
from src.banking.domain.ports.common.responses import *
from src.banking.domain.ports.schemas.customers import CustomersResponseDto, CustomersRequestDto
from src.banking.domain.ports.services.customer import CustomerService


class DefaultCustomerService(CustomerService):

    # Constructor Injection
    def __init__(self, customer_repository: SqlAlchemyCustomerRepository):
        super().__init__(customer_repository)
        self.customer_repository: SqlAlchemyCustomerRepository = customer_repository

    def get_all_customers(self) -> ResponseSuccess:
        customers_ = self.customer_repository.find_all()
        customers: list[CustomersResponseDto] = []
        for customer in customers_:
            customers.append(CustomersResponseDto.from_orm(customer))

        return ResponseSuccess(value=customers)

    def get_customer(self, customer_id: str) -> ResponseSuccess:
        customer: Customers = self.customer_repository.by_id(customer_id)
        return ResponseSuccess(value=customer)

    def create_customer(self, customer: CustomersRequestDto) -> Union[ResponseFailure, ResponseSuccess]:
        try:
            customer = customer_factory(customer.name,
                                        customer.city,
                                        customer.zipcode,
                                        customer.date_of_birth)

            print(f"Saved customer before: {customer}")
            customer_ = self.customer_repository.add(customer)
            print(f"Saved customer: {customer_}")
            return ResponseSuccess(value=CustomersResponseDto.from_orm(customer_))

        except Exception as e:
            return ResponseFailure(400, "internal server error")
