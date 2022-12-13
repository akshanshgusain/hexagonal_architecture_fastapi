from dependency_injector import containers, providers

from src.banking.adapters.db.orm import Database
from src.banking.adapters.repositories.customer import SqlAlchemyCustomerRepository
from src.banking.adapters.services.customer import DefaultCustomerService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "src.banking.adapters.entrypoints.api.v1"
        ])

    # Db
    db = providers.Singleton(
        Database,
        db_url="postgresql://hello_fastapi:hello_fastapi@localhost:5432/banking"
    )

    # repositories
    customer_repository = providers.Factory(
        SqlAlchemyCustomerRepository,
        session_factory=db.provided.session,
    )

    # services
    customer_service = providers.Factory(
        DefaultCustomerService,
        customer_repository=customer_repository
    )
