# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evidence.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='evidence.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x65vidence.proto\"H\n\x08\x45vidence\x12\x16\n\x0eProverIdentity\x18\x01 \x01(\t\x12\x0f\n\x07\x42lockID\x18\x02 \x01(\t\x12\x13\n\x0bMeasurement\x18\x03 \x01(\tb\x06proto3'
)




_EVIDENCE = _descriptor.Descriptor(
  name='Evidence',
  full_name='Evidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ProverIdentity', full_name='Evidence.ProverIdentity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='BlockID', full_name='Evidence.BlockID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Measurement', full_name='Evidence.Measurement', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=18,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['Evidence'] = _EVIDENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Evidence = _reflection.GeneratedProtocolMessageType('Evidence', (_message.Message,), {
  'DESCRIPTOR' : _EVIDENCE,
  '__module__' : 'evidence_pb2'
  })
_sym_db.RegisterMessage(Evidence)

