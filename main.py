from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import grpc

import desenho_pb2
import desenho_pb2_grpc

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)
channel = grpc.insecure_channel("localhost:50051")
stub = desenho_pb2_grpc.DesenhoServiceStub(channel)

@app.get("/reclamar")
def reclamar(evento: str = "click"):
    response = stub.Reclamar(
        desenho_pb2.ReclamacaoRequest(evento=evento)
    )

    return {
        "evento": evento,
        "texto": response.texto
    }
