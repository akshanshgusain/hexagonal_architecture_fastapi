from src.banking.domain.models.models import Customers
from src.banking.domain.ports.repositories.customer import CustomerRepository
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session


class SqlAlchemyCustomerRepository(CustomerRepository):

    # Constructor Injection
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    def find_all(self) -> list[Customers]:
        with self.session_factory() as session:
            return session.query(Customers).all()

    def by_id(self, id_: str) -> Customers:
        with self.session_factory() as session:
            return session.query(Customers).filter_by(customer_id=id_).first()

    def add(self, customer: Customers) -> Customers:
        with self.session_factory() as session:
            session.add(customer)
            session.commit()
            session.refresh(customer)
            return customer

    def update(self, customer: Customers) -> Customers:
        with self.session_factory() as session:
            existing_customer = session.query(Customers).filter_by(customer_id=customer.customer_id).first()
            existing_customer.city = customer.city
            existing_customer.zipcode = customer.zipcode
            existing_customer.date_of_birth = customer.date_of_birth
            existing_customer.status = customer.status
            session.commit()
            session.refresh(existing_customer)
            return existing_customer

    def delete(self, id_: int):
        pass