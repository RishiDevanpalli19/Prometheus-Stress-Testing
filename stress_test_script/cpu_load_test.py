import logging
import psutil
import random
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

threshold = 80

def cpu_load_test(duration=120, cpu_usage_target=0.8):
    logging.info('Starting CPU load test...')
    start_time = time.time()
    while (time.time() - start_time) < duration:
        for _ in range(10000):
            random.random() * 2
        current_cpu_usage = psutil.cpu_percent(interval=0.005)
        logging.info('Current CPU usage: %s', current_cpu_usage)
        if current_cpu_usage > threshold:
            logging.warning('CPU usage exceeded 80%.')
