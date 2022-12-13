"""Application module."""

from fastapi import FastAPI


from src.banking.configurator.containers import Container
from src.banking.adapters.entrypoints.api.base import api_router

'''Application factory creates container, wires it with the endpoints module, creates FastAPI app, and setup routes.'''


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()
    db.start_mappers()

    app = FastAPI()
    app.container = container
    app.include_router(api_router)
    return app


# Entry Point
app = create_app()

