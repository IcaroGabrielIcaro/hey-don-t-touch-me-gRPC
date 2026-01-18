from fastapi import FastAPI
import grpc

import desenho_pb2
import desenho_pb2_grpc

app = FastAPI()

@app.get("/clicar")
def clicar():
    channel = grpc.insecure_channel("localhost:50051")
    stub = desenho_pb2_grpc.DesenhoServiceStub(channel)

    response = stub.Reclamar(
        desenho_pb2.ReclamacaoRequest(evento="click")
    )

    return {"texto": response.texto}
