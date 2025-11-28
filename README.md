# Remote System Monitor

**Author:** Muhammad Ali Khan    
**Course:** Computer Networks CYS2003  
**Project:** Socket Programming – Remote System Monitoring Tool  

---

## **Project Overview**
This project implements a **Remote System Monitoring Tool** using Python **TCP sockets**.  
It consists of:

- **Server (Monitoring Agent)** running on **Kali Linux VM**  
- **Client (GUI Dashboard)** running on **Windows Host**

The client connects to the server over a network and retrieves **CPU, RAM, and Disk usage information** in real time.  
This simulates a simplified **enterprise monitoring environment** like those used in SOCs (Security Operations Centers) for endpoint telemetry monitoring.

---

## **Features**
- Real time system monitoring over the network  
- Cross platform communication (Linux server → Windows client)  
- GUI dashboard using Tkinter  
- Threshold-based alerts with color coded system usage  
- TCP socket based client-server architecture  
- JSON based data transfer  
- Multi threaded communication for responsiveness  

---

## **Technologies Used**
- **Python 3**  
- **Socket Library** – for TCP communication  
- **psutil** – collects CPU, memory, and disk usage  
- **Tkinter** – GUI for client dashboard  
- **JSON** – data serialization  
- **Threading** – for concurrent execution  

---

## **Setup Instructions**

### **1. Server (Kali Linux VM)**
1. Ensure Python 3 is installed:
    ```bash
    python3 --version
    ```
2. Install required library:
    ```bash
    sudo apt install python3-pip
    pip3 install psutil
    ```
3. Save the server script as `server.py`:
    ```bash
    nano server.py
    ```
4. Run the server:
    ```bash
    python3 server.py
    ```
5. Note the VM’s IP address (replace in client):
    ```bash
    ip a
    ```
   Example IP: `192.168.122.128`

---

### **2. Client (Windows Host)**
1. Install Python 3 if not already installed.  
2. Save the client script as `client.py`.  
3. Update the server IP and port:
    ```python
    serverIp = "192.168.122.128"
    serverPort = 5050
    ```
4. Run the client:
    ```bash
    python client.py
    ```
5. The GUI dashboard will display live CPU, RAM, and Disk usage.

---

## **Networking Requirements**
- VM must allow communication with host:  
  - **Recommended:** Bridged Adapter or Host Only Adapter  
  - **Not recommended:** NAT only (client cannot reach VM)  
- Ensure port 5050 is open on the server.

---

## **Socket Communication Flow**
1. Client sends a connection request.  
2. Server accepts the connection.  
3. Server sends system statistics periodically.  
4. Client receives and displays data in GUI.  
5. Connection closes when client exits.

---

## **Cybersecurity Perspective**
- **Server** acts like a real world monitoring agent (Elastic Beats, OSQuery, Wazuh).  
- **Client** acts like a SOC dashboard.  
- Demonstrates safe **home lab monitoring environment**.  
- Teaches **endpoint monitoring**, **socket-based telemetry**, and **network communication**.  

---

## **Benefits of This Lab Setup**
- Safe testing of client-server communication  
- Hands-on experience with network programming  
- Understanding real-time monitoring in enterprise environments  
- Prepares for building security monitoring tools in professional setups  

---

## **License**
This project is for educational purposes only.  

---

## **Screenshot / Demo**
*(Optional: Add screenshots of your GUI dashboard here if available)*
