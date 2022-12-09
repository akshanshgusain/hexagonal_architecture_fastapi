from fastapi import FastAPI

from .containers import Container
from . import endpoints


def create_app() -> FastAPI:
    container = Container()

    # Create Database
    create_db(container)

    # Create app instance
    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


def create_db(container: Container):
    db = container.db()
    db.create_database()


# Entry point
app = create_app()
