def format_metric_data(result):
    if isinstance(result, list) and result:
        formatted_data = []
        for item in result:
            formatted_data.append({
                "metric": item["metric"],
                "value": [
                    time.time(),
                    item["value"][1]
                ]
            })
        return formatted_data
    else:
        return "Error collecting metric"

def format_metrics(metrics):
    output = {
        "cpu_query": format_metric_data(metrics.get("cpu_query")),
        "memory_usage": format_metric_data(metrics.get("memory_usage")),
        "disk_usage": format_metric_data(metrics.get("disk_usage")),
        "network_receive": format_metric_data(metrics.get("network_receive")),
        "network_transmit": format_metric_data(metrics.get("network_transmit")),
        "processes_running": format_metric_data(metrics.get("processes_running")),
        "logs": "Error collecting metric" if any(v == "Error collecting metric" for v in metrics.values()) else ""
    }
    return output