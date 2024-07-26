# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ftp/ftp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rftp/ftp.proto\x12\x0emavsdk.rpc.ftp\x1a\x14mavsdk_options.proto\"Z\n\x18SubscribeDownloadRequest\x12\x18\n\x10remote_file_path\x18\x01 \x01(\t\x12\x11\n\tlocal_dir\x18\x02 \x01(\t\x12\x11\n\tuse_burst\x18\x03 \x01(\x08\"v\n\x10\x44ownloadResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\x12\x33\n\rprogress_data\x18\x02 \x01(\x0b\x32\x1c.mavsdk.rpc.ftp.ProgressData\"E\n\x16SubscribeUploadRequest\x12\x17\n\x0flocal_file_path\x18\x01 \x01(\t\x12\x12\n\nremote_dir\x18\x02 \x01(\t\"t\n\x0eUploadResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\x12\x33\n\rprogress_data\x18\x02 \x01(\x0b\x32\x1c.mavsdk.rpc.ftp.ProgressData\"*\n\x14ListDirectoryRequest\x12\x12\n\nremote_dir\x18\x01 \x01(\t\"U\n\x15ListDirectoryResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\x12\r\n\x05paths\x18\x02 \x03(\t\",\n\x16\x43reateDirectoryRequest\x12\x12\n\nremote_dir\x18\x01 \x01(\t\"H\n\x17\x43reateDirectoryResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\",\n\x16RemoveDirectoryRequest\x12\x12\n\nremote_dir\x18\x01 \x01(\t\"H\n\x17RemoveDirectoryResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\"-\n\x11RemoveFileRequest\x12\x18\n\x10remote_file_path\x18\x01 \x01(\t\"C\n\x12RemoveFileResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\"A\n\rRenameRequest\x12\x18\n\x10remote_from_path\x18\x01 \x01(\t\x12\x16\n\x0eremote_to_path\x18\x02 \x01(\t\"?\n\x0eRenameResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\"M\n\x18\x41reFilesIdenticalRequest\x12\x17\n\x0flocal_file_path\x18\x01 \x01(\t\x12\x18\n\x10remote_file_path\x18\x02 \x01(\t\"a\n\x19\x41reFilesIdenticalResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\x12\x15\n\rare_identical\x18\x02 \x01(\x08\"(\n\x16SetTargetCompidRequest\x12\x0e\n\x06\x63ompid\x18\x01 \x01(\r\"H\n\x17SetTargetCompidResponse\x12-\n\nftp_result\x18\x01 \x01(\x0b\x32\x19.mavsdk.rpc.ftp.FtpResult\">\n\x0cProgressData\x12\x19\n\x11\x62ytes_transferred\x18\x01 \x01(\r\x12\x13\n\x0btotal_bytes\x18\x02 \x01(\r\"\x8e\x03\n\tFtpResult\x12\x30\n\x06result\x18\x01 \x01(\x0e\x32 .mavsdk.rpc.ftp.FtpResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xba\x02\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x0f\n\x0bRESULT_NEXT\x10\x02\x12\x12\n\x0eRESULT_TIMEOUT\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x18\n\x14RESULT_FILE_IO_ERROR\x10\x05\x12\x16\n\x12RESULT_FILE_EXISTS\x10\x06\x12\x1e\n\x1aRESULT_FILE_DOES_NOT_EXIST\x10\x07\x12\x19\n\x15RESULT_FILE_PROTECTED\x10\x08\x12\x1c\n\x18RESULT_INVALID_PARAMETER\x10\t\x12\x16\n\x12RESULT_UNSUPPORTED\x10\n\x12\x19\n\x15RESULT_PROTOCOL_ERROR\x10\x0b\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x0c\x32\x84\x07\n\nFtpService\x12k\n\x11SubscribeDownload\x12(.mavsdk.rpc.ftp.SubscribeDownloadRequest\x1a .mavsdk.rpc.ftp.DownloadResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\x65\n\x0fSubscribeUpload\x12&.mavsdk.rpc.ftp.SubscribeUploadRequest\x1a\x1e.mavsdk.rpc.ftp.UploadResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12^\n\rListDirectory\x12$.mavsdk.rpc.ftp.ListDirectoryRequest\x1a%.mavsdk.rpc.ftp.ListDirectoryResponse\"\x00\x12\x64\n\x0f\x43reateDirectory\x12&.mavsdk.rpc.ftp.CreateDirectoryRequest\x1a\'.mavsdk.rpc.ftp.CreateDirectoryResponse\"\x00\x12\x64\n\x0fRemoveDirectory\x12&.mavsdk.rpc.ftp.RemoveDirectoryRequest\x1a\'.mavsdk.rpc.ftp.RemoveDirectoryResponse\"\x00\x12U\n\nRemoveFile\x12!.mavsdk.rpc.ftp.RemoveFileRequest\x1a\".mavsdk.rpc.ftp.RemoveFileResponse\"\x00\x12I\n\x06Rename\x12\x1d.mavsdk.rpc.ftp.RenameRequest\x1a\x1e.mavsdk.rpc.ftp.RenameResponse\"\x00\x12j\n\x11\x41reFilesIdentical\x12(.mavsdk.rpc.ftp.AreFilesIdenticalRequest\x1a).mavsdk.rpc.ftp.AreFilesIdenticalResponse\"\x00\x12h\n\x0fSetTargetCompid\x12&.mavsdk.rpc.ftp.SetTargetCompidRequest\x1a\'.mavsdk.rpc.ftp.SetTargetCompidResponse\"\x04\x80\xb5\x18\x01\x42\x19\n\rio.mavsdk.ftpB\x08\x46tpProtob\x06proto3')



_SUBSCRIBEDOWNLOADREQUEST = DESCRIPTOR.message_types_by_name['SubscribeDownloadRequest']
_DOWNLOADRESPONSE = DESCRIPTOR.message_types_by_name['DownloadResponse']
_SUBSCRIBEUPLOADREQUEST = DESCRIPTOR.message_types_by_name['SubscribeUploadRequest']
_UPLOADRESPONSE = DESCRIPTOR.message_types_by_name['UploadResponse']
_LISTDIRECTORYREQUEST = DESCRIPTOR.message_types_by_name['ListDirectoryRequest']
_LISTDIRECTORYRESPONSE = DESCRIPTOR.message_types_by_name['ListDirectoryResponse']
_CREATEDIRECTORYREQUEST = DESCRIPTOR.message_types_by_name['CreateDirectoryRequest']
_CREATEDIRECTORYRESPONSE = DESCRIPTOR.message_types_by_name['CreateDirectoryResponse']
_REMOVEDIRECTORYREQUEST = DESCRIPTOR.message_types_by_name['RemoveDirectoryRequest']
_REMOVEDIRECTORYRESPONSE = DESCRIPTOR.message_types_by_name['RemoveDirectoryResponse']
_REMOVEFILEREQUEST = DESCRIPTOR.message_types_by_name['RemoveFileRequest']
_REMOVEFILERESPONSE = DESCRIPTOR.message_types_by_name['RemoveFileResponse']
_RENAMEREQUEST = DESCRIPTOR.message_types_by_name['RenameRequest']
_RENAMERESPONSE = DESCRIPTOR.message_types_by_name['RenameResponse']
_AREFILESIDENTICALREQUEST = DESCRIPTOR.message_types_by_name['AreFilesIdenticalRequest']
_AREFILESIDENTICALRESPONSE = DESCRIPTOR.message_types_by_name['AreFilesIdenticalResponse']
_SETTARGETCOMPIDREQUEST = DESCRIPTOR.message_types_by_name['SetTargetCompidRequest']
_SETTARGETCOMPIDRESPONSE = DESCRIPTOR.message_types_by_name['SetTargetCompidResponse']
_PROGRESSDATA = DESCRIPTOR.message_types_by_name['ProgressData']
_FTPRESULT = DESCRIPTOR.message_types_by_name['FtpResult']
_FTPRESULT_RESULT = _FTPRESULT.enum_types_by_name['Result']
SubscribeDownloadRequest = _reflection.GeneratedProtocolMessageType('SubscribeDownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEDOWNLOADREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.SubscribeDownloadRequest)
  })
_sym_db.RegisterMessage(SubscribeDownloadRequest)

DownloadResponse = _reflection.GeneratedProtocolMessageType('DownloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADRESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.DownloadResponse)
  })
_sym_db.RegisterMessage(DownloadResponse)

SubscribeUploadRequest = _reflection.GeneratedProtocolMessageType('SubscribeUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEUPLOADREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.SubscribeUploadRequest)
  })
_sym_db.RegisterMessage(SubscribeUploadRequest)

UploadResponse = _reflection.GeneratedProtocolMessageType('UploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADRESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.UploadResponse)
  })
_sym_db.RegisterMessage(UploadResponse)

ListDirectoryRequest = _reflection.GeneratedProtocolMessageType('ListDirectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDIRECTORYREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.ListDirectoryRequest)
  })
_sym_db.RegisterMessage(ListDirectoryRequest)

ListDirectoryResponse = _reflection.GeneratedProtocolMessageType('ListDirectoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDIRECTORYRESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.ListDirectoryResponse)
  })
_sym_db.RegisterMessage(ListDirectoryResponse)

CreateDirectoryRequest = _reflection.GeneratedProtocolMessageType('CreateDirectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDIRECTORYREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.CreateDirectoryRequest)
  })
_sym_db.RegisterMessage(CreateDirectoryRequest)

CreateDirectoryResponse = _reflection.GeneratedProtocolMessageType('CreateDirectoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDIRECTORYRESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.CreateDirectoryResponse)
  })
_sym_db.RegisterMessage(CreateDirectoryResponse)

RemoveDirectoryRequest = _reflection.GeneratedProtocolMessageType('RemoveDirectoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEDIRECTORYREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.RemoveDirectoryRequest)
  })
_sym_db.RegisterMessage(RemoveDirectoryRequest)

RemoveDirectoryResponse = _reflection.GeneratedProtocolMessageType('RemoveDirectoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEDIRECTORYRESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.RemoveDirectoryResponse)
  })
_sym_db.RegisterMessage(RemoveDirectoryResponse)

RemoveFileRequest = _reflection.GeneratedProtocolMessageType('RemoveFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFILEREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.RemoveFileRequest)
  })
_sym_db.RegisterMessage(RemoveFileRequest)

RemoveFileResponse = _reflection.GeneratedProtocolMessageType('RemoveFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEFILERESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.RemoveFileResponse)
  })
_sym_db.RegisterMessage(RemoveFileResponse)

RenameRequest = _reflection.GeneratedProtocolMessageType('RenameRequest', (_message.Message,), {
  'DESCRIPTOR' : _RENAMEREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.RenameRequest)
  })
_sym_db.RegisterMessage(RenameRequest)

RenameResponse = _reflection.GeneratedProtocolMessageType('RenameResponse', (_message.Message,), {
  'DESCRIPTOR' : _RENAMERESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.RenameResponse)
  })
_sym_db.RegisterMessage(RenameResponse)

AreFilesIdenticalRequest = _reflection.GeneratedProtocolMessageType('AreFilesIdenticalRequest', (_message.Message,), {
  'DESCRIPTOR' : _AREFILESIDENTICALREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.AreFilesIdenticalRequest)
  })
_sym_db.RegisterMessage(AreFilesIdenticalRequest)

AreFilesIdenticalResponse = _reflection.GeneratedProtocolMessageType('AreFilesIdenticalResponse', (_message.Message,), {
  'DESCRIPTOR' : _AREFILESIDENTICALRESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.AreFilesIdenticalResponse)
  })
_sym_db.RegisterMessage(AreFilesIdenticalResponse)

SetTargetCompidRequest = _reflection.GeneratedProtocolMessageType('SetTargetCompidRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETTARGETCOMPIDREQUEST,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.SetTargetCompidRequest)
  })
_sym_db.RegisterMessage(SetTargetCompidRequest)

SetTargetCompidResponse = _reflection.GeneratedProtocolMessageType('SetTargetCompidResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETTARGETCOMPIDRESPONSE,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.SetTargetCompidResponse)
  })
_sym_db.RegisterMessage(SetTargetCompidResponse)

ProgressData = _reflection.GeneratedProtocolMessageType('ProgressData', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSDATA,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.ProgressData)
  })
_sym_db.RegisterMessage(ProgressData)

FtpResult = _reflection.GeneratedProtocolMessageType('FtpResult', (_message.Message,), {
  'DESCRIPTOR' : _FTPRESULT,
  '__module__' : 'ftp.ftp_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.ftp.FtpResult)
  })
_sym_db.RegisterMessage(FtpResult)

_FTPSERVICE = DESCRIPTOR.services_by_name['FtpService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rio.mavsdk.ftpB\010FtpProto'
  _FTPSERVICE.methods_by_name['SubscribeDownload']._options = None
  _FTPSERVICE.methods_by_name['SubscribeDownload']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _FTPSERVICE.methods_by_name['SubscribeUpload']._options = None
  _FTPSERVICE.methods_by_name['SubscribeUpload']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _FTPSERVICE.methods_by_name['SetTargetCompid']._options = None
  _FTPSERVICE.methods_by_name['SetTargetCompid']._serialized_options = b'\200\265\030\001'
  _SUBSCRIBEDOWNLOADREQUEST._serialized_start=55
  _SUBSCRIBEDOWNLOADREQUEST._serialized_end=145
  _DOWNLOADRESPONSE._serialized_start=147
  _DOWNLOADRESPONSE._serialized_end=265
  _SUBSCRIBEUPLOADREQUEST._serialized_start=267
  _SUBSCRIBEUPLOADREQUEST._serialized_end=336
  _UPLOADRESPONSE._serialized_start=338
  _UPLOADRESPONSE._serialized_end=454
  _LISTDIRECTORYREQUEST._serialized_start=456
  _LISTDIRECTORYREQUEST._serialized_end=498
  _LISTDIRECTORYRESPONSE._serialized_start=500
  _LISTDIRECTORYRESPONSE._serialized_end=585
  _CREATEDIRECTORYREQUEST._serialized_start=587
  _CREATEDIRECTORYREQUEST._serialized_end=631
  _CREATEDIRECTORYRESPONSE._serialized_start=633
  _CREATEDIRECTORYRESPONSE._serialized_end=705
  _REMOVEDIRECTORYREQUEST._serialized_start=707
  _REMOVEDIRECTORYREQUEST._serialized_end=751
  _REMOVEDIRECTORYRESPONSE._serialized_start=753
  _REMOVEDIRECTORYRESPONSE._serialized_end=825
  _REMOVEFILEREQUEST._serialized_start=827
  _REMOVEFILEREQUEST._serialized_end=872
  _REMOVEFILERESPONSE._serialized_start=874
  _REMOVEFILERESPONSE._serialized_end=941
  _RENAMEREQUEST._serialized_start=943
  _RENAMEREQUEST._serialized_end=1008
  _RENAMERESPONSE._serialized_start=1010
  _RENAMERESPONSE._serialized_end=1073
  _AREFILESIDENTICALREQUEST._serialized_start=1075
  _AREFILESIDENTICALREQUEST._serialized_end=1152
  _AREFILESIDENTICALRESPONSE._serialized_start=1154
  _AREFILESIDENTICALRESPONSE._serialized_end=1251
  _SETTARGETCOMPIDREQUEST._serialized_start=1253
  _SETTARGETCOMPIDREQUEST._serialized_end=1293
  _SETTARGETCOMPIDRESPONSE._serialized_start=1295
  _SETTARGETCOMPIDRESPONSE._serialized_end=1367
  _PROGRESSDATA._serialized_start=1369
  _PROGRESSDATA._serialized_end=1431
  _FTPRESULT._serialized_start=1434
  _FTPRESULT._serialized_end=1832
  _FTPRESULT_RESULT._serialized_start=1518
  _FTPRESULT_RESULT._serialized_end=1832
  _FTPSERVICE._serialized_start=1835
  _FTPSERVICE._serialized_end=2735
# @@protoc_insertion_point(module_scope)
