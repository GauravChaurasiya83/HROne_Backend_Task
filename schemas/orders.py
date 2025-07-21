from config.database import orders_collection, products_collection
from bson import ObjectId

def create_order(data: dict) -> dict:
    items = data["items"]
    total_amount = 0

    for item in items:
        product = products_collection.find_one({"_id": ObjectId(item["product_id"])})
        if product:
            total_amount += product["price"] * item["quantity"]

    order_data = {
        "user_id": data["user_id"],
        "items": items,
        "total_amount": total_amount
    }

    result = orders_collection.insert_one(order_data)
    return {"id": str(result.inserted_id)}

def get_orders_by_user(user_id: str, limit: int, offset: int) -> dict:
    query = {"user_id": user_id}
    filteredOrders = orders_collection.find(query).skip(offset).limit(limit)
    orders = []

    for order in filteredOrders:
        items = []
        for item in order.get("items", []):
            product = products_collection.find_one({"_id": ObjectId(item["product_id"])})
            product_details = {
                "name": product["name"],
                "id": str(product["_id"])
            } if product else {}

            items.append({
                "productDetails": product_details,
                "qty": item["quantity"]
            })

        orders.append({
            "id": str(order["_id"]),
            "items": items,
            "total": order["total_amount"]
        })

    return {
        "data": orders,
        "page": {
            "next": str(offset + limit),
            "limit": limit,
            "previous": offset - limit
        }
    }
