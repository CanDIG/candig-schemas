# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/bio_metadata_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.ga4gh import bio_metadata_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_bio__metadata__pb2
from ga4gh.schemas.ga4gh import common_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2
from ga4gh.schemas.google.api import annotations_pb2 as ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/bio_metadata_service.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n.ga4gh/schemas/ga4gh/bio_metadata_service.proto\x12\x13ga4gh.schemas.ga4gh\x1a&ga4gh/schemas/ga4gh/bio_metadata.proto\x1a ga4gh/schemas/ga4gh/common.proto\x1a*ga4gh/schemas/google/api/annotations.proto\"q\n\x18SearchIndividualsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\"-\n\x14GetIndividualRequest\x12\x15\n\rindividual_id\x18\x01 \x01(\t\"j\n\x19SearchIndividualsResponse\x12\x34\n\x0bindividuals\x18\x01 \x03(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Individual\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x1e\n\x0cTempoRequest\x12\x0e\n\x06valami\x18\x01 \x01(\t\"\x1f\n\rTempoResponse\x12\x0e\n\x06valami\x18\x01 \x01(\t\"y\n\x17SearchBiosamplesRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rindividual_id\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"+\n\x13GetBiosampleRequest\x12\x14\n\x0c\x62iosample_id\x18\x01 \x01(\t\"g\n\x18SearchBiosamplesResponse\x12\x32\n\nbiosamples\x18\x01 \x03(\x0b\x32\x1e.ga4gh.schemas.ga4gh.Biosample\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"e\n\x18SearchExperimentsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\"-\n\x14GetExperimentRequest\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\"j\n\x19SearchExperimentsResponse\x12\x34\n\x0b\x65xperiments\x18\x01 \x03(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Experiment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"b\n\x15SearchAnalysesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\")\n\x12GetAnalysisRequest\x12\x13\n\x0b\x61nalysis_id\x18\x01 \x01(\t\"b\n\x16SearchAnalysesResponse\x12/\n\x08\x61nalyses\x18\x01 \x03(\x0b\x32\x1d.ga4gh.schemas.ga4gh.Analysis\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa8\t\n\x12\x42ioMetadataService\x12\x9c\x01\n\x11SearchIndividuals\x12-.ga4gh.schemas.ga4gh.SearchIndividualsRequest\x1a..ga4gh.schemas.ga4gh.SearchIndividualsResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/v0.6.0a10/individuals/search:\x01*\x12\x9c\x01\n\x11SearchExperiments\x12-.ga4gh.schemas.ga4gh.SearchExperimentsRequest\x1a..ga4gh.schemas.ga4gh.SearchExperimentsResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/v0.6.0a10/experiments/search:\x01*\x12\x90\x01\n\x0eSearchAnalyses\x12*.ga4gh.schemas.ga4gh.SearchAnalysesRequest\x1a+.ga4gh.schemas.ga4gh.SearchAnalysesResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v0.6.0a10/analyses/search:\x01*\x12\x98\x01\n\x10SearchBiosamples\x12,.ga4gh.schemas.ga4gh.SearchBiosamplesRequest\x1a-.ga4gh.schemas.ga4gh.SearchBiosamplesResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v0.6.0a10/biosamples/search:\x01*\x12\x8b\x01\n\rGetIndividual\x12).ga4gh.schemas.ga4gh.GetIndividualRequest\x1a\x1f.ga4gh.schemas.ga4gh.Individual\".\x82\xd3\xe4\x93\x02(\x12&/v0.6.0a10/individuals/{individual_id}\x12\x8b\x01\n\rGetExperiment\x12).ga4gh.schemas.ga4gh.GetExperimentRequest\x1a\x1f.ga4gh.schemas.ga4gh.Experiment\".\x82\xd3\xe4\x93\x02(\x12&/v0.6.0a10/experiments/{experiment_id}\x12\x80\x01\n\x0bGetAnalysis\x12\'.ga4gh.schemas.ga4gh.GetAnalysisRequest\x1a\x1d.ga4gh.schemas.ga4gh.Analysis\")\x82\xd3\xe4\x93\x02#\x12!/v0.6.0a10/analyses/{analysis_id}\x12\x86\x01\n\x0cGetBiosample\x12(.ga4gh.schemas.ga4gh.GetBiosampleRequest\x1a\x1e.ga4gh.schemas.ga4gh.Biosample\",\x82\xd3\xe4\x93\x02&\x12$/v0.6.0a10/biosamples/{biosample_id}b\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_ga4gh_dot_bio__metadata__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHINDIVIDUALSREQUEST = _descriptor.Descriptor(
  name='SearchIndividualsRequest',
  full_name='ga4gh.schemas.ga4gh.SearchIndividualsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.SearchIndividualsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.SearchIndividualsRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchIndividualsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchIndividualsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='ga4gh.schemas.ga4gh.SearchIndividualsRequest.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=189,
  serialized_end=302,
)


_GETINDIVIDUALREQUEST = _descriptor.Descriptor(
  name='GetIndividualRequest',
  full_name='ga4gh.schemas.ga4gh.GetIndividualRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='ga4gh.schemas.ga4gh.GetIndividualRequest.individual_id', index=0,
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
  serialized_start=304,
  serialized_end=349,
)


_SEARCHINDIVIDUALSRESPONSE = _descriptor.Descriptor(
  name='SearchIndividualsResponse',
  full_name='ga4gh.schemas.ga4gh.SearchIndividualsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individuals', full_name='ga4gh.schemas.ga4gh.SearchIndividualsResponse.individuals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchIndividualsResponse.next_page_token', index=1,
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
  serialized_start=351,
  serialized_end=457,
)


_TEMPOREQUEST = _descriptor.Descriptor(
  name='TempoRequest',
  full_name='ga4gh.schemas.ga4gh.TempoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valami', full_name='ga4gh.schemas.ga4gh.TempoRequest.valami', index=0,
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
  serialized_start=459,
  serialized_end=489,
)


_TEMPORESPONSE = _descriptor.Descriptor(
  name='TempoResponse',
  full_name='ga4gh.schemas.ga4gh.TempoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valami', full_name='ga4gh.schemas.ga4gh.TempoResponse.valami', index=0,
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
  serialized_start=491,
  serialized_end=522,
)


_SEARCHBIOSAMPLESREQUEST = _descriptor.Descriptor(
  name='SearchBiosamplesRequest',
  full_name='ga4gh.schemas.ga4gh.SearchBiosamplesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.SearchBiosamplesRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.SearchBiosamplesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='ga4gh.schemas.ga4gh.SearchBiosamplesRequest.individual_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchBiosamplesRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchBiosamplesRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=524,
  serialized_end=645,
)


_GETBIOSAMPLEREQUEST = _descriptor.Descriptor(
  name='GetBiosampleRequest',
  full_name='ga4gh.schemas.ga4gh.GetBiosampleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='ga4gh.schemas.ga4gh.GetBiosampleRequest.biosample_id', index=0,
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
  serialized_start=647,
  serialized_end=690,
)


_SEARCHBIOSAMPLESRESPONSE = _descriptor.Descriptor(
  name='SearchBiosamplesResponse',
  full_name='ga4gh.schemas.ga4gh.SearchBiosamplesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosamples', full_name='ga4gh.schemas.ga4gh.SearchBiosamplesResponse.biosamples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchBiosamplesResponse.next_page_token', index=1,
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
  serialized_start=692,
  serialized_end=795,
)


_SEARCHEXPERIMENTSREQUEST = _descriptor.Descriptor(
  name='SearchExperimentsRequest',
  full_name='ga4gh.schemas.ga4gh.SearchExperimentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.SearchExperimentsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='ga4gh.schemas.ga4gh.SearchExperimentsRequest.biosample_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchExperimentsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchExperimentsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=797,
  serialized_end=898,
)


_GETEXPERIMENTREQUEST = _descriptor.Descriptor(
  name='GetExperimentRequest',
  full_name='ga4gh.schemas.ga4gh.GetExperimentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='ga4gh.schemas.ga4gh.GetExperimentRequest.experiment_id', index=0,
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
  serialized_start=900,
  serialized_end=945,
)


_SEARCHEXPERIMENTSRESPONSE = _descriptor.Descriptor(
  name='SearchExperimentsResponse',
  full_name='ga4gh.schemas.ga4gh.SearchExperimentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiments', full_name='ga4gh.schemas.ga4gh.SearchExperimentsResponse.experiments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchExperimentsResponse.next_page_token', index=1,
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
  serialized_start=947,
  serialized_end=1053,
)


_SEARCHANALYSESREQUEST = _descriptor.Descriptor(
  name='SearchAnalysesRequest',
  full_name='ga4gh.schemas.ga4gh.SearchAnalysesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.SearchAnalysesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='ga4gh.schemas.ga4gh.SearchAnalysesRequest.biosample_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.schemas.ga4gh.SearchAnalysesRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.schemas.ga4gh.SearchAnalysesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1055,
  serialized_end=1153,
)


_GETANALYSISREQUEST = _descriptor.Descriptor(
  name='GetAnalysisRequest',
  full_name='ga4gh.schemas.ga4gh.GetAnalysisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analysis_id', full_name='ga4gh.schemas.ga4gh.GetAnalysisRequest.analysis_id', index=0,
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
  serialized_start=1155,
  serialized_end=1196,
)


_SEARCHANALYSESRESPONSE = _descriptor.Descriptor(
  name='SearchAnalysesResponse',
  full_name='ga4gh.schemas.ga4gh.SearchAnalysesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyses', full_name='ga4gh.schemas.ga4gh.SearchAnalysesResponse.analyses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.schemas.ga4gh.SearchAnalysesResponse.next_page_token', index=1,
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
  serialized_start=1198,
  serialized_end=1296,
)

_SEARCHINDIVIDUALSRESPONSE.fields_by_name['individuals'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_bio__metadata__pb2._INDIVIDUAL
_SEARCHBIOSAMPLESRESPONSE.fields_by_name['biosamples'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_bio__metadata__pb2._BIOSAMPLE
_SEARCHEXPERIMENTSRESPONSE.fields_by_name['experiments'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._EXPERIMENT
_SEARCHANALYSESRESPONSE.fields_by_name['analyses'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ANALYSIS
DESCRIPTOR.message_types_by_name['SearchIndividualsRequest'] = _SEARCHINDIVIDUALSREQUEST
DESCRIPTOR.message_types_by_name['GetIndividualRequest'] = _GETINDIVIDUALREQUEST
DESCRIPTOR.message_types_by_name['SearchIndividualsResponse'] = _SEARCHINDIVIDUALSRESPONSE
DESCRIPTOR.message_types_by_name['TempoRequest'] = _TEMPOREQUEST
DESCRIPTOR.message_types_by_name['TempoResponse'] = _TEMPORESPONSE
DESCRIPTOR.message_types_by_name['SearchBiosamplesRequest'] = _SEARCHBIOSAMPLESREQUEST
DESCRIPTOR.message_types_by_name['GetBiosampleRequest'] = _GETBIOSAMPLEREQUEST
DESCRIPTOR.message_types_by_name['SearchBiosamplesResponse'] = _SEARCHBIOSAMPLESRESPONSE
DESCRIPTOR.message_types_by_name['SearchExperimentsRequest'] = _SEARCHEXPERIMENTSREQUEST
DESCRIPTOR.message_types_by_name['GetExperimentRequest'] = _GETEXPERIMENTREQUEST
DESCRIPTOR.message_types_by_name['SearchExperimentsResponse'] = _SEARCHEXPERIMENTSRESPONSE
DESCRIPTOR.message_types_by_name['SearchAnalysesRequest'] = _SEARCHANALYSESREQUEST
DESCRIPTOR.message_types_by_name['GetAnalysisRequest'] = _GETANALYSISREQUEST
DESCRIPTOR.message_types_by_name['SearchAnalysesResponse'] = _SEARCHANALYSESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchIndividualsRequest = _reflection.GeneratedProtocolMessageType('SearchIndividualsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchIndividualsRequest)
  ))
_sym_db.RegisterMessage(SearchIndividualsRequest)

GetIndividualRequest = _reflection.GeneratedProtocolMessageType('GetIndividualRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINDIVIDUALREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetIndividualRequest)
  ))
_sym_db.RegisterMessage(GetIndividualRequest)

SearchIndividualsResponse = _reflection.GeneratedProtocolMessageType('SearchIndividualsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchIndividualsResponse)
  ))
_sym_db.RegisterMessage(SearchIndividualsResponse)

TempoRequest = _reflection.GeneratedProtocolMessageType('TempoRequest', (_message.Message,), dict(
  DESCRIPTOR = _TEMPOREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.TempoRequest)
  ))
_sym_db.RegisterMessage(TempoRequest)

TempoResponse = _reflection.GeneratedProtocolMessageType('TempoResponse', (_message.Message,), dict(
  DESCRIPTOR = _TEMPORESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.TempoResponse)
  ))
_sym_db.RegisterMessage(TempoResponse)

SearchBiosamplesRequest = _reflection.GeneratedProtocolMessageType('SearchBiosamplesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchBiosamplesRequest)
  ))
_sym_db.RegisterMessage(SearchBiosamplesRequest)

GetBiosampleRequest = _reflection.GeneratedProtocolMessageType('GetBiosampleRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBIOSAMPLEREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetBiosampleRequest)
  ))
_sym_db.RegisterMessage(GetBiosampleRequest)

SearchBiosamplesResponse = _reflection.GeneratedProtocolMessageType('SearchBiosamplesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchBiosamplesResponse)
  ))
_sym_db.RegisterMessage(SearchBiosamplesResponse)

SearchExperimentsRequest = _reflection.GeneratedProtocolMessageType('SearchExperimentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHEXPERIMENTSREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchExperimentsRequest)
  ))
_sym_db.RegisterMessage(SearchExperimentsRequest)

GetExperimentRequest = _reflection.GeneratedProtocolMessageType('GetExperimentRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETEXPERIMENTREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetExperimentRequest)
  ))
_sym_db.RegisterMessage(GetExperimentRequest)

SearchExperimentsResponse = _reflection.GeneratedProtocolMessageType('SearchExperimentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHEXPERIMENTSRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchExperimentsResponse)
  ))
_sym_db.RegisterMessage(SearchExperimentsResponse)

SearchAnalysesRequest = _reflection.GeneratedProtocolMessageType('SearchAnalysesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHANALYSESREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchAnalysesRequest)
  ))
_sym_db.RegisterMessage(SearchAnalysesRequest)

GetAnalysisRequest = _reflection.GeneratedProtocolMessageType('GetAnalysisRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETANALYSISREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.GetAnalysisRequest)
  ))
_sym_db.RegisterMessage(GetAnalysisRequest)

SearchAnalysesResponse = _reflection.GeneratedProtocolMessageType('SearchAnalysesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHANALYSESRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.SearchAnalysesResponse)
  ))
_sym_db.RegisterMessage(SearchAnalysesResponse)


# @@protoc_insertion_point(module_scope)
