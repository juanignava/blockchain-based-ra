
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_SE.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11response_SE.proto\",\n\x0bresponse_SE\x12\x0e\n\x06Result\x18\x01 \x01(\t\x12\r\n\x05State\x18\x02 \x01(\tb\x06proto3')
)




_RESPONSE_SE = _descriptor.Descriptor(
  name='response_SE',
  full_name='response_SE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='response_SE.Result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='State', full_name='response_SE.State', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=21,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['response_SE'] = _RESPONSE_SE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

response_SE = _reflection.GeneratedProtocolMessageType('response_SE', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_SE,
  __module__ = 'response_SE_pb2'
  # @@protoc_insertion_point(class_scope:response_SE)
  ))
_sym_db.RegisterMessage(response_SE)


# @@protoc_insertion_point(module_scope)
