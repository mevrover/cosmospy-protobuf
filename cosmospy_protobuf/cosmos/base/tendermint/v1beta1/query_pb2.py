
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....tendermint.p2p import types_pb2 as tendermint_dot_p2p_dot_types__pb2
from .....tendermint.types import block_pb2 as tendermint_dot_types_dot_block__pb2
from .....tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from .....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cosmos/base/tendermint/v1beta1/query.proto\x12\x1ecosmos.base.tendermint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1atendermint/p2p/types.proto\x1a\x1ctendermint/types/block.proto\x1a\x1ctendermint/types/types.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x19cosmos_proto/cosmos.proto"l\n\x1eGetValidatorSetByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xb3\x01\n\x1fGetValidatorSetByHeightResponse\x12\x14\n\x0cblock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b2).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Z\n\x1cGetLatestValidatorSetRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xb1\x01\n\x1dGetLatestValidatorSetResponse\x12\x14\n\x0cblock_height\x18\x01 \x01(\x03\x12=\n\nvalidators\x18\x02 \x03(\x0b2).cosmos.base.tendermint.v1beta1.Validator\x12;\n\npagination\x18\x03 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x8e\x01\n\tValidator\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12%\n\x07pub_key\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12\x14\n\x0cvoting_power\x18\x03 \x01(\x03\x12\x19\n\x11proposer_priority\x18\x04 \x01(\x03")\n\x17GetBlockByHeightRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03"o\n\x18GetBlockByHeightResponse\x12+\n\x08block_id\x18\x01 \x01(\x0b2\x19.tendermint.types.BlockID\x12&\n\x05block\x18\x02 \x01(\x0b2\x17.tendermint.types.Block"\x17\n\x15GetLatestBlockRequest"m\n\x16GetLatestBlockResponse\x12+\n\x08block_id\x18\x01 \x01(\x0b2\x19.tendermint.types.BlockID\x12&\n\x05block\x18\x02 \x01(\x0b2\x17.tendermint.types.Block"\x13\n\x11GetSyncingRequest"%\n\x12GetSyncingResponse\x12\x0f\n\x07syncing\x18\x01 \x01(\x08"\x14\n\x12GetNodeInfoRequest"\x8c\x01\n\x13GetNodeInfoResponse\x12+\n\tnode_info\x18\x01 \x01(\x0b2\x18.tendermint.p2p.NodeInfo\x12H\n\x13application_version\x18\x02 \x01(\x0b2+.cosmos.base.tendermint.v1beta1.VersionInfo"\xd2\x01\n\x0bVersionInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08app_name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12\x12\n\ngit_commit\x18\x04 \x01(\t\x12\x12\n\nbuild_tags\x18\x05 \x01(\t\x12\x12\n\ngo_version\x18\x06 \x01(\t\x12:\n\nbuild_deps\x18\x07 \x03(\x0b2&.cosmos.base.tendermint.v1beta1.Module\x12\x1a\n\x12cosmos_sdk_version\x18\x08 \x01(\t"4\n\x06Module\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03sum\x18\x03 \x01(\t"M\n\x10ABCIQueryRequest\x12\x0c\n\x04data\x18\x01 \x01(\x0c\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x03\x12\r\n\x05prove\x18\x04 \x01(\x08"\xcd\x01\n\x11ABCIQueryResponse\x12\x0c\n\x04code\x18\x01 \x01(\r\x12\x0b\n\x03log\x18\x03 \x01(\t\x12\x0c\n\x04info\x18\x04 \x01(\t\x12\r\n\x05index\x18\x05 \x01(\x03\x12\x0b\n\x03key\x18\x06 \x01(\x0c\x12\r\n\x05value\x18\x07 \x01(\x0c\x12;\n\tproof_ops\x18\x08 \x01(\x0b2(.cosmos.base.tendermint.v1beta1.ProofOps\x12\x0e\n\x06height\x18\t \x01(\x03\x12\x11\n\tcodespace\x18\n \x01(\tJ\x04\x08\x02\x10\x03"2\n\x07ProofOp\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04data\x18\x03 \x01(\x0c"F\n\x08ProofOps\x12:\n\x03ops\x18\x01 \x03(\x0b2\'.cosmos.base.tendermint.v1beta1.ProofOpB\x04\xc8\xde\x1f\x002\xaf\n\n\x07Service\x12\xa9\x01\n\x0bGetNodeInfo\x122.cosmos.base.tendermint.v1beta1.GetNodeInfoRequest\x1a3.cosmos.base.tendermint.v1beta1.GetNodeInfoResponse"1\x82\xd3\xe4\x93\x02+\x12)/cosmos/base/tendermint/v1beta1/node_info\x12\xa4\x01\n\nGetSyncing\x121.cosmos.base.tendermint.v1beta1.GetSyncingRequest\x1a2.cosmos.base.tendermint.v1beta1.GetSyncingResponse"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/base/tendermint/v1beta1/syncing\x12\xb6\x01\n\x0eGetLatestBlock\x125.cosmos.base.tendermint.v1beta1.GetLatestBlockRequest\x1a6.cosmos.base.tendermint.v1beta1.GetLatestBlockResponse"5\x82\xd3\xe4\x93\x02/\x12-/cosmos/base/tendermint/v1beta1/blocks/latest\x12\xbe\x01\n\x10GetBlockByHeight\x127.cosmos.base.tendermint.v1beta1.GetBlockByHeightRequest\x1a8.cosmos.base.tendermint.v1beta1.GetBlockByHeightResponse"7\x82\xd3\xe4\x93\x021\x12//cosmos/base/tendermint/v1beta1/blocks/{height}\x12\xd2\x01\n\x15GetLatestValidatorSet\x12<.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetRequest\x1a=.cosmos.base.tendermint.v1beta1.GetLatestValidatorSetResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/base/tendermint/v1beta1/validatorsets/latest\x12\xda\x01\n\x17GetValidatorSetByHeight\x12>.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightRequest\x1a?.cosmos.base.tendermint.v1beta1.GetValidatorSetByHeightResponse">\x82\xd3\xe4\x93\x028\x126/cosmos/base/tendermint/v1beta1/validatorsets/{height}\x12\xa4\x01\n\tABCIQuery\x120.cosmos.base.tendermint.v1beta1.ABCIQueryRequest\x1a1.cosmos.base.tendermint.v1beta1.ABCIQueryResponse"2\x82\xd3\xe4\x93\x02,\x12*/cosmos/base/tendermint/v1beta1/abci_queryB4Z2github.com/cosmos/cosmos-sdk/client/grpc/tmserviceb\x06proto3')
_GETVALIDATORSETBYHEIGHTREQUEST = DESCRIPTOR.message_types_by_name['GetValidatorSetByHeightRequest']
_GETVALIDATORSETBYHEIGHTRESPONSE = DESCRIPTOR.message_types_by_name['GetValidatorSetByHeightResponse']
_GETLATESTVALIDATORSETREQUEST = DESCRIPTOR.message_types_by_name['GetLatestValidatorSetRequest']
_GETLATESTVALIDATORSETRESPONSE = DESCRIPTOR.message_types_by_name['GetLatestValidatorSetResponse']
_VALIDATOR = DESCRIPTOR.message_types_by_name['Validator']
_GETBLOCKBYHEIGHTREQUEST = DESCRIPTOR.message_types_by_name['GetBlockByHeightRequest']
_GETBLOCKBYHEIGHTRESPONSE = DESCRIPTOR.message_types_by_name['GetBlockByHeightResponse']
_GETLATESTBLOCKREQUEST = DESCRIPTOR.message_types_by_name['GetLatestBlockRequest']
_GETLATESTBLOCKRESPONSE = DESCRIPTOR.message_types_by_name['GetLatestBlockResponse']
_GETSYNCINGREQUEST = DESCRIPTOR.message_types_by_name['GetSyncingRequest']
_GETSYNCINGRESPONSE = DESCRIPTOR.message_types_by_name['GetSyncingResponse']
_GETNODEINFOREQUEST = DESCRIPTOR.message_types_by_name['GetNodeInfoRequest']
_GETNODEINFORESPONSE = DESCRIPTOR.message_types_by_name['GetNodeInfoResponse']
_VERSIONINFO = DESCRIPTOR.message_types_by_name['VersionInfo']
_MODULE = DESCRIPTOR.message_types_by_name['Module']
_ABCIQUERYREQUEST = DESCRIPTOR.message_types_by_name['ABCIQueryRequest']
_ABCIQUERYRESPONSE = DESCRIPTOR.message_types_by_name['ABCIQueryResponse']
_PROOFOP = DESCRIPTOR.message_types_by_name['ProofOp']
_PROOFOPS = DESCRIPTOR.message_types_by_name['ProofOps']
GetValidatorSetByHeightRequest = _reflection.GeneratedProtocolMessageType('GetValidatorSetByHeightRequest', (_message.Message,), {'DESCRIPTOR': _GETVALIDATORSETBYHEIGHTREQUEST, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetValidatorSetByHeightRequest)
GetValidatorSetByHeightResponse = _reflection.GeneratedProtocolMessageType('GetValidatorSetByHeightResponse', (_message.Message,), {'DESCRIPTOR': _GETVALIDATORSETBYHEIGHTRESPONSE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetValidatorSetByHeightResponse)
GetLatestValidatorSetRequest = _reflection.GeneratedProtocolMessageType('GetLatestValidatorSetRequest', (_message.Message,), {'DESCRIPTOR': _GETLATESTVALIDATORSETREQUEST, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetLatestValidatorSetRequest)
GetLatestValidatorSetResponse = _reflection.GeneratedProtocolMessageType('GetLatestValidatorSetResponse', (_message.Message,), {'DESCRIPTOR': _GETLATESTVALIDATORSETRESPONSE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetLatestValidatorSetResponse)
Validator = _reflection.GeneratedProtocolMessageType('Validator', (_message.Message,), {'DESCRIPTOR': _VALIDATOR, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(Validator)
GetBlockByHeightRequest = _reflection.GeneratedProtocolMessageType('GetBlockByHeightRequest', (_message.Message,), {'DESCRIPTOR': _GETBLOCKBYHEIGHTREQUEST, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetBlockByHeightRequest)
GetBlockByHeightResponse = _reflection.GeneratedProtocolMessageType('GetBlockByHeightResponse', (_message.Message,), {'DESCRIPTOR': _GETBLOCKBYHEIGHTRESPONSE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetBlockByHeightResponse)
GetLatestBlockRequest = _reflection.GeneratedProtocolMessageType('GetLatestBlockRequest', (_message.Message,), {'DESCRIPTOR': _GETLATESTBLOCKREQUEST, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetLatestBlockRequest)
GetLatestBlockResponse = _reflection.GeneratedProtocolMessageType('GetLatestBlockResponse', (_message.Message,), {'DESCRIPTOR': _GETLATESTBLOCKRESPONSE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetLatestBlockResponse)
GetSyncingRequest = _reflection.GeneratedProtocolMessageType('GetSyncingRequest', (_message.Message,), {'DESCRIPTOR': _GETSYNCINGREQUEST, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetSyncingRequest)
GetSyncingResponse = _reflection.GeneratedProtocolMessageType('GetSyncingResponse', (_message.Message,), {'DESCRIPTOR': _GETSYNCINGRESPONSE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetSyncingResponse)
GetNodeInfoRequest = _reflection.GeneratedProtocolMessageType('GetNodeInfoRequest', (_message.Message,), {'DESCRIPTOR': _GETNODEINFOREQUEST, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetNodeInfoRequest)
GetNodeInfoResponse = _reflection.GeneratedProtocolMessageType('GetNodeInfoResponse', (_message.Message,), {'DESCRIPTOR': _GETNODEINFORESPONSE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(GetNodeInfoResponse)
VersionInfo = _reflection.GeneratedProtocolMessageType('VersionInfo', (_message.Message,), {'DESCRIPTOR': _VERSIONINFO, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(VersionInfo)
Module = _reflection.GeneratedProtocolMessageType('Module', (_message.Message,), {'DESCRIPTOR': _MODULE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(Module)
ABCIQueryRequest = _reflection.GeneratedProtocolMessageType('ABCIQueryRequest', (_message.Message,), {'DESCRIPTOR': _ABCIQUERYREQUEST, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(ABCIQueryRequest)
ABCIQueryResponse = _reflection.GeneratedProtocolMessageType('ABCIQueryResponse', (_message.Message,), {'DESCRIPTOR': _ABCIQUERYRESPONSE, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(ABCIQueryResponse)
ProofOp = _reflection.GeneratedProtocolMessageType('ProofOp', (_message.Message,), {'DESCRIPTOR': _PROOFOP, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(ProofOp)
ProofOps = _reflection.GeneratedProtocolMessageType('ProofOps', (_message.Message,), {'DESCRIPTOR': _PROOFOPS, '__module__': 'cosmos.base.tendermint.v1beta1.query_pb2'})
_sym_db.RegisterMessage(ProofOps)
_SERVICE = DESCRIPTOR.services_by_name['Service']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z2github.com/cosmos/cosmos-sdk/client/grpc/tmservice'
    _VALIDATOR.fields_by_name['address']._options = None
    _VALIDATOR.fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _PROOFOPS.fields_by_name['ops']._options = None
    _PROOFOPS.fields_by_name['ops']._serialized_options = b'\xc8\xde\x1f\x00'
    _SERVICE.methods_by_name['GetNodeInfo']._options = None
    _SERVICE.methods_by_name['GetNodeInfo']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/cosmos/base/tendermint/v1beta1/node_info'
    _SERVICE.methods_by_name['GetSyncing']._options = None
    _SERVICE.methods_by_name['GetSyncing']._serialized_options = b"\x82\xd3\xe4\x93\x02)\x12'/cosmos/base/tendermint/v1beta1/syncing"
    _SERVICE.methods_by_name['GetLatestBlock']._options = None
    _SERVICE.methods_by_name['GetLatestBlock']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/cosmos/base/tendermint/v1beta1/blocks/latest'
    _SERVICE.methods_by_name['GetBlockByHeight']._options = None
    _SERVICE.methods_by_name['GetBlockByHeight']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//cosmos/base/tendermint/v1beta1/blocks/{height}'
    _SERVICE.methods_by_name['GetLatestValidatorSet']._options = None
    _SERVICE.methods_by_name['GetLatestValidatorSet']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/base/tendermint/v1beta1/validatorsets/latest'
    _SERVICE.methods_by_name['GetValidatorSetByHeight']._options = None
    _SERVICE.methods_by_name['GetValidatorSetByHeight']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/cosmos/base/tendermint/v1beta1/validatorsets/{height}'
    _SERVICE.methods_by_name['ABCIQuery']._options = None
    _SERVICE.methods_by_name['ABCIQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02,\x12*/cosmos/base/tendermint/v1beta1/abci_query'
    _GETVALIDATORSETBYHEIGHTREQUEST._serialized_start = 316
    _GETVALIDATORSETBYHEIGHTREQUEST._serialized_end = 424
    _GETVALIDATORSETBYHEIGHTRESPONSE._serialized_start = 427
    _GETVALIDATORSETBYHEIGHTRESPONSE._serialized_end = 606
    _GETLATESTVALIDATORSETREQUEST._serialized_start = 608
    _GETLATESTVALIDATORSETREQUEST._serialized_end = 698
    _GETLATESTVALIDATORSETRESPONSE._serialized_start = 701
    _GETLATESTVALIDATORSETRESPONSE._serialized_end = 878
    _VALIDATOR._serialized_start = 881
    _VALIDATOR._serialized_end = 1023
    _GETBLOCKBYHEIGHTREQUEST._serialized_start = 1025
    _GETBLOCKBYHEIGHTREQUEST._serialized_end = 1066
    _GETBLOCKBYHEIGHTRESPONSE._serialized_start = 1068
    _GETBLOCKBYHEIGHTRESPONSE._serialized_end = 1179
    _GETLATESTBLOCKREQUEST._serialized_start = 1181
    _GETLATESTBLOCKREQUEST._serialized_end = 1204
    _GETLATESTBLOCKRESPONSE._serialized_start = 1206
    _GETLATESTBLOCKRESPONSE._serialized_end = 1315
    _GETSYNCINGREQUEST._serialized_start = 1317
    _GETSYNCINGREQUEST._serialized_end = 1336
    _GETSYNCINGRESPONSE._serialized_start = 1338
    _GETSYNCINGRESPONSE._serialized_end = 1375
    _GETNODEINFOREQUEST._serialized_start = 1377
    _GETNODEINFOREQUEST._serialized_end = 1397
    _GETNODEINFORESPONSE._serialized_start = 1400
    _GETNODEINFORESPONSE._serialized_end = 1540
    _VERSIONINFO._serialized_start = 1543
    _VERSIONINFO._serialized_end = 1753
    _MODULE._serialized_start = 1755
    _MODULE._serialized_end = 1807
    _ABCIQUERYREQUEST._serialized_start = 1809
    _ABCIQUERYREQUEST._serialized_end = 1886
    _ABCIQUERYRESPONSE._serialized_start = 1889
    _ABCIQUERYRESPONSE._serialized_end = 2094
    _PROOFOP._serialized_start = 2096
    _PROOFOP._serialized_end = 2146
    _PROOFOPS._serialized_start = 2148
    _PROOFOPS._serialized_end = 2218
    _SERVICE._serialized_start = 2221
    _SERVICE._serialized_end = 3548
