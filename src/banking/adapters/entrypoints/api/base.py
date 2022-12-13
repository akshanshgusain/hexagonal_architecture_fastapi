from fastapi import APIRouter

from src.banking.adapters.entrypoints.api.v1 import customer_routes as customer_routes_v1

api_router = APIRouter()
api_router.include_router(customer_routes_v1.router, prefix="/v1/customers", tags=["customers_v1"])

