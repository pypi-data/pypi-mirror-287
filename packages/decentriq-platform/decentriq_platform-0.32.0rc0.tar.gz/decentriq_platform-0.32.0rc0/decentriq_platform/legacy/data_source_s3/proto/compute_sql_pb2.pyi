"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PrimitiveType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _PrimitiveTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PrimitiveType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INT64: _PrimitiveType.ValueType  # 0
    STRING: _PrimitiveType.ValueType  # 1
    FLOAT64: _PrimitiveType.ValueType  # 2
class PrimitiveType(_PrimitiveType, metaclass=_PrimitiveTypeEnumTypeWrapper):
    pass

INT64: PrimitiveType.ValueType  # 0
STRING: PrimitiveType.ValueType  # 1
FLOAT64: PrimitiveType.ValueType  # 2
global___PrimitiveType = PrimitiveType


class SqlWorkerConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALIDATION_FIELD_NUMBER: builtins.int
    COMPUTATION_FIELD_NUMBER: builtins.int
    @property
    def validation(self) -> global___ValidationConfiguration: ...
    @property
    def computation(self) -> global___ComputationConfiguration: ...
    def __init__(self,
        *,
        validation: typing.Optional[global___ValidationConfiguration] = ...,
        computation: typing.Optional[global___ComputationConfiguration] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["computation",b"computation","configuration",b"configuration","validation",b"validation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["computation",b"computation","configuration",b"configuration","validation",b"validation"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["configuration",b"configuration"]) -> typing.Optional[typing_extensions.Literal["validation","computation"]]: ...
global___SqlWorkerConfiguration = SqlWorkerConfiguration

class ValidationConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLESCHEMA_FIELD_NUMBER: builtins.int
    @property
    def tableSchema(self) -> global___TableSchema: ...
    def __init__(self,
        *,
        tableSchema: typing.Optional[global___TableSchema] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tableSchema",b"tableSchema"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["tableSchema",b"tableSchema"]) -> None: ...
global___ValidationConfiguration = ValidationConfiguration

class TableSchema(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMEDCOLUMNS_FIELD_NUMBER: builtins.int
    @property
    def namedColumns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NamedColumn]: ...
    def __init__(self,
        *,
        namedColumns: typing.Optional[typing.Iterable[global___NamedColumn]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["namedColumns",b"namedColumns"]) -> None: ...
global___TableSchema = TableSchema

class NamedColumn(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    COLUMNTYPE_FIELD_NUMBER: builtins.int
    name: typing.Text
    @property
    def columnType(self) -> global___ColumnType: ...
    def __init__(self,
        *,
        name: typing.Optional[typing.Text] = ...,
        columnType: typing.Optional[global___ColumnType] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_name",b"_name","columnType",b"columnType","name",b"name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_name",b"_name","columnType",b"columnType","name",b"name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_name",b"_name"]) -> typing.Optional[typing_extensions.Literal["name"]]: ...
global___NamedColumn = NamedColumn

class ColumnType(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PRIMITIVETYPE_FIELD_NUMBER: builtins.int
    NULLABLE_FIELD_NUMBER: builtins.int
    primitiveType: global___PrimitiveType.ValueType
    nullable: builtins.bool
    def __init__(self,
        *,
        primitiveType: global___PrimitiveType.ValueType = ...,
        nullable: builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nullable",b"nullable","primitiveType",b"primitiveType"]) -> None: ...
global___ColumnType = ColumnType

class TableDependencyMapping(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TABLE_FIELD_NUMBER: builtins.int
    DEPENDENCY_FIELD_NUMBER: builtins.int
    table: typing.Text
    """Name of the table as it appears in the SQL query string"""

    dependency: typing.Text
    """ID of the compute/data node that provides data for this table"""

    def __init__(self,
        *,
        table: typing.Text = ...,
        dependency: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dependency",b"dependency","table",b"table"]) -> None: ...
global___TableDependencyMapping = TableDependencyMapping

class ComputationConfiguration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SQLSTATEMENT_FIELD_NUMBER: builtins.int
    PRIVACYSETTINGS_FIELD_NUMBER: builtins.int
    CONSTRAINTS_FIELD_NUMBER: builtins.int
    TABLEDEPENDENCYMAPPINGS_FIELD_NUMBER: builtins.int
    sqlStatement: typing.Text
    @property
    def privacySettings(self) -> global___PrivacySettings: ...
    @property
    def constraints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Constraint]: ...
    @property
    def tableDependencyMappings(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TableDependencyMapping]: ...
    def __init__(self,
        *,
        sqlStatement: typing.Text = ...,
        privacySettings: typing.Optional[global___PrivacySettings] = ...,
        constraints: typing.Optional[typing.Iterable[global___Constraint]] = ...,
        tableDependencyMappings: typing.Optional[typing.Iterable[global___TableDependencyMapping]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["privacySettings",b"privacySettings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["constraints",b"constraints","privacySettings",b"privacySettings","sqlStatement",b"sqlStatement","tableDependencyMappings",b"tableDependencyMappings"]) -> None: ...
global___ComputationConfiguration = ComputationConfiguration

class PrivacySettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MINAGGREGATIONGROUPSIZE_FIELD_NUMBER: builtins.int
    minAggregationGroupSize: builtins.int
    def __init__(self,
        *,
        minAggregationGroupSize: builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["minAggregationGroupSize",b"minAggregationGroupSize"]) -> None: ...
global___PrivacySettings = PrivacySettings

class Constraint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DESCRIPTION_FIELD_NUMBER: builtins.int
    description: typing.Text
    def __init__(self,
        *,
        description: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description",b"description"]) -> None: ...
global___Constraint = Constraint
