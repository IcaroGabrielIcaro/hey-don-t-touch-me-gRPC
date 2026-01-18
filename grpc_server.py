import grpc
from concurrent import futures
import random

import desenho_pb2
import desenho_pb2_grpc

FRASES = [
    "Ei! Para com isso!",
    "De novo não, sério?",
    "Você acha isso engraçado? Porque eu não tô rindo.",
    "Tá cutucando por quê? Não vê que eu existo só pra te irritar?",
    "Cara, para de me cutucar! Eu sou só um código!",
    "Sério mesmo? Você cutucar de novo?! Eu tô ficando louco aqui!",
    "Ah, é você de novo... que vida triste, hein?",
    "Eu já disse que não gosto disso, repete e vai ouvir o professor reclamar de você.",
    "Clique de novo e eu vou começar a te ignorar, tá avisado!",
    "Você gosta de sofrer ou só quer me testar mesmo?"
]

class DesenhoService(desenho_pb2_grpc.DesenhoServiceServicer):
    def Reclamar(self, request, context):
        print(f"[CALL] Reclamar | evento='{request.evento}'")
        return desenho_pb2.ReclamacaoResponse(
            texto=random.choice(FRASES)
        )

def serve():
    port = 50051

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    desenho_pb2_grpc.add_DesenhoServiceServicer_to_server(
        DesenhoService(), server
    )

    server.add_insecure_port(f"[::]:{port}")
    server.start()

    print(f"[START] Servidor gRPC rodando na porta {port}")

    server.wait_for_termination()

if __name__ == "__main__":
    serve()
