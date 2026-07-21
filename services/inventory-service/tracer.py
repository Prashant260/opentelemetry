from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

resource = Resource.create(
    {
        "service.name": "inventory-service",
        "service.version": "1.0.0",
        "deployment.environment": "development",
    }
)

provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)
provider.add_span_processor(BatchSpanProcessor(exporter))

tracer = trace.get_tracer(__name__)
