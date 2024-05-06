# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: warrants.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='warrants.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0ewarrants.proto\"H\n\x07Warrant\x12\x11\n\tWarrantor\x18\x01 \x01(\t\x12\x11\n\tWarrantee\x18\x02 \x01(\t\x12\x17\n\x0f\x41ttestationType\x18\x03 \x01(\t\")\n\x0bWarrantList\x12\x1a\n\x08Warrants\x18\x01 \x03(\x0b\x32\x08.Warrantb\x06proto3')
)




_WARRANT = _descriptor.Descriptor(
  name='Warrant',
  full_name='Warrant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Warrantor', full_name='Warrant.Warrantor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Warrantee', full_name='Warrant.Warrantee', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='AttestationType', full_name='Warrant.AttestationType', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=18,
  serialized_end=90,
)


_WARRANTLIST = _descriptor.Descriptor(
  name='WarrantList',
  full_name='WarrantList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Warrants', full_name='WarrantList.Warrants', index=0,
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
  serialized_start=92,
  serialized_end=133,
)

_WARRANTLIST.fields_by_name['Warrants'].message_type = _WARRANT
DESCRIPTOR.message_types_by_name['Warrant'] = _WARRANT
DESCRIPTOR.message_types_by_name['WarrantList'] = _WARRANTLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Warrant = _reflection.GeneratedProtocolMessageType('Warrant', (_message.Message,), dict(
  DESCRIPTOR = _WARRANT,
  __module__ = 'warrants_pb2'
  # @@protoc_insertion_point(class_scope:Warrant)
  ))
_sym_db.RegisterMessage(Warrant)

WarrantList = _reflection.GeneratedProtocolMessageType('WarrantList', (_message.Message,), dict(
  DESCRIPTOR = _WARRANTLIST,
  __module__ = 'warrants_pb2'
  # @@protoc_insertion_point(class_scope:WarrantList)
  ))
_sym_db.RegisterMessage(WarrantList)


# @@protoc_insertion_point(module_scope)