"""
main_window.py
Entry point for the client
"""

__author__     = "Prakash Manandhar"
__copyright__  = "Copyright 2021, Prakash Manandhar"
__credits__    = ["Prakash Manandhar"]
__license__    = "MIT"
__version__    = "1.0.0"
__maintainer__ = "Prakash Manandhar"
__email__      = "prakashm@alum.mit.edu"
__status__     = "Production"

import sys, time, grpc, configparser
from datetime import datetime, timedelta
from PySide6 import QtCore, QtWidgets, QtGui
from qt_material import apply_stylesheet
from PySide6.QtCore import QTimer, Signal
from ..generated import garden_pb2_grpc, garden_pb2

config = configparser.ConfigParser()
config.read('client_config.ini')

RPI_IP_ADDRESS_PORT = \
    f"{config.get('Network', 'MissionControlRPiIPAddress')}:" \
    f"{config.get('Network', 'GRPCPort')}"

HEARTBEAT_TIMEOUT   = \
    config.getint('Network', 'HeartbeatTimeout')
GRPC_CALL_TIMEOUT   = \
    config.getint('Network', 'GRPCTimeout')

class RPiHeartBeat(QtCore.QThread):
    done = Signal(object)
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):
        global RPI_IP_ADDRESS_PORT, GRPC_CALL_TIMEOUT
        response = None
        try:
            timestamp = int(time.time()*1000)
            with grpc.insecure_channel(RPI_IP_ADDRESS_PORT) as channel:
                stub = garden_pb2_grpc.GardenStub(channel)
                response = stub.HeartBeat (
                    garden_pb2.Request(request_timestamp_ms = timestamp),
                    timeout = GRPC_CALL_TIMEOUT )
                print("Server HeartBeat received at: " + str(datetime.now()))
                print(response)
        
        except Exception as e:
            info = f"Error connecting to RPi Server at: {RPI_IP_ADDRESS_PORT}: + {str(e)}"
            print(info)

        self.done.emit(response)

class MainWindow(QtWidgets.QWidget):

    def _addTreeChildren(self, pNode):
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Light"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Temperature"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Humidity"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Moisture"]))

    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.button = QtWidgets.QPushButton("Test")
        self.main_layout.addWidget(self.button)
        
        l1 = QtWidgets.QTreeWidgetItem([ "Living Room Spider Plant"])
        l2 = QtWidgets.QTreeWidgetItem([ "Kitchen Orchid"])
    
        self._addTreeChildren(l1)
        self._addTreeChildren(l2)
        
        tw = QtWidgets.QTreeWidget(self)
        tw.setColumnCount(1)
        tw.setHeaderLabels(["My Plants"])
        tw.addTopLevelItem(l1)
        tw.addTopLevelItem(l2)
        self.main_layout.addWidget(tw)
        self.setLayout(self.main_layout)

        self.heartbeat_timer=QTimer()
        self.heartbeat_timer.timeout.connect(self.onHeartBeat)
        global HEARTBEAT_TIMEOUT
        self.heartbeat_timer.start(HEARTBEAT_TIMEOUT)

    def onHeartBeat(self):
        self.threads = []
        client_thread = RPiHeartBeat()
        #client_thread.done.connect(self.on_heartbeat_received)
        self.threads.append(client_thread)
        client_thread.start()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.resize(1500, 740)
    window.show()
    sys.exit(app.exec_())
