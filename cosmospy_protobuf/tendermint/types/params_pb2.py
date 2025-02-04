
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtendermint/types/params.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto"\xf3\x01\n\x0fConsensusParams\x122\n\x05block\x18\x01 \x01(\x0b2\x1d.tendermint.types.BlockParamsB\x04\xc8\xde\x1f\x00\x128\n\x08evidence\x18\x02 \x01(\x0b2 .tendermint.types.EvidenceParamsB\x04\xc8\xde\x1f\x00\x12:\n\tvalidator\x18\x03 \x01(\x0b2!.tendermint.types.ValidatorParamsB\x04\xc8\xde\x1f\x00\x126\n\x07version\x18\x04 \x01(\x0b2\x1f.tendermint.types.VersionParamsB\x04\xc8\xde\x1f\x00"G\n\x0bBlockParams\x12\x11\n\tmax_bytes\x18\x01 \x01(\x03\x12\x0f\n\x07max_gas\x18\x02 \x01(\x03\x12\x14\n\x0ctime_iota_ms\x18\x03 \x01(\x03"~\n\x0eEvidenceParams\x12\x1a\n\x12max_age_num_blocks\x18\x01 \x01(\x03\x12=\n\x10max_age_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x11\n\tmax_bytes\x18\x03 \x01(\x03"2\n\x0fValidatorParams\x12\x15\n\rpub_key_types\x18\x01 \x03(\t:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01".\n\rVersionParams\x12\x13\n\x0bapp_version\x18\x01 \x01(\x04:\x08\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01">\n\x0cHashedParams\x12\x17\n\x0fblock_max_bytes\x18\x01 \x01(\x03\x12\x15\n\rblock_max_gas\x18\x02 \x01(\x03B=Z7github.com/tendermint/tendermint/proto/tendermint/types\xa8\xe2\x1e\x01b\x06proto3')
_CONSENSUSPARAMS = DESCRIPTOR.message_types_by_name['ConsensusParams']
_BLOCKPARAMS = DESCRIPTOR.message_types_by_name['BlockParams']
_EVIDENCEPARAMS = DESCRIPTOR.message_types_by_name['EvidenceParams']
_VALIDATORPARAMS = DESCRIPTOR.message_types_by_name['ValidatorParams']
_VERSIONPARAMS = DESCRIPTOR.message_types_by_name['VersionParams']
_HASHEDPARAMS = DESCRIPTOR.message_types_by_name['HashedParams']
ConsensusParams = _reflection.GeneratedProtocolMessageType('ConsensusParams', (_message.Message,), {'DESCRIPTOR': _CONSENSUSPARAMS, '__module__': 'tendermint.types.params_pb2'})
_sym_db.RegisterMessage(ConsensusParams)
BlockParams = _reflection.GeneratedProtocolMessageType('BlockParams', (_message.Message,), {'DESCRIPTOR': _BLOCKPARAMS, '__module__': 'tendermint.types.params_pb2'})
_sym_db.RegisterMessage(BlockParams)
EvidenceParams = _reflection.GeneratedProtocolMessageType('EvidenceParams', (_message.Message,), {'DESCRIPTOR': _EVIDENCEPARAMS, '__module__': 'tendermint.types.params_pb2'})
_sym_db.RegisterMessage(EvidenceParams)
ValidatorParams = _reflection.GeneratedProtocolMessageType('ValidatorParams', (_message.Message,), {'DESCRIPTOR': _VALIDATORPARAMS, '__module__': 'tendermint.types.params_pb2'})
_sym_db.RegisterMessage(ValidatorParams)
VersionParams = _reflection.GeneratedProtocolMessageType('VersionParams', (_message.Message,), {'DESCRIPTOR': _VERSIONPARAMS, '__module__': 'tendermint.types.params_pb2'})
_sym_db.RegisterMessage(VersionParams)
HashedParams = _reflection.GeneratedProtocolMessageType('HashedParams', (_message.Message,), {'DESCRIPTOR': _HASHEDPARAMS, '__module__': 'tendermint.types.params_pb2'})
_sym_db.RegisterMessage(HashedParams)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/tendermint/tendermint/proto/tendermint/types\xa8\xe2\x1e\x01'
    _CONSENSUSPARAMS.fields_by_name['block']._options = None
    _CONSENSUSPARAMS.fields_by_name['block']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONSENSUSPARAMS.fields_by_name['evidence']._options = None
    _CONSENSUSPARAMS.fields_by_name['evidence']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONSENSUSPARAMS.fields_by_name['validator']._options = None
    _CONSENSUSPARAMS.fields_by_name['validator']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONSENSUSPARAMS.fields_by_name['version']._options = None
    _CONSENSUSPARAMS.fields_by_name['version']._serialized_options = b'\xc8\xde\x1f\x00'
    _EVIDENCEPARAMS.fields_by_name['max_age_duration']._options = None
    _EVIDENCEPARAMS.fields_by_name['max_age_duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _VALIDATORPARAMS._options = None
    _VALIDATORPARAMS._serialized_options = b'\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01'
    _VERSIONPARAMS._options = None
    _VERSIONPARAMS._serialized_options = b'\xb8\xa0\x1f\x01\xe8\xa0\x1f\x01'
    _CONSENSUSPARAMS._serialized_start = 106
    _CONSENSUSPARAMS._serialized_end = 349
    _BLOCKPARAMS._serialized_start = 351
    _BLOCKPARAMS._serialized_end = 422
    _EVIDENCEPARAMS._serialized_start = 424
    _EVIDENCEPARAMS._serialized_end = 550
    _VALIDATORPARAMS._serialized_start = 552
    _VALIDATORPARAMS._serialized_end = 602
    _VERSIONPARAMS._serialized_start = 604
    _VERSIONPARAMS._serialized_end = 650
    _HASHEDPARAMS._serialized_start = 652
    _HASHEDPARAMS._serialized_end = 714
