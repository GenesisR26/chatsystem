# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\nconnection\":\n\x14\x43reateAccountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"(\n\x15\x43reateAccountResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\" \n\rLoginResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"-\n\x19\x43lientDisconnectedRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"-\n\x1a\x43lientDisconnectedResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"7\n\x12SendMessageRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"&\n\x13SendMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"+\n\x17\x42roadcastMessageRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"D\n\x18\x42roadcastMessageResponse\x12\x17\n\x0fsender_username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x07\n\x05\x45mpty\"\x19\n\x08UserList\x12\r\n\x05users\x18\x01 \x03(\t\")\n\x07moodVal\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04mood\x18\x02 \x01(\t2\xf2\x03\n\x11\x43onnectionService\x12T\n\rCreateAccount\x12 .connection.CreateAccountRequest\x1a!.connection.CreateAccountResponse\x12<\n\x05Login\x12\x18.connection.LoginRequest\x1a\x19.connection.LoginResponse\x12\x63\n\x12\x43lientDisconnected\x12%.connection.ClientDisconnectedRequest\x1a&.connection.ClientDisconnectedResponse\x12N\n\x0bSendMessage\x12\x1e.connection.SendMessageRequest\x1a\x1f.connection.SendMessageResponse\x12_\n\x10\x42roadcastMessage\x12#.connection.BroadcastMessageRequest\x1a$.connection.BroadcastMessageResponse0\x01\x12\x33\n\x08getUsers\x12\x11.connection.Empty\x1a\x14.connection.UserListb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEACCOUNTREQUEST._serialized_start=26
  _CREATEACCOUNTREQUEST._serialized_end=84
  _CREATEACCOUNTRESPONSE._serialized_start=86
  _CREATEACCOUNTRESPONSE._serialized_end=126
  _LOGINREQUEST._serialized_start=128
  _LOGINREQUEST._serialized_end=178
  _LOGINRESPONSE._serialized_start=180
  _LOGINRESPONSE._serialized_end=212
  _CLIENTDISCONNECTEDREQUEST._serialized_start=214
  _CLIENTDISCONNECTEDREQUEST._serialized_end=259
  _CLIENTDISCONNECTEDRESPONSE._serialized_start=261
  _CLIENTDISCONNECTEDRESPONSE._serialized_end=306
  _SENDMESSAGEREQUEST._serialized_start=308
  _SENDMESSAGEREQUEST._serialized_end=363
  _SENDMESSAGERESPONSE._serialized_start=365
  _SENDMESSAGERESPONSE._serialized_end=403
  _BROADCASTMESSAGEREQUEST._serialized_start=405
  _BROADCASTMESSAGEREQUEST._serialized_end=448
  _BROADCASTMESSAGERESPONSE._serialized_start=450
  _BROADCASTMESSAGERESPONSE._serialized_end=518
  _EMPTY._serialized_start=520
  _EMPTY._serialized_end=527
  _USERLIST._serialized_start=529
  _USERLIST._serialized_end=554
  _MOODVAL._serialized_start=556
  _MOODVAL._serialized_end=597
  _CONNECTIONSERVICE._serialized_start=600
  _CONNECTIONSERVICE._serialized_end=1098
# @@protoc_insertion_point(module_scope)
