import socket
import json
import tkinter as tk
from tkinter import messagebox
import threading

serverIp = "192.168.122.128"   
serverPort = 5050

class MonitorApp:
    def __init__(self, rootWindow):
        self.rootWindow = rootWindow
        self.rootWindow.title("System Monitor Client")
        self.rootWindow.geometry("400x300")
        self.rootWindow.configure(bg="#1e1e1e")

        self.statusLabel = tk.Label(rootWindow, text="Disconnected", fg="white", bg="#1e1e1e", font=("Arial", 14))
        self.statusLabel.pack(pady=10)

        self.cpuLabel = tk.Label(rootWindow, text="CPU: --%", fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.cpuLabel.pack(pady=5)

        self.memoryLabel = tk.Label(rootWindow, text="Memory: --%", fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.memoryLabel.pack(pady=5)

        self.diskLabel = tk.Label(rootWindow, text="Disk: --%", fg="white", bg="#1e1e1e", font=("Arial", 12))
        self.diskLabel.pack(pady=5)

        self.connectButton = tk.Button(rootWindow, text="Connect", command=self.connectToServer)
        self.connectButton.pack(pady=10)

        self.isReceiving = False


    def connectToServer(self):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((serverIp, serverPort))

            self.statusLabel.config(text="Connected", fg="lightgreen")
            self.isReceiving = True

            threading.Thread(target=self.receiveData, daemon=True).start()

        except Exception as error:
            messagebox.showerror("Connection Error", str(error))


    def receiveData(self):
        while self.isReceiving:
            try:
                receivedData = self.clientSocket.recv(1024).decode()
                systemData = json.loads(receivedData)

                self.updateLabels(systemData)

            except:
                self.isReceiving = False
                break


    def updateLabels(self, statData):
        cpuVal = statData["cpuUsage"]
        memoryVal = statData["memoryUsage"]
        diskVal = statData["diskUsage"]

        self.cpuLabel.config(text=f"CPU: {cpuVal}%")
        self.memoryLabel.config(text=f"Memory: {memoryVal}%")
        self.diskLabel.config(text=f"Disk: {diskVal}%")

        self.colorize(self.cpuLabel, cpuVal)
        self.colorize(self.memoryLabel, memoryVal)
        self.colorize(self.diskLabel, diskVal)


    def colorize(self, label, value):
        if value < 50:
            label.config(fg="lightgreen")
        elif value < 80:
            label.config(fg="yellow")
        else:
            label.config(fg="red")


rootWindow = tk.Tk()
app = MonitorApp(rootWindow)
rootWindow.mainloop()
