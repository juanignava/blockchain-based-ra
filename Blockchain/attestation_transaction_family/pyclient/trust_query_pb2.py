
import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='trust_query.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11trust_query.proto\".\n\nTrustQuery\x12\x0f\n\x07Trustor\x18\x01 \x01(\t\x12\x0f\n\x07Trustee\x18\x02 \x01(\tb\x06proto3')
)




_TRUSTQUERY = _descriptor.Descriptor(
  name='TrustQuery',
  full_name='TrustQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Trustor', full_name='TrustQuery.Trustor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Trustee', full_name='TrustQuery.Trustee', index=1,
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
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['TrustQuery'] = _TRUSTQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrustQuery = _reflection.GeneratedProtocolMessageType('TrustQuery', (_message.Message,), dict(
  DESCRIPTOR = _TRUSTQUERY,
  __module__ = 'trust_query_pb2'
  # @@protoc_insertion_point(class_scope:TrustQuery)
  ))
_sym_db.RegisterMessage(TrustQuery)


# @@protoc_insertion_point(module_scope)
