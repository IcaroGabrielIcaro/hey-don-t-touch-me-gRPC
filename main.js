'use strict';

const Hapi = require('@hapi/hapi');
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

// Carregamento do proto
const packageDefinition = protoLoader.loadSync(
  __dirname + '/desenho.proto',
  {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
  }
);

const desenhoProto = grpc.loadPackageDefinition(packageDefinition);

// Canal gRPC (equivalente ao grpc.insecure_channel)
const client = new desenhoProto.desenho.DesenhoService(
  'localhost:50051',
  grpc.credentials.createInsecure()
);

// Servidor Hapi
const init = async () => {
  const server = Hapi.server({
    port: 3000,
    host: 'localhost',
    routes: {
      cors: {
        origin: ['*'],       // allow_origins=["*"]
        headers: ['*'],      // allow_headers=["*"]
        additionalHeaders: ['*']
      }
    }
  });

  // Rota GET /reclamar
  server.route({
    method: 'GET',
    path: '/reclamar',
    handler: (request, h) => {
      const evento = request.query.evento || 'click';

      return new Promise((resolve, reject) => {
        client.Reclamar(
          { evento: evento },
          (err, response) => {
            if (err) {
              return reject(err);
            }

            resolve({
              evento: evento,
              texto: response.texto
            });
          }
        );
      });
    }
  });

  await server.start();
  console.log('Servidor rodando em:', server.info.uri);
};

process.on('unhandledRejection', (err) => {
  console.error(err);
  process.exit(1);
});

init();
