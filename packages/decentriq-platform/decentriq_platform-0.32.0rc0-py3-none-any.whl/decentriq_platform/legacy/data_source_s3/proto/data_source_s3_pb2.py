# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_source_s3.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64\x61ta_source_s3.proto\x12\x0e\x64\x61ta_source_s3\"=\n\x08S3Source\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\x11\n\tobjectKey\x18\x03 \x01(\t\"\x9a\x01\n\x1f\x44\x61taSourceS3WorkerConfiguration\x12(\n\x06source\x18\x01 \x01(\x0b\x32\x18.data_source_s3.S3Source\x12\x1d\n\x15\x63redentialsDependency\x18\x02 \x01(\t\x12.\n\ns3Provider\x18\x03 \x01(\x0e\x32\x1a.data_source_s3.S3Provider*\x1e\n\nS3Provider\x12\x07\n\x03\x41WS\x10\x00\x12\x07\n\x03GCS\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_source_s3_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_S3PROVIDER']._serialized_start=260
  _globals['_S3PROVIDER']._serialized_end=290
  _globals['_S3SOURCE']._serialized_start=40
  _globals['_S3SOURCE']._serialized_end=101
  _globals['_DATASOURCES3WORKERCONFIGURATION']._serialized_start=104
  _globals['_DATASOURCES3WORKERCONFIGURATION']._serialized_end=258
# @@protoc_insertion_point(module_scope)
