import requests

def query_prometheus(query):
    try:
        response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': query})
        response.raise_for_status()
        result = response.json()
        if result['status'] == 'success':
            return result['data']['result']
        else:
            raise Exception(f"Query failed: {result['status']}")
    except Exception as e:
        print(f"Error querying Prometheus: {e}")
        return None