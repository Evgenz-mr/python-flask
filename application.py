from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)
REQUESTS = Counter("flask_http_requests_total", "HTTP requests", ["method", "path", "status"])
LATENCY = Histogram("flask_http_request_duration_seconds", "HTTP request latency", ["path"])

@app.before_request
def _timer_start():
    request._started_at = time.time()

@app.after_request
def _record(response):
    path = request.url_rule.rule if request.url_rule else request.path
    REQUESTS.labels(request.method, path, str(response.status_code)).inc()
    LATENCY.labels(path).observe(time.time() - request._started_at)
    return response

@app.get("/")
def index():
    return jsonify(service="python-flask-lab", status="ok")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/ready")
def ready():
    return jsonify(status="ready")

@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
