from abc import ABC, abstractmethod

from src.banking.domain.models.models import Customers


class CustomerRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Customers]:
        raise NotImplementedError

    @abstractmethod
    def by_id(self, id_: str) -> Customers:
        raise NotImplementedError

    @abstractmethod
    def add(self, customer: Customers) -> Customers:
        raise NotImplementedError

    @abstractmethod
    def update(self, customer: Customers) -> Customers:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id_: int):
        raise NotImplementedError
