import sys
import os
import serial
import serial.tools.list_ports
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Main.UI.main_window_ui import Ui_MainWindow

class SerialApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serial_conn = None
        
        # Initialize UI states
        self.ui.cb_Ports.setEnabled(False)
        self.ui.cb_Baudrate.setEnabled(False)
        self.ui.b_ConnectDisconnect.setEnabled(False)
        self.ui.cb_Objective.setEnabled(False)
        self.ui.le_Exposure.setEnabled(False)
        self.ui.sB_Nx.setEnabled(False)
        self.ui.sB_Ny.setEnabled(False)
        self.ui.le_Rx.setEnabled(False)
        self.ui.le_Ry.setEnabled(False)
        self.ui.b_Launch.setEnabled(False)
        
        # Connect buttons
        self.ui.b_ScanPorts.clicked.connect(self.scan_ports)
        self.ui.b_ConnectDisconnect.clicked.connect(self.toggle_connection)
        self.ui.b_Launch.clicked.connect(self.launch_measure)
        
        # Populate baud rate options
        self.ui.cb_Baudrate.addItems(["9600","19200","28800","115200"])
    
    def scan_ports(self):
        self.ui.cb_Ports.clear()
        ports = [port.device for port in serial.tools.list_ports.comports()]
        self.ui.cb_Ports.addItems(ports)
        
        if ports:
            self.ui.cb_Ports.setEnabled(True)
            self.ui.cb_Baudrate.setEnabled(True)
            self.ui.b_ConnectDisconnect.setEnabled(True)
    
    def toggle_connection(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.disconnect_from_serial()
        else:
            self.connect_to_serial()
    
    def connect_to_serial(self):
        port = self.ui.cb_Ports.currentText()
        baudrate = int(self.ui.cb_Baudrate.currentText())
        
        try:
            self.serial_conn = serial.Serial(port, baudrate, timeout=1)
            self.ui.tB_Log.append(f"Connected to {port} at {baudrate}")
            
            # Enable all widgets after connection
            self.ui.cb_Objective.setEnabled(True)
            self.ui.le_Exposure.setEnabled(True)
            self.ui.sB_Nx.setEnabled(True)
            self.ui.sB_Ny.setEnabled(True)
            self.ui.le_Rx.setEnabled(True)
            self.ui.le_Ry.setEnabled(True)
            self.ui.b_Launch.setEnabled(True)
            
            self.load_objectives()
        except Exception as e:
            QMessageBox.critical(self, "Connection Error", str(e))
    
    def disconnect_from_serial(self):
        if self.serial_conn:
            self.serial_conn.close()
            self.serial_conn = None
            self.ui.tB_Log.append("Disconnected from serial port.")
            self.ui.cb_Objective.setEnabled(False)
            self.ui.le_Exposure.setEnabled(False)
            self.ui.sB_Nx.setEnabled(False)
            self.ui.sB_Ny.setEnabled(False)
            self.ui.le_Rx.setEnabled(False)
            self.ui.le_Ry.setEnabled(False)
            self.ui.b_Launch.setEnabled(False)
    
    def load_objectives(self):
        try:
            directory = os.path.dirname(os.path.realpath(__file__))
            directory = "/".join(directory.split("/")[:-1])
            df = pd.read_excel(f"{directory}/objectives.xlsx", header=None)
            self.objectives = df.to_dict(orient='records')
            self.ui.cb_Objective.clear()
            for obj in self.objectives:
                self.ui.cb_Objective.addItem(str(obj[0]))
        except Exception as e:
            QMessageBox.critical(self, "File Error", f"Could not load objectives: {e}")
    
    def launch_measure(self):
        if not self.serial_conn or not self.serial_conn.is_open:
            QMessageBox.warning(self, "Error", "Serial port not connected.")
            return
        
        objective_index = self.ui.cb_Objective.currentIndex()
        if objective_index < 0:
            QMessageBox.warning(self, "Error", "No objective selected.")
            return
        
        exposure = self.ui.le_Exposure.text()
        nx = self.ui.sB_Nx.value()
        ny = self.ui.sB_Ny.value()
        deltax = self.ui.le_Rx.text()
        deltay = self.ui.le_Ry.text()
        dx = self.objectives[objective_index][1]
        dy = self.objectives[objective_index][2]
        xval = -nx * float(deltax) / 2
        yval = -ny * float(deltay) / 2
        
        commands = [
            f"SN X=2 Y=1",
            f"RT Z={float(exposure):.4f}",
            "TTL Y=2",
            "B X=0.1 Y=0.1",
            f"R X={float(dx):.4f} Y={float(dy):.4f}",
            "Z",
            f"AR X={nx} Y={ny} Z={float(deltax):.4f} F={float(deltay):.4f}",
            f"AH X={float(xval):.4f} Y={float(yval):.4f}",
            "AR"
        ]
        
        for cmd in commands:
            self.send_command(cmd)
    
    def send_command(self, cmd):
        if self.serial_conn:
            self.serial_conn.write(f"{cmd}\r\n".encode())
            response = self.serial_conn.readline().decode().strip()
            self.ui.tB_Log.append(f"> {cmd}")
            
            if response != ":A":
                QMessageBox.critical(self, "Error", f"Unexpected response: {response}")
                self.disconnect_from_serial()
                return
            
            self.ui.tB_Log.append(f"< {response}")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SerialApp()
    window.show()
    sys.exit(app.exec())
