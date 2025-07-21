from config.database import products_collection
from bson import ObjectId

def create_product(data: dict) -> dict:
    result = products_collection.insert_one(data)
    return {"id": str(result.inserted_id)}

def list_products(filters: dict, limit: int, offset: int) -> dict:
    cursor = products_collection.find(filters).skip(offset).limit(limit)
    products = []
    for product in cursor:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        })

    return {
        "data": products,
        "page": {
            "next": str(offset + limit),
            "limit": limit,
            "previous": offset - limit
        }
    }
