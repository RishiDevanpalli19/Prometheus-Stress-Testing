import metrics_collector
import metric_formatter
import genai_client
import notification_sender

def automation():
    metrics_response = metrics_collector.collect_metrics()
    formatted_metrics = metric_formatter.format_metrics(metrics_response)
    gemini_insights = genai_client.get_insights_from_genai(formatted_metrics)
    notification_sender.send_whatsapp_notification(gemini_insights)
    notification_sender.send_email_notification("Metrics Insights", gemini_insights)

if __name__ == "__main__":
    automation()