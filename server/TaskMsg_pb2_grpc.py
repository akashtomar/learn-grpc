# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import TaskMsg_pb2 as TaskMsg__pb2


class FileCreaterStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateFile = channel.unary_unary(
                '/createfile.FileCreater/CreateFile',
                request_serializer=TaskMsg__pb2.CreateFileRequest.SerializeToString,
                response_deserializer=TaskMsg__pb2.CreateFileReply.FromString,
                )


class FileCreaterServicer(object):
    """Missing associated documentation comment in .proto file"""

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileCreaterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=TaskMsg__pb2.CreateFileRequest.FromString,
                    response_serializer=TaskMsg__pb2.CreateFileReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'createfile.FileCreater', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileCreater(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/createfile.FileCreater/CreateFile',
            TaskMsg__pb2.CreateFileRequest.SerializeToString,
            TaskMsg__pb2.CreateFileReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
