# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'EntryBigqueryDateShardedSpec',
    'EntryBigqueryTableSpec',
    'EntryBigqueryTableSpecTableSpec',
    'EntryBigqueryTableSpecViewSpec',
    'EntryGcsFilesetSpec',
    'EntryGcsFilesetSpecSampleGcsFileSpec',
    'EntryGroupIamBindingCondition',
    'EntryGroupIamMemberCondition',
    'PolicyTagIamBindingCondition',
    'PolicyTagIamMemberCondition',
    'TagField',
    'TagTemplateField',
    'TagTemplateFieldType',
    'TagTemplateFieldTypeEnumType',
    'TagTemplateFieldTypeEnumTypeAllowedValue',
    'TagTemplateIamBindingCondition',
    'TagTemplateIamMemberCondition',
    'TaxonomyIamBindingCondition',
    'TaxonomyIamMemberCondition',
]

@pulumi.output_type
class EntryBigqueryDateShardedSpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "shardCount":
            suggest = "shard_count"
        elif key == "tablePrefix":
            suggest = "table_prefix"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EntryBigqueryDateShardedSpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EntryBigqueryDateShardedSpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EntryBigqueryDateShardedSpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dataset: Optional[str] = None,
                 shard_count: Optional[int] = None,
                 table_prefix: Optional[str] = None):
        """
        :param str dataset: (Output)
               The Data Catalog resource name of the dataset entry the current table belongs to, for example,
               projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}
        :param int shard_count: (Output)
               Total number of shards.
        :param str table_prefix: (Output)
               The table name prefix of the shards. The name of any given shard is [tablePrefix]YYYYMMDD,
               for example, for shard MyTable20180101, the tablePrefix is MyTable.
        """
        if dataset is not None:
            pulumi.set(__self__, "dataset", dataset)
        if shard_count is not None:
            pulumi.set(__self__, "shard_count", shard_count)
        if table_prefix is not None:
            pulumi.set(__self__, "table_prefix", table_prefix)

    @property
    @pulumi.getter
    def dataset(self) -> Optional[str]:
        """
        (Output)
        The Data Catalog resource name of the dataset entry the current table belongs to, for example,
        projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}
        """
        return pulumi.get(self, "dataset")

    @property
    @pulumi.getter(name="shardCount")
    def shard_count(self) -> Optional[int]:
        """
        (Output)
        Total number of shards.
        """
        return pulumi.get(self, "shard_count")

    @property
    @pulumi.getter(name="tablePrefix")
    def table_prefix(self) -> Optional[str]:
        """
        (Output)
        The table name prefix of the shards. The name of any given shard is [tablePrefix]YYYYMMDD,
        for example, for shard MyTable20180101, the tablePrefix is MyTable.
        """
        return pulumi.get(self, "table_prefix")


@pulumi.output_type
class EntryBigqueryTableSpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "tableSourceType":
            suggest = "table_source_type"
        elif key == "tableSpecs":
            suggest = "table_specs"
        elif key == "viewSpecs":
            suggest = "view_specs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EntryBigqueryTableSpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EntryBigqueryTableSpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EntryBigqueryTableSpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 table_source_type: Optional[str] = None,
                 table_specs: Optional[Sequence['outputs.EntryBigqueryTableSpecTableSpec']] = None,
                 view_specs: Optional[Sequence['outputs.EntryBigqueryTableSpecViewSpec']] = None):
        """
        :param str table_source_type: (Output)
               The table source type.
        :param Sequence['EntryBigqueryTableSpecTableSpecArgs'] table_specs: (Output)
               Spec of a BigQuery table. This field should only be populated if tableSourceType is BIGQUERY_TABLE.
               Structure is documented below.
        :param Sequence['EntryBigqueryTableSpecViewSpecArgs'] view_specs: (Output)
               Table view specification. This field should only be populated if tableSourceType is BIGQUERY_VIEW.
               Structure is documented below.
        """
        if table_source_type is not None:
            pulumi.set(__self__, "table_source_type", table_source_type)
        if table_specs is not None:
            pulumi.set(__self__, "table_specs", table_specs)
        if view_specs is not None:
            pulumi.set(__self__, "view_specs", view_specs)

    @property
    @pulumi.getter(name="tableSourceType")
    def table_source_type(self) -> Optional[str]:
        """
        (Output)
        The table source type.
        """
        return pulumi.get(self, "table_source_type")

    @property
    @pulumi.getter(name="tableSpecs")
    def table_specs(self) -> Optional[Sequence['outputs.EntryBigqueryTableSpecTableSpec']]:
        """
        (Output)
        Spec of a BigQuery table. This field should only be populated if tableSourceType is BIGQUERY_TABLE.
        Structure is documented below.
        """
        return pulumi.get(self, "table_specs")

    @property
    @pulumi.getter(name="viewSpecs")
    def view_specs(self) -> Optional[Sequence['outputs.EntryBigqueryTableSpecViewSpec']]:
        """
        (Output)
        Table view specification. This field should only be populated if tableSourceType is BIGQUERY_VIEW.
        Structure is documented below.
        """
        return pulumi.get(self, "view_specs")


@pulumi.output_type
class EntryBigqueryTableSpecTableSpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupedEntry":
            suggest = "grouped_entry"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EntryBigqueryTableSpecTableSpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EntryBigqueryTableSpecTableSpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EntryBigqueryTableSpecTableSpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 grouped_entry: Optional[str] = None):
        """
        :param str grouped_entry: (Output)
               If the table is a dated shard, i.e., with name pattern [prefix]YYYYMMDD, groupedEntry is the
               Data Catalog resource name of the date sharded grouped entry, for example,
               projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}.
               Otherwise, groupedEntry is empty.
        """
        if grouped_entry is not None:
            pulumi.set(__self__, "grouped_entry", grouped_entry)

    @property
    @pulumi.getter(name="groupedEntry")
    def grouped_entry(self) -> Optional[str]:
        """
        (Output)
        If the table is a dated shard, i.e., with name pattern [prefix]YYYYMMDD, groupedEntry is the
        Data Catalog resource name of the date sharded grouped entry, for example,
        projects/{project_id}/locations/{location}/entrygroups/{entryGroupId}/entries/{entryId}.
        Otherwise, groupedEntry is empty.
        """
        return pulumi.get(self, "grouped_entry")


@pulumi.output_type
class EntryBigqueryTableSpecViewSpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "viewQuery":
            suggest = "view_query"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EntryBigqueryTableSpecViewSpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EntryBigqueryTableSpecViewSpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EntryBigqueryTableSpecViewSpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 view_query: Optional[str] = None):
        """
        :param str view_query: (Output)
               The query that defines the table view.
        """
        if view_query is not None:
            pulumi.set(__self__, "view_query", view_query)

    @property
    @pulumi.getter(name="viewQuery")
    def view_query(self) -> Optional[str]:
        """
        (Output)
        The query that defines the table view.
        """
        return pulumi.get(self, "view_query")


@pulumi.output_type
class EntryGcsFilesetSpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "filePatterns":
            suggest = "file_patterns"
        elif key == "sampleGcsFileSpecs":
            suggest = "sample_gcs_file_specs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EntryGcsFilesetSpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EntryGcsFilesetSpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EntryGcsFilesetSpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 file_patterns: Sequence[str],
                 sample_gcs_file_specs: Optional[Sequence['outputs.EntryGcsFilesetSpecSampleGcsFileSpec']] = None):
        """
        :param Sequence[str] file_patterns: Patterns to identify a set of files in Google Cloud Storage.
               See [Cloud Storage documentation](https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames)
               for more information. Note that bucket wildcards are currently not supported. Examples of valid filePatterns:
               * gs://bucket_name/dir/*: matches all files within bucket_name/dir directory.
               * gs://bucket_name/dir/**: matches all files in bucket_name/dir spanning all subdirectories.
               * gs://bucket_name/file*: matches files prefixed by file in bucket_name
               * gs://bucket_name/??.txt: matches files with two characters followed by .txt in bucket_name
               * gs://bucket_name/[aeiou].txt: matches files that contain a single vowel character followed by .txt in bucket_name
               * gs://bucket_name/[a-m].txt: matches files that contain a, b, ... or m followed by .txt in bucket_name
               * gs://bucket_name/a/*/b: matches all files in bucket_name that match a/*/b pattern, such as a/c/b, a/d/b
               * gs://another_bucket/a.txt: matches gs://another_bucket/a.txt
        :param Sequence['EntryGcsFilesetSpecSampleGcsFileSpecArgs'] sample_gcs_file_specs: (Output)
               Sample files contained in this fileset, not all files contained in this fileset are represented here.
               Structure is documented below.
               
               
               <a name="nested_sample_gcs_file_specs"></a>The `sample_gcs_file_specs` block contains:
        """
        pulumi.set(__self__, "file_patterns", file_patterns)
        if sample_gcs_file_specs is not None:
            pulumi.set(__self__, "sample_gcs_file_specs", sample_gcs_file_specs)

    @property
    @pulumi.getter(name="filePatterns")
    def file_patterns(self) -> Sequence[str]:
        """
        Patterns to identify a set of files in Google Cloud Storage.
        See [Cloud Storage documentation](https://cloud.google.com/storage/docs/gsutil/addlhelp/WildcardNames)
        for more information. Note that bucket wildcards are currently not supported. Examples of valid filePatterns:
        * gs://bucket_name/dir/*: matches all files within bucket_name/dir directory.
        * gs://bucket_name/dir/**: matches all files in bucket_name/dir spanning all subdirectories.
        * gs://bucket_name/file*: matches files prefixed by file in bucket_name
        * gs://bucket_name/??.txt: matches files with two characters followed by .txt in bucket_name
        * gs://bucket_name/[aeiou].txt: matches files that contain a single vowel character followed by .txt in bucket_name
        * gs://bucket_name/[a-m].txt: matches files that contain a, b, ... or m followed by .txt in bucket_name
        * gs://bucket_name/a/*/b: matches all files in bucket_name that match a/*/b pattern, such as a/c/b, a/d/b
        * gs://another_bucket/a.txt: matches gs://another_bucket/a.txt
        """
        return pulumi.get(self, "file_patterns")

    @property
    @pulumi.getter(name="sampleGcsFileSpecs")
    def sample_gcs_file_specs(self) -> Optional[Sequence['outputs.EntryGcsFilesetSpecSampleGcsFileSpec']]:
        """
        (Output)
        Sample files contained in this fileset, not all files contained in this fileset are represented here.
        Structure is documented below.


        <a name="nested_sample_gcs_file_specs"></a>The `sample_gcs_file_specs` block contains:
        """
        return pulumi.get(self, "sample_gcs_file_specs")


@pulumi.output_type
class EntryGcsFilesetSpecSampleGcsFileSpec(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "filePath":
            suggest = "file_path"
        elif key == "sizeBytes":
            suggest = "size_bytes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EntryGcsFilesetSpecSampleGcsFileSpec. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EntryGcsFilesetSpecSampleGcsFileSpec.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EntryGcsFilesetSpecSampleGcsFileSpec.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 file_path: Optional[str] = None,
                 size_bytes: Optional[int] = None):
        """
        :param str file_path: The full file path
        :param int size_bytes: The size of the file, in bytes.
        """
        if file_path is not None:
            pulumi.set(__self__, "file_path", file_path)
        if size_bytes is not None:
            pulumi.set(__self__, "size_bytes", size_bytes)

    @property
    @pulumi.getter(name="filePath")
    def file_path(self) -> Optional[str]:
        """
        The full file path
        """
        return pulumi.get(self, "file_path")

    @property
    @pulumi.getter(name="sizeBytes")
    def size_bytes(self) -> Optional[int]:
        """
        The size of the file, in bytes.
        """
        return pulumi.get(self, "size_bytes")


@pulumi.output_type
class EntryGroupIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class EntryGroupIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class PolicyTagIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class PolicyTagIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class TagField(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fieldName":
            suggest = "field_name"
        elif key == "boolValue":
            suggest = "bool_value"
        elif key == "displayName":
            suggest = "display_name"
        elif key == "doubleValue":
            suggest = "double_value"
        elif key == "enumValue":
            suggest = "enum_value"
        elif key == "stringValue":
            suggest = "string_value"
        elif key == "timestampValue":
            suggest = "timestamp_value"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TagField. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TagField.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TagField.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 field_name: str,
                 bool_value: Optional[bool] = None,
                 display_name: Optional[str] = None,
                 double_value: Optional[float] = None,
                 enum_value: Optional[str] = None,
                 order: Optional[int] = None,
                 string_value: Optional[str] = None,
                 timestamp_value: Optional[str] = None):
        """
        :param str field_name: The identifier for this object. Format specified above.
        :param bool bool_value: Holds the value for a tag field with boolean type.
        :param str display_name: (Output)
               The display name of this field
        :param float double_value: Holds the value for a tag field with double type.
        :param str enum_value: Holds the value for a tag field with enum type. This value must be one of the allowed values in the definition of this enum.
               
               - - -
        :param int order: (Output)
               The order of this field with respect to other fields in this tag. For example, a higher value can indicate
               a more important field. The value can be negative. Multiple fields can have the same order, and field orders
               within a tag do not have to be sequential.
        :param str string_value: Holds the value for a tag field with string type.
        :param str timestamp_value: Holds the value for a tag field with timestamp type.
        """
        pulumi.set(__self__, "field_name", field_name)
        if bool_value is not None:
            pulumi.set(__self__, "bool_value", bool_value)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if double_value is not None:
            pulumi.set(__self__, "double_value", double_value)
        if enum_value is not None:
            pulumi.set(__self__, "enum_value", enum_value)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if string_value is not None:
            pulumi.set(__self__, "string_value", string_value)
        if timestamp_value is not None:
            pulumi.set(__self__, "timestamp_value", timestamp_value)

    @property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> str:
        """
        The identifier for this object. Format specified above.
        """
        return pulumi.get(self, "field_name")

    @property
    @pulumi.getter(name="boolValue")
    def bool_value(self) -> Optional[bool]:
        """
        Holds the value for a tag field with boolean type.
        """
        return pulumi.get(self, "bool_value")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        (Output)
        The display name of this field
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="doubleValue")
    def double_value(self) -> Optional[float]:
        """
        Holds the value for a tag field with double type.
        """
        return pulumi.get(self, "double_value")

    @property
    @pulumi.getter(name="enumValue")
    def enum_value(self) -> Optional[str]:
        """
        Holds the value for a tag field with enum type. This value must be one of the allowed values in the definition of this enum.

        - - -
        """
        return pulumi.get(self, "enum_value")

    @property
    @pulumi.getter
    def order(self) -> Optional[int]:
        """
        (Output)
        The order of this field with respect to other fields in this tag. For example, a higher value can indicate
        a more important field. The value can be negative. Multiple fields can have the same order, and field orders
        within a tag do not have to be sequential.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="stringValue")
    def string_value(self) -> Optional[str]:
        """
        Holds the value for a tag field with string type.
        """
        return pulumi.get(self, "string_value")

    @property
    @pulumi.getter(name="timestampValue")
    def timestamp_value(self) -> Optional[str]:
        """
        Holds the value for a tag field with timestamp type.
        """
        return pulumi.get(self, "timestamp_value")


@pulumi.output_type
class TagTemplateField(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fieldId":
            suggest = "field_id"
        elif key == "displayName":
            suggest = "display_name"
        elif key == "isRequired":
            suggest = "is_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TagTemplateField. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TagTemplateField.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TagTemplateField.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 field_id: str,
                 type: 'outputs.TagTemplateFieldType',
                 description: Optional[str] = None,
                 display_name: Optional[str] = None,
                 is_required: Optional[bool] = None,
                 name: Optional[str] = None,
                 order: Optional[int] = None):
        """
        :param str field_id: The identifier for this object. Format specified above.
        :param 'TagTemplateFieldTypeArgs' type: The type of value this tag field can contain.
               Structure is documented below.
        :param str description: A description for this field.
        :param str display_name: The display name for this field.
        :param bool is_required: Whether this is a required field. Defaults to false.
        :param str name: (Output)
               The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}
        :param int order: The order of this field with respect to other fields in this tag template.
               A higher value indicates a more important field. The value can be negative.
               Multiple fields can have the same order, and field orders within a tag do not have to be sequential.
        """
        pulumi.set(__self__, "field_id", field_id)
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if is_required is not None:
            pulumi.set(__self__, "is_required", is_required)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order is not None:
            pulumi.set(__self__, "order", order)

    @property
    @pulumi.getter(name="fieldId")
    def field_id(self) -> str:
        """
        The identifier for this object. Format specified above.
        """
        return pulumi.get(self, "field_id")

    @property
    @pulumi.getter
    def type(self) -> 'outputs.TagTemplateFieldType':
        """
        The type of value this tag field can contain.
        Structure is documented below.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for this field.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name for this field.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="isRequired")
    def is_required(self) -> Optional[bool]:
        """
        Whether this is a required field. Defaults to false.
        """
        return pulumi.get(self, "is_required")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        (Output)
        The resource name of the tag template field in URL format. Example: projects/{project_id}/locations/{location}/tagTemplates/{tagTemplateId}/fields/{field}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def order(self) -> Optional[int]:
        """
        The order of this field with respect to other fields in this tag template.
        A higher value indicates a more important field. The value can be negative.
        Multiple fields can have the same order, and field orders within a tag do not have to be sequential.
        """
        return pulumi.get(self, "order")


@pulumi.output_type
class TagTemplateFieldType(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enumType":
            suggest = "enum_type"
        elif key == "primitiveType":
            suggest = "primitive_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TagTemplateFieldType. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TagTemplateFieldType.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TagTemplateFieldType.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enum_type: Optional['outputs.TagTemplateFieldTypeEnumType'] = None,
                 primitive_type: Optional[str] = None):
        """
        :param 'TagTemplateFieldTypeEnumTypeArgs' enum_type: Represents an enum type.
               Exactly one of `primitive_type` or `enum_type` must be set
               Structure is documented below.
        :param str primitive_type: Represents primitive types - string, bool etc.
               Exactly one of `primitive_type` or `enum_type` must be set
               Possible values are: `DOUBLE`, `STRING`, `BOOL`, `TIMESTAMP`.
        """
        if enum_type is not None:
            pulumi.set(__self__, "enum_type", enum_type)
        if primitive_type is not None:
            pulumi.set(__self__, "primitive_type", primitive_type)

    @property
    @pulumi.getter(name="enumType")
    def enum_type(self) -> Optional['outputs.TagTemplateFieldTypeEnumType']:
        """
        Represents an enum type.
        Exactly one of `primitive_type` or `enum_type` must be set
        Structure is documented below.
        """
        return pulumi.get(self, "enum_type")

    @property
    @pulumi.getter(name="primitiveType")
    def primitive_type(self) -> Optional[str]:
        """
        Represents primitive types - string, bool etc.
        Exactly one of `primitive_type` or `enum_type` must be set
        Possible values are: `DOUBLE`, `STRING`, `BOOL`, `TIMESTAMP`.
        """
        return pulumi.get(self, "primitive_type")


@pulumi.output_type
class TagTemplateFieldTypeEnumType(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedValues":
            suggest = "allowed_values"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TagTemplateFieldTypeEnumType. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TagTemplateFieldTypeEnumType.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TagTemplateFieldTypeEnumType.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_values: Sequence['outputs.TagTemplateFieldTypeEnumTypeAllowedValue']):
        """
        :param Sequence['TagTemplateFieldTypeEnumTypeAllowedValueArgs'] allowed_values: The set of allowed values for this enum. The display names of the
               values must be case-insensitively unique within this set. Currently,
               enum values can only be added to the list of allowed values. Deletion
               and renaming of enum values are not supported.
               Can have up to 500 allowed values.
               Structure is documented below.
        """
        pulumi.set(__self__, "allowed_values", allowed_values)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Sequence['outputs.TagTemplateFieldTypeEnumTypeAllowedValue']:
        """
        The set of allowed values for this enum. The display names of the
        values must be case-insensitively unique within this set. Currently,
        enum values can only be added to the list of allowed values. Deletion
        and renaming of enum values are not supported.
        Can have up to 500 allowed values.
        Structure is documented below.
        """
        return pulumi.get(self, "allowed_values")


@pulumi.output_type
class TagTemplateFieldTypeEnumTypeAllowedValue(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayName":
            suggest = "display_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TagTemplateFieldTypeEnumTypeAllowedValue. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TagTemplateFieldTypeEnumTypeAllowedValue.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TagTemplateFieldTypeEnumTypeAllowedValue.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 display_name: str):
        """
        :param str display_name: The display name for this template.
        """
        pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name for this template.
        """
        return pulumi.get(self, "display_name")


@pulumi.output_type
class TagTemplateIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class TagTemplateIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class TaxonomyIamBindingCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


@pulumi.output_type
class TaxonomyIamMemberCondition(dict):
    def __init__(__self__, *,
                 expression: str,
                 title: str,
                 description: Optional[str] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> str:
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def title(self) -> str:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")


