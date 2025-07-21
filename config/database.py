# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
# import os
# from dotenv import load_dotenv

# load_dotenv()


# # Create a new client and connect to the server
# client = MongoClient(os.getenv("MONGODB_URL"), server_api=ServerApi('1'))

# db = client["ecommerce"]
# products_collection = db["products"]
# orders_collection = db["orders"]
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URL"), tls=True, tlsCAFile=certifi.where())

db = client["ecommerce"]
products_collection = db["products"]
orders_collection = db["orders"]


