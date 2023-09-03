# Block_IP
Create a simple daemon to block IP addresses using python.

# Block_IP Daemon

Block_IP is a Python script that runs as a daemon to block specific IP addresses using the `iptables` firewall on a Linux system. It periodically checks a list of IP addresses specified in a configuration file and blocks them from incoming network traffic.

## Features

- **Customizable Configuration**: Easily configure the list of IP addresses to block and the check interval through a `config.ini` file.
- **Logging**: Detailed logging of blocked IP addresses and daemon activities in the `ip_blocker_daemon.log` file.
- **Graceful Shutdown**: Handles SIGTERM signals for graceful termination of the daemon.
- **Error Handling**: Robust error handling to ensure the daemon continues running even in the presence of exceptions.
- **PID File Management**: Proper management of a PID file for the daemon process.
- **Security Considerations**: Designed to run with appropriate permissions, following best security practices.

## Prerequisites

- A Linux system with the `iptables` command available.
- Python 3.x installed on your system.
- The `daemonize` Python package. You can install it via pip using `pip install daemonize`.

## Installation and Usage

1. Clone or download this repository to your system.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Customize the `config.ini` file to specify the IP addresses you want to block and the check interval.
4. Run the `Block_IP` script to start the daemon:

   - python Block_IP.py start

   To stop the daemon gracefully, use:

   - python Block_IP.py stop

## Configuration

You can configure the script by editing the `config.ini` file. Here's a breakdown of the configuration options:

- `BlockedIPs`: A comma-separated list of IP addresses to block.
- `CheckInterval`: The frequency, in seconds, at which the script checks and blocks IP addresses.

## Logs

Logs of the script's activities, including blocked IP addresses, are stored in the `ip_blocker_daemon.log` file in the same directory as the script.

## License

This script is provided under the MIT License.

## Disclaimer

Blocking IP addresses should be done responsibly and in compliance with all applicable laws and regulations. Use this script responsibly and ensure you have the necessary permissions and authorization.

## Author

[Sudo Jvck]

If you have any questions you can find me @SudoJvck


