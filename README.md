# Observable Python Flask Service

A small HTTP service used as a CI/CD, container and observability test workload.

## Endpoints

- `GET /` — service information
- `GET /health` — liveness endpoint
- `GET /ready` — readiness endpoint
- `GET /metrics` — Prometheus metrics

## Local run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python application.py
curl http://localhost:8080/health
```

## Container run

```bash
docker build -t python-flask-lab .
docker run --rm -p 8080:8080 python-flask-lab
```

## Portfolio purpose

The service is intentionally simple. Its value is as a predictable workload for testing health probes, container builds, Prometheus scraping, CI validation and deployment automation.
