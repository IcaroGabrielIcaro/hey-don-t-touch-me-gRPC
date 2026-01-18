# Hey Don’t Touch Me – gRPC + FastAPI + Front

Sistema simples para testar **interação entre frontend, FastAPI e gRPC**, com respostas divertidas e imagens que mudam ao clicar.

## 💡 Ideia

* gRPC = **core de lógica**: responde com frases aleatórias quando o usuário “clica”
* FastAPI = **adapter HTTP**: recebe requisição do front, chama gRPC e retorna JSON
* Front (index.html) = **interface**: mostra imagem feliz, troca para raiva ao clicar e exibe a mensagem do backend

Funciona como um mini “jogo de interação” entre usuário e código.

## 🚀 Como rodar

1. **Subir o servidor gRPC**

```bash
python grpc_server.py
```

Saída esperada:

```
[START] Servidor gRPC rodando na porta 50051
```

2. **Subir o servidor FastAPI**

```bash
uvicorn main:app --reload
```

Saída esperada:

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

3. **Abrir o front**

* Abra `index.html` no navegador (ou sirva pelo Live Server)
* Clique na imagem:

  * Mensagem aparece
  * Imagem muda para “raiva” por 3 segundos
  * Depois volta pra “feliz” e a mensagem desaparece


## ⚡ Observações

* Se abrir o HTML fora do mesmo host do FastAPI, habilite **CORS** no `main.py`
* Frases do gRPC são aleatórias, algumas quebram a quarta parede de forma divertida
* Ideal para **testes de integração gRPC ↔ HTTP ↔ Front**

