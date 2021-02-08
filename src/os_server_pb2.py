# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: os_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='os_server.proto',
  package='osserver',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fos_server.proto\x12\x08osserver\"\x12\n\x03Req\x12\x0b\n\x03req\x18\x01 \x01(\x05\"I\n\x02PR\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\n\n\x02rr\x18\x04 \x01(\x01\x12\n\n\x02rp\x18\x05 \x01(\x01\x12\n\n\x02ry\x18\x06 \x01(\x01\"\xb4\x01\n\x05Joint\x12\x12\n\ntargetPose\x18\x01 \x01(\x01\x12\x0f\n\x07targetV\x18\x02 \x01(\x01\x12\x0f\n\x07targetA\x18\x03 \x01(\x01\x12\x14\n\x0ctargetTorque\x18\x04 \x01(\x01\x12\x12\n\nactualPose\x18\x05 \x01(\x01\x12\x0f\n\x07\x61\x63tualV\x18\x06 \x01(\x01\x12\x0f\n\x07\x61\x63tualA\x18\x07 \x01(\x01\x12\x14\n\x0c\x61\x63tualTorque\x18\x08 \x01(\x01\x12\x13\n\x0btemperature\x18\t \x01(\x01\"\xa7\x01\n\x08RingData\x12\x1f\n\x06joints\x18\x01 \x03(\x0b\x32\x0f.osserver.Joint\x12\x0b\n\x03num\x18\x02 \x01(\x05\x12 \n\ntargetPose\x18\x03 \x01(\x0b\x32\x0c.osserver.PR\x12 \n\nactualPose\x18\x04 \x01(\x0b\x32\x0c.osserver.PR\x12)\n\x07voltage\x18\x05 \x01(\x0b\x32\x18.osserver.CurrentVoltage\"N\n\x0e\x43urrentVoltage\x12\r\n\x05power\x18\x01 \x01(\x01\x12\x0c\n\x04\x66lan\x18\x02 \x01(\x01\x12\r\n\x05joint\x18\x03 \x03(\x01\x12\x10\n\x08io_power\x18\x04 \x01(\x01\x32>\n\x08OsServer\x12\x32\n\x0bgetRingData\x12\r.osserver.Req\x1a\x12.osserver.RingData0\x01\x62\x06proto3'
)




_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='osserver.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='osserver.Req.req', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=47,
)


_PR = _descriptor.Descriptor(
  name='PR',
  full_name='osserver.PR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='osserver.PR.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='osserver.PR.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='osserver.PR.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rr', full_name='osserver.PR.rr', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rp', full_name='osserver.PR.rp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ry', full_name='osserver.PR.ry', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=49,
  serialized_end=122,
)


_JOINT = _descriptor.Descriptor(
  name='Joint',
  full_name='osserver.Joint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetPose', full_name='osserver.Joint.targetPose', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetV', full_name='osserver.Joint.targetV', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetA', full_name='osserver.Joint.targetA', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetTorque', full_name='osserver.Joint.targetTorque', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actualPose', full_name='osserver.Joint.actualPose', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actualV', full_name='osserver.Joint.actualV', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actualA', full_name='osserver.Joint.actualA', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actualTorque', full_name='osserver.Joint.actualTorque', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='osserver.Joint.temperature', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=125,
  serialized_end=305,
)


_RINGDATA = _descriptor.Descriptor(
  name='RingData',
  full_name='osserver.RingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='joints', full_name='osserver.RingData.joints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num', full_name='osserver.RingData.num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetPose', full_name='osserver.RingData.targetPose', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actualPose', full_name='osserver.RingData.actualPose', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voltage', full_name='osserver.RingData.voltage', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=308,
  serialized_end=475,
)


_CURRENTVOLTAGE = _descriptor.Descriptor(
  name='CurrentVoltage',
  full_name='osserver.CurrentVoltage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='power', full_name='osserver.CurrentVoltage.power', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flan', full_name='osserver.CurrentVoltage.flan', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='joint', full_name='osserver.CurrentVoltage.joint', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='io_power', full_name='osserver.CurrentVoltage.io_power', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=477,
  serialized_end=555,
)

_RINGDATA.fields_by_name['joints'].message_type = _JOINT
_RINGDATA.fields_by_name['targetPose'].message_type = _PR
_RINGDATA.fields_by_name['actualPose'].message_type = _PR
_RINGDATA.fields_by_name['voltage'].message_type = _CURRENTVOLTAGE
DESCRIPTOR.message_types_by_name['Req'] = _REQ
DESCRIPTOR.message_types_by_name['PR'] = _PR
DESCRIPTOR.message_types_by_name['Joint'] = _JOINT
DESCRIPTOR.message_types_by_name['RingData'] = _RINGDATA
DESCRIPTOR.message_types_by_name['CurrentVoltage'] = _CURRENTVOLTAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Req = _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), {
  'DESCRIPTOR' : _REQ,
  '__module__' : 'os_server_pb2'
  # @@protoc_insertion_point(class_scope:osserver.Req)
  })
_sym_db.RegisterMessage(Req)

PR = _reflection.GeneratedProtocolMessageType('PR', (_message.Message,), {
  'DESCRIPTOR' : _PR,
  '__module__' : 'os_server_pb2'
  # @@protoc_insertion_point(class_scope:osserver.PR)
  })
_sym_db.RegisterMessage(PR)

Joint = _reflection.GeneratedProtocolMessageType('Joint', (_message.Message,), {
  'DESCRIPTOR' : _JOINT,
  '__module__' : 'os_server_pb2'
  # @@protoc_insertion_point(class_scope:osserver.Joint)
  })
_sym_db.RegisterMessage(Joint)

RingData = _reflection.GeneratedProtocolMessageType('RingData', (_message.Message,), {
  'DESCRIPTOR' : _RINGDATA,
  '__module__' : 'os_server_pb2'
  # @@protoc_insertion_point(class_scope:osserver.RingData)
  })
_sym_db.RegisterMessage(RingData)

CurrentVoltage = _reflection.GeneratedProtocolMessageType('CurrentVoltage', (_message.Message,), {
  'DESCRIPTOR' : _CURRENTVOLTAGE,
  '__module__' : 'os_server_pb2'
  # @@protoc_insertion_point(class_scope:osserver.CurrentVoltage)
  })
_sym_db.RegisterMessage(CurrentVoltage)



_OSSERVER = _descriptor.ServiceDescriptor(
  name='OsServer',
  full_name='osserver.OsServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=557,
  serialized_end=619,
  methods=[
  _descriptor.MethodDescriptor(
    name='getRingData',
    full_name='osserver.OsServer.getRingData',
    index=0,
    containing_service=None,
    input_type=_REQ,
    output_type=_RINGDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OSSERVER)

DESCRIPTOR.services_by_name['OsServer'] = _OSSERVER

# @@protoc_insertion_point(module_scope)