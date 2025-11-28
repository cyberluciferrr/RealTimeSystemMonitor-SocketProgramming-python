import socket
import threading
import psutil
import json
import time

hostAddress = "0.0.0.0"
hostPort = 5050

def handleClient(clientConnection, clientAddress):
    print(f"[CONNECTED] Client joined: {clientAddress}")

    try:
        while True:
            systemStats = {
                "cpuUsage": psutil.cpu_percent(),
                "memoryUsage": psutil.virtual_memory().percent,
                "diskUsage": psutil.disk_usage('/').percent
            }

            dataToSend = json.dumps(systemStats).encode()
            clientConnection.sendall(dataToSend)

            time.sleep(2)  # Delay between updates

    except:
        print(f"[DISCONNECTED] Client left: {clientAddress}")
    finally:
        clientConnection.close()


def startServer():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((hostAddress, hostPort))
    serverSocket.listen()

    print(f"[SERVER ACTIVE] Listening on port {hostPort}...")

    while True:
        clientConnection, clientAddress = serverSocket.accept()
        thread = threading.Thread(target=handleClient, args=(clientConnection, clientAddress))
        thread.start()


if __name__ == "__main__":
    startServer()
