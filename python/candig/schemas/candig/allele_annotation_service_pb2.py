# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candig/schemas/candig/allele_annotation_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from candig.schemas.candig import allele_annotations_pb2 as candig_dot_schemas_dot_candig_dot_allele__annotations__pb2
from candig.schemas.candig import common_pb2 as candig_dot_schemas_dot_candig_dot_common__pb2
from candig.schemas.google.api import annotations_pb2 as candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candig/schemas/candig/allele_annotation_service.proto',
  package='candig.schemas.candig',
  syntax='proto3',
  serialized_pb=_b('\n5candig/schemas/candig/allele_annotation_service.proto\x12\x15\x63\x61ndig.schemas.candig\x1a.candig/schemas/candig/allele_annotations.proto\x1a\"candig/schemas/candig/common.proto\x1a+candig/schemas/google/api/annotations.proto\"\xeb\x01\n\x1fSearchVariantAnnotationsRequest\x12!\n\x19variant_annotation_set_id\x18\x01 \x01(\t\x12\x16\n\x0ereference_name\x18\x02 \x01(\t\x12\x14\n\x0creference_id\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x03\x12\x34\n\x07\x65\x66\x66\x65\x63ts\x18\x06 \x03(\x0b\x32#.candig.schemas.candig.OntologyTerm\x12\x11\n\tpage_size\x18\x07 \x01(\x05\x12\x12\n\npage_token\x18\x08 \x01(\t\"\x82\x01\n SearchVariantAnnotationsResponse\x12\x45\n\x13variant_annotations\x18\x01 \x03(\x0b\x32(.candig.schemas.candig.VariantAnnotation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"c\n\"SearchVariantAnnotationSetsRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"\x8c\x01\n#SearchVariantAnnotationSetsResponse\x12L\n\x17variant_annotation_sets\x18\x01 \x03(\x0b\x32+.candig.schemas.candig.VariantAnnotationSet\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"C\n\x1eGetVariantAnnotationSetRequest\x12!\n\x19variant_annotation_set_id\x18\x01 \x01(\t2\xe0\x04\n\x17\x41lleleAnnotationService\x12\xb9\x01\n\x18SearchVariantAnnotations\x12\x36.candig.schemas.candig.SearchVariantAnnotationsRequest\x1a\x37.candig.schemas.candig.SearchVariantAnnotationsResponse\",\x82\xd3\xe4\x93\x02&\"!/v0.8.0/variantannotations/search:\x01*\x12\xc5\x01\n\x1bSearchVariantAnnotationSets\x12\x39.candig.schemas.candig.SearchVariantAnnotationSetsRequest\x1a:.candig.schemas.candig.SearchVariantAnnotationSetsResponse\"/\x82\xd3\xe4\x93\x02)\"$/v0.8.0/variantannotationsets/search:\x01*\x12\xc0\x01\n\x17GetVariantAnnotationSet\x12\x35.candig.schemas.candig.GetVariantAnnotationSetRequest\x1a+.candig.schemas.candig.VariantAnnotationSet\"A\x82\xd3\xe4\x93\x02;\x12\x39/v0.8.0/variantannotationsets/{variant_annotation_set_id}b\x06proto3')
  ,
  dependencies=[candig_dot_schemas_dot_candig_dot_allele__annotations__pb2.DESCRIPTOR,candig_dot_schemas_dot_candig_dot_common__pb2.DESCRIPTOR,candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHVARIANTANNOTATIONSREQUEST = _descriptor.Descriptor(
  name='SearchVariantAnnotationsRequest',
  full_name='candig.schemas.candig.SearchVariantAnnotationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_annotation_set_id', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.variant_annotation_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.reference_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_id', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.reference_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.start', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.end', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effects', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.effects', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.page_size', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchVariantAnnotationsRequest.page_token', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=445,
)


_SEARCHVARIANTANNOTATIONSRESPONSE = _descriptor.Descriptor(
  name='SearchVariantAnnotationsResponse',
  full_name='candig.schemas.candig.SearchVariantAnnotationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_annotations', full_name='candig.schemas.candig.SearchVariantAnnotationsResponse.variant_annotations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchVariantAnnotationsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=578,
)


_SEARCHVARIANTANNOTATIONSETSREQUEST = _descriptor.Descriptor(
  name='SearchVariantAnnotationSetsRequest',
  full_name='candig.schemas.candig.SearchVariantAnnotationSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='candig.schemas.candig.SearchVariantAnnotationSetsRequest.variant_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchVariantAnnotationSetsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchVariantAnnotationSetsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=580,
  serialized_end=679,
)


_SEARCHVARIANTANNOTATIONSETSRESPONSE = _descriptor.Descriptor(
  name='SearchVariantAnnotationSetsResponse',
  full_name='candig.schemas.candig.SearchVariantAnnotationSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_annotation_sets', full_name='candig.schemas.candig.SearchVariantAnnotationSetsResponse.variant_annotation_sets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchVariantAnnotationSetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=822,
)


_GETVARIANTANNOTATIONSETREQUEST = _descriptor.Descriptor(
  name='GetVariantAnnotationSetRequest',
  full_name='candig.schemas.candig.GetVariantAnnotationSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_annotation_set_id', full_name='candig.schemas.candig.GetVariantAnnotationSetRequest.variant_annotation_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=824,
  serialized_end=891,
)

_SEARCHVARIANTANNOTATIONSREQUEST.fields_by_name['effects'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ONTOLOGYTERM
_SEARCHVARIANTANNOTATIONSRESPONSE.fields_by_name['variant_annotations'].message_type = candig_dot_schemas_dot_candig_dot_allele__annotations__pb2._VARIANTANNOTATION
_SEARCHVARIANTANNOTATIONSETSRESPONSE.fields_by_name['variant_annotation_sets'].message_type = candig_dot_schemas_dot_candig_dot_allele__annotations__pb2._VARIANTANNOTATIONSET
DESCRIPTOR.message_types_by_name['SearchVariantAnnotationsRequest'] = _SEARCHVARIANTANNOTATIONSREQUEST
DESCRIPTOR.message_types_by_name['SearchVariantAnnotationsResponse'] = _SEARCHVARIANTANNOTATIONSRESPONSE
DESCRIPTOR.message_types_by_name['SearchVariantAnnotationSetsRequest'] = _SEARCHVARIANTANNOTATIONSETSREQUEST
DESCRIPTOR.message_types_by_name['SearchVariantAnnotationSetsResponse'] = _SEARCHVARIANTANNOTATIONSETSRESPONSE
DESCRIPTOR.message_types_by_name['GetVariantAnnotationSetRequest'] = _GETVARIANTANNOTATIONSETREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchVariantAnnotationsRequest = _reflection.GeneratedProtocolMessageType('SearchVariantAnnotationsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTANNOTATIONSREQUEST,
  __module__ = 'candig.schemas.candig.allele_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchVariantAnnotationsRequest)
  ))
_sym_db.RegisterMessage(SearchVariantAnnotationsRequest)

SearchVariantAnnotationsResponse = _reflection.GeneratedProtocolMessageType('SearchVariantAnnotationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTANNOTATIONSRESPONSE,
  __module__ = 'candig.schemas.candig.allele_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchVariantAnnotationsResponse)
  ))
_sym_db.RegisterMessage(SearchVariantAnnotationsResponse)

SearchVariantAnnotationSetsRequest = _reflection.GeneratedProtocolMessageType('SearchVariantAnnotationSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTANNOTATIONSETSREQUEST,
  __module__ = 'candig.schemas.candig.allele_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchVariantAnnotationSetsRequest)
  ))
_sym_db.RegisterMessage(SearchVariantAnnotationSetsRequest)

SearchVariantAnnotationSetsResponse = _reflection.GeneratedProtocolMessageType('SearchVariantAnnotationSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHVARIANTANNOTATIONSETSRESPONSE,
  __module__ = 'candig.schemas.candig.allele_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchVariantAnnotationSetsResponse)
  ))
_sym_db.RegisterMessage(SearchVariantAnnotationSetsResponse)

GetVariantAnnotationSetRequest = _reflection.GeneratedProtocolMessageType('GetVariantAnnotationSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVARIANTANNOTATIONSETREQUEST,
  __module__ = 'candig.schemas.candig.allele_annotation_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetVariantAnnotationSetRequest)
  ))
_sym_db.RegisterMessage(GetVariantAnnotationSetRequest)


# @@protoc_insertion_point(module_scope)