from fastapi import FastAPI

app = FastAPI(debug=True)

from orders.api.v1 import api
