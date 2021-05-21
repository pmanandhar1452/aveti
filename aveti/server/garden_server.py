from ..generated import garden_pb2_grpc, garden_pb2
from .hardware import HardwareFactory

import time

class Garden(garden_pb2_grpc.GardenServicer):

    def __init__(self):
        pass

    def HeartBeat(self, request, context):
        timestamp = int(time.time()*1000)
        cpu_temp = HardwareFactory.getRPi() \
            .get_cpu_temperature()

        rig_hardware = HardwareFactory.getRig()

        return garden_pb2.HeartBeatReply(
            request_timestamp_ms = request.request_timestamp_ms,
            timestamp_ms = timestamp,
            cpu_temperature_degC = cpu_temp)