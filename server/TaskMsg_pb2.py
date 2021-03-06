# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TaskMsg.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TaskMsg.proto',
  package='createfile',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rTaskMsg.proto\x12\ncreatefile\"6\n\x11\x43reateFileRequest\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\"\"\n\x0f\x43reateFileReply\x12\x0f\n\x07message\x18\x01 \x01(\t2Y\n\x0b\x46ileCreater\x12J\n\nCreateFile\x12\x1d.createfile.CreateFileRequest\x1a\x1b.createfile.CreateFileReply\"\x00\x62\x06proto3'
)




_CREATEFILEREQUEST = _descriptor.Descriptor(
  name='CreateFileRequest',
  full_name='createfile.CreateFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fileName', full_name='createfile.CreateFileRequest.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='createfile.CreateFileRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=83,
)


_CREATEFILEREPLY = _descriptor.Descriptor(
  name='CreateFileReply',
  full_name='createfile.CreateFileReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='createfile.CreateFileReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['CreateFileRequest'] = _CREATEFILEREQUEST
DESCRIPTOR.message_types_by_name['CreateFileReply'] = _CREATEFILEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateFileRequest = _reflection.GeneratedProtocolMessageType('CreateFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFILEREQUEST,
  '__module__' : 'TaskMsg_pb2'
  # @@protoc_insertion_point(class_scope:createfile.CreateFileRequest)
  })
_sym_db.RegisterMessage(CreateFileRequest)

CreateFileReply = _reflection.GeneratedProtocolMessageType('CreateFileReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEFILEREPLY,
  '__module__' : 'TaskMsg_pb2'
  # @@protoc_insertion_point(class_scope:createfile.CreateFileReply)
  })
_sym_db.RegisterMessage(CreateFileReply)



_FILECREATER = _descriptor.ServiceDescriptor(
  name='FileCreater',
  full_name='createfile.FileCreater',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=121,
  serialized_end=210,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateFile',
    full_name='createfile.FileCreater.CreateFile',
    index=0,
    containing_service=None,
    input_type=_CREATEFILEREQUEST,
    output_type=_CREATEFILEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILECREATER)

DESCRIPTOR.services_by_name['FileCreater'] = _FILECREATER

# @@protoc_insertion_point(module_scope)
