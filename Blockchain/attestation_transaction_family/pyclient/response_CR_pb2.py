
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_CR.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11response_CR.proto\"0\n\x0bresponse_CR\x12\x11\n\tTimestamp\x18\x01 \x01(\t\x12\x0e\n\x06Result\x18\x02 \x01(\x05\x62\x06proto3')
)




_RESPONSE_CR = _descriptor.Descriptor(
  name='response_CR',
  full_name='response_CR',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='response_CR.Timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Result', full_name='response_CR.Result', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=69,
)

DESCRIPTOR.message_types_by_name['response_CR'] = _RESPONSE_CR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

response_CR = _reflection.GeneratedProtocolMessageType('response_CR', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE_CR,
  __module__ = 'response_CR_pb2'
  # @@protoc_insertion_point(class_scope:response_CR)
  ))
_sym_db.RegisterMessage(response_CR)


# @@protoc_insertion_point(module_scope)
