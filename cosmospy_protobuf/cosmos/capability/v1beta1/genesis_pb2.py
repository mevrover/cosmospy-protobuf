
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.capability.v1beta1 import capability_pb2 as cosmos_dot_capability_dot_v1beta1_dot_capability__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cosmos/capability/v1beta1/genesis.proto\x12\x19cosmos.capability.v1beta1\x1a\x14gogoproto/gogo.proto\x1a*cosmos/capability/v1beta1/capability.proto"g\n\rGenesisOwners\x12\r\n\x05index\x18\x01 \x01(\x04\x12G\n\x0cindex_owners\x18\x02 \x01(\x0b2+.cosmos.capability.v1beta1.CapabilityOwnersB\x04\xc8\xde\x1f\x00"]\n\x0cGenesisState\x12\r\n\x05index\x18\x01 \x01(\x04\x12>\n\x06owners\x18\x02 \x03(\x0b2(.cosmos.capability.v1beta1.GenesisOwnersB\x04\xc8\xde\x1f\x00B1Z/github.com/cosmos/cosmos-sdk/x/capability/typesb\x06proto3')
_GENESISOWNERS = DESCRIPTOR.message_types_by_name['GenesisOwners']
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisOwners = _reflection.GeneratedProtocolMessageType('GenesisOwners', (_message.Message,), {'DESCRIPTOR': _GENESISOWNERS, '__module__': 'cosmos.capability.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisOwners)
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'cosmos.capability.v1beta1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z/github.com/cosmos/cosmos-sdk/x/capability/types'
    _GENESISOWNERS.fields_by_name['index_owners']._options = None
    _GENESISOWNERS.fields_by_name['index_owners']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['owners']._options = None
    _GENESISSTATE.fields_by_name['owners']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISOWNERS._serialized_start = 136
    _GENESISOWNERS._serialized_end = 239
    _GENESISSTATE._serialized_start = 241
    _GENESISSTATE._serialized_end = 334
