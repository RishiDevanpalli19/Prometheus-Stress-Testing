from prometheus_client import query_prometheus

queries = {
    "cpu_query": '100 * (1 - avg(rate(node_cpu_seconds_total{mode="idle",instance="192.168.43.109:9100"}[1m])))',
    "memory_usage": 'node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes',
    "disk_usage": 'node_filesystem_avail_bytes / node_filesystem_size_bytes',
    "network_receive": 'irate(node_network_receive_bytes_total{device="enp0s3", instance="192.168.72.234:9100", job="prometheus"}[1m])',
    "network_transmit": 'rate(node_network_transmit_bytes_total[1m])',
    "processes_running": 'node_procs_running',
}

def collect_metrics():
    metrics = {}
    for metric, query in queries.items():
        result = query_prometheus(query)
        if result:
            metrics[metric] = result
        else:
            metrics[metric] = "Error collecting metric"
    return metrics