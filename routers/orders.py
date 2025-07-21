from fastapi import APIRouter
from models.orders import OrderCreate
from schemas.orders import create_order, get_orders_by_user

router = APIRouter()

@router.post("/", status_code=201)
def add_order(order: OrderCreate):
    order_dict = order.dict()
    return create_order(order_dict)

@router.get("/{user_id}", status_code=200)
def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    return get_orders_by_user(user_id, limit, offset)
