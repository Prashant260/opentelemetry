from fastapi import FastAPI
import time

from tracer import tracer

app = FastAPI(title="Order Service")


@app.get("/")
def home():
    with tracer.start_as_current_span("order-home"):
        time.sleep(1)
        return {"service": "order-service", "message": "Order service is running"}


@app.post("/orders")
def create_order():
    with tracer.start_as_current_span("create-order"):
        time.sleep(1)
        return {"status": "Order created"}
