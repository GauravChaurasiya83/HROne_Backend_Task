from fastapi import APIRouter, Query
from models.products import ProductCreate
from schemas.products import create_product, list_products

router = APIRouter()

@router.post("/", status_code=201)
def add_product(product: ProductCreate):
    return create_product(product.dict())

@router.get("/", status_code=200)
def get_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
):
    filters = {}
    if name:
        filters["name"] = {"$regex": name, "$options": "i"}
    if size:
        filters["sizes.size"] = size

    return list_products(filters, limit, offset)
