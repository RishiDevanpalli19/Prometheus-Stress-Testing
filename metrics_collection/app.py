from flask import Flask, request
from main import automation
from config import Config
from genai_client import GenAI_Client
from metric_formatting import format_metrics
from metrics_collector import collect_metrics
from notification_sender import send_notification
from prometheus_client import PrometheusClient

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h2>Hello world - Integration Activity Flask Deployment Lab: try 10 <h2><hr/>"


@app.route('/mywebhook', methods=['POST', 'GET'])
def alert_api():
    data = request.json
    config = Config()
    genai_client = GenAI_Client(config)
    metrics = collect_metrics(genai_client)
    formatted_metrics = format_metrics(metrics)
    prometheus_client = PrometheusClient()
    prometheus_client.send_metrics(formatted_metrics)
    send_notification(formatted_metrics)
    automation.automation()
    return "Notification Sent"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)