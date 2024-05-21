
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_TQ.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11response_TQ.proto\"X\n\nresponseTQ\x12\x0e\n\x06Result\x18\x01 \x01(\t\x12\x10\n\x08ProverID\x18\x02 \x01(\t\x12\x13\n\x0bRequestorID\x18\x03 \x01(\t\x12\x13\n\x0bTrustStatus\x18\x04 \x01(\x02\x62\x06proto3')
)




_RESPONSETQ = _descriptor.Descriptor(
  name='responseTQ',
  full_name='responseTQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='responseTQ.Result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ProverID', full_name='responseTQ.ProverID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='RequestorID', full_name='responseTQ.RequestorID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TrustStatus', full_name='responseTQ.TrustStatus', index=3,
      number=4, type=2, cpp_type=6, label=1,
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
  serialized_start=21,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['responseTQ'] = _RESPONSETQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

responseTQ = _reflection.GeneratedProtocolMessageType('responseTQ', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSETQ,
  __module__ = 'response_TQ_pb2'
  # @@protoc_insertion_point(class_scope:responseTQ)
  ))
_sym_db.RegisterMessage(responseTQ)


# @@protoc_insertion_point(module_scope)
