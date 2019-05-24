# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/search_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.google.api import annotations_pb2 as ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2
from ga4gh.schemas.ga4gh import clinical_metadata_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2
from ga4gh.schemas.ga4gh import clinical_metadata_service_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2
from ga4gh.schemas.ga4gh import variants_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_variants__pb2
from ga4gh.schemas.ga4gh import variant_service_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_variant__service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/search_service.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n(ga4gh/schemas/ga4gh/search_service.proto\x12\x13ga4gh.schemas.ga4gh\x1a*ga4gh/schemas/google/api/annotations.proto\x1a+ga4gh/schemas/ga4gh/clinical_metadata.proto\x1a\x33ga4gh/schemas/ga4gh/clinical_metadata_service.proto\x1a\"ga4gh/schemas/ga4gh/variants.proto\x1a)ga4gh/schemas/ga4gh/variant_service.proto\"\xbf\n\n\tComponent\x12\n\n\x02id\x18\x01 \x01(\t\x12>\n\x08patients\x18\x02 \x01(\x0b\x32*.ga4gh.schemas.ga4gh.SearchPatientsRequestH\x00\x12\x44\n\x0b\x65nrollments\x18\x03 \x01(\x0b\x32-.ga4gh.schemas.ga4gh.SearchEnrollmentsRequestH\x00\x12>\n\x08\x63onsents\x18\x04 \x01(\x0b\x32*.ga4gh.schemas.ga4gh.SearchConsentsRequestH\x00\x12@\n\tdiagnoses\x18\x05 \x01(\x0b\x32+.ga4gh.schemas.ga4gh.SearchDiagnosesRequestH\x00\x12<\n\x07samples\x18\x06 \x01(\x0b\x32).ga4gh.schemas.ga4gh.SearchSamplesRequestH\x00\x12\x42\n\ntreatments\x18\x07 \x01(\x0b\x32,.ga4gh.schemas.ga4gh.SearchTreatmentsRequestH\x00\x12>\n\x08outcomes\x18\x08 \x01(\x0b\x32*.ga4gh.schemas.ga4gh.SearchOutcomesRequestH\x00\x12H\n\rcomplications\x18\t \x01(\x0b\x32/.ga4gh.schemas.ga4gh.SearchComplicationsRequestH\x00\x12\x46\n\x0ctumourboards\x18\n \x01(\x0b\x32..ga4gh.schemas.ga4gh.SearchTumourboardsRequestH\x00\x12>\n\x08variants\x18\x0b \x01(\x0b\x32*.ga4gh.schemas.ga4gh.SearchVariantsRequestH\x00\x12N\n\x0evariantsByGene\x18\x0c \x01(\x0b\x32\x34.ga4gh.schemas.ga4gh.SearchVariantsByGeneNameRequestH\x00\x12:\n\x06slides\x18\r \x01(\x0b\x32(.ga4gh.schemas.ga4gh.SearchSlidesRequestH\x00\x12<\n\x07studies\x18\x0e \x01(\x0b\x32).ga4gh.schemas.ga4gh.SearchStudiesRequestH\x00\x12>\n\x08labtests\x18\x0f \x01(\x0b\x32*.ga4gh.schemas.ga4gh.SearchLabtestsRequestH\x00\x12J\n\x0e\x63hemotherapies\x18\x10 \x01(\x0b\x32\x30.ga4gh.schemas.ga4gh.SearchChemotherapiesRequestH\x00\x12J\n\x0eradiotherapies\x18\x11 \x01(\x0b\x32\x30.ga4gh.schemas.ga4gh.SearchRadiotherapiesRequestH\x00\x12L\n\x0fimmunotherapies\x18\x12 \x01(\x0b\x32\x31.ga4gh.schemas.ga4gh.SearchImmunotherapiesRequestH\x00\x12@\n\tsurgeries\x18\x13 \x01(\x0b\x32+.ga4gh.schemas.ga4gh.SearchSurgeriesRequestH\x00\x12L\n\x0f\x63\x65lltransplants\x18\x14 \x01(\x0b\x32\x31.ga4gh.schemas.ga4gh.SearchCelltransplantsRequestH\x00\x42\n\n\x08\x65ndpoint\"t\n\x05Logic\x12\'\n\x03\x61nd\x18\x01 \x03(\x0b\x32\x1a.ga4gh.schemas.ga4gh.Logic\x12&\n\x02or\x18\x02 \x03(\x0b\x32\x1a.ga4gh.schemas.ga4gh.Logic\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0e\n\x06negate\x18\x04 \x01(\x08\"w\n\x06Result\x12\r\n\x05table\x18\x01 \x01(\t\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\x12\r\n\x05start\x18\x03 \x01(\t\x12\x0b\n\x03\x65nd\x18\x04 \x01(\t\x12\x15\n\rreferenceName\x18\x05 \x01(\t\x12\x0c\n\x04gene\x18\x06 \x01(\t\x12\r\n\x05\x63ount\x18\x07 \x03(\t\"\xeb\x01\n\x12SearchQueryRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12)\n\x05logic\x18\x02 \x01(\x0b\x32\x1a.ga4gh.schemas.ga4gh.Logic\x12\x32\n\ncomponents\x18\x03 \x03(\x0b\x32\x1e.ga4gh.schemas.ga4gh.Component\x12,\n\x07results\x18\x04 \x03(\x0b\x32\x1b.ga4gh.schemas.ga4gh.Result\x12\r\n\x05limit\x18\x05 \x01(\x05\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x12\n\npage_token\x18\x07 \x01(\t\"\xd6\x07\n\x13SearchQueryResponse\x12.\n\x08patients\x18\x01 \x03(\x0b\x32\x1c.ga4gh.schemas.ga4gh.Patient\x12\x34\n\x0b\x65nrollments\x18\x02 \x03(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Enrollment\x12.\n\x08\x63onsents\x18\x03 \x03(\x0b\x32\x1c.ga4gh.schemas.ga4gh.Consent\x12\x31\n\tdiagnoses\x18\x04 \x03(\x0b\x32\x1e.ga4gh.schemas.ga4gh.Diagnosis\x12,\n\x07samples\x18\x05 \x03(\x0b\x32\x1b.ga4gh.schemas.ga4gh.Sample\x12\x32\n\ntreatments\x18\x06 \x03(\x0b\x32\x1e.ga4gh.schemas.ga4gh.Treatment\x12.\n\x08outcomes\x18\x07 \x03(\x0b\x32\x1c.ga4gh.schemas.ga4gh.Outcome\x12\x38\n\rcomplications\x18\x08 \x03(\x0b\x32!.ga4gh.schemas.ga4gh.Complication\x12\x36\n\x0ctumourboards\x18\t \x03(\x0b\x32 .ga4gh.schemas.ga4gh.Tumourboard\x12.\n\x08variants\x18\n \x03(\x0b\x32\x1c.ga4gh.schemas.ga4gh.Variant\x12*\n\x06slides\x18\x0b \x03(\x0b\x32\x1a.ga4gh.schemas.ga4gh.Slide\x12+\n\x07studies\x18\x0c \x03(\x0b\x32\x1a.ga4gh.schemas.ga4gh.Study\x12.\n\x08labtests\x18\r \x03(\x0b\x32\x1c.ga4gh.schemas.ga4gh.Labtest\x12/\n\tsurgeries\x18\x0e \x03(\x0b\x32\x1c.ga4gh.schemas.ga4gh.Surgery\x12\x39\n\x0e\x63hemotherapies\x18\x0f \x03(\x0b\x32!.ga4gh.schemas.ga4gh.Chemotherapy\x12;\n\x0fimmunotherapies\x18\x10 \x03(\x0b\x32\".ga4gh.schemas.ga4gh.Immunotherapy\x12\x39\n\x0eradiotherapies\x18\x11 \x03(\x0b\x32!.ga4gh.schemas.ga4gh.Radiotherapy\x12<\n\x0f\x63\x65lltransplants\x18\x12 \x03(\x0b\x32#.ga4gh.schemas.ga4gh.Celltransplant\x12\x17\n\x0fnext_page_token\x18\x13 \x01(\t2\x8b\x01\n\rSearchService\x12z\n\x07GetItem\x12\'.ga4gh.schemas.ga4gh.SearchQueryRequest\x1a(.ga4gh.schemas.ga4gh.SearchQueryResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v0.6.0a10/search:\x01*b\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_variants__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_variant__service__pb2.DESCRIPTOR,])




_COMPONENT = _descriptor.Descriptor(
  name='Component',
  full_name='ga4gh.schemas.ga4gh.Component',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Component.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patients', full_name='ga4gh.schemas.ga4gh.Component.patients', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enrollments', full_name='ga4gh.schemas.ga4gh.Component.enrollments', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consents', full_name='ga4gh.schemas.ga4gh.Component.consents', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diagnoses', full_name='ga4gh.schemas.ga4gh.Component.diagnoses', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='ga4gh.schemas.ga4gh.Component.samples', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='treatments', full_name='ga4gh.schemas.ga4gh.Component.treatments', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outcomes', full_name='ga4gh.schemas.ga4gh.Component.outcomes', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complications', full_name='ga4gh.schemas.ga4gh.Component.complications', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tumourboards', full_name='ga4gh.schemas.ga4gh.Component.tumourboards', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variants', full_name='ga4gh.schemas.ga4gh.Component.variants', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variantsByGene', full_name='ga4gh.schemas.ga4gh.Component.variantsByGene', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slides', full_name='ga4gh.schemas.ga4gh.Component.slides', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='studies', full_name='ga4gh.schemas.ga4gh.Component.studies', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labtests', full_name='ga4gh.schemas.ga4gh.Component.labtests', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chemotherapies', full_name='ga4gh.schemas.ga4gh.Component.chemotherapies', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='radiotherapies', full_name='ga4gh.schemas.ga4gh.Component.radiotherapies', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='immunotherapies', full_name='ga4gh.schemas.ga4gh.Component.immunotherapies', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surgeries', full_name='ga4gh.schemas.ga4gh.Component.surgeries', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='celltransplants', full_name='ga4gh.schemas.ga4gh.Component.celltransplants', index=19,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='endpoint', full_name='ga4gh.schemas.ga4gh.Component.endpoint',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=287,
  serialized_end=1630,
)


_LOGIC = _descriptor.Descriptor(
  name='Logic',
  full_name='ga4gh.schemas.ga4gh.Logic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='and', full_name='ga4gh.schemas.ga4gh.Logic.and', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='or', full_name='ga4gh.schemas.ga4gh.Logic.or', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Logic.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negate', full_name='ga4gh.schemas.ga4gh.Logic.negate', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1632,
  serialized_end=1748,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='ga4gh.schemas.ga4gh.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='ga4gh.schemas.ga4gh.Result.table', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fields', full_name='ga4gh.schemas.ga4gh.Result.fields', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.schemas.ga4gh.Result.start', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.schemas.ga4gh.Result.end', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceName', full_name='ga4gh.schemas.ga4gh.Result.referenceName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene', full_name='ga4gh.schemas.ga4gh.Result.gene', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='ga4gh.schemas.ga4gh.Result.count', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1750,
  serialized_end=1869,
)


_SEARCHQUERYREQUEST = _descriptor.Descriptor(
  name='SearchQueryRequest',
  full_name='ga4gh.schemas.ga4gh.SearchQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.SearchQueryRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logic', full_name='ga4gh.schemas.ga4gh.SearchQueryRequest.logic', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='components', full_name='ga4gh.schemas.ga4gh.SearchQueryRequest.components', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='results', full_name='ga4gh.schemas.ga4gh.SearchQueryRequest.results', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='ga4gh.schemas.ga4gh.SearchQueryRequest.limit', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchQueryRequest.page_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchQueryRequest.page_token', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=1872,
  serialized_end=2107,
)


_SEARCHQUERYRESPONSE = _descriptor.Descriptor(
  name='SearchQueryResponse',
  full_name='ga4gh.schemas.ga4gh.SearchQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='patients', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.patients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enrollments', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.enrollments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consents', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.consents', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diagnoses', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.diagnoses', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.samples', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='treatments', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.treatments', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outcomes', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.outcomes', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complications', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.complications', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tumourboards', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.tumourboards', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variants', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.variants', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slides', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.slides', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='studies', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.studies', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labtests', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.labtests', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surgeries', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.surgeries', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chemotherapies', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.chemotherapies', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='immunotherapies', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.immunotherapies', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='radiotherapies', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.radiotherapies', index=16,
      number=17, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='celltransplants', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.celltransplants', index=17,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchQueryResponse.next_page_token', index=18,
      number=19, type=9, cpp_type=9, label=1,
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
  serialized_start=2110,
  serialized_end=3092,
)

_COMPONENT.fields_by_name['patients'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHPATIENTSREQUEST
_COMPONENT.fields_by_name['enrollments'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHENROLLMENTSREQUEST
_COMPONENT.fields_by_name['consents'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHCONSENTSREQUEST
_COMPONENT.fields_by_name['diagnoses'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHDIAGNOSESREQUEST
_COMPONENT.fields_by_name['samples'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHSAMPLESREQUEST
_COMPONENT.fields_by_name['treatments'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHTREATMENTSREQUEST
_COMPONENT.fields_by_name['outcomes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHOUTCOMESREQUEST
_COMPONENT.fields_by_name['complications'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHCOMPLICATIONSREQUEST
_COMPONENT.fields_by_name['tumourboards'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHTUMOURBOARDSREQUEST
_COMPONENT.fields_by_name['variants'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_variant__service__pb2._SEARCHVARIANTSREQUEST
_COMPONENT.fields_by_name['variantsByGene'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_variant__service__pb2._SEARCHVARIANTSBYGENENAMEREQUEST
_COMPONENT.fields_by_name['slides'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHSLIDESREQUEST
_COMPONENT.fields_by_name['studies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHSTUDIESREQUEST
_COMPONENT.fields_by_name['labtests'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHLABTESTSREQUEST
_COMPONENT.fields_by_name['chemotherapies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHCHEMOTHERAPIESREQUEST
_COMPONENT.fields_by_name['radiotherapies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHRADIOTHERAPIESREQUEST
_COMPONENT.fields_by_name['immunotherapies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHIMMUNOTHERAPIESREQUEST
_COMPONENT.fields_by_name['surgeries'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHSURGERIESREQUEST
_COMPONENT.fields_by_name['celltransplants'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__service__pb2._SEARCHCELLTRANSPLANTSREQUEST
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['patients'])
_COMPONENT.fields_by_name['patients'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['enrollments'])
_COMPONENT.fields_by_name['enrollments'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['consents'])
_COMPONENT.fields_by_name['consents'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['diagnoses'])
_COMPONENT.fields_by_name['diagnoses'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['samples'])
_COMPONENT.fields_by_name['samples'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['treatments'])
_COMPONENT.fields_by_name['treatments'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['outcomes'])
_COMPONENT.fields_by_name['outcomes'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['complications'])
_COMPONENT.fields_by_name['complications'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['tumourboards'])
_COMPONENT.fields_by_name['tumourboards'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['variants'])
_COMPONENT.fields_by_name['variants'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['variantsByGene'])
_COMPONENT.fields_by_name['variantsByGene'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['slides'])
_COMPONENT.fields_by_name['slides'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['studies'])
_COMPONENT.fields_by_name['studies'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['labtests'])
_COMPONENT.fields_by_name['labtests'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['chemotherapies'])
_COMPONENT.fields_by_name['chemotherapies'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['radiotherapies'])
_COMPONENT.fields_by_name['radiotherapies'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['immunotherapies'])
_COMPONENT.fields_by_name['immunotherapies'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['surgeries'])
_COMPONENT.fields_by_name['surgeries'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_COMPONENT.oneofs_by_name['endpoint'].fields.append(
  _COMPONENT.fields_by_name['celltransplants'])
_COMPONENT.fields_by_name['celltransplants'].containing_oneof = _COMPONENT.oneofs_by_name['endpoint']
_LOGIC.fields_by_name['and'].message_type = _LOGIC
_LOGIC.fields_by_name['or'].message_type = _LOGIC
_SEARCHQUERYREQUEST.fields_by_name['logic'].message_type = _LOGIC
_SEARCHQUERYREQUEST.fields_by_name['components'].message_type = _COMPONENT
_SEARCHQUERYREQUEST.fields_by_name['results'].message_type = _RESULT
_SEARCHQUERYRESPONSE.fields_by_name['patients'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._PATIENT
_SEARCHQUERYRESPONSE.fields_by_name['enrollments'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._ENROLLMENT
_SEARCHQUERYRESPONSE.fields_by_name['consents'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._CONSENT
_SEARCHQUERYRESPONSE.fields_by_name['diagnoses'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._DIAGNOSIS
_SEARCHQUERYRESPONSE.fields_by_name['samples'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._SAMPLE
_SEARCHQUERYRESPONSE.fields_by_name['treatments'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._TREATMENT
_SEARCHQUERYRESPONSE.fields_by_name['outcomes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._OUTCOME
_SEARCHQUERYRESPONSE.fields_by_name['complications'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._COMPLICATION
_SEARCHQUERYRESPONSE.fields_by_name['tumourboards'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._TUMOURBOARD
_SEARCHQUERYRESPONSE.fields_by_name['variants'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_variants__pb2._VARIANT
_SEARCHQUERYRESPONSE.fields_by_name['slides'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._SLIDE
_SEARCHQUERYRESPONSE.fields_by_name['studies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._STUDY
_SEARCHQUERYRESPONSE.fields_by_name['labtests'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._LABTEST
_SEARCHQUERYRESPONSE.fields_by_name['surgeries'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._SURGERY
_SEARCHQUERYRESPONSE.fields_by_name['chemotherapies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._CHEMOTHERAPY
_SEARCHQUERYRESPONSE.fields_by_name['immunotherapies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._IMMUNOTHERAPY
_SEARCHQUERYRESPONSE.fields_by_name['radiotherapies'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._RADIOTHERAPY
_SEARCHQUERYRESPONSE.fields_by_name['celltransplants'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._CELLTRANSPLANT
DESCRIPTOR.message_types_by_name['Component'] = _COMPONENT
DESCRIPTOR.message_types_by_name['Logic'] = _LOGIC
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['SearchQueryRequest'] = _SEARCHQUERYREQUEST
DESCRIPTOR.message_types_by_name['SearchQueryResponse'] = _SEARCHQUERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Component = _reflection.GeneratedProtocolMessageType('Component', (_message.Message,), dict(
  DESCRIPTOR = _COMPONENT,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Component)
  ))
_sym_db.RegisterMessage(Component)

Logic = _reflection.GeneratedProtocolMessageType('Logic', (_message.Message,), dict(
  DESCRIPTOR = _LOGIC,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Logic)
  ))
_sym_db.RegisterMessage(Logic)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Result)
  ))
_sym_db.RegisterMessage(Result)

SearchQueryRequest = _reflection.GeneratedProtocolMessageType('SearchQueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHQUERYREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchQueryRequest)
  ))
_sym_db.RegisterMessage(SearchQueryRequest)

SearchQueryResponse = _reflection.GeneratedProtocolMessageType('SearchQueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHQUERYRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchQueryResponse)
  ))
_sym_db.RegisterMessage(SearchQueryResponse)


# @@protoc_insertion_point(module_scope)
