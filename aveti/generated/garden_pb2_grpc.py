# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import garden_pb2 as garden__pb2


class GardenStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HeartBeat = channel.unary_unary(
                '/garden.Garden/HeartBeat',
                request_serializer=garden__pb2.Request.SerializeToString,
                response_deserializer=garden__pb2.HeartBeatReply.FromString,
                )
        self.ListPlants = channel.unary_unary(
                '/garden.Garden/ListPlants',
                request_serializer=garden__pb2.Request.SerializeToString,
                response_deserializer=garden__pb2.PlantListReply.FromString,
                )
        self.GetData = channel.unary_unary(
                '/garden.Garden/GetData',
                request_serializer=garden__pb2.PlantRequest.SerializeToString,
                response_deserializer=garden__pb2.PlantDataReply.FromString,
                )
        self.HistoricalData = channel.unary_unary(
                '/garden.Garden/HistoricalData',
                request_serializer=garden__pb2.PlantHistoricalRequest.SerializeToString,
                response_deserializer=garden__pb2.HistoricalDataReply.FromString,
                )
        self.WaterPlant = channel.unary_unary(
                '/garden.Garden/WaterPlant',
                request_serializer=garden__pb2.PlantRequest.SerializeToString,
                response_deserializer=garden__pb2.CommandResponse.FromString,
                )


class GardenServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPlants(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HistoricalData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaterPlant(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GardenServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=garden__pb2.Request.FromString,
                    response_serializer=garden__pb2.HeartBeatReply.SerializeToString,
            ),
            'ListPlants': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPlants,
                    request_deserializer=garden__pb2.Request.FromString,
                    response_serializer=garden__pb2.PlantListReply.SerializeToString,
            ),
            'GetData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=garden__pb2.PlantRequest.FromString,
                    response_serializer=garden__pb2.PlantDataReply.SerializeToString,
            ),
            'HistoricalData': grpc.unary_unary_rpc_method_handler(
                    servicer.HistoricalData,
                    request_deserializer=garden__pb2.PlantHistoricalRequest.FromString,
                    response_serializer=garden__pb2.HistoricalDataReply.SerializeToString,
            ),
            'WaterPlant': grpc.unary_unary_rpc_method_handler(
                    servicer.WaterPlant,
                    request_deserializer=garden__pb2.PlantRequest.FromString,
                    response_serializer=garden__pb2.CommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'garden.Garden', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Garden(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/garden.Garden/HeartBeat',
            garden__pb2.Request.SerializeToString,
            garden__pb2.HeartBeatReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPlants(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/garden.Garden/ListPlants',
            garden__pb2.Request.SerializeToString,
            garden__pb2.PlantListReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/garden.Garden/GetData',
            garden__pb2.PlantRequest.SerializeToString,
            garden__pb2.PlantDataReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HistoricalData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/garden.Garden/HistoricalData',
            garden__pb2.PlantHistoricalRequest.SerializeToString,
            garden__pb2.HistoricalDataReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaterPlant(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/garden.Garden/WaterPlant',
            garden__pb2.PlantRequest.SerializeToString,
            garden__pb2.CommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
