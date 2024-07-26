# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/knowledgebox.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nucliadb_protos import utils_pb2 as nucliadb__protos_dot_utils__pb2
from nucliadb_protos import nodewriter_pb2 as nucliadb__protos_dot_nodewriter__pb2
try:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodewriter__pb2.nucliadb__protos_dot_noderesources__pb2
except AttributeError:
  nucliadb__protos_dot_noderesources__pb2 = nucliadb__protos_dot_nodewriter__pb2.nucliadb_protos.noderesources_pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodewriter__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_nodewriter__pb2.nucliadb_protos.utils_pb2

from nucliadb_protos.utils_pb2 import *
from nucliadb_protos.nodewriter_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"nucliadb_protos/knowledgebox.proto\x12\x0cknowledgebox\x1a\x1bnucliadb_protos/utils.proto\x1a nucliadb_protos/nodewriter.proto\",\n\x0eKnowledgeBoxID\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"\'\n\x14\x43reatePineconeConfig\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\"\xad\x01\n\x14StoredPineconeConfig\x12\x19\n\x11\x65ncrypted_api_key\x18\x01 \x01(\t\x12G\n\x0bindex_hosts\x18\x02 \x03(\x0b\x32\x32.knowledgebox.StoredPineconeConfig.IndexHostsEntry\x1a\x31\n\x0fIndexHostsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa5\x01\n#CreateExternalIndexProviderMetadata\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.knowledgebox.ExternalIndexProviderType\x12=\n\x0fpinecone_config\x18\x02 \x01(\x0b\x32\".knowledgebox.CreatePineconeConfigH\x00\x42\x08\n\x06\x63onfig\"\xa5\x01\n#StoredExternalIndexProviderMetadata\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.knowledgebox.ExternalIndexProviderType\x12=\n\x0fpinecone_config\x18\x02 \x01(\x0b\x32\".knowledgebox.StoredPineconeConfigH\x00\x42\x08\n\x06\x63onfig\"\xc1\x02\n\x12KnowledgeBoxConfig\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0c\n\x04slug\x18\x05 \x01(\t\x12\x19\n\x11migration_version\x18\x07 \x01(\x03\x12R\n\x17\x65xternal_index_provider\x18\t \x01(\x0b\x32\x31.knowledgebox.StoredExternalIndexProviderMetadata\x12\x1b\n\x0f\x65nabled_filters\x18\x03 \x03(\tB\x02\x18\x01\x12\x1c\n\x10\x65nabled_insights\x18\x04 \x03(\tB\x02\x18\x01\x12\x1b\n\x0f\x64isable_vectors\x18\x06 \x01(\x08\x42\x02\x18\x01\x12\x32\n\x0frelease_channel\x18\x08 \x01(\x0e\x32\x15.utils.ReleaseChannelB\x02\x18\x01\"\xbf\x03\n\x0fKnowledgeBoxNew\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x30\n\x06\x63onfig\x18\x02 \x01(\x0b\x32 .knowledgebox.KnowledgeBoxConfig\x12\x11\n\tforceuuid\x18\x03 \x01(\t\x12+\n\nsimilarity\x18\x04 \x01(\x0e\x32\x17.utils.VectorSimilarity\x12\x1d\n\x10vector_dimension\x18\x05 \x01(\x05H\x00\x88\x01\x01\x12\"\n\x11\x64\x65\x66\x61ult_min_score\x18\x06 \x01(\x02\x42\x02\x18\x01H\x01\x88\x01\x01\x12\x1d\n\x15matryoshka_dimensions\x18\t \x03(\r\x12R\n\x17\x65xternal_index_provider\x18\n \x01(\x0b\x32\x31.knowledgebox.CreateExternalIndexProviderMetadata\x12\x1b\n\x0flearning_config\x18\x08 \x01(\tB\x02\x18\x01\x12.\n\x0frelease_channel\x18\x07 \x01(\x0e\x32\x15.utils.ReleaseChannelB\x13\n\x11_vector_dimensionB\x14\n\x12_default_min_score\"a\n\x17NewKnowledgeBoxResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.knowledgebox.KnowledgeBoxResponseStatus\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"b\n\x12KnowledgeBoxUpdate\x12\x0c\n\x04slug\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x30\n\x06\x63onfig\x18\x03 \x01(\x0b\x32 .knowledgebox.KnowledgeBoxConfig\"d\n\x1aUpdateKnowledgeBoxResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.knowledgebox.KnowledgeBoxResponseStatus\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"V\n\x1a\x44\x65leteKnowledgeBoxResponse\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.knowledgebox.KnowledgeBoxResponseStatus\"B\n\x05Label\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07related\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x0b\n\x03uri\x18\x05 \x01(\t\"\xe0\x01\n\x08LabelSet\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12#\n\x06labels\x18\x03 \x03(\x0b\x32\x13.knowledgebox.Label\x12\x10\n\x08multiple\x18\x04 \x01(\x08\x12\x31\n\x04kind\x18\x05 \x03(\x0e\x32#.knowledgebox.LabelSet.LabelSetKind\"L\n\x0cLabelSetKind\x12\r\n\tRESOURCES\x10\x00\x12\x0e\n\nPARAGRAPHS\x10\x01\x12\r\n\tSENTENCES\x10\x02\x12\x0e\n\nSELECTIONS\x10\x03\"\x87\x01\n\x06Labels\x12\x34\n\x08labelset\x18\x01 \x03(\x0b\x32\".knowledgebox.Labels.LabelsetEntry\x1aG\n\rLabelsetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.knowledgebox.LabelSet:\x02\x38\x01\"L\n\x06\x45ntity\x12\r\n\x05value\x18\x02 \x01(\t\x12\x12\n\nrepresents\x18\x04 \x03(\t\x12\x0e\n\x06merged\x18\x03 \x01(\x08\x12\x0f\n\x07\x64\x65leted\x18\x05 \x01(\x08\"D\n\x14\x45ntitiesGroupSummary\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\x0e\n\x06\x63ustom\x18\x04 \x01(\x08\"\xc1\x01\n\rEntitiesGroup\x12;\n\x08\x65ntities\x18\x01 \x03(\x0b\x32).knowledgebox.EntitiesGroup.EntitiesEntry\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\x0e\n\x06\x63ustom\x18\x04 \x01(\x08\x1a\x45\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.knowledgebox.Entity:\x02\x38\x01\"0\n\x15\x44\x65letedEntitiesGroups\x12\x17\n\x0f\x65ntities_groups\x18\x01 \x03(\t\"\xaf\x01\n\x0e\x45ntitiesGroups\x12I\n\x0f\x65ntities_groups\x18\x01 \x03(\x0b\x32\x30.knowledgebox.EntitiesGroups.EntitiesGroupsEntry\x1aR\n\x13\x45ntitiesGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.knowledgebox.EntitiesGroup:\x02\x38\x01\"\xf3\x03\n\x19\x45ntityGroupDuplicateIndex\x12T\n\x0f\x65ntities_groups\x18\x01 \x03(\x0b\x32;.knowledgebox.EntityGroupDuplicateIndex.EntitiesGroupsEntry\x1a&\n\x10\x45ntityDuplicates\x12\x12\n\nduplicates\x18\x01 \x03(\t\x1a\xe1\x01\n\x15\x45ntityGroupDuplicates\x12]\n\x08\x65ntities\x18\x01 \x03(\x0b\x32K.knowledgebox.EntityGroupDuplicateIndex.EntityGroupDuplicates.EntitiesEntry\x1ai\n\rEntitiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12G\n\x05value\x18\x02 \x01(\x0b\x32\x38.knowledgebox.EntityGroupDuplicateIndex.EntityDuplicates:\x02\x38\x01\x1at\n\x13\x45ntitiesGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12L\n\x05value\x18\x02 \x01(\x0b\x32=.knowledgebox.EntityGroupDuplicateIndex.EntityGroupDuplicates:\x02\x38\x01\"K\n\tVectorSet\x12\x11\n\tdimension\x18\x01 \x01(\x05\x12+\n\nsimilarity\x18\x02 \x01(\x0e\x32\x17.utils.VectorSimilarity\"\x96\x01\n\nVectorSets\x12<\n\nvectorsets\x18\x01 \x03(\x0b\x32(.knowledgebox.VectorSets.VectorsetsEntry\x1aJ\n\x0fVectorsetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.knowledgebox.VectorSet:\x02\x38\x01\"\x85\x01\n\x0fVectorSetConfig\x12\x14\n\x0cvectorset_id\x18\x01 \x01(\t\x12=\n\x16vectorset_index_config\x18\x02 \x01(\x0b\x32\x1d.nodewriter.VectorIndexConfig\x12\x1d\n\x15matryoshka_dimensions\x18\x03 \x03(\r\"Q\n\x1cKnowledgeBoxVectorSetsConfig\x12\x31\n\nvectorsets\x18\x01 \x03(\x0b\x32\x1d.knowledgebox.VectorSetConfig\" \n\x0cTermSynonyms\x12\x10\n\x08synonyms\x18\x01 \x03(\t\"\x86\x01\n\x08Synonyms\x12\x30\n\x05terms\x18\x01 \x03(\x0b\x32!.knowledgebox.Synonyms.TermsEntry\x1aH\n\nTermsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.knowledgebox.TermSynonyms:\x02\x38\x01\"\xda\x01\n\x15SemanticModelMetadata\x12\x34\n\x13similarity_function\x18\x01 \x01(\x0e\x32\x17.utils.VectorSimilarity\x12\x1d\n\x10vector_dimension\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\"\n\x11\x64\x65\x66\x61ult_min_score\x18\x03 \x01(\x02\x42\x02\x18\x01H\x01\x88\x01\x01\x12\x1d\n\x15matryoshka_dimensions\x18\x04 \x03(\rB\x13\n\x11_vector_dimensionB\x14\n\x12_default_min_score\"\x8c\x01\n\x0fKBConfiguration\x12\x16\n\x0esemantic_model\x18\x02 \x01(\t\x12\x18\n\x10generative_model\x18\x03 \x01(\t\x12\x11\n\tner_model\x18\x04 \x01(\t\x12\x1b\n\x13\x61nonymization_model\x18\x05 \x01(\t\x12\x17\n\x0fvisual_labeling\x18\x06 \x01(\t*K\n\x1aKnowledgeBoxResponseStatus\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08\x43ONFLICT\x10\x01\x12\x0c\n\x08NOTFOUND\x10\x02\x12\t\n\x05\x45RROR\x10\x03*4\n\x19\x45xternalIndexProviderType\x12\t\n\x05UNSET\x10\x00\x12\x0c\n\x08PINECONE\x10\x01P\x00P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.knowledgebox_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STOREDPINECONECONFIG_INDEXHOSTSENTRY']._options = None
  _globals['_STOREDPINECONECONFIG_INDEXHOSTSENTRY']._serialized_options = b'8\001'
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['enabled_filters']._options = None
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['enabled_filters']._serialized_options = b'\030\001'
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['enabled_insights']._options = None
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['enabled_insights']._serialized_options = b'\030\001'
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['disable_vectors']._options = None
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['disable_vectors']._serialized_options = b'\030\001'
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['release_channel']._options = None
  _globals['_KNOWLEDGEBOXCONFIG'].fields_by_name['release_channel']._serialized_options = b'\030\001'
  _globals['_KNOWLEDGEBOXNEW'].fields_by_name['default_min_score']._options = None
  _globals['_KNOWLEDGEBOXNEW'].fields_by_name['default_min_score']._serialized_options = b'\030\001'
  _globals['_KNOWLEDGEBOXNEW'].fields_by_name['learning_config']._options = None
  _globals['_KNOWLEDGEBOXNEW'].fields_by_name['learning_config']._serialized_options = b'\030\001'
  _globals['_LABELS_LABELSETENTRY']._options = None
  _globals['_LABELS_LABELSETENTRY']._serialized_options = b'8\001'
  _globals['_ENTITIESGROUP_ENTITIESENTRY']._options = None
  _globals['_ENTITIESGROUP_ENTITIESENTRY']._serialized_options = b'8\001'
  _globals['_ENTITIESGROUPS_ENTITIESGROUPSENTRY']._options = None
  _globals['_ENTITIESGROUPS_ENTITIESGROUPSENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYGROUPDUPLICATES_ENTITIESENTRY']._options = None
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYGROUPDUPLICATES_ENTITIESENTRY']._serialized_options = b'8\001'
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITIESGROUPSENTRY']._options = None
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITIESGROUPSENTRY']._serialized_options = b'8\001'
  _globals['_VECTORSETS_VECTORSETSENTRY']._options = None
  _globals['_VECTORSETS_VECTORSETSENTRY']._serialized_options = b'8\001'
  _globals['_SYNONYMS_TERMSENTRY']._options = None
  _globals['_SYNONYMS_TERMSENTRY']._serialized_options = b'8\001'
  _globals['_SEMANTICMODELMETADATA'].fields_by_name['default_min_score']._options = None
  _globals['_SEMANTICMODELMETADATA'].fields_by_name['default_min_score']._serialized_options = b'\030\001'
  _globals['_KNOWLEDGEBOXRESPONSESTATUS']._serialized_start=4368
  _globals['_KNOWLEDGEBOXRESPONSESTATUS']._serialized_end=4443
  _globals['_EXTERNALINDEXPROVIDERTYPE']._serialized_start=4445
  _globals['_EXTERNALINDEXPROVIDERTYPE']._serialized_end=4497
  _globals['_KNOWLEDGEBOXID']._serialized_start=115
  _globals['_KNOWLEDGEBOXID']._serialized_end=159
  _globals['_CREATEPINECONECONFIG']._serialized_start=161
  _globals['_CREATEPINECONECONFIG']._serialized_end=200
  _globals['_STOREDPINECONECONFIG']._serialized_start=203
  _globals['_STOREDPINECONECONFIG']._serialized_end=376
  _globals['_STOREDPINECONECONFIG_INDEXHOSTSENTRY']._serialized_start=327
  _globals['_STOREDPINECONECONFIG_INDEXHOSTSENTRY']._serialized_end=376
  _globals['_CREATEEXTERNALINDEXPROVIDERMETADATA']._serialized_start=379
  _globals['_CREATEEXTERNALINDEXPROVIDERMETADATA']._serialized_end=544
  _globals['_STOREDEXTERNALINDEXPROVIDERMETADATA']._serialized_start=547
  _globals['_STOREDEXTERNALINDEXPROVIDERMETADATA']._serialized_end=712
  _globals['_KNOWLEDGEBOXCONFIG']._serialized_start=715
  _globals['_KNOWLEDGEBOXCONFIG']._serialized_end=1036
  _globals['_KNOWLEDGEBOXNEW']._serialized_start=1039
  _globals['_KNOWLEDGEBOXNEW']._serialized_end=1486
  _globals['_NEWKNOWLEDGEBOXRESPONSE']._serialized_start=1488
  _globals['_NEWKNOWLEDGEBOXRESPONSE']._serialized_end=1585
  _globals['_KNOWLEDGEBOXUPDATE']._serialized_start=1587
  _globals['_KNOWLEDGEBOXUPDATE']._serialized_end=1685
  _globals['_UPDATEKNOWLEDGEBOXRESPONSE']._serialized_start=1687
  _globals['_UPDATEKNOWLEDGEBOXRESPONSE']._serialized_end=1787
  _globals['_DELETEKNOWLEDGEBOXRESPONSE']._serialized_start=1789
  _globals['_DELETEKNOWLEDGEBOXRESPONSE']._serialized_end=1875
  _globals['_LABEL']._serialized_start=1877
  _globals['_LABEL']._serialized_end=1943
  _globals['_LABELSET']._serialized_start=1946
  _globals['_LABELSET']._serialized_end=2170
  _globals['_LABELSET_LABELSETKIND']._serialized_start=2094
  _globals['_LABELSET_LABELSETKIND']._serialized_end=2170
  _globals['_LABELS']._serialized_start=2173
  _globals['_LABELS']._serialized_end=2308
  _globals['_LABELS_LABELSETENTRY']._serialized_start=2237
  _globals['_LABELS_LABELSETENTRY']._serialized_end=2308
  _globals['_ENTITY']._serialized_start=2310
  _globals['_ENTITY']._serialized_end=2386
  _globals['_ENTITIESGROUPSUMMARY']._serialized_start=2388
  _globals['_ENTITIESGROUPSUMMARY']._serialized_end=2456
  _globals['_ENTITIESGROUP']._serialized_start=2459
  _globals['_ENTITIESGROUP']._serialized_end=2652
  _globals['_ENTITIESGROUP_ENTITIESENTRY']._serialized_start=2583
  _globals['_ENTITIESGROUP_ENTITIESENTRY']._serialized_end=2652
  _globals['_DELETEDENTITIESGROUPS']._serialized_start=2654
  _globals['_DELETEDENTITIESGROUPS']._serialized_end=2702
  _globals['_ENTITIESGROUPS']._serialized_start=2705
  _globals['_ENTITIESGROUPS']._serialized_end=2880
  _globals['_ENTITIESGROUPS_ENTITIESGROUPSENTRY']._serialized_start=2798
  _globals['_ENTITIESGROUPS_ENTITIESGROUPSENTRY']._serialized_end=2880
  _globals['_ENTITYGROUPDUPLICATEINDEX']._serialized_start=2883
  _globals['_ENTITYGROUPDUPLICATEINDEX']._serialized_end=3382
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYDUPLICATES']._serialized_start=2998
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYDUPLICATES']._serialized_end=3036
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYGROUPDUPLICATES']._serialized_start=3039
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYGROUPDUPLICATES']._serialized_end=3264
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYGROUPDUPLICATES_ENTITIESENTRY']._serialized_start=3159
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITYGROUPDUPLICATES_ENTITIESENTRY']._serialized_end=3264
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITIESGROUPSENTRY']._serialized_start=3266
  _globals['_ENTITYGROUPDUPLICATEINDEX_ENTITIESGROUPSENTRY']._serialized_end=3382
  _globals['_VECTORSET']._serialized_start=3384
  _globals['_VECTORSET']._serialized_end=3459
  _globals['_VECTORSETS']._serialized_start=3462
  _globals['_VECTORSETS']._serialized_end=3612
  _globals['_VECTORSETS_VECTORSETSENTRY']._serialized_start=3538
  _globals['_VECTORSETS_VECTORSETSENTRY']._serialized_end=3612
  _globals['_VECTORSETCONFIG']._serialized_start=3615
  _globals['_VECTORSETCONFIG']._serialized_end=3748
  _globals['_KNOWLEDGEBOXVECTORSETSCONFIG']._serialized_start=3750
  _globals['_KNOWLEDGEBOXVECTORSETSCONFIG']._serialized_end=3831
  _globals['_TERMSYNONYMS']._serialized_start=3833
  _globals['_TERMSYNONYMS']._serialized_end=3865
  _globals['_SYNONYMS']._serialized_start=3868
  _globals['_SYNONYMS']._serialized_end=4002
  _globals['_SYNONYMS_TERMSENTRY']._serialized_start=3930
  _globals['_SYNONYMS_TERMSENTRY']._serialized_end=4002
  _globals['_SEMANTICMODELMETADATA']._serialized_start=4005
  _globals['_SEMANTICMODELMETADATA']._serialized_end=4223
  _globals['_KBCONFIGURATION']._serialized_start=4226
  _globals['_KBCONFIGURATION']._serialized_end=4366
# @@protoc_insertion_point(module_scope)
