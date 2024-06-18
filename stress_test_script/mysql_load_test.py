import os
import time
import logging
import pymysql

def mysql_load_test(duration=5*60, host='localhost', user='root', password='', db='test'):
    logging.info('Starting MySQL load test...')
    logging.info('The MySQL usage before test is: %s', get_mysql_load(host, user, password, db))

    start_time = time.time()

    def mysql_intensive_task():
        while True:
            if time.time() - start_time >= duration:
                break
            connection = pymysql.connect(host=host, user=user, password=password, db=db)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM large_table")
            cursor.close()
            connection.close()

    def print_mysql_load():
        while True:
            time.sleep(1)
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration:
                break
            logging.info(f"MySQL load: {get_mysql_load(host, user, password, db)}")

    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(mysql_intensive_task)
        executor.submit(print_mysql_load)

    elapsed_time = time.time() - start_time
    logging.warning(f"\nTest duration reached. Stopping the test.")
    logging.info(f"Average MySQL load: {get_mysql_load(host, user, password, db)}")

def get_mysql_load(host, user, password, db):
    connection = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM information_schema.PROCESSLIST WHERE COMMAND NOT IN ('Sleep', 'Binlog Dump')")
    result = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return result