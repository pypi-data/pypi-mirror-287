# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bitdeer/aicloud/resource/v1/resource.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*bitdeer/aicloud/resource/v1/resource.proto\x12\x1b\x62itdeer.aicloud.resource.v1\"\xc7\x01\n\x0cStorageClass\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\"\n\nclass_name\x18\x03 \x01(\tH\x00R\tclassName\x88\x01\x01\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04sort\x18\x05 \x01(\x05R\x04sort\x12*\n\x11storage_class_key\x18\x06 \x01(\tR\x0fstorageClassKeyB\r\n\x0b_class_name\"\xf9\x04\n\rSpecification\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x19\n\x08spec_key\x18\x04 \x01(\tR\x07specKey\x12!\n\x0cis_available\x18\x05 \x01(\x08R\x0bisAvailable\x12\x19\n\x08gpu_spec\x18\x06 \x01(\tR\x07gpuSpec\x12\x1b\n\tgpu_count\x18\x07 \x01(\x05R\x08gpuCount\x12%\n\x0fgpu_mem_size_mb\x18\x08 \x01(\x05R\x0cgpuMemSizeMb\x12\"\n\rcpu_core_spec\x18\t \x01(\tR\x0b\x63puCoreSpec\x12$\n\x0e\x63pu_core_count\x18\n \x01(\x05R\x0c\x63puCoreCount\x12$\n\x0ememory_size_mb\x18\x0b \x01(\x05R\x0cmemorySizeMb\x12\x12\n\x04sort\x18\x0c \x01(\x05R\x04sort\x12\x65\n\x19supported_storage_classes\x18\r \x03(\x0b\x32).bitdeer.aicloud.resource.v1.StorageClassR\x17supportedStorageClasses\x12[\n\x0bnode_labels\x18\x0e \x03(\x0b\x32:.bitdeer.aicloud.resource.v1.Specification.NodeLabelsEntryR\nnodeLabels\x1a=\n\x0fNodeLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42TZRgitlab.bitdeer.vip/mininglab/playground/gen/bitdeer/aicloud/resource/v1;resourcev1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bitdeer.aicloud.resource.v1.resource_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZRgitlab.bitdeer.vip/mininglab/playground/gen/bitdeer/aicloud/resource/v1;resourcev1'
  _globals['_SPECIFICATION_NODELABELSENTRY']._options = None
  _globals['_SPECIFICATION_NODELABELSENTRY']._serialized_options = b'8\001'
  _globals['_STORAGECLASS']._serialized_start=76
  _globals['_STORAGECLASS']._serialized_end=275
  _globals['_SPECIFICATION']._serialized_start=278
  _globals['_SPECIFICATION']._serialized_end=911
  _globals['_SPECIFICATION_NODELABELSENTRY']._serialized_start=850
  _globals['_SPECIFICATION_NODELABELSENTRY']._serialized_end=911
# @@protoc_insertion_point(module_scope)
