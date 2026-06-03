
```markdown
# CodeAlpha - Basic Network Sniffer

A lightweight and efficient Command-Line Interface (CLI) network packet sniffer developed in Python using the **Scapy** library. This project was built as part of the Cyber Security Internship program at **CodeAlpha**.

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Expected Output Format](#-expected-output-format)
- [Code Structure](#-code-structure)
- [Troubleshooting](#-troubleshooting)

---

## 🔍 Overview
This project is designed to capture, decode, and analyze network traffic packets in real-time. It provides deep visibility into network flows, protocol headers, and packet payloads, serving as a foundational tool for network auditing, troubleshooting, and security monitoring.

## ✨ Features
- **Real-Time Capture:** Continuously intercepts incoming and outgoing live network traffic.
- **Protocol Analysis:** Automatically detects and parses critical network/transport layer protocols:
  - **Layer 3 (Network):** IPv4 (Source/Destination IP mapping).
  - **Layer 4 (Transport):** TCP & UDP (Source/Destination Port parsing) and ICMP (Type/Code extraction).
- **Payload Inspection:** Extracts and displays raw application-layer data payloads (first 100 bytes) for non-encrypted streams.
- **Resource Efficient:** Disables packet archiving in memory (`store=0`) to ensure low system overhead during extended captures.
- **Robust Error Handling:** Features built-in exceptions for managing unauthorized execution (`PermissionError`) and graceful user termination (`Ctrl+C`).

## 🛠️ Prerequisites
Before running the tool, ensure your system meets the following requirements:
1. **Python 3.x** installed.
2. **Administrative Privileges:** The tool opens raw network sockets, requiring Root/Administrator rights.
3. **Packet Capture Driver (Windows Only):** Windows requires a packet sniffing driver to capture Layer 2/3 traffic. Please download and install **[Npcap](https://npcap.com/)**.
   - *Crucial:* During installation, check the box that says `"Install Npcap with WinPcap compatibility mode"`.

---

## 🚀 Installation & Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/solda-rasam/CodeAlpha_BasicNetworkSniffer.git
cd CodeAlpha_BasicNetworkSniffer

```
 2. **Install Required Libraries:**
```bash
pip install scapy

```
## 💻 Usage
### Windows (Command Prompt / PowerShell)
Open your terminal **as an Administrator** and execute:
```bash
python sniffer.py

```
### Linux / macOS
Run the script using sudo to grant raw socket permissions:
```bash
sudo python3 sniffer.py

```
## 📊 Expected Output Format
```text
[*] Starting Basic Network Sniffer...
[*] Listening for network traffic... (Press Ctrl+C to stop)

============================================================
[+] New Packet: 192.168.1.15 -> 93.184.216.34 | Protocol: TCP
[Layer 4] TCP Port: 53241 -> 80
[Payload] (First 100 bytes): b'GET / HTTP/1.1\r\nHost: example.com\r\n...'
============================================================

```
## 🏗️ Code Structure
 * sniffer.py: The core program containing the packet capturing loop and the callback processing logic.
 * packet_callback(packet): Inspects individual packets, checks for the presence of the IP layer, parses transport layer details, and securely prints data logs to the console.
 * main(): Initiates Scapy's asynchronous sniff() function with optimal performance parameters.
## ⚠️ Troubleshooting
 * **RuntimeError: Winpcap is not installed:** This means Scapy cannot find your network driver. Install **Npcap** and make sure you enable WinPcap compatibility mode during the setup, then restart your system.
 * **PermissionError / Access Denied:** Ensure you are running your terminal/IDE with **Run as Administrator** (Windows) or using sudo (Linux).
```

