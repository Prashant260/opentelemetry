from fastapi import FastAPI
import time

from tracer import tracer

app = FastAPI(title="Payment Service")


@app.get("/")
def home():
    with tracer.start_as_current_span("payment-home"):
        time.sleep(0.5)
        return {"service": "payment-service", "message": "Payment service is running"}


@app.post("/payments")
def create_payment():
    with tracer.start_as_current_span("create-payment"):
        time.sleep(1)
        return {"status": "Payment processed"}
