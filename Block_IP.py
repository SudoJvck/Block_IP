import subprocess
import time
import logging
import signal
import configparser
import sys
import os

logging.basicConfig(filename='ip_blocker_daemon.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def block_ip(ip):
    try:
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        logging.info(f"Blocked IP: {ip}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to block IP {ip}: {e}")

def block_ips_periodically(config):
    while True:
        try:
            blocked_ips = config['Block_IP']['BlockedIPs'].split(',')
            check_interval = int(config['Block_IP']['CheckInterval'])

            for ip in blocked_ips:
                block_ip(ip)

            logging.info("IP blocking completed.")
            time.sleep(check_interval)
        except KeyboardInterrupt:
            logging.info("Received KeyboardInterrupt. Exiting gracefully.")
            sys.exit(0)
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    pid_file = '/var/run/ip_blocker_daemon.pid'

    def sigterm_handler(signum, frame):
        logging.info("Received SIGTERM signal. Exiting gracefully.")
        sys.exit(0)

    signal.signal(signal.SIGTERM, sigterm_handler)

    if os.path.isfile(pid_file):
        logging.error("Block_IP daemon is already running. Exiting.")
        sys.exit(1)

    try:
        with open(pid_file, 'w') as pidfile:
            pidfile.write(str(os.getpid()))

        block_ips_periodically(config)
    finally:
        os.remove(pid_file)
