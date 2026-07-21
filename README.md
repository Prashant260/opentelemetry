# Cloud Native Observability Platform

This workspace contains a starter structure for a cloud-native observability platform.

## Structure

- services/ - application services
- collector/ - OpenTelemetry Collector config
- grafana/ - Grafana datasource config
- prometheus/ - Prometheus config
- loki/ - Loki config
- postgres/ - Postgres storage folder
- redis/ - Redis storage folder
- kubernetes/ - deployment manifests and Helm chart directory
- docs/ - documentation
- dashboards/ - dashboard definitions

## Run

```bash
docker compose up --build
```
