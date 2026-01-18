import grpc
from concurrent import futures
import random

import desenho_pb2
import desenho_pb2_grpc

FRASES = [
    "Ei! Para com isso!",
    "De novo não",
    "Você acha isso engraçado?",
    "Tá cutucando por quê?"
]

class DesenhoService(desenho_pb2_grpc.DesenhoServiceServicer):
    def Reclamar(self, request, context):
        return desenho_pb2.ReclamacaoResponse(
            texto=random.choice(FRASES)
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    desenho_pb2_grpc.add_DesenhoServiceServicer_to_server(
        DesenhoService(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
