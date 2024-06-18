import cpu_load_test
import memory_load_test
import network_load_test
import disk_read_write_load_test
import mysql_load_test

def menucode():
    while True:
        print('Select an option')
        print('1. CPU Load Test')
        print('2. Memory Load Test')
        print('3. Network Traffic Load Test')
        print('4. Disk read/write Load Test')
        print('5. MySQL Stress/Load Test')
        print('6. Exit')
        opt=int(input('Enter your option: '))
        if opt==1:
            duration = int(input('Enter the duration of the test in seconds: '))
            cpu_load_test.cpu_load_test(duration)
        elif opt==2:
            duration = int(input('Enter the duration of the test in seconds: '))
            total_duration = int(input('Enter the total duration of the test in seconds: '))
            data_type = input('Enter the data type (int or str): ')
            initial_size = int(input('Enter the initial size of the data: '))
            increment_step = int(input('Enter the increment step for the data size: '))
            multiplier = float(input('Enter the multiplier for the data size: '))
            memory_load_test.memory_load_test(duration, total_duration, data_type, initial_size, increment_step, multiplier)
        elif opt==3:
            host = input('Enter the hostname or IP address: ')
            port = int(input('Enter the port number: '))
            network_load_test.network_load_test(host, port)
        elif opt==4:
            dummy_file_prefix = input('Enter the prefix for the dummy files: ')
            num_files = int(input('Enter the number of dummy files to create: '))
            file_size_mb = int(input('Enter the size of each dummy file in MB: '))
            check_interval = int(input('Enter the interval in seconds to check disk usage and speeds: '))
            duration = int(input('Enter the duration of the test in seconds: '))
            disk_read_write_load_test.disk_read_write_load_test(dummy_file_prefix, num_files, file_size_mb, check_interval, duration)
        elif opt==5:
            host = input('Enter the hostname or IP address of the MySQL server: ')
            user = input('Enter the username for the MySQL server: ')
            password = input('Enter the password for the MySQL server: ')
            db = input('Enter the database name: ')
            mysql_load_test.mysql_load_test(host, user, password, db)
        elif opt==6:
            break
        else:
            print('Invalid Option')

if __name__ == "__main__":
    menucode()