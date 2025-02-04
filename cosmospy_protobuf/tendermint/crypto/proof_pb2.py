
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtendermint/crypto/proof.proto\x12\x11tendermint.crypto\x1a\x14gogoproto/gogo.proto"G\n\x05Proof\x12\r\n\x05total\x18\x01 \x01(\x03\x12\r\n\x05index\x18\x02 \x01(\x03\x12\x11\n\tleaf_hash\x18\x03 \x01(\x0c\x12\r\n\x05aunts\x18\x04 \x03(\x0c"?\n\x07ValueOp\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\'\n\x05proof\x18\x02 \x01(\x0b2\x18.tendermint.crypto.Proof"6\n\x08DominoOp\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05input\x18\x02 \x01(\t\x12\x0e\n\x06output\x18\x03 \x01(\t"2\n\x07ProofOp\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x12\x0c\n\x04data\x18\x03 \x01(\x0c"9\n\x08ProofOps\x12-\n\x03ops\x18\x01 \x03(\x0b2\x1a.tendermint.crypto.ProofOpB\x04\xc8\xde\x1f\x00B:Z8github.com/tendermint/tendermint/proto/tendermint/cryptob\x06proto3')
_PROOF = DESCRIPTOR.message_types_by_name['Proof']
_VALUEOP = DESCRIPTOR.message_types_by_name['ValueOp']
_DOMINOOP = DESCRIPTOR.message_types_by_name['DominoOp']
_PROOFOP = DESCRIPTOR.message_types_by_name['ProofOp']
_PROOFOPS = DESCRIPTOR.message_types_by_name['ProofOps']
Proof = _reflection.GeneratedProtocolMessageType('Proof', (_message.Message,), {'DESCRIPTOR': _PROOF, '__module__': 'tendermint.crypto.proof_pb2'})
_sym_db.RegisterMessage(Proof)
ValueOp = _reflection.GeneratedProtocolMessageType('ValueOp', (_message.Message,), {'DESCRIPTOR': _VALUEOP, '__module__': 'tendermint.crypto.proof_pb2'})
_sym_db.RegisterMessage(ValueOp)
DominoOp = _reflection.GeneratedProtocolMessageType('DominoOp', (_message.Message,), {'DESCRIPTOR': _DOMINOOP, '__module__': 'tendermint.crypto.proof_pb2'})
_sym_db.RegisterMessage(DominoOp)
ProofOp = _reflection.GeneratedProtocolMessageType('ProofOp', (_message.Message,), {'DESCRIPTOR': _PROOFOP, '__module__': 'tendermint.crypto.proof_pb2'})
_sym_db.RegisterMessage(ProofOp)
ProofOps = _reflection.GeneratedProtocolMessageType('ProofOps', (_message.Message,), {'DESCRIPTOR': _PROOFOPS, '__module__': 'tendermint.crypto.proof_pb2'})
_sym_db.RegisterMessage(ProofOps)
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/tendermint/tendermint/proto/tendermint/crypto'
    _PROOFOPS.fields_by_name['ops']._options = None
    _PROOFOPS.fields_by_name['ops']._serialized_options = b'\xc8\xde\x1f\x00'
    _PROOF._serialized_start = 74
    _PROOF._serialized_end = 145
    _VALUEOP._serialized_start = 147
    _VALUEOP._serialized_end = 210
    _DOMINOOP._serialized_start = 212
    _DOMINOOP._serialized_end = 266
    _PROOFOP._serialized_start = 268
    _PROOFOP._serialized_end = 318
    _PROOFOPS._serialized_start = 320
    _PROOFOPS._serialized_end = 377
