from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='device.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x64\x65vice.proto\"\x81\x01\n\x06\x44\x65vice\x12\x16\n\x0e\x44\x65viceIdentity\x18\x01 \x01(\t\x12\x14\n\x0cTimeFunction\x18\x02 \x01(\t\x12\x13\n\x0bMeasurement\x18\x03 \x01(\t\x12\x0c\n\x04xmin\x18\x04 \x01(\x02\x12\x0c\n\x04xmax\x18\x05 \x01(\x02\x12\x18\n\x10ReliabilityScore\x18\x06 \x01(\x02\"&\n\x0b\x44\x65vicesList\x12\x17\n\x06\x44\x65vice\x18\x01 \x03(\x0b\x32\x07.Deviceb\x06proto3'
)




_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='DeviceIdentity', full_name='Device.DeviceIdentity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TimeFunction', full_name='Device.TimeFunction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Measurement', full_name='Device.Measurement', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xmin', full_name='Device.xmin', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xmax', full_name='Device.xmax', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ReliabilityScore', full_name='Device.ReliabilityScore', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=17,
  serialized_end=146,
)


_DEVICESLIST = _descriptor.Descriptor(
  name='DevicesList',
  full_name='DevicesList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Device', full_name='DevicesList.Device', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=148,
  serialized_end=186,
)

_DEVICESLIST.fields_by_name['Device'].message_type = _DEVICE
DESCRIPTOR.message_types_by_name['Device'] = _DEVICE
DESCRIPTOR.message_types_by_name['DevicesList'] = _DEVICESLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), {
  'DESCRIPTOR' : _DEVICE,
  '__module__' : 'device_pb2'
  })
_sym_db.RegisterMessage(Device)

DevicesList = _reflection.GeneratedProtocolMessageType('DevicesList', (_message.Message,), {
  'DESCRIPTOR' : _DEVICESLIST,
  '__module__' : 'device_pb2'
  })
_sym_db.RegisterMessage(DevicesList)
