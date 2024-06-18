import os
import time
import logging
import psutil
import random
import sys

def memory_load_test(duration=5, total_duration=210, data_type='int', initial_size=500000, increment_step=1000000, multiplier=1.3):
    logging.info('Starting Memory load test...')
    logging.info('The Memory usage before test is: %s', psutil.virtual_memory().percent)

    data_generator = (lambda: random.randint(1, 10000) if data_type == 'int' else lambda: chr(random.randint(65, 90)))
    current_data_size = initial_size
    end_time = time.time() + total_duration

    while time.time() < end_time:
        large_data = []
        start_time = time.time()
        try:
            while (time.time() - start_time) < duration:
                large_data.extend([data_generator() for _ in range(current_data_size)])
                current_data_size = int(current_data_size * multiplier)
        except MemoryError:
            logging.error('MemoryError: Unable to allocate more memory.')
            break

        memory_usage = sys.getsizeof(large_data) / (1024 * 1024)
        logging.info('The Memory usage with %s elements is: %s', current_data_size, memory_usage)
        if memory_usage > 80:
            logging.warning('Memory usage exceeded 80%.')

        time.sleep(1)