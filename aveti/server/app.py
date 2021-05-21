from concurrent import futures
import grpc

from ..generated import garden_pb2_grpc, garden_pb2
from .garden_server import Garden

class Server:

    @staticmethod
    def run():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        garden_pb2_grpc.add_GardenServicer_to_server(Garden(), server)
        server.add_insecure_port('0.0.0.0:50051')
        server.start()
        print("Garden Server Started [OK], Use Ctrl-C to close")
        server.wait_for_termination()