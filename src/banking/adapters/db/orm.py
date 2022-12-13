"""Database module."""

from contextlib import contextmanager, AbstractContextManager
from typing import Callable
import logging

from sqlalchemy import (
    create_engine,
    orm,
    Boolean,
    Column,
    Date,
    MetaData,
    String,
    Table, BigInteger, Sequence, Integer,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, registry

from src.banking.domain.models import models

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:

    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()

    metadata = MetaData()
    mapper_registry = registry(metadata=metadata)

    customers = Table(
        "customers",
        mapper_registry.metadata,
        Column("customer_id", BigInteger, primary_key=True, autoincrement=True),
        Column("name", String, unique=True, nullable=False),
        Column("date_of_birth", Date, nullable=False),
        Column("city", String, nullable=False),
        Column("zipcode", String, nullable=False),
        Column("status", Integer, default=False),
    )

    def start_mappers(self):
        customers_mapper = self.mapper_registry.map_imperatively(
            models.Customers,
            self.customers,
        )
