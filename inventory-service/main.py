from fastapi import FastAPI
import time

from tracer import tracer

app = FastAPI(title="Inventory Service")


@app.get("/")
def home():
    with tracer.start_as_current_span("inventory-home"):
        time.sleep(0.5)
        return {"service": "inventory-service", "message": "Inventory service is running"}


@app.get("/inventory")
def check_inventory():
    with tracer.start_as_current_span("check-inventory"):
        time.sleep(1)
        return {"status": "Inventory available"}
