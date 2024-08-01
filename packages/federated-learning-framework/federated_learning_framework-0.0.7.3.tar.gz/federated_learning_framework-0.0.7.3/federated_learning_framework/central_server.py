# import asyncio
# import logging
# import numpy as np
# from federated_learning_framework.connection import ConnectionServer
# from websockets.exceptions import ConnectionClosedError
# from federated_learning_framework.encryption import create_context

# class CentralServer:
#     def __init__(self, connection_type='websocket', host='0.0.0.0', port=8089, context=None):
#         self.model_weights = None
#         self.lock = asyncio.Lock()
#         self.clients = set()
#         self.logger = logging.getLogger(__name__)
#         self.connection = ConnectionServer(connection_type, host, port, self.handle_client)
#         self.context = context or create_context()

#     async def run_server(self):
#         self.logger.info("Central Server is starting...")
#         await self.connection.start()

#     async def handle_client(self, websocket, client_id):
#         self.clients.add(client_id)
#         self.logger.info(f"Central Server: Client {client_id} connected")
#         try:
#             while True:
#                 message = await self.connection.receive(client_id)
#                 if isinstance(message, dict):
#                     if 'weights' in message:
#                         await self.transmit_weights(message['weights'])
#                     elif 'data_request' in message:
#                         data = await self.get_data_from_client(client_id)
#                         await self.send_data_to_client(client_id, {'data': data})
#         except ConnectionClosedError:
#             self.logger.info(f"Central Server: Client {client_id} disconnected")
#         finally:
#             self.clients.remove(client_id)

#     async def transmit_weights(self, weights):
#         async with self.lock:
#             self.model_weights = weights
#             await asyncio.gather(*[self.connection.send(client_id, {'weights': self.model_weights}) for client_id in self.clients])
#             self.logger.info("Central Server: Transmitted weights to clients")

#     async def send_data_to_client(self, client_id, data):
#         self.logger.info(f"Central Server: Sending data to client {client_id}")
#         await self.connection.send(client_id, data)

#     async def get_data_from_client(self, client_id):
#         self.logger.info(f"Central Server: Requesting data from client {client_id}. Simulating response.")
#         await asyncio.sleep(1)
#         return np.random.rand(10, 3072)

#     def query_active_learning(self, unlabeled_data, model):
#         uncertainty = model.predict(unlabeled_data)
#         selected_indices = np.argsort(uncertainty.max(axis=1))[:5]
#         return selected_indices

import asyncio
import logging
import pickle
import websockets

class CentralServer:
    def __init__(self, connection_type, context, port=8089):
        self.connection_type = connection_type
        self.context = context
        self.port = port
        self.clients = {}
        self.logger = logging.getLogger(__name__)
        self.model_weights = None

    async def run_server(self):
        if self.connection_type == 'websocket':
            try:
                async with websockets.serve(self.handle_client, 'localhost', self.port):
                    self.logger.info(f"Server started on port {self.port}")
                    await asyncio.Future()  # Run forever
            except Exception as e:
                self.logger.error(f"Error starting server: {e}")
        else:
            raise NotImplementedError(f"Connection type {self.connection_type} not supported")

    async def handle_client(self, websocket, path):
        client_id = len(self.clients) + 1
        self.clients[client_id] = websocket
        self.logger.info(f"Client {client_id} connected")

        try:
            # Initial message should contain client ID
            message = await websocket.recv()
            data = pickle.loads(message)
            self.logger.info(f"Received from client {client_id}: {data}")

            if 'client_id' in data:
                # Send initial model weights to the client
                await self.send_weights(client_id)

                # Listen for weight updates
                while True:
                    message = await websocket.recv()
                    data = pickle.loads(message)
                    if 'weights' in data:
                        self.logger.info(f"Received weights from client {client_id}")
                        # Handle weight aggregation here (e.g., averaging weights from all clients)
                        self.model_weights = data['weights']  # For simplicity, we just set it here
                        await self.broadcast_weights()
        except websockets.ConnectionClosed:
            self.logger.info(f"Client {client_id} disconnected")
            del self.clients[client_id]

    async def send_weights(self, client_id):
        if self.model_weights is not None:
            await self.send_message(client_id, {'weights': self.model_weights})

    async def send_message(self, client_id, message):
        try:
            serialized_message = pickle.dumps(message)
            await self.clients[client_id].send(serialized_message)
        except Exception as e:
            self.logger.error(f"Error sending message to client {client_id}: {e}")

    async def broadcast_weights(self):
        for client_id in self.clients.keys():
            await self.send_weights(client_id)


