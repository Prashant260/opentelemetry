from fastapi import FastAPI
import time

from tracer import tracer

app = FastAPI()


@app.get("/")
def home():

    with tracer.start_as_current_span("home-span"):

        time.sleep(1)

        return {
            "message": "Welcome to OpenTelemetry"
        }


@app.get("/payment")
def payment():

    with tracer.start_as_current_span("payment-span"):

        time.sleep(2)

        return {
            "status": "Payment Successful"
        }


@app.get("/order")
def order():

    with tracer.start_as_current_span("order-span"):

        time.sleep(3)

        return {
            "status": "Order Created"
        }