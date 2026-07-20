from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetery.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor   
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

resource = Resource.create(
    {
        "service.name": "order-service",
        "service.version": "1.0.0",
        "deployment.environment": "development",
    }
)

provider = TracerProvider(resource=resource)

trace.set_tracer_provider(provider)

exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",
    insecure=True,
)

span_processor = BatchSpanProcessor(exporter)

provider.add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)