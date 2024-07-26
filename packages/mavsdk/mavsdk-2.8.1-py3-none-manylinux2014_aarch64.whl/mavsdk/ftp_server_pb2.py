# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ftp_server/ftp_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66tp_server/ftp_server.proto\x12\x15mavsdk.rpc.ftp_server\x1a\x14mavsdk_options.proto\"!\n\x11SetRootDirRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"W\n\x12SetRootDirResponse\x12\x41\n\x11\x66tp_server_result\x18\x01 \x01(\x0b\x32&.mavsdk.rpc.ftp_server.FtpServerResult\"\xc2\x01\n\x0f\x46tpServerResult\x12=\n\x06result\x18\x01 \x01(\x0e\x32-.mavsdk.rpc.ftp_server.FtpServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\\\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x19\n\x15RESULT_DOES_NOT_EXIST\x10\x02\x12\x0f\n\x0bRESULT_BUSY\x10\x03\x32{\n\x10\x46tpServerService\x12g\n\nSetRootDir\x12(.mavsdk.rpc.ftp_server.SetRootDirRequest\x1a).mavsdk.rpc.ftp_server.SetRootDirResponse\"\x04\x80\xb5\x18\x01\x42&\n\x14io.mavsdk.ftp_serverB\x0e\x46tpServerProtob\x06proto3')



_SETROOTDIRREQUEST = DESCRIPTOR.message_types_by_name['SetRootDirRequest']
_SETROOTDIRRESPONSE = DESCRIPTOR.message_types_by_name['SetRootDirResponse']
_FTPSERVERRESULT = DESCRIPTOR.message_types_by_name['FtpServerResult']
_FTPSERVERRESULT_RESULT = _FTPSERVERRESULT.enum_types_by_name['Result']
SetRootDirRequest = _reflection.GeneratedProtocolMessageType('SetRootDirRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETROOTDIRREQUEST,
  '__module__' : 'ftp_server.ftp_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp_server.SetRootDirRequest)
  })
_sym_db.RegisterMessage(SetRootDirRequest)

SetRootDirResponse = _reflection.GeneratedProtocolMessageType('SetRootDirResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETROOTDIRRESPONSE,
  '__module__' : 'ftp_server.ftp_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp_server.SetRootDirResponse)
  })
_sym_db.RegisterMessage(SetRootDirResponse)

FtpServerResult = _reflection.GeneratedProtocolMessageType('FtpServerResult', (_message.Message,), {
  'DESCRIPTOR' : _FTPSERVERRESULT,
  '__module__' : 'ftp_server.ftp_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp_server.FtpServerResult)
  })
_sym_db.RegisterMessage(FtpServerResult)

_FTPSERVERSERVICE = DESCRIPTOR.services_by_name['FtpServerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024io.mavsdk.ftp_serverB\016FtpServerProto'
  _FTPSERVERSERVICE.methods_by_name['SetRootDir']._options = None
  _FTPSERVERSERVICE.methods_by_name['SetRootDir']._serialized_options = b'\200\265\030\001'
  _SETROOTDIRREQUEST._serialized_start=76
  _SETROOTDIRREQUEST._serialized_end=109
  _SETROOTDIRRESPONSE._serialized_start=111
  _SETROOTDIRRESPONSE._serialized_end=198
  _FTPSERVERRESULT._serialized_start=201
  _FTPSERVERRESULT._serialized_end=395
  _FTPSERVERRESULT_RESULT._serialized_start=303
  _FTPSERVERRESULT_RESULT._serialized_end=395
  _FTPSERVERSERVICE._serialized_start=397
  _FTPSERVERSERVICE._serialized_end=520
# @@protoc_insertion_point(module_scope)
