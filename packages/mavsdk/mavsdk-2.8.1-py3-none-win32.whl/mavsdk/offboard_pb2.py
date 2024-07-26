# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: offboard/offboard.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17offboard/offboard.proto\x12\x13mavsdk.rpc.offboard\x1a\x14mavsdk_options.proto\"\x0e\n\x0cStartRequest\"M\n\rStartResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\r\n\x0bStopRequest\"L\n\x0cStopResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\x11\n\x0fIsActiveRequest\"%\n\x10IsActiveResponse\x12\x11\n\tis_active\x18\x01 \x01(\x08\"E\n\x12SetAttitudeRequest\x12/\n\x08\x61ttitude\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.offboard.Attitude\"S\n\x13SetAttitudeResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"[\n\x19SetActuatorControlRequest\x12>\n\x10\x61\x63tuator_control\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.offboard.ActuatorControl\"Z\n\x1aSetActuatorControlResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"R\n\x16SetAttitudeRateRequest\x12\x38\n\rattitude_rate\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.offboard.AttitudeRate\"W\n\x17SetAttitudeRateResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"V\n\x15SetPositionNedRequest\x12=\n\x10position_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\"V\n\x16SetPositionNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"_\n\x18SetPositionGlobalRequest\x12\x43\n\x13position_global_yaw\x18\x01 \x01(\x0b\x32&.mavsdk.rpc.offboard.PositionGlobalYaw\"Y\n\x19SetPositionGlobalResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"c\n\x16SetVelocityBodyRequest\x12I\n\x16velocity_body_yawspeed\x18\x01 \x01(\x0b\x32).mavsdk.rpc.offboard.VelocityBodyYawspeed\"W\n\x17SetVelocityBodyResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"V\n\x15SetVelocityNedRequest\x12=\n\x10velocity_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\"V\n\x16SetVelocityNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\x9d\x01\n\x1dSetPositionVelocityNedRequest\x12=\n\x10position_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\x12=\n\x10velocity_ned_yaw\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\"\xe9\x01\n)SetPositionVelocityAccelerationNedRequest\x12=\n\x10position_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\x12=\n\x10velocity_ned_yaw\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\x12>\n\x10\x61\x63\x63\x65leration_ned\x18\x03 \x01(\x0b\x32$.mavsdk.rpc.offboard.AccelerationNed\"^\n\x1eSetPositionVelocityNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"j\n*SetPositionVelocityAccelerationNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"[\n\x19SetAccelerationNedRequest\x12>\n\x10\x61\x63\x63\x65leration_ned\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.offboard.AccelerationNed\"Z\n\x1aSetAccelerationNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"V\n\x08\x41ttitude\x12\x10\n\x08roll_deg\x18\x01 \x01(\x02\x12\x11\n\tpitch_deg\x18\x02 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x03 \x01(\x02\x12\x14\n\x0cthrust_value\x18\x04 \x01(\x02\"(\n\x14\x41\x63tuatorControlGroup\x12\x10\n\x08\x63ontrols\x18\x01 \x03(\x02\"L\n\x0f\x41\x63tuatorControl\x12\x39\n\x06groups\x18\x01 \x03(\x0b\x32).mavsdk.rpc.offboard.ActuatorControlGroup\"`\n\x0c\x41ttitudeRate\x12\x12\n\nroll_deg_s\x18\x01 \x01(\x02\x12\x13\n\x0bpitch_deg_s\x18\x02 \x01(\x02\x12\x11\n\tyaw_deg_s\x18\x03 \x01(\x02\x12\x14\n\x0cthrust_value\x18\x04 \x01(\x02\"R\n\x0ePositionNedYaw\x12\x0f\n\x07north_m\x18\x01 \x01(\x02\x12\x0e\n\x06\x65\x61st_m\x18\x02 \x01(\x02\x12\x0e\n\x06\x64own_m\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\"\xfc\x01\n\x11PositionGlobalYaw\x12\x0f\n\x07lat_deg\x18\x01 \x01(\x01\x12\x0f\n\x07lon_deg\x18\x02 \x01(\x01\x12\r\n\x05\x61lt_m\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\x12J\n\raltitude_type\x18\x05 \x01(\x0e\x32\x33.mavsdk.rpc.offboard.PositionGlobalYaw.AltitudeType\"Y\n\x0c\x41ltitudeType\x12\x1a\n\x16\x41LTITUDE_TYPE_REL_HOME\x10\x00\x12\x16\n\x12\x41LTITUDE_TYPE_AMSL\x10\x01\x12\x15\n\x11\x41LTITUDE_TYPE_AGL\x10\x02\"h\n\x14VelocityBodyYawspeed\x12\x13\n\x0b\x66orward_m_s\x18\x01 \x01(\x02\x12\x11\n\tright_m_s\x18\x02 \x01(\x02\x12\x10\n\x08\x64own_m_s\x18\x03 \x01(\x02\x12\x16\n\x0eyawspeed_deg_s\x18\x04 \x01(\x02\"X\n\x0eVelocityNedYaw\x12\x11\n\tnorth_m_s\x18\x01 \x01(\x02\x12\x10\n\x08\x65\x61st_m_s\x18\x02 \x01(\x02\x12\x10\n\x08\x64own_m_s\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\"K\n\x0f\x41\x63\x63\x65lerationNed\x12\x12\n\nnorth_m_s2\x18\x01 \x01(\x02\x12\x11\n\teast_m_s2\x18\x02 \x01(\x02\x12\x11\n\tdown_m_s2\x18\x03 \x01(\x02\"\xb5\x02\n\x0eOffboardResult\x12:\n\x06result\x18\x01 \x01(\x0e\x32*.mavsdk.rpc.offboard.OffboardResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xd2\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06\x12\x1a\n\x16RESULT_NO_SETPOINT_SET\x10\x07\x12\x11\n\rRESULT_FAILED\x10\x08\x32\xef\x0b\n\x0fOffboardService\x12P\n\x05Start\x12!.mavsdk.rpc.offboard.StartRequest\x1a\".mavsdk.rpc.offboard.StartResponse\"\x00\x12M\n\x04Stop\x12 .mavsdk.rpc.offboard.StopRequest\x1a!.mavsdk.rpc.offboard.StopResponse\"\x00\x12]\n\x08IsActive\x12$.mavsdk.rpc.offboard.IsActiveRequest\x1a%.mavsdk.rpc.offboard.IsActiveResponse\"\x04\x80\xb5\x18\x01\x12\x66\n\x0bSetAttitude\x12\'.mavsdk.rpc.offboard.SetAttitudeRequest\x1a(.mavsdk.rpc.offboard.SetAttitudeResponse\"\x04\x80\xb5\x18\x01\x12{\n\x12SetActuatorControl\x12..mavsdk.rpc.offboard.SetActuatorControlRequest\x1a/.mavsdk.rpc.offboard.SetActuatorControlResponse\"\x04\x80\xb5\x18\x01\x12r\n\x0fSetAttitudeRate\x12+.mavsdk.rpc.offboard.SetAttitudeRateRequest\x1a,.mavsdk.rpc.offboard.SetAttitudeRateResponse\"\x04\x80\xb5\x18\x01\x12o\n\x0eSetPositionNed\x12*.mavsdk.rpc.offboard.SetPositionNedRequest\x1a+.mavsdk.rpc.offboard.SetPositionNedResponse\"\x04\x80\xb5\x18\x01\x12x\n\x11SetPositionGlobal\x12-.mavsdk.rpc.offboard.SetPositionGlobalRequest\x1a..mavsdk.rpc.offboard.SetPositionGlobalResponse\"\x04\x80\xb5\x18\x01\x12r\n\x0fSetVelocityBody\x12+.mavsdk.rpc.offboard.SetVelocityBodyRequest\x1a,.mavsdk.rpc.offboard.SetVelocityBodyResponse\"\x04\x80\xb5\x18\x01\x12o\n\x0eSetVelocityNed\x12*.mavsdk.rpc.offboard.SetVelocityNedRequest\x1a+.mavsdk.rpc.offboard.SetVelocityNedResponse\"\x04\x80\xb5\x18\x01\x12\x87\x01\n\x16SetPositionVelocityNed\x12\x32.mavsdk.rpc.offboard.SetPositionVelocityNedRequest\x1a\x33.mavsdk.rpc.offboard.SetPositionVelocityNedResponse\"\x04\x80\xb5\x18\x01\x12\xab\x01\n\"SetPositionVelocityAccelerationNed\x12>.mavsdk.rpc.offboard.SetPositionVelocityAccelerationNedRequest\x1a?.mavsdk.rpc.offboard.SetPositionVelocityAccelerationNedResponse\"\x04\x80\xb5\x18\x01\x12{\n\x12SetAccelerationNed\x12..mavsdk.rpc.offboard.SetAccelerationNedRequest\x1a/.mavsdk.rpc.offboard.SetAccelerationNedResponse\"\x04\x80\xb5\x18\x01\x42#\n\x12io.mavsdk.offboardB\rOffboardProtob\x06proto3')



_STARTREQUEST = DESCRIPTOR.message_types_by_name['StartRequest']
_STARTRESPONSE = DESCRIPTOR.message_types_by_name['StartResponse']
_STOPREQUEST = DESCRIPTOR.message_types_by_name['StopRequest']
_STOPRESPONSE = DESCRIPTOR.message_types_by_name['StopResponse']
_ISACTIVEREQUEST = DESCRIPTOR.message_types_by_name['IsActiveRequest']
_ISACTIVERESPONSE = DESCRIPTOR.message_types_by_name['IsActiveResponse']
_SETATTITUDEREQUEST = DESCRIPTOR.message_types_by_name['SetAttitudeRequest']
_SETATTITUDERESPONSE = DESCRIPTOR.message_types_by_name['SetAttitudeResponse']
_SETACTUATORCONTROLREQUEST = DESCRIPTOR.message_types_by_name['SetActuatorControlRequest']
_SETACTUATORCONTROLRESPONSE = DESCRIPTOR.message_types_by_name['SetActuatorControlResponse']
_SETATTITUDERATEREQUEST = DESCRIPTOR.message_types_by_name['SetAttitudeRateRequest']
_SETATTITUDERATERESPONSE = DESCRIPTOR.message_types_by_name['SetAttitudeRateResponse']
_SETPOSITIONNEDREQUEST = DESCRIPTOR.message_types_by_name['SetPositionNedRequest']
_SETPOSITIONNEDRESPONSE = DESCRIPTOR.message_types_by_name['SetPositionNedResponse']
_SETPOSITIONGLOBALREQUEST = DESCRIPTOR.message_types_by_name['SetPositionGlobalRequest']
_SETPOSITIONGLOBALRESPONSE = DESCRIPTOR.message_types_by_name['SetPositionGlobalResponse']
_SETVELOCITYBODYREQUEST = DESCRIPTOR.message_types_by_name['SetVelocityBodyRequest']
_SETVELOCITYBODYRESPONSE = DESCRIPTOR.message_types_by_name['SetVelocityBodyResponse']
_SETVELOCITYNEDREQUEST = DESCRIPTOR.message_types_by_name['SetVelocityNedRequest']
_SETVELOCITYNEDRESPONSE = DESCRIPTOR.message_types_by_name['SetVelocityNedResponse']
_SETPOSITIONVELOCITYNEDREQUEST = DESCRIPTOR.message_types_by_name['SetPositionVelocityNedRequest']
_SETPOSITIONVELOCITYACCELERATIONNEDREQUEST = DESCRIPTOR.message_types_by_name['SetPositionVelocityAccelerationNedRequest']
_SETPOSITIONVELOCITYNEDRESPONSE = DESCRIPTOR.message_types_by_name['SetPositionVelocityNedResponse']
_SETPOSITIONVELOCITYACCELERATIONNEDRESPONSE = DESCRIPTOR.message_types_by_name['SetPositionVelocityAccelerationNedResponse']
_SETACCELERATIONNEDREQUEST = DESCRIPTOR.message_types_by_name['SetAccelerationNedRequest']
_SETACCELERATIONNEDRESPONSE = DESCRIPTOR.message_types_by_name['SetAccelerationNedResponse']
_ATTITUDE = DESCRIPTOR.message_types_by_name['Attitude']
_ACTUATORCONTROLGROUP = DESCRIPTOR.message_types_by_name['ActuatorControlGroup']
_ACTUATORCONTROL = DESCRIPTOR.message_types_by_name['ActuatorControl']
_ATTITUDERATE = DESCRIPTOR.message_types_by_name['AttitudeRate']
_POSITIONNEDYAW = DESCRIPTOR.message_types_by_name['PositionNedYaw']
_POSITIONGLOBALYAW = DESCRIPTOR.message_types_by_name['PositionGlobalYaw']
_VELOCITYBODYYAWSPEED = DESCRIPTOR.message_types_by_name['VelocityBodyYawspeed']
_VELOCITYNEDYAW = DESCRIPTOR.message_types_by_name['VelocityNedYaw']
_ACCELERATIONNED = DESCRIPTOR.message_types_by_name['AccelerationNed']
_OFFBOARDRESULT = DESCRIPTOR.message_types_by_name['OffboardResult']
_POSITIONGLOBALYAW_ALTITUDETYPE = _POSITIONGLOBALYAW.enum_types_by_name['AltitudeType']
_OFFBOARDRESULT_RESULT = _OFFBOARDRESULT.enum_types_by_name['Result']
StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.StartRequest)
  })
_sym_db.RegisterMessage(StartRequest)

StartResponse = _reflection.GeneratedProtocolMessageType('StartResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.StartResponse)
  })
_sym_db.RegisterMessage(StartResponse)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.StopResponse)
  })
_sym_db.RegisterMessage(StopResponse)

IsActiveRequest = _reflection.GeneratedProtocolMessageType('IsActiveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ISACTIVEREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.IsActiveRequest)
  })
_sym_db.RegisterMessage(IsActiveRequest)

IsActiveResponse = _reflection.GeneratedProtocolMessageType('IsActiveResponse', (_message.Message,), {
  'DESCRIPTOR' : _ISACTIVERESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.IsActiveResponse)
  })
_sym_db.RegisterMessage(IsActiveResponse)

SetAttitudeRequest = _reflection.GeneratedProtocolMessageType('SetAttitudeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETATTITUDEREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetAttitudeRequest)
  })
_sym_db.RegisterMessage(SetAttitudeRequest)

SetAttitudeResponse = _reflection.GeneratedProtocolMessageType('SetAttitudeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETATTITUDERESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetAttitudeResponse)
  })
_sym_db.RegisterMessage(SetAttitudeResponse)

SetActuatorControlRequest = _reflection.GeneratedProtocolMessageType('SetActuatorControlRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETACTUATORCONTROLREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetActuatorControlRequest)
  })
_sym_db.RegisterMessage(SetActuatorControlRequest)

SetActuatorControlResponse = _reflection.GeneratedProtocolMessageType('SetActuatorControlResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETACTUATORCONTROLRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetActuatorControlResponse)
  })
_sym_db.RegisterMessage(SetActuatorControlResponse)

SetAttitudeRateRequest = _reflection.GeneratedProtocolMessageType('SetAttitudeRateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETATTITUDERATEREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetAttitudeRateRequest)
  })
_sym_db.RegisterMessage(SetAttitudeRateRequest)

SetAttitudeRateResponse = _reflection.GeneratedProtocolMessageType('SetAttitudeRateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETATTITUDERATERESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetAttitudeRateResponse)
  })
_sym_db.RegisterMessage(SetAttitudeRateResponse)

SetPositionNedRequest = _reflection.GeneratedProtocolMessageType('SetPositionNedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONNEDREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionNedRequest)
  })
_sym_db.RegisterMessage(SetPositionNedRequest)

SetPositionNedResponse = _reflection.GeneratedProtocolMessageType('SetPositionNedResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONNEDRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionNedResponse)
  })
_sym_db.RegisterMessage(SetPositionNedResponse)

SetPositionGlobalRequest = _reflection.GeneratedProtocolMessageType('SetPositionGlobalRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONGLOBALREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionGlobalRequest)
  })
_sym_db.RegisterMessage(SetPositionGlobalRequest)

SetPositionGlobalResponse = _reflection.GeneratedProtocolMessageType('SetPositionGlobalResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONGLOBALRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionGlobalResponse)
  })
_sym_db.RegisterMessage(SetPositionGlobalResponse)

SetVelocityBodyRequest = _reflection.GeneratedProtocolMessageType('SetVelocityBodyRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETVELOCITYBODYREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetVelocityBodyRequest)
  })
_sym_db.RegisterMessage(SetVelocityBodyRequest)

SetVelocityBodyResponse = _reflection.GeneratedProtocolMessageType('SetVelocityBodyResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETVELOCITYBODYRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetVelocityBodyResponse)
  })
_sym_db.RegisterMessage(SetVelocityBodyResponse)

SetVelocityNedRequest = _reflection.GeneratedProtocolMessageType('SetVelocityNedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETVELOCITYNEDREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetVelocityNedRequest)
  })
_sym_db.RegisterMessage(SetVelocityNedRequest)

SetVelocityNedResponse = _reflection.GeneratedProtocolMessageType('SetVelocityNedResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETVELOCITYNEDRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetVelocityNedResponse)
  })
_sym_db.RegisterMessage(SetVelocityNedResponse)

SetPositionVelocityNedRequest = _reflection.GeneratedProtocolMessageType('SetPositionVelocityNedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONVELOCITYNEDREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionVelocityNedRequest)
  })
_sym_db.RegisterMessage(SetPositionVelocityNedRequest)

SetPositionVelocityAccelerationNedRequest = _reflection.GeneratedProtocolMessageType('SetPositionVelocityAccelerationNedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONVELOCITYACCELERATIONNEDREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionVelocityAccelerationNedRequest)
  })
_sym_db.RegisterMessage(SetPositionVelocityAccelerationNedRequest)

SetPositionVelocityNedResponse = _reflection.GeneratedProtocolMessageType('SetPositionVelocityNedResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONVELOCITYNEDRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionVelocityNedResponse)
  })
_sym_db.RegisterMessage(SetPositionVelocityNedResponse)

SetPositionVelocityAccelerationNedResponse = _reflection.GeneratedProtocolMessageType('SetPositionVelocityAccelerationNedResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPOSITIONVELOCITYACCELERATIONNEDRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetPositionVelocityAccelerationNedResponse)
  })
_sym_db.RegisterMessage(SetPositionVelocityAccelerationNedResponse)

SetAccelerationNedRequest = _reflection.GeneratedProtocolMessageType('SetAccelerationNedRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETACCELERATIONNEDREQUEST,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetAccelerationNedRequest)
  })
_sym_db.RegisterMessage(SetAccelerationNedRequest)

SetAccelerationNedResponse = _reflection.GeneratedProtocolMessageType('SetAccelerationNedResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETACCELERATIONNEDRESPONSE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.SetAccelerationNedResponse)
  })
_sym_db.RegisterMessage(SetAccelerationNedResponse)

Attitude = _reflection.GeneratedProtocolMessageType('Attitude', (_message.Message,), {
  'DESCRIPTOR' : _ATTITUDE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.Attitude)
  })
_sym_db.RegisterMessage(Attitude)

ActuatorControlGroup = _reflection.GeneratedProtocolMessageType('ActuatorControlGroup', (_message.Message,), {
  'DESCRIPTOR' : _ACTUATORCONTROLGROUP,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.ActuatorControlGroup)
  })
_sym_db.RegisterMessage(ActuatorControlGroup)

ActuatorControl = _reflection.GeneratedProtocolMessageType('ActuatorControl', (_message.Message,), {
  'DESCRIPTOR' : _ACTUATORCONTROL,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.ActuatorControl)
  })
_sym_db.RegisterMessage(ActuatorControl)

AttitudeRate = _reflection.GeneratedProtocolMessageType('AttitudeRate', (_message.Message,), {
  'DESCRIPTOR' : _ATTITUDERATE,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.AttitudeRate)
  })
_sym_db.RegisterMessage(AttitudeRate)

PositionNedYaw = _reflection.GeneratedProtocolMessageType('PositionNedYaw', (_message.Message,), {
  'DESCRIPTOR' : _POSITIONNEDYAW,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.PositionNedYaw)
  })
_sym_db.RegisterMessage(PositionNedYaw)

PositionGlobalYaw = _reflection.GeneratedProtocolMessageType('PositionGlobalYaw', (_message.Message,), {
  'DESCRIPTOR' : _POSITIONGLOBALYAW,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.PositionGlobalYaw)
  })
_sym_db.RegisterMessage(PositionGlobalYaw)

VelocityBodyYawspeed = _reflection.GeneratedProtocolMessageType('VelocityBodyYawspeed', (_message.Message,), {
  'DESCRIPTOR' : _VELOCITYBODYYAWSPEED,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.VelocityBodyYawspeed)
  })
_sym_db.RegisterMessage(VelocityBodyYawspeed)

VelocityNedYaw = _reflection.GeneratedProtocolMessageType('VelocityNedYaw', (_message.Message,), {
  'DESCRIPTOR' : _VELOCITYNEDYAW,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.VelocityNedYaw)
  })
_sym_db.RegisterMessage(VelocityNedYaw)

AccelerationNed = _reflection.GeneratedProtocolMessageType('AccelerationNed', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATIONNED,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.AccelerationNed)
  })
_sym_db.RegisterMessage(AccelerationNed)

OffboardResult = _reflection.GeneratedProtocolMessageType('OffboardResult', (_message.Message,), {
  'DESCRIPTOR' : _OFFBOARDRESULT,
  '__module__' : 'offboard.offboard_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.offboard.OffboardResult)
  })
_sym_db.RegisterMessage(OffboardResult)

_OFFBOARDSERVICE = DESCRIPTOR.services_by_name['OffboardService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022io.mavsdk.offboardB\rOffboardProto'
  _OFFBOARDSERVICE.methods_by_name['IsActive']._options = None
  _OFFBOARDSERVICE.methods_by_name['IsActive']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetAttitude']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetAttitude']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetActuatorControl']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetActuatorControl']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetAttitudeRate']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetAttitudeRate']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetPositionNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetPositionNed']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetPositionGlobal']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetPositionGlobal']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetVelocityBody']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetVelocityBody']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetVelocityNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetVelocityNed']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetPositionVelocityNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetPositionVelocityNed']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetPositionVelocityAccelerationNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetPositionVelocityAccelerationNed']._serialized_options = b'\200\265\030\001'
  _OFFBOARDSERVICE.methods_by_name['SetAccelerationNed']._options = None
  _OFFBOARDSERVICE.methods_by_name['SetAccelerationNed']._serialized_options = b'\200\265\030\001'
  _STARTREQUEST._serialized_start=70
  _STARTREQUEST._serialized_end=84
  _STARTRESPONSE._serialized_start=86
  _STARTRESPONSE._serialized_end=163
  _STOPREQUEST._serialized_start=165
  _STOPREQUEST._serialized_end=178
  _STOPRESPONSE._serialized_start=180
  _STOPRESPONSE._serialized_end=256
  _ISACTIVEREQUEST._serialized_start=258
  _ISACTIVEREQUEST._serialized_end=275
  _ISACTIVERESPONSE._serialized_start=277
  _ISACTIVERESPONSE._serialized_end=314
  _SETATTITUDEREQUEST._serialized_start=316
  _SETATTITUDEREQUEST._serialized_end=385
  _SETATTITUDERESPONSE._serialized_start=387
  _SETATTITUDERESPONSE._serialized_end=470
  _SETACTUATORCONTROLREQUEST._serialized_start=472
  _SETACTUATORCONTROLREQUEST._serialized_end=563
  _SETACTUATORCONTROLRESPONSE._serialized_start=565
  _SETACTUATORCONTROLRESPONSE._serialized_end=655
  _SETATTITUDERATEREQUEST._serialized_start=657
  _SETATTITUDERATEREQUEST._serialized_end=739
  _SETATTITUDERATERESPONSE._serialized_start=741
  _SETATTITUDERATERESPONSE._serialized_end=828
  _SETPOSITIONNEDREQUEST._serialized_start=830
  _SETPOSITIONNEDREQUEST._serialized_end=916
  _SETPOSITIONNEDRESPONSE._serialized_start=918
  _SETPOSITIONNEDRESPONSE._serialized_end=1004
  _SETPOSITIONGLOBALREQUEST._serialized_start=1006
  _SETPOSITIONGLOBALREQUEST._serialized_end=1101
  _SETPOSITIONGLOBALRESPONSE._serialized_start=1103
  _SETPOSITIONGLOBALRESPONSE._serialized_end=1192
  _SETVELOCITYBODYREQUEST._serialized_start=1194
  _SETVELOCITYBODYREQUEST._serialized_end=1293
  _SETVELOCITYBODYRESPONSE._serialized_start=1295
  _SETVELOCITYBODYRESPONSE._serialized_end=1382
  _SETVELOCITYNEDREQUEST._serialized_start=1384
  _SETVELOCITYNEDREQUEST._serialized_end=1470
  _SETVELOCITYNEDRESPONSE._serialized_start=1472
  _SETVELOCITYNEDRESPONSE._serialized_end=1558
  _SETPOSITIONVELOCITYNEDREQUEST._serialized_start=1561
  _SETPOSITIONVELOCITYNEDREQUEST._serialized_end=1718
  _SETPOSITIONVELOCITYACCELERATIONNEDREQUEST._serialized_start=1721
  _SETPOSITIONVELOCITYACCELERATIONNEDREQUEST._serialized_end=1954
  _SETPOSITIONVELOCITYNEDRESPONSE._serialized_start=1956
  _SETPOSITIONVELOCITYNEDRESPONSE._serialized_end=2050
  _SETPOSITIONVELOCITYACCELERATIONNEDRESPONSE._serialized_start=2052
  _SETPOSITIONVELOCITYACCELERATIONNEDRESPONSE._serialized_end=2158
  _SETACCELERATIONNEDREQUEST._serialized_start=2160
  _SETACCELERATIONNEDREQUEST._serialized_end=2251
  _SETACCELERATIONNEDRESPONSE._serialized_start=2253
  _SETACCELERATIONNEDRESPONSE._serialized_end=2343
  _ATTITUDE._serialized_start=2345
  _ATTITUDE._serialized_end=2431
  _ACTUATORCONTROLGROUP._serialized_start=2433
  _ACTUATORCONTROLGROUP._serialized_end=2473
  _ACTUATORCONTROL._serialized_start=2475
  _ACTUATORCONTROL._serialized_end=2551
  _ATTITUDERATE._serialized_start=2553
  _ATTITUDERATE._serialized_end=2649
  _POSITIONNEDYAW._serialized_start=2651
  _POSITIONNEDYAW._serialized_end=2733
  _POSITIONGLOBALYAW._serialized_start=2736
  _POSITIONGLOBALYAW._serialized_end=2988
  _POSITIONGLOBALYAW_ALTITUDETYPE._serialized_start=2899
  _POSITIONGLOBALYAW_ALTITUDETYPE._serialized_end=2988
  _VELOCITYBODYYAWSPEED._serialized_start=2990
  _VELOCITYBODYYAWSPEED._serialized_end=3094
  _VELOCITYNEDYAW._serialized_start=3096
  _VELOCITYNEDYAW._serialized_end=3184
  _ACCELERATIONNED._serialized_start=3186
  _ACCELERATIONNED._serialized_end=3261
  _OFFBOARDRESULT._serialized_start=3264
  _OFFBOARDRESULT._serialized_end=3573
  _OFFBOARDRESULT_RESULT._serialized_start=3363
  _OFFBOARDRESULT_RESULT._serialized_end=3573
  _OFFBOARDSERVICE._serialized_start=3576
  _OFFBOARDSERVICE._serialized_end=5095
# @@protoc_insertion_point(module_scope)
