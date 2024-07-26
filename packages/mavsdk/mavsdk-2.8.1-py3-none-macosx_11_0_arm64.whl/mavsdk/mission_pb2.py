# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mission/mission.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15mission/mission.proto\x12\x12mavsdk.rpc.mission\x1a\x14mavsdk_options.proto\"M\n\x14UploadMissionRequest\x12\x35\n\x0cmission_plan\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.mission.MissionPlan\"R\n\x15UploadMissionResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"b\n)SubscribeUploadMissionWithProgressRequest\x12\x35\n\x0cmission_plan\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.mission.MissionPlan\"\x97\x01\n!UploadMissionWithProgressResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\x12\x37\n\rprogress_data\x18\x02 \x01(\x0b\x32 .mavsdk.rpc.mission.ProgressData\"\x1c\n\x1a\x43\x61ncelMissionUploadRequest\"X\n\x1b\x43\x61ncelMissionUploadResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"\x18\n\x16\x44ownloadMissionRequest\"\x8b\x01\n\x17\x44ownloadMissionResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\x12\x35\n\x0cmission_plan\x18\x02 \x01(\x0b\x32\x1f.mavsdk.rpc.mission.MissionPlan\"-\n+SubscribeDownloadMissionWithProgressRequest\"\xa2\x01\n#DownloadMissionWithProgressResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\x12@\n\rprogress_data\x18\x02 \x01(\x0b\x32).mavsdk.rpc.mission.ProgressDataOrMission\"\x1e\n\x1c\x43\x61ncelMissionDownloadRequest\"Z\n\x1d\x43\x61ncelMissionDownloadResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"\x15\n\x13StartMissionRequest\"Q\n\x14StartMissionResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"\x15\n\x13PauseMissionRequest\"Q\n\x14PauseMissionResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"\x15\n\x13\x43learMissionRequest\"Q\n\x14\x43learMissionResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"-\n\x1cSetCurrentMissionItemRequest\x12\r\n\x05index\x18\x01 \x01(\x05\"Z\n\x1dSetCurrentMissionItemResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"\x1a\n\x18IsMissionFinishedRequest\"k\n\x19IsMissionFinishedResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\x12\x13\n\x0bis_finished\x18\x02 \x01(\x08\"!\n\x1fSubscribeMissionProgressRequest\"X\n\x17MissionProgressResponse\x12=\n\x10mission_progress\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.mission.MissionProgress\"&\n$GetReturnToLaunchAfterMissionRequest\"r\n%GetReturnToLaunchAfterMissionResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\"6\n$SetReturnToLaunchAfterMissionRequest\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"b\n%SetReturnToLaunchAfterMissionResponse\x12\x39\n\x0emission_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.mission.MissionResult\"\xad\x08\n\x0bMissionItem\x12(\n\x0clatitude_deg\x18\x01 \x01(\x01\x42\x12\x82\xb5\x18\x03NaN\x89\xb5\x18H\xaf\xbc\x9a\xf2\xd7z>\x12)\n\rlongitude_deg\x18\x02 \x01(\x01\x42\x12\x82\xb5\x18\x03NaN\x89\xb5\x18H\xaf\xbc\x9a\xf2\xd7z>\x12$\n\x13relative_altitude_m\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1a\n\tspeed_m_s\x18\x04 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12!\n\x0eis_fly_through\x18\x05 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12,\n\x10gimbal_pitch_deg\x18\x06 \x01(\x02\x42\x12\x82\xb5\x18\x03NaN\x89\xb5\x18-C\x1c\xeb\xe2\x36\x1a?\x12*\n\x0egimbal_yaw_deg\x18\x07 \x01(\x02\x42\x12\x82\xb5\x18\x03NaN\x89\xb5\x18-C\x1c\xeb\xe2\x36\x1a?\x12\x43\n\rcamera_action\x18\x08 \x01(\x0e\x32,.mavsdk.rpc.mission.MissionItem.CameraAction\x12\x1e\n\rloiter_time_s\x18\t \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12(\n\x17\x63\x61mera_photo_interval_s\x18\n \x01(\x01\x42\x07\x82\xb5\x18\x03\x31.0\x12$\n\x13\x61\x63\x63\x65ptance_radius_m\x18\x0b \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x18\n\x07yaw_deg\x18\x0c \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12(\n\x17\x63\x61mera_photo_distance_m\x18\r \x01(\x02\x42\x07\x82\xb5\x18\x03NAN\x12\x45\n\x0evehicle_action\x18\x0e \x01(\x0e\x32-.mavsdk.rpc.mission.MissionItem.VehicleAction\"\x9f\x02\n\x0c\x43\x61meraAction\x12\x16\n\x12\x43\x41MERA_ACTION_NONE\x10\x00\x12\x1c\n\x18\x43\x41MERA_ACTION_TAKE_PHOTO\x10\x01\x12&\n\"CAMERA_ACTION_START_PHOTO_INTERVAL\x10\x02\x12%\n!CAMERA_ACTION_STOP_PHOTO_INTERVAL\x10\x03\x12\x1d\n\x19\x43\x41MERA_ACTION_START_VIDEO\x10\x04\x12\x1c\n\x18\x43\x41MERA_ACTION_STOP_VIDEO\x10\x05\x12&\n\"CAMERA_ACTION_START_PHOTO_DISTANCE\x10\x06\x12%\n!CAMERA_ACTION_STOP_PHOTO_DISTANCE\x10\x07\"\xa7\x01\n\rVehicleAction\x12\x17\n\x13VEHICLE_ACTION_NONE\x10\x00\x12\x1a\n\x16VEHICLE_ACTION_TAKEOFF\x10\x01\x12\x17\n\x13VEHICLE_ACTION_LAND\x10\x02\x12#\n\x1fVEHICLE_ACTION_TRANSITION_TO_FW\x10\x03\x12#\n\x1fVEHICLE_ACTION_TRANSITION_TO_MC\x10\x04\"E\n\x0bMissionPlan\x12\x36\n\rmission_items\x18\x01 \x03(\x0b\x32\x1f.mavsdk.rpc.mission.MissionItem\"1\n\x0fMissionProgress\x12\x0f\n\x07\x63urrent\x18\x01 \x01(\x05\x12\r\n\x05total\x18\x02 \x01(\x05\"\xff\x03\n\rMissionResult\x12\x38\n\x06result\x18\x01 \x01(\x0e\x32(.mavsdk.rpc.mission.MissionResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x9f\x03\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x10\n\x0cRESULT_ERROR\x10\x02\x12!\n\x1dRESULT_TOO_MANY_MISSION_ITEMS\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x12\n\x0eRESULT_TIMEOUT\x10\x05\x12\x1b\n\x17RESULT_INVALID_ARGUMENT\x10\x06\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x07\x12\x1f\n\x1bRESULT_NO_MISSION_AVAILABLE\x10\x08\x12\"\n\x1eRESULT_UNSUPPORTED_MISSION_CMD\x10\x0b\x12\x1d\n\x19RESULT_TRANSFER_CANCELLED\x10\x0c\x12\x14\n\x10RESULT_NO_SYSTEM\x10\r\x12\x0f\n\x0bRESULT_NEXT\x10\x0e\x12\x11\n\rRESULT_DENIED\x10\x0f\x12\x19\n\x15RESULT_PROTOCOL_ERROR\x10\x10\x12%\n!RESULT_INT_MESSAGES_NOT_SUPPORTED\x10\x11\")\n\x0cProgressData\x12\x19\n\x08progress\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"\x9f\x01\n\x15ProgressDataOrMission\x12\x1f\n\x0chas_progress\x18\x01 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12\x19\n\x08progress\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x13\n\x0bhas_mission\x18\x03 \x01(\x08\x12\x35\n\x0cmission_plan\x18\x04 \x01(\x0b\x32\x1f.mavsdk.rpc.mission.MissionPlan2\xa5\x0e\n\x0eMissionService\x12\x66\n\rUploadMission\x12(.mavsdk.rpc.mission.UploadMissionRequest\x1a).mavsdk.rpc.mission.UploadMissionResponse\"\x00\x12\xa6\x01\n\"SubscribeUploadMissionWithProgress\x12=.mavsdk.rpc.mission.SubscribeUploadMissionWithProgressRequest\x1a\x35.mavsdk.rpc.mission.UploadMissionWithProgressResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12|\n\x13\x43\x61ncelMissionUpload\x12..mavsdk.rpc.mission.CancelMissionUploadRequest\x1a/.mavsdk.rpc.mission.CancelMissionUploadResponse\"\x04\x80\xb5\x18\x01\x12l\n\x0f\x44ownloadMission\x12*.mavsdk.rpc.mission.DownloadMissionRequest\x1a+.mavsdk.rpc.mission.DownloadMissionResponse\"\x00\x12\xac\x01\n$SubscribeDownloadMissionWithProgress\x12?.mavsdk.rpc.mission.SubscribeDownloadMissionWithProgressRequest\x1a\x37.mavsdk.rpc.mission.DownloadMissionWithProgressResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\x82\x01\n\x15\x43\x61ncelMissionDownload\x12\x30.mavsdk.rpc.mission.CancelMissionDownloadRequest\x1a\x31.mavsdk.rpc.mission.CancelMissionDownloadResponse\"\x04\x80\xb5\x18\x01\x12\x63\n\x0cStartMission\x12\'.mavsdk.rpc.mission.StartMissionRequest\x1a(.mavsdk.rpc.mission.StartMissionResponse\"\x00\x12\x63\n\x0cPauseMission\x12\'.mavsdk.rpc.mission.PauseMissionRequest\x1a(.mavsdk.rpc.mission.PauseMissionResponse\"\x00\x12\x63\n\x0c\x43learMission\x12\'.mavsdk.rpc.mission.ClearMissionRequest\x1a(.mavsdk.rpc.mission.ClearMissionResponse\"\x00\x12~\n\x15SetCurrentMissionItem\x12\x30.mavsdk.rpc.mission.SetCurrentMissionItemRequest\x1a\x31.mavsdk.rpc.mission.SetCurrentMissionItemResponse\"\x00\x12v\n\x11IsMissionFinished\x12,.mavsdk.rpc.mission.IsMissionFinishedRequest\x1a-.mavsdk.rpc.mission.IsMissionFinishedResponse\"\x04\x80\xb5\x18\x01\x12\x80\x01\n\x18SubscribeMissionProgress\x12\x33.mavsdk.rpc.mission.SubscribeMissionProgressRequest\x1a+.mavsdk.rpc.mission.MissionProgressResponse\"\x00\x30\x01\x12\x9a\x01\n\x1dGetReturnToLaunchAfterMission\x12\x38.mavsdk.rpc.mission.GetReturnToLaunchAfterMissionRequest\x1a\x39.mavsdk.rpc.mission.GetReturnToLaunchAfterMissionResponse\"\x04\x80\xb5\x18\x01\x12\x9a\x01\n\x1dSetReturnToLaunchAfterMission\x12\x38.mavsdk.rpc.mission.SetReturnToLaunchAfterMissionRequest\x1a\x39.mavsdk.rpc.mission.SetReturnToLaunchAfterMissionResponse\"\x04\x80\xb5\x18\x01\x42!\n\x11io.mavsdk.missionB\x0cMissionProtob\x06proto3')



_UPLOADMISSIONREQUEST = DESCRIPTOR.message_types_by_name['UploadMissionRequest']
_UPLOADMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['UploadMissionResponse']
_SUBSCRIBEUPLOADMISSIONWITHPROGRESSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeUploadMissionWithProgressRequest']
_UPLOADMISSIONWITHPROGRESSRESPONSE = DESCRIPTOR.message_types_by_name['UploadMissionWithProgressResponse']
_CANCELMISSIONUPLOADREQUEST = DESCRIPTOR.message_types_by_name['CancelMissionUploadRequest']
_CANCELMISSIONUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['CancelMissionUploadResponse']
_DOWNLOADMISSIONREQUEST = DESCRIPTOR.message_types_by_name['DownloadMissionRequest']
_DOWNLOADMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['DownloadMissionResponse']
_SUBSCRIBEDOWNLOADMISSIONWITHPROGRESSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeDownloadMissionWithProgressRequest']
_DOWNLOADMISSIONWITHPROGRESSRESPONSE = DESCRIPTOR.message_types_by_name['DownloadMissionWithProgressResponse']
_CANCELMISSIONDOWNLOADREQUEST = DESCRIPTOR.message_types_by_name['CancelMissionDownloadRequest']
_CANCELMISSIONDOWNLOADRESPONSE = DESCRIPTOR.message_types_by_name['CancelMissionDownloadResponse']
_STARTMISSIONREQUEST = DESCRIPTOR.message_types_by_name['StartMissionRequest']
_STARTMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['StartMissionResponse']
_PAUSEMISSIONREQUEST = DESCRIPTOR.message_types_by_name['PauseMissionRequest']
_PAUSEMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['PauseMissionResponse']
_CLEARMISSIONREQUEST = DESCRIPTOR.message_types_by_name['ClearMissionRequest']
_CLEARMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['ClearMissionResponse']
_SETCURRENTMISSIONITEMREQUEST = DESCRIPTOR.message_types_by_name['SetCurrentMissionItemRequest']
_SETCURRENTMISSIONITEMRESPONSE = DESCRIPTOR.message_types_by_name['SetCurrentMissionItemResponse']
_ISMISSIONFINISHEDREQUEST = DESCRIPTOR.message_types_by_name['IsMissionFinishedRequest']
_ISMISSIONFINISHEDRESPONSE = DESCRIPTOR.message_types_by_name['IsMissionFinishedResponse']
_SUBSCRIBEMISSIONPROGRESSREQUEST = DESCRIPTOR.message_types_by_name['SubscribeMissionProgressRequest']
_MISSIONPROGRESSRESPONSE = DESCRIPTOR.message_types_by_name['MissionProgressResponse']
_GETRETURNTOLAUNCHAFTERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['GetReturnToLaunchAfterMissionRequest']
_GETRETURNTOLAUNCHAFTERMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['GetReturnToLaunchAfterMissionResponse']
_SETRETURNTOLAUNCHAFTERMISSIONREQUEST = DESCRIPTOR.message_types_by_name['SetReturnToLaunchAfterMissionRequest']
_SETRETURNTOLAUNCHAFTERMISSIONRESPONSE = DESCRIPTOR.message_types_by_name['SetReturnToLaunchAfterMissionResponse']
_MISSIONITEM = DESCRIPTOR.message_types_by_name['MissionItem']
_MISSIONPLAN = DESCRIPTOR.message_types_by_name['MissionPlan']
_MISSIONPROGRESS = DESCRIPTOR.message_types_by_name['MissionProgress']
_MISSIONRESULT = DESCRIPTOR.message_types_by_name['MissionResult']
_PROGRESSDATA = DESCRIPTOR.message_types_by_name['ProgressData']
_PROGRESSDATAORMISSION = DESCRIPTOR.message_types_by_name['ProgressDataOrMission']
_MISSIONITEM_CAMERAACTION = _MISSIONITEM.enum_types_by_name['CameraAction']
_MISSIONITEM_VEHICLEACTION = _MISSIONITEM.enum_types_by_name['VehicleAction']
_MISSIONRESULT_RESULT = _MISSIONRESULT.enum_types_by_name['Result']
UploadMissionRequest = _reflection.GeneratedProtocolMessageType('UploadMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMISSIONREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.UploadMissionRequest)
  })
_sym_db.RegisterMessage(UploadMissionRequest)

UploadMissionResponse = _reflection.GeneratedProtocolMessageType('UploadMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMISSIONRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.UploadMissionResponse)
  })
_sym_db.RegisterMessage(UploadMissionResponse)

SubscribeUploadMissionWithProgressRequest = _reflection.GeneratedProtocolMessageType('SubscribeUploadMissionWithProgressRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEUPLOADMISSIONWITHPROGRESSREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.SubscribeUploadMissionWithProgressRequest)
  })
_sym_db.RegisterMessage(SubscribeUploadMissionWithProgressRequest)

UploadMissionWithProgressResponse = _reflection.GeneratedProtocolMessageType('UploadMissionWithProgressResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADMISSIONWITHPROGRESSRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.UploadMissionWithProgressResponse)
  })
_sym_db.RegisterMessage(UploadMissionWithProgressResponse)

CancelMissionUploadRequest = _reflection.GeneratedProtocolMessageType('CancelMissionUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONUPLOADREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.CancelMissionUploadRequest)
  })
_sym_db.RegisterMessage(CancelMissionUploadRequest)

CancelMissionUploadResponse = _reflection.GeneratedProtocolMessageType('CancelMissionUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONUPLOADRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.CancelMissionUploadResponse)
  })
_sym_db.RegisterMessage(CancelMissionUploadResponse)

DownloadMissionRequest = _reflection.GeneratedProtocolMessageType('DownloadMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADMISSIONREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.DownloadMissionRequest)
  })
_sym_db.RegisterMessage(DownloadMissionRequest)

DownloadMissionResponse = _reflection.GeneratedProtocolMessageType('DownloadMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADMISSIONRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.DownloadMissionResponse)
  })
_sym_db.RegisterMessage(DownloadMissionResponse)

SubscribeDownloadMissionWithProgressRequest = _reflection.GeneratedProtocolMessageType('SubscribeDownloadMissionWithProgressRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEDOWNLOADMISSIONWITHPROGRESSREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.SubscribeDownloadMissionWithProgressRequest)
  })
_sym_db.RegisterMessage(SubscribeDownloadMissionWithProgressRequest)

DownloadMissionWithProgressResponse = _reflection.GeneratedProtocolMessageType('DownloadMissionWithProgressResponse', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADMISSIONWITHPROGRESSRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.DownloadMissionWithProgressResponse)
  })
_sym_db.RegisterMessage(DownloadMissionWithProgressResponse)

CancelMissionDownloadRequest = _reflection.GeneratedProtocolMessageType('CancelMissionDownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONDOWNLOADREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.CancelMissionDownloadRequest)
  })
_sym_db.RegisterMessage(CancelMissionDownloadRequest)

CancelMissionDownloadResponse = _reflection.GeneratedProtocolMessageType('CancelMissionDownloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELMISSIONDOWNLOADRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.CancelMissionDownloadResponse)
  })
_sym_db.RegisterMessage(CancelMissionDownloadResponse)

StartMissionRequest = _reflection.GeneratedProtocolMessageType('StartMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTMISSIONREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.StartMissionRequest)
  })
_sym_db.RegisterMessage(StartMissionRequest)

StartMissionResponse = _reflection.GeneratedProtocolMessageType('StartMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTMISSIONRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.StartMissionResponse)
  })
_sym_db.RegisterMessage(StartMissionResponse)

PauseMissionRequest = _reflection.GeneratedProtocolMessageType('PauseMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAUSEMISSIONREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.PauseMissionRequest)
  })
_sym_db.RegisterMessage(PauseMissionRequest)

PauseMissionResponse = _reflection.GeneratedProtocolMessageType('PauseMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAUSEMISSIONRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.PauseMissionResponse)
  })
_sym_db.RegisterMessage(PauseMissionResponse)

ClearMissionRequest = _reflection.GeneratedProtocolMessageType('ClearMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLEARMISSIONREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.ClearMissionRequest)
  })
_sym_db.RegisterMessage(ClearMissionRequest)

ClearMissionResponse = _reflection.GeneratedProtocolMessageType('ClearMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLEARMISSIONRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.ClearMissionResponse)
  })
_sym_db.RegisterMessage(ClearMissionResponse)

SetCurrentMissionItemRequest = _reflection.GeneratedProtocolMessageType('SetCurrentMissionItemRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETCURRENTMISSIONITEMREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.SetCurrentMissionItemRequest)
  })
_sym_db.RegisterMessage(SetCurrentMissionItemRequest)

SetCurrentMissionItemResponse = _reflection.GeneratedProtocolMessageType('SetCurrentMissionItemResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETCURRENTMISSIONITEMRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.SetCurrentMissionItemResponse)
  })
_sym_db.RegisterMessage(SetCurrentMissionItemResponse)

IsMissionFinishedRequest = _reflection.GeneratedProtocolMessageType('IsMissionFinishedRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISMISSIONFINISHEDREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.IsMissionFinishedRequest)
  })
_sym_db.RegisterMessage(IsMissionFinishedRequest)

IsMissionFinishedResponse = _reflection.GeneratedProtocolMessageType('IsMissionFinishedResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISMISSIONFINISHEDRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.IsMissionFinishedResponse)
  })
_sym_db.RegisterMessage(IsMissionFinishedResponse)

SubscribeMissionProgressRequest = _reflection.GeneratedProtocolMessageType('SubscribeMissionProgressRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEMISSIONPROGRESSREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.SubscribeMissionProgressRequest)
  })
_sym_db.RegisterMessage(SubscribeMissionProgressRequest)

MissionProgressResponse = _reflection.GeneratedProtocolMessageType('MissionProgressResponse', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONPROGRESSRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.MissionProgressResponse)
  })
_sym_db.RegisterMessage(MissionProgressResponse)

GetReturnToLaunchAfterMissionRequest = _reflection.GeneratedProtocolMessageType('GetReturnToLaunchAfterMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETRETURNTOLAUNCHAFTERMISSIONREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.GetReturnToLaunchAfterMissionRequest)
  })
_sym_db.RegisterMessage(GetReturnToLaunchAfterMissionRequest)

GetReturnToLaunchAfterMissionResponse = _reflection.GeneratedProtocolMessageType('GetReturnToLaunchAfterMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETRETURNTOLAUNCHAFTERMISSIONRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.GetReturnToLaunchAfterMissionResponse)
  })
_sym_db.RegisterMessage(GetReturnToLaunchAfterMissionResponse)

SetReturnToLaunchAfterMissionRequest = _reflection.GeneratedProtocolMessageType('SetReturnToLaunchAfterMissionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETRETURNTOLAUNCHAFTERMISSIONREQUEST,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.SetReturnToLaunchAfterMissionRequest)
  })
_sym_db.RegisterMessage(SetReturnToLaunchAfterMissionRequest)

SetReturnToLaunchAfterMissionResponse = _reflection.GeneratedProtocolMessageType('SetReturnToLaunchAfterMissionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETRETURNTOLAUNCHAFTERMISSIONRESPONSE,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.SetReturnToLaunchAfterMissionResponse)
  })
_sym_db.RegisterMessage(SetReturnToLaunchAfterMissionResponse)

MissionItem = _reflection.GeneratedProtocolMessageType('MissionItem', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONITEM,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.MissionItem)
  })
_sym_db.RegisterMessage(MissionItem)

MissionPlan = _reflection.GeneratedProtocolMessageType('MissionPlan', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONPLAN,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.MissionPlan)
  })
_sym_db.RegisterMessage(MissionPlan)

MissionProgress = _reflection.GeneratedProtocolMessageType('MissionProgress', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONPROGRESS,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.MissionProgress)
  })
_sym_db.RegisterMessage(MissionProgress)

MissionResult = _reflection.GeneratedProtocolMessageType('MissionResult', (_message.Message,), {
  'DESCRIPTOR' : _MISSIONRESULT,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.MissionResult)
  })
_sym_db.RegisterMessage(MissionResult)

ProgressData = _reflection.GeneratedProtocolMessageType('ProgressData', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSDATA,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.ProgressData)
  })
_sym_db.RegisterMessage(ProgressData)

ProgressDataOrMission = _reflection.GeneratedProtocolMessageType('ProgressDataOrMission', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSDATAORMISSION,
  '__module__' : 'mission.mission_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.mission.ProgressDataOrMission)
  })
_sym_db.RegisterMessage(ProgressDataOrMission)

_MISSIONSERVICE = DESCRIPTOR.services_by_name['MissionService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021io.mavsdk.missionB\014MissionProto'
  _MISSIONITEM.fields_by_name['latitude_deg']._options = None
  _MISSIONITEM.fields_by_name['latitude_deg']._serialized_options = b'\202\265\030\003NaN\211\265\030H\257\274\232\362\327z>'
  _MISSIONITEM.fields_by_name['longitude_deg']._options = None
  _MISSIONITEM.fields_by_name['longitude_deg']._serialized_options = b'\202\265\030\003NaN\211\265\030H\257\274\232\362\327z>'
  _MISSIONITEM.fields_by_name['relative_altitude_m']._options = None
  _MISSIONITEM.fields_by_name['relative_altitude_m']._serialized_options = b'\202\265\030\003NaN'
  _MISSIONITEM.fields_by_name['speed_m_s']._options = None
  _MISSIONITEM.fields_by_name['speed_m_s']._serialized_options = b'\202\265\030\003NaN'
  _MISSIONITEM.fields_by_name['is_fly_through']._options = None
  _MISSIONITEM.fields_by_name['is_fly_through']._serialized_options = b'\202\265\030\005false'
  _MISSIONITEM.fields_by_name['gimbal_pitch_deg']._options = None
  _MISSIONITEM.fields_by_name['gimbal_pitch_deg']._serialized_options = b'\202\265\030\003NaN\211\265\030-C\034\353\3426\032?'
  _MISSIONITEM.fields_by_name['gimbal_yaw_deg']._options = None
  _MISSIONITEM.fields_by_name['gimbal_yaw_deg']._serialized_options = b'\202\265\030\003NaN\211\265\030-C\034\353\3426\032?'
  _MISSIONITEM.fields_by_name['loiter_time_s']._options = None
  _MISSIONITEM.fields_by_name['loiter_time_s']._serialized_options = b'\202\265\030\003NaN'
  _MISSIONITEM.fields_by_name['camera_photo_interval_s']._options = None
  _MISSIONITEM.fields_by_name['camera_photo_interval_s']._serialized_options = b'\202\265\030\0031.0'
  _MISSIONITEM.fields_by_name['acceptance_radius_m']._options = None
  _MISSIONITEM.fields_by_name['acceptance_radius_m']._serialized_options = b'\202\265\030\003NaN'
  _MISSIONITEM.fields_by_name['yaw_deg']._options = None
  _MISSIONITEM.fields_by_name['yaw_deg']._serialized_options = b'\202\265\030\003NaN'
  _MISSIONITEM.fields_by_name['camera_photo_distance_m']._options = None
  _MISSIONITEM.fields_by_name['camera_photo_distance_m']._serialized_options = b'\202\265\030\003NAN'
  _PROGRESSDATA.fields_by_name['progress']._options = None
  _PROGRESSDATA.fields_by_name['progress']._serialized_options = b'\202\265\030\003NaN'
  _PROGRESSDATAORMISSION.fields_by_name['has_progress']._options = None
  _PROGRESSDATAORMISSION.fields_by_name['has_progress']._serialized_options = b'\202\265\030\005false'
  _PROGRESSDATAORMISSION.fields_by_name['progress']._options = None
  _PROGRESSDATAORMISSION.fields_by_name['progress']._serialized_options = b'\202\265\030\003NaN'
  _MISSIONSERVICE.methods_by_name['SubscribeUploadMissionWithProgress']._options = None
  _MISSIONSERVICE.methods_by_name['SubscribeUploadMissionWithProgress']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _MISSIONSERVICE.methods_by_name['CancelMissionUpload']._options = None
  _MISSIONSERVICE.methods_by_name['CancelMissionUpload']._serialized_options = b'\200\265\030\001'
  _MISSIONSERVICE.methods_by_name['SubscribeDownloadMissionWithProgress']._options = None
  _MISSIONSERVICE.methods_by_name['SubscribeDownloadMissionWithProgress']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _MISSIONSERVICE.methods_by_name['CancelMissionDownload']._options = None
  _MISSIONSERVICE.methods_by_name['CancelMissionDownload']._serialized_options = b'\200\265\030\001'
  _MISSIONSERVICE.methods_by_name['IsMissionFinished']._options = None
  _MISSIONSERVICE.methods_by_name['IsMissionFinished']._serialized_options = b'\200\265\030\001'
  _MISSIONSERVICE.methods_by_name['GetReturnToLaunchAfterMission']._options = None
  _MISSIONSERVICE.methods_by_name['GetReturnToLaunchAfterMission']._serialized_options = b'\200\265\030\001'
  _MISSIONSERVICE.methods_by_name['SetReturnToLaunchAfterMission']._options = None
  _MISSIONSERVICE.methods_by_name['SetReturnToLaunchAfterMission']._serialized_options = b'\200\265\030\001'
  _UPLOADMISSIONREQUEST._serialized_start=67
  _UPLOADMISSIONREQUEST._serialized_end=144
  _UPLOADMISSIONRESPONSE._serialized_start=146
  _UPLOADMISSIONRESPONSE._serialized_end=228
  _SUBSCRIBEUPLOADMISSIONWITHPROGRESSREQUEST._serialized_start=230
  _SUBSCRIBEUPLOADMISSIONWITHPROGRESSREQUEST._serialized_end=328
  _UPLOADMISSIONWITHPROGRESSRESPONSE._serialized_start=331
  _UPLOADMISSIONWITHPROGRESSRESPONSE._serialized_end=482
  _CANCELMISSIONUPLOADREQUEST._serialized_start=484
  _CANCELMISSIONUPLOADREQUEST._serialized_end=512
  _CANCELMISSIONUPLOADRESPONSE._serialized_start=514
  _CANCELMISSIONUPLOADRESPONSE._serialized_end=602
  _DOWNLOADMISSIONREQUEST._serialized_start=604
  _DOWNLOADMISSIONREQUEST._serialized_end=628
  _DOWNLOADMISSIONRESPONSE._serialized_start=631
  _DOWNLOADMISSIONRESPONSE._serialized_end=770
  _SUBSCRIBEDOWNLOADMISSIONWITHPROGRESSREQUEST._serialized_start=772
  _SUBSCRIBEDOWNLOADMISSIONWITHPROGRESSREQUEST._serialized_end=817
  _DOWNLOADMISSIONWITHPROGRESSRESPONSE._serialized_start=820
  _DOWNLOADMISSIONWITHPROGRESSRESPONSE._serialized_end=982
  _CANCELMISSIONDOWNLOADREQUEST._serialized_start=984
  _CANCELMISSIONDOWNLOADREQUEST._serialized_end=1014
  _CANCELMISSIONDOWNLOADRESPONSE._serialized_start=1016
  _CANCELMISSIONDOWNLOADRESPONSE._serialized_end=1106
  _STARTMISSIONREQUEST._serialized_start=1108
  _STARTMISSIONREQUEST._serialized_end=1129
  _STARTMISSIONRESPONSE._serialized_start=1131
  _STARTMISSIONRESPONSE._serialized_end=1212
  _PAUSEMISSIONREQUEST._serialized_start=1214
  _PAUSEMISSIONREQUEST._serialized_end=1235
  _PAUSEMISSIONRESPONSE._serialized_start=1237
  _PAUSEMISSIONRESPONSE._serialized_end=1318
  _CLEARMISSIONREQUEST._serialized_start=1320
  _CLEARMISSIONREQUEST._serialized_end=1341
  _CLEARMISSIONRESPONSE._serialized_start=1343
  _CLEARMISSIONRESPONSE._serialized_end=1424
  _SETCURRENTMISSIONITEMREQUEST._serialized_start=1426
  _SETCURRENTMISSIONITEMREQUEST._serialized_end=1471
  _SETCURRENTMISSIONITEMRESPONSE._serialized_start=1473
  _SETCURRENTMISSIONITEMRESPONSE._serialized_end=1563
  _ISMISSIONFINISHEDREQUEST._serialized_start=1565
  _ISMISSIONFINISHEDREQUEST._serialized_end=1591
  _ISMISSIONFINISHEDRESPONSE._serialized_start=1593
  _ISMISSIONFINISHEDRESPONSE._serialized_end=1700
  _SUBSCRIBEMISSIONPROGRESSREQUEST._serialized_start=1702
  _SUBSCRIBEMISSIONPROGRESSREQUEST._serialized_end=1735
  _MISSIONPROGRESSRESPONSE._serialized_start=1737
  _MISSIONPROGRESSRESPONSE._serialized_end=1825
  _GETRETURNTOLAUNCHAFTERMISSIONREQUEST._serialized_start=1827
  _GETRETURNTOLAUNCHAFTERMISSIONREQUEST._serialized_end=1865
  _GETRETURNTOLAUNCHAFTERMISSIONRESPONSE._serialized_start=1867
  _GETRETURNTOLAUNCHAFTERMISSIONRESPONSE._serialized_end=1981
  _SETRETURNTOLAUNCHAFTERMISSIONREQUEST._serialized_start=1983
  _SETRETURNTOLAUNCHAFTERMISSIONREQUEST._serialized_end=2037
  _SETRETURNTOLAUNCHAFTERMISSIONRESPONSE._serialized_start=2039
  _SETRETURNTOLAUNCHAFTERMISSIONRESPONSE._serialized_end=2137
  _MISSIONITEM._serialized_start=2140
  _MISSIONITEM._serialized_end=3209
  _MISSIONITEM_CAMERAACTION._serialized_start=2752
  _MISSIONITEM_CAMERAACTION._serialized_end=3039
  _MISSIONITEM_VEHICLEACTION._serialized_start=3042
  _MISSIONITEM_VEHICLEACTION._serialized_end=3209
  _MISSIONPLAN._serialized_start=3211
  _MISSIONPLAN._serialized_end=3280
  _MISSIONPROGRESS._serialized_start=3282
  _MISSIONPROGRESS._serialized_end=3331
  _MISSIONRESULT._serialized_start=3334
  _MISSIONRESULT._serialized_end=3845
  _MISSIONRESULT_RESULT._serialized_start=3430
  _MISSIONRESULT_RESULT._serialized_end=3845
  _PROGRESSDATA._serialized_start=3847
  _PROGRESSDATA._serialized_end=3888
  _PROGRESSDATAORMISSION._serialized_start=3891
  _PROGRESSDATAORMISSION._serialized_end=4050
  _MISSIONSERVICE._serialized_start=4053
  _MISSIONSERVICE._serialized_end=5882
# @@protoc_insertion_point(module_scope)
