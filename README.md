# HROne Backend Task

This project is a backend system built using **FastAPI** and **MongoDB** to manage products and user orders. It includes APIs for creating and listing products and placing orders with automatic total calculation.

## Tech Stack

- **FastAPI**
- **Python 3.10+**
- **MongoDB** with `pymongo`
- **Uvicorn**
- **Pydantic** for schema validation

## Project Structure:

├── config/
│ └── __init__.py
│ └── database.py
├── models/
│ ├── orders.py
│ └── products.py
├── routers/
│ ├── orders.py
│ └── products.py
├── schemas/
│ ├── orders.py
│ └── products.py
├── .env
├── main.py
├── requirements.txt
└── README.md