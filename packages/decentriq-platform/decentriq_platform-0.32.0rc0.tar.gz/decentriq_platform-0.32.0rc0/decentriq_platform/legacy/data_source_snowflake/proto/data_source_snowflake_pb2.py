# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_source_snowflake.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x64\x61ta_source_snowflake.proto\x12\x15\x64\x61ta_source_snowflake\"x\n\x0fSnowflakeSource\x12\x15\n\rwarehouseName\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x61tabaseName\x18\x02 \x01(\t\x12\x12\n\nschemaName\x18\x03 \x01(\t\x12\x11\n\ttableName\x18\x04 \x01(\t\x12\x11\n\tstageName\x18\x05 \x01(\t\"\x7f\n&DataSourceSnowflakeWorkerConfiguration\x12\x36\n\x06source\x18\x01 \x01(\x0b\x32&.data_source_snowflake.SnowflakeSource\x12\x1d\n\x15\x63redentialsDependency\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_source_snowflake_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SNOWFLAKESOURCE']._serialized_start=54
  _globals['_SNOWFLAKESOURCE']._serialized_end=174
  _globals['_DATASOURCESNOWFLAKEWORKERCONFIGURATION']._serialized_start=176
  _globals['_DATASOURCESNOWFLAKEWORKERCONFIGURATION']._serialized_end=303
# @@protoc_insertion_point(module_scope)
