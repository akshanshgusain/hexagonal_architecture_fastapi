import json

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response
from fastapi.encoders import jsonable_encoder

from src.banking.adapters.entrypoints import STATUS_CODES
from src.banking.configurator.containers import Container
from src.banking.domain.ports.schemas.customers import CustomersRequestDto
from src.banking.domain.ports.services.customer import CustomerService

router = APIRouter()


@router.get("/")
@inject
def get_all_customers(customer_service: CustomerService = Depends(Provide[Container.customer_service]), ):  # Injected
    response = customer_service.get_all_customers()
    data = jsonable_encoder(response.value)

    return Response(
        content=json.dumps(data),
        media_type="application/json",
        status_code=STATUS_CODES[response.type]
    )


@router.get("/{c_id}")
@inject
def get_customer(c_id: int, customer_service: CustomerService = Depends(Provide[Container.customer_service])):
    response = customer_service.get_customer(str(c_id))
    data = jsonable_encoder(response.value)
    return Response(
        content=json.dumps(data),
        media_type="application/json",
        status_code=STATUS_CODES[response.type]
    )


@router.post("/")
@inject
def add_customer(
        customer: CustomersRequestDto,
        customer_service: CustomerService = Depends(Provide[Container.customer_service])):
    response = customer_service.create_customer(customer)
    data = jsonable_encoder(response.value)
    return Response(
        content=json.dumps(data),
        media_type="application/json",
        status_code=200
    )
