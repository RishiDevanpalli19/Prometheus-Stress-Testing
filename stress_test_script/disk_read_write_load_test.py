import os
import time
import logging
import psutil
from concurrent.futures import ThreadPoolExecutor

def disk_read_write_load_test(dummy_file_prefix, num_files=1, file_size_mb=100, check_interval=7, duration=5*60):
    logging.info('Starting Disk Read/Write load test...')
    logging.info('The Disk usage before test is: %s', psutil.disk_usage('/').percent)

    data = os.urandom(file_size_mb * 1024 * 1024)  # Size of random data to write per file

    start_time = time.time()

    disk_usage_exceeded = False

    def create_dummy_file(filename, size_mb):
        with open(filename, 'wb') as f:
            f.write(os.urandom(size_mb * 1024 * 1024))
        logging.info(f"\nCreated dummy file '{filename}' of size {size_mb} MB")

    def append_to_dummy_file(filename, data):
        with open(filename, 'ab') as f:
            f.write(data)

    def write_data_to_file(file_index):
        nonlocal disk_usage_exceeded
        dummy_file = f"{dummy_file_prefix}_{file_index}.bin"
        create_dummy_file(dummy_file, file_size_mb)
        while True:
            append_to_dummy_file(dummy_file, data)
            disk_usage = psutil.disk_usage('/')
            used_percent = disk_usage.percent
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration:
                break
            time.sleep(0.9)
            if used_percent >= 80:
                logging.warning("Disk usage exceeded 80%! Current usage: {:.2f}%".format(used_percent))
                disk_usage_exceeded = True
        return dummy_file

    def print_disk_usage_and_speeds():
        nonlocal disk_usage_exceeded
        while True:
            time.sleep(check_interval)
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration:
                break
            read_bytes = psutil.disk_io_counters().read_bytes
            write_bytes = psutil.disk_io_counters().write_bytes
            total_read_mb = read_bytes / (1024 * 1024)
            total_write_mb = write_bytes / (1024 * 1024)
            average_read_speed = (read_bytes * 8 / elapsed_time) / (1024 * 1024)  # in Mbps
            average_write_speed = (write_bytes * 8 / elapsed_time) / (1024 * 1024)  # in Mbps
            disk_usage = psutil.disk_usage('/')
            used_percent = disk_usage.percent

            logging.info(f"\nDisk usage: {used_percent:.2f}%")
            logging.info(f"Total Read: {total_read_mb:.2f} MB, Total Write: {total_write_mb:.2f} MB")
            logging.info(f"Average Read Speed: {average_read_speed:.2f} Mbps")
            logging.info(f"Average Write Speed: {average_write_speed:.2f} Mbps")

            if used_percent >= 80:
                logging.warning("Disk usage exceeded 80%! Current usage: {:.2f}%".format(used_percent))
                disk_usage_exceeded = True

    with ThreadPoolExecutor(max_workers=num_files + 1) as executor:
        futures = [executor.submit(write_data_to_file, i) for i in range(num_files)]
        futures.append(executor.submit(print_disk_usage_and_speeds))
        completed_files = [f.result() for f in futures if f!= futures[-1]]

    elapsed_time = time.time() - start_time

    # Get final disk I/O counters
    read_bytes = psutil.disk_io_counters().read_bytes
    write_bytes = psutil.disk_io_counters().write_bytes

    # Convert read and write bytes to MB
    total_read_mb = read_bytes / (1024 * 1024)
    total_write_mb = write_bytes / (1024 * 1024)

    # Calculate average read and write speeds in Mbps
    average_read_speed = (read_bytes * 8 / elapsed_time) / (1024 * 1024)  # in Mbps
    average_write_speed = (write_bytes * 8 / elapsed_time) / (1024 * 1024)  # in Mbps

    logging.warning(f"\nTest duration reached. Stopping the test.")
    logging.info(f"Total Read: {total_read_mb:.2f} MB, Total Write: {total_write_mb:.2f} MB")
    logging.info(f"Average Read Speed: {average_read_speed:.2f} Mbps")
    logging.info(f"Average Write Speed: {average_write_speed:.2f} Mbps")

    # Clean up
    for dummy_file in completed_files:
        os.remove(dummy_file)
        logging.warning(f"Deleted dummy file '{dummy_file}'")

    return disk_usage_exceeded