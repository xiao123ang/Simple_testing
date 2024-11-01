from prometheus_client import start_http_server

def start_metrics_server(port=8000):
    start_http_server(port)
    print(f"Prometheus metrics server started on port {port}")

if __name__ == "__main__":
    start_metrics_server()