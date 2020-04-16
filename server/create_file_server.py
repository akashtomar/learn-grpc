from concurrent import futures
import logging

import grpc

import TaskMsg_pb2
import TaskMsg_pb2_grpc
import simple_task


class CreateFile(TaskMsg_pb2_grpc.FileCreaterServicer):
    
    def CreateFile(self, request, context):
        #print('request', request)
        msg = simple_task.create_file(request.fileName, request.content)
        return TaskMsg_pb2.CreateFileReply(message=msg)



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TaskMsg_pb2_grpc.add_FileCreaterServicer_to_server(CreateFile(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
	print("here here!")
	logging.basicConfig()
	serve()
