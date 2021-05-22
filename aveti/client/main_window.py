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
import pyqtgraph as pg
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

class BaseGrpcThread(QtCore.QThread):
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
                response = self._get_response(stub, timestamp)
                
        except Exception as e:
            info = f"Error connecting to RPi Server at: {RPI_IP_ADDRESS_PORT}: + {str(e)}"
            print(info)

        self.done.emit(response)
    
    def _get_response(self, stub, timestamp):
        return None

class RPiHeartBeat(BaseGrpcThread):
    def _get_response(self, stub, timestamp):
        response = stub.HeartBeat (
            garden_pb2.Request(request_timestamp_ms = timestamp),
            timeout = GRPC_CALL_TIMEOUT )
        print("Server HeartBeat received at: " + str(datetime.now()))
        print(response)

        return response

class WaterPlantThread(BaseGrpcThread):

    def __init__(self, plant_id):
        super(WaterPlantThread, self).__init__()
        self.plant_id = plant_id

    def _get_response(self, stub, timestamp):
        response = stub.WaterPlant (
            garden_pb2.PlantRequest(
                request_timestamp_ms = timestamp,
                plant_id = self.plant_id),
            timeout = GRPC_CALL_TIMEOUT )
        print(response)
        return response

class GetDataThread(BaseGrpcThread):
    def __init__(self, plant_id):
        super(GetDataThread, self).__init__()
        self.plant_id = plant_id
        
    def _get_response(self, stub, timestamp):
        response = stub.GetData (
            garden_pb2.PlantRequest(
                request_timestamp_ms = timestamp,
                plant_id = self.plant_id),
            timeout = GRPC_CALL_TIMEOUT )
        print("Get Data Response")
        print(response)

        return response

class MainWindow(QtWidgets.QWidget):

    def _addTreeChildren(self, pNode):
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Light"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Temperature"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Humidity"]))
        pNode.addChild(QtWidgets.QTreeWidgetItem(["Moisture"]))

    def __init__(self):
        self.threads = []
        super(MainWindow, self).__init__()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.button = QtWidgets.QPushButton("Water Plant")
        self.main_layout.addWidget(self.button)
        self.button.clicked.connect(self.onTestClick)
        
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

        self.plot = pg.PlotWidget()
        self.plot.showGrid(x = True, y = True, alpha = 1.0)
        self.plot.getAxis('bottom').setLabel(f't (s)')
        self.plot.getAxis('left').setLabel(f'T (deg C)')
        self.start_time = time.time()
        self.sensor_timestamp_s = []
        self.temp_degC = []
        self.scatter = pg.ScatterPlotItem(
            pen=pg.mkPen(width=7, color='r'), symbol='o', size=3)
        self.plot.addItem(self.scatter)
        self.main_layout.addWidget(self.plot)

        self.heartbeat_timer=QTimer()
        self.heartbeat_timer.timeout.connect(self.onHeartBeat)
        global HEARTBEAT_TIMEOUT
        self.heartbeat_timer.start(HEARTBEAT_TIMEOUT)

    def onHeartBeat(self):
        client_thread = RPiHeartBeat()
        #client_thread.done.connect(self.on_heartbeat_received)
        self.threads.append(client_thread)
        client_thread.start()

        data_thread = GetDataThread(0)
        data_thread.done.connect(self.on_data_received)
        self.threads.append(data_thread)
        data_thread.start()

    @QtCore.Slot(object)
    def on_data_received(self, response):
        if (response != None):
            self.sensor_timestamp_s.append(
                response.sensor_timestamp_s - self.start_time)
            self.temp_degC.append(response.temp_degC)
            self.scatter.setData(self.sensor_timestamp_s, self.temp_degC)

    def onTestClick(self):
        client_thread = WaterPlantThread(0)
        self.threads.append(client_thread)
        client_thread.start()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    window = MainWindow()
    window.resize(1500, 740)
    window.show()
    sys.exit(app.exec_())
