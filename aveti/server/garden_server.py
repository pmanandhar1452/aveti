from ..generated import garden_pb2_grpc, garden_pb2
from .hardware import HardwareFactory

import time

class Garden(garden_pb2_grpc.GardenServicer):

    def __init__(self):
        pass

    def HeartBeat(self, request, context):
        cpu_temp = HardwareFactory.getRPi() \
            .get_cpu_temperature()
        timestamp_ms = int(time.time()*1000)
        
        return garden_pb2.HeartBeatReply(
            request_timestamp_ms = request.request_timestamp_ms,
            timestamp_ms = timestamp_ms,
            cpu_temperature_degC = cpu_temp)

    def WaterPlant(self, request, context):
        timestamp_ms = int(time.time()*1000)
        HardwareFactory.getRPi().water_plant(request.plant_id)
        return garden_pb2.CommandResponse(
            request_timestamp_ms = request.request_timestamp_ms,
            timestamp_ms = timestamp_ms,
            status = garden_pb2.EXECUTED)

    def GetData(self, request, context):
        timestamp_ms = int(time.time()*1000)
        rpi = HardwareFactory.getRPi()
        data = rpi.get_temp_rh(request.plant_id)
        sensor_timestamp_s = time.time()
        return garden_pb2.PlantDataReply(
            request_timestamp_ms = request.request_timestamp_ms,
            timestamp_ms = timestamp_ms,
            sensor_timestamp_s = sensor_timestamp_s,
            temp_degC = data["temp_degC"],
            rh_percent = data["rh_percent"])