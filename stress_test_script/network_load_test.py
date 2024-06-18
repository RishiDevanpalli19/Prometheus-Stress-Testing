import logging
import socket
import os
import time
from concurrent.futures import ThreadPoolExecutor


def execute_script_on_remote_vm(remote_host, remote_user, private_key_path, remote_script_path):
    try:
        # Set up SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Load the private key
        key = paramiko.RSAKey.from_private_key_file(private_key_path)

        # Connect to the remote host
        logging.info("Connecting to the remote host")
        client.connect(remote_host, username=remote_user, pkey=key)

        # Execute the script
        logging.info("Executing the script on the remote host")
        stdin, stdout, stderr = client.exec_command(f'python3 {remote_script_path}')

        # Wait for the command to complete
        exit_status = stdout.channel.recv_exit_status()

        # Print the output and errors
        logging.info("Output:\n" + stdout.read().decode())
        logging.error("Errors:\n" + stderr.read().decode())

        # Close the connection
        client.close()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
