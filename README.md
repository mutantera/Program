---

# Security Tools

This repository contains two security tools:

1. **Python Port Scanner**
2. **SSH Brute-Force**

## 1. Python Port Scanner

A simple Python-based port scanner that utilizes Nmap for network scanning. This tool helps you scan ports on a given target to identify open ports and their status.

### Features

- Scans specified ports on a target host.
- Utilizes Nmap for detailed network scanning.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/security-tools.git
   cd security-tools
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the port scanner:
   ```bash
   python port_scanner.py <target_ip> <port_range>
   ```

   - `<target_ip>`: The IP address of the target.
   - `<port_range>`: The range of ports to scan (e.g., `1-1024`).

2. Example:
   ```bash
   python port_scanner.py 192.168.1.1 1-1024
   ```

### Example Output

```
Scanning target 192.168.1.1 on ports 1-1024...
Port 22: Open
Port 80: Closed
...
```

## 2. SSH Brute-Force

A tool to perform brute-force attacks on SSH passwords using a wordlist. This script attempts to authenticate to an SSH server using passwords from a list.

### Features

- Attempts to connect to an SSH server with passwords from a wordlist.
- Logs the progress and results of the brute-force attempts.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/security-tools.git
   cd security-tools
   ```

2. Install the required Python packages:
   ```bash
   pip install paramiko
   ```

### Usage

1. Run the SSH brute-force tool:
   ```bash
   python ssh_bruteforce.py
   ```

   Make sure to modify the script to include the correct `host`, `username`, and path to your password list.

2. Example:
   ```bash
   python ssh_bruteforce.py
   ```

### Example Output

```
[0] Attempting password: 'password123'!
[X] Invalid Password!
[1] Attempting password: 'admin'!
[>] Valid Password found: 'admin'!
```

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

---

Feel free to adjust the example paths, commands, and details based on your actual setup and preferences.
