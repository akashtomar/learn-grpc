from concurrent import futures
import logging

import grpc

import TaskMsg_pb2
import TaskMsg_pb2_grpc


class CreateFile(TaskMsg_pb2_grpc.FileCreaterServicer):
    
    def CreateFile(self, request, context):
        print('request', request)
        return TaskMsg_pb2.CreateFileReply(message="Task added")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_worker=10))
    TaskMsg_pb2_grpc.add_FileCreaterServicer_to_server(CreateFile(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == 'main':
    logging.basicConfig()
    serve()