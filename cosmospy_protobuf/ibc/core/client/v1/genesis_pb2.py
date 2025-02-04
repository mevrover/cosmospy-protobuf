
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n ibc/core/client/v1/genesis.proto\x12\x12ibc.core.client.v1\x1a\x1fibc/core/client/v1/client.proto\x1a\x14gogoproto/gogo.proto"\xff\x03\n\x0cGenesisState\x12Z\n\x07clients\x18\x01 \x03(\x0b2).ibc.core.client.v1.IdentifiedClientStateB\x1e\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStates\x12\x80\x01\n\x11clients_consensus\x18\x02 \x03(\x0b2).ibc.core.client.v1.ClientConsensusStatesB:\xc8\xde\x1f\x00\xaa\xdf\x1f\x16ClientsConsensusStates\xf2\xde\x1f\x18yaml:"clients_consensus"\x12h\n\x10clients_metadata\x18\x03 \x03(\x0b2-.ibc.core.client.v1.IdentifiedGenesisMetadataB\x1f\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"clients_metadata"\x120\n\x06params\x18\x04 \x01(\x0b2\x1a.ibc.core.client.v1.ParamsB\x04\xc8\xde\x1f\x00\x125\n\x10create_localhost\x18\x05 \x01(\x08B\x1b\xf2\xde\x1f\x17yaml:"create_localhost"\x12=\n\x14next_client_sequence\x18\x06 \x01(\x04B\x1f\xf2\xde\x1f\x1byaml:"next_client_sequence""3\n\x0fGenesisMetadata\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c:\x04\x88\xa0\x1f\x00"\xa2\x01\n\x19IdentifiedGenesisMetadata\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12\\\n\x0fclient_metadata\x18\x02 \x03(\x0b2#.ibc.core.client.v1.GenesisMetadataB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"client_metadata"B:Z8github.com/cosmos/ibc-go/v3/modules/core/02-client/typesb\x06proto3')
_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
_GENESISMETADATA = DESCRIPTOR.message_types_by_name['GenesisMetadata']
_IDENTIFIEDGENESISMETADATA = DESCRIPTOR.message_types_by_name['IdentifiedGenesisMetadata']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {'DESCRIPTOR': _GENESISSTATE, '__module__': 'ibc.core.client.v1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisState)
GenesisMetadata = _reflection.GeneratedProtocolMessageType('GenesisMetadata', (_message.Message,), {'DESCRIPTOR': _GENESISMETADATA, '__module__': 'ibc.core.client.v1.genesis_pb2'})
_sym_db.RegisterMessage(GenesisMetadata)
IdentifiedGenesisMetadata = _reflection.GeneratedProtocolMessageType('IdentifiedGenesisMetadata', (_message.Message,), {'DESCRIPTOR': _IDENTIFIEDGENESISMETADATA, '__module__': 'ibc.core.client.v1.genesis_pb2'})
_sym_db.RegisterMessage(IdentifiedGenesisMetadata)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/cosmos/ibc-go/v3/modules/core/02-client/types'
    _GENESISSTATE.fields_by_name['clients']._options = None
    _GENESISSTATE.fields_by_name['clients']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x16IdentifiedClientStates'
    _GENESISSTATE.fields_by_name['clients_consensus']._options = None
    _GENESISSTATE.fields_by_name['clients_consensus']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x16ClientsConsensusStates\xf2\xde\x1f\x18yaml:"clients_consensus"'
    _GENESISSTATE.fields_by_name['clients_metadata']._options = None
    _GENESISSTATE.fields_by_name['clients_metadata']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"clients_metadata"'
    _GENESISSTATE.fields_by_name['params']._options = None
    _GENESISSTATE.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['create_localhost']._options = None
    _GENESISSTATE.fields_by_name['create_localhost']._serialized_options = b'\xf2\xde\x1f\x17yaml:"create_localhost"'
    _GENESISSTATE.fields_by_name['next_client_sequence']._options = None
    _GENESISSTATE.fields_by_name['next_client_sequence']._serialized_options = b'\xf2\xde\x1f\x1byaml:"next_client_sequence"'
    _GENESISMETADATA._options = None
    _GENESISMETADATA._serialized_options = b'\x88\xa0\x1f\x00'
    _IDENTIFIEDGENESISMETADATA.fields_by_name['client_id']._options = None
    _IDENTIFIEDGENESISMETADATA.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _IDENTIFIEDGENESISMETADATA.fields_by_name['client_metadata']._options = None
    _IDENTIFIEDGENESISMETADATA.fields_by_name['client_metadata']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"client_metadata"'
    _GENESISSTATE._serialized_start = 112
    _GENESISSTATE._serialized_end = 623
    _GENESISMETADATA._serialized_start = 625
    _GENESISMETADATA._serialized_end = 676
    _IDENTIFIEDGENESISMETADATA._serialized_start = 679
    _IDENTIFIEDGENESISMETADATA._serialized_end = 841
