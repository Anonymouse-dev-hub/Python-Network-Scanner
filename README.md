
# 🐍 PyStealthScanner

![Language](https://img.shields.io/badge/Language-Python3-blue)
![Library](https://img.shields.io/badge/Library-Scapy-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview
**PyStealthScanner** is a custom multi-threaded network scanner built with Python's **Scapy** library. 

Unlike standard socket scanners that complete a full TCP handshake (which logs a connection on the target server), this tool performs a **TCP SYN "Stealth" Scan**. It initiates a connection but abruptly resets it before completion, making it faster and often less visible to older logging systems.

## ⚙️ How It Works (The TCP Half-Open Scan)
The script manually crafts raw IP packets to exploit the TCP handshake mechanism:

```mermaid
sequenceDiagram
    participant Attacker
    participant Target
    Attacker->>Target: SYN Packet (Do you want to talk?)
    Note right of Target: Port is OPEN
    Target->>Attacker: SYN-ACK (Yes, let's talk!)
    Note right of Attacker: Captures Response
    Attacker->>Target: RST Packet (Nevermind, bye.)
    Note left of Attacker: Connection never established
````

### Technical Concepts Demonstrated

  * **Raw Packet Manipulation:** Using `Scapy` to build custom TCP/IP headers.
  * **Multi-Threading:** Using Python's `threading` and `queue` libraries to scan effectively.
  * **Network Protocols:** Practical application of the TCP 3-Way Handshake.

## 🚀 Features

  * **High Speed:** Scans 1000 ports in seconds using concurrent threads.
  * **Service Detection:** Identifies standard service names (HTTP, SSH, FTP) running on open ports.
  * **Stealth Mode:** Uses "Half-Open" scanning to avoid full connection logging.

## 🛠️ Installation & Usage

### Prerequisites

  * Python 3.x
  * **Npcap** (Windows) or **libpcap** (Linux) for packet sniffing.

### Setup

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Anonymouse-dev-hub/PyStealthScanner.git](https://github.com/Anonymouse-dev-hub/PyStealthScanner.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Scan

**Note:** Raw packet manipulation requires Administrator/Root privileges.

**Windows (Run Command Prompt as Admin):**

```bash
python scanner.py <TARGET_IP>
```

**Linux (Run with Sudo):**

```bash
sudo python3 scanner.py <TARGET_IP>
```

## ⚠️ Disclaimer

This tool is for **educational purposes only**. Only use this on networks you own or have explicit permission to test. Unauthorized scanning of networks is illegal.

## 🤝 Contributing

Contributions are welcome\!

1.  Fork the repository.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 📧 Contact

**Anonymouse-dev-hub** Project Link: [https://github.com/Anonymouse-dev-hub/PyStealthScanner](https://github.com/Anonymouse-dev-hub/PyStealthScanner)

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

```
```
