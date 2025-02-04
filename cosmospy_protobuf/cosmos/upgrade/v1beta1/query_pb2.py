
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.upgrade.v1beta1 import upgrade_pb2 as cosmos_dot_upgrade_dot_v1beta1_dot_upgrade__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/upgrade/v1beta1/query.proto\x12\x16cosmos.upgrade.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a$cosmos/upgrade/v1beta1/upgrade.proto"\x19\n\x17QueryCurrentPlanRequest"F\n\x18QueryCurrentPlanResponse\x12*\n\x04plan\x18\x01 \x01(\x0b2\x1c.cosmos.upgrade.v1beta1.Plan"\'\n\x17QueryAppliedPlanRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"*\n\x18QueryAppliedPlanResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03"=\n"QueryUpgradedConsensusStateRequest\x12\x13\n\x0blast_height\x18\x01 \x01(\x03:\x02\x18\x01"Q\n#QueryUpgradedConsensusStateResponse\x12 \n\x18upgraded_consensus_state\x18\x02 \x01(\x0c:\x02\x18\x01J\x04\x08\x01\x10\x02"1\n\x1aQueryModuleVersionsRequest\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t"]\n\x1bQueryModuleVersionsResponse\x12>\n\x0fmodule_versions\x18\x01 \x03(\x0b2%.cosmos.upgrade.v1beta1.ModuleVersion"\x17\n\x15QueryAuthorityRequest")\n\x16QueryAuthorityResponse\x12\x0f\n\x07address\x18\x01 \x01(\t2\xf4\x06\n\x05Query\x12\x9e\x01\n\x0bCurrentPlan\x12/.cosmos.upgrade.v1beta1.QueryCurrentPlanRequest\x1a0.cosmos.upgrade.v1beta1.QueryCurrentPlanResponse",\x82\xd3\xe4\x93\x02&\x12$/cosmos/upgrade/v1beta1/current_plan\x12\xa5\x01\n\x0bAppliedPlan\x12/.cosmos.upgrade.v1beta1.QueryAppliedPlanRequest\x1a0.cosmos.upgrade.v1beta1.QueryAppliedPlanResponse"3\x82\xd3\xe4\x93\x02-\x12+/cosmos/upgrade/v1beta1/applied_plan/{name}\x12\xdc\x01\n\x16UpgradedConsensusState\x12:.cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateRequest\x1a;.cosmos.upgrade.v1beta1.QueryUpgradedConsensusStateResponse"I\x88\x02\x01\x82\xd3\xe4\x93\x02@\x12>/cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height}\x12\xaa\x01\n\x0eModuleVersions\x122.cosmos.upgrade.v1beta1.QueryModuleVersionsRequest\x1a3.cosmos.upgrade.v1beta1.QueryModuleVersionsResponse"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/upgrade/v1beta1/module_versions\x12\x95\x01\n\tAuthority\x12-.cosmos.upgrade.v1beta1.QueryAuthorityRequest\x1a..cosmos.upgrade.v1beta1.QueryAuthorityResponse")\x82\xd3\xe4\x93\x02#\x12!/cosmos/upgrade/v1beta1/authorityB.Z,github.com/cosmos/cosmos-sdk/x/upgrade/typesb\x06proto3')
_QUERYCURRENTPLANREQUEST = DESCRIPTOR.message_types_by_name['QueryCurrentPlanRequest']
_QUERYCURRENTPLANRESPONSE = DESCRIPTOR.message_types_by_name['QueryCurrentPlanResponse']
_QUERYAPPLIEDPLANREQUEST = DESCRIPTOR.message_types_by_name['QueryAppliedPlanRequest']
_QUERYAPPLIEDPLANRESPONSE = DESCRIPTOR.message_types_by_name['QueryAppliedPlanResponse']
_QUERYUPGRADEDCONSENSUSSTATEREQUEST = DESCRIPTOR.message_types_by_name['QueryUpgradedConsensusStateRequest']
_QUERYUPGRADEDCONSENSUSSTATERESPONSE = DESCRIPTOR.message_types_by_name['QueryUpgradedConsensusStateResponse']
_QUERYMODULEVERSIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryModuleVersionsRequest']
_QUERYMODULEVERSIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryModuleVersionsResponse']
_QUERYAUTHORITYREQUEST = DESCRIPTOR.message_types_by_name['QueryAuthorityRequest']
_QUERYAUTHORITYRESPONSE = DESCRIPTOR.message_types_by_name['QueryAuthorityResponse']
QueryCurrentPlanRequest = _reflection.GeneratedProtocolMessageType('QueryCurrentPlanRequest', (_message.Message,), {'DESCRIPTOR': _QUERYCURRENTPLANREQUEST, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCurrentPlanRequest)
QueryCurrentPlanResponse = _reflection.GeneratedProtocolMessageType('QueryCurrentPlanResponse', (_message.Message,), {'DESCRIPTOR': _QUERYCURRENTPLANRESPONSE, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryCurrentPlanResponse)
QueryAppliedPlanRequest = _reflection.GeneratedProtocolMessageType('QueryAppliedPlanRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAPPLIEDPLANREQUEST, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAppliedPlanRequest)
QueryAppliedPlanResponse = _reflection.GeneratedProtocolMessageType('QueryAppliedPlanResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAPPLIEDPLANRESPONSE, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAppliedPlanResponse)
QueryUpgradedConsensusStateRequest = _reflection.GeneratedProtocolMessageType('QueryUpgradedConsensusStateRequest', (_message.Message,), {'DESCRIPTOR': _QUERYUPGRADEDCONSENSUSSTATEREQUEST, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryUpgradedConsensusStateRequest)
QueryUpgradedConsensusStateResponse = _reflection.GeneratedProtocolMessageType('QueryUpgradedConsensusStateResponse', (_message.Message,), {'DESCRIPTOR': _QUERYUPGRADEDCONSENSUSSTATERESPONSE, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryUpgradedConsensusStateResponse)
QueryModuleVersionsRequest = _reflection.GeneratedProtocolMessageType('QueryModuleVersionsRequest', (_message.Message,), {'DESCRIPTOR': _QUERYMODULEVERSIONSREQUEST, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryModuleVersionsRequest)
QueryModuleVersionsResponse = _reflection.GeneratedProtocolMessageType('QueryModuleVersionsResponse', (_message.Message,), {'DESCRIPTOR': _QUERYMODULEVERSIONSRESPONSE, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryModuleVersionsResponse)
QueryAuthorityRequest = _reflection.GeneratedProtocolMessageType('QueryAuthorityRequest', (_message.Message,), {'DESCRIPTOR': _QUERYAUTHORITYREQUEST, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAuthorityRequest)
QueryAuthorityResponse = _reflection.GeneratedProtocolMessageType('QueryAuthorityResponse', (_message.Message,), {'DESCRIPTOR': _QUERYAUTHORITYRESPONSE, '__module__': 'cosmos.upgrade.v1beta1.query_pb2'})
_sym_db.RegisterMessage(QueryAuthorityResponse)
_QUERY = DESCRIPTOR.services_by_name['Query']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/upgrade/types'
    _QUERYUPGRADEDCONSENSUSSTATEREQUEST._options = None
    _QUERYUPGRADEDCONSENSUSSTATEREQUEST._serialized_options = b'\x18\x01'
    _QUERYUPGRADEDCONSENSUSSTATERESPONSE._options = None
    _QUERYUPGRADEDCONSENSUSSTATERESPONSE._serialized_options = b'\x18\x01'
    _QUERY.methods_by_name['CurrentPlan']._options = None
    _QUERY.methods_by_name['CurrentPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/cosmos/upgrade/v1beta1/current_plan'
    _QUERY.methods_by_name['AppliedPlan']._options = None
    _QUERY.methods_by_name['AppliedPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/cosmos/upgrade/v1beta1/applied_plan/{name}'
    _QUERY.methods_by_name['UpgradedConsensusState']._options = None
    _QUERY.methods_by_name['UpgradedConsensusState']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02@\x12>/cosmos/upgrade/v1beta1/upgraded_consensus_state/{last_height}'
    _QUERY.methods_by_name['ModuleVersions']._options = None
    _QUERY.methods_by_name['ModuleVersions']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/cosmos/upgrade/v1beta1/module_versions"
    _QUERY.methods_by_name['Authority']._options = None
    _QUERY.methods_by_name['Authority']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/cosmos/upgrade/v1beta1/authority'
    _QUERYCURRENTPLANREQUEST._serialized_start = 130
    _QUERYCURRENTPLANREQUEST._serialized_end = 155
    _QUERYCURRENTPLANRESPONSE._serialized_start = 157
    _QUERYCURRENTPLANRESPONSE._serialized_end = 227
    _QUERYAPPLIEDPLANREQUEST._serialized_start = 229
    _QUERYAPPLIEDPLANREQUEST._serialized_end = 268
    _QUERYAPPLIEDPLANRESPONSE._serialized_start = 270
    _QUERYAPPLIEDPLANRESPONSE._serialized_end = 312
    _QUERYUPGRADEDCONSENSUSSTATEREQUEST._serialized_start = 314
    _QUERYUPGRADEDCONSENSUSSTATEREQUEST._serialized_end = 375
    _QUERYUPGRADEDCONSENSUSSTATERESPONSE._serialized_start = 377
    _QUERYUPGRADEDCONSENSUSSTATERESPONSE._serialized_end = 458
    _QUERYMODULEVERSIONSREQUEST._serialized_start = 460
    _QUERYMODULEVERSIONSREQUEST._serialized_end = 509
    _QUERYMODULEVERSIONSRESPONSE._serialized_start = 511
    _QUERYMODULEVERSIONSRESPONSE._serialized_end = 604
    _QUERYAUTHORITYREQUEST._serialized_start = 606
    _QUERYAUTHORITYREQUEST._serialized_end = 629
    _QUERYAUTHORITYRESPONSE._serialized_start = 631
    _QUERYAUTHORITYRESPONSE._serialized_end = 672
    _QUERY._serialized_start = 675
    _QUERY._serialized_end = 1559
