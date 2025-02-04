
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ibc/applications/transfer/v1/tx.proto\x12\x1cibc.applications.transfer.v1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1fibc/core/client/v1/client.proto"\xd5\x02\n\x0bMsgTransfer\x12+\n\x0bsource_port\x18\x01 \x01(\tB\x16\xf2\xde\x1f\x12yaml:"source_port"\x121\n\x0esource_channel\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"source_channel"\x12.\n\x05token\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06sender\x18\x04 \x01(\t\x12\x10\n\x08receiver\x18\x05 \x01(\t\x12Q\n\x0etimeout_height\x18\x06 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1d\xf2\xde\x1f\x15yaml:"timeout_height"\xc8\xde\x1f\x00\x127\n\x11timeout_timestamp\x18\x07 \x01(\x04B\x1c\xf2\xde\x1f\x18yaml:"timeout_timestamp":\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00"\x15\n\x13MsgTransferResponse2o\n\x03Msg\x12h\n\x08Transfer\x12).ibc.applications.transfer.v1.MsgTransfer\x1a1.ibc.applications.transfer.v1.MsgTransferResponseB9Z7github.com/cosmos/ibc-go/v3/modules/apps/transfer/typesb\x06proto3')
_MSGTRANSFER = DESCRIPTOR.message_types_by_name['MsgTransfer']
_MSGTRANSFERRESPONSE = DESCRIPTOR.message_types_by_name['MsgTransferResponse']
MsgTransfer = _reflection.GeneratedProtocolMessageType('MsgTransfer', (_message.Message,), {'DESCRIPTOR': _MSGTRANSFER, '__module__': 'ibc.applications.transfer.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgTransfer)
MsgTransferResponse = _reflection.GeneratedProtocolMessageType('MsgTransferResponse', (_message.Message,), {'DESCRIPTOR': _MSGTRANSFERRESPONSE, '__module__': 'ibc.applications.transfer.v1.tx_pb2'})
_sym_db.RegisterMessage(MsgTransferResponse)
_MSG = DESCRIPTOR.services_by_name['Msg']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/cosmos/ibc-go/v3/modules/apps/transfer/types'
    _MSGTRANSFER.fields_by_name['source_port']._options = None
    _MSGTRANSFER.fields_by_name['source_port']._serialized_options = b'\xf2\xde\x1f\x12yaml:"source_port"'
    _MSGTRANSFER.fields_by_name['source_channel']._options = None
    _MSGTRANSFER.fields_by_name['source_channel']._serialized_options = b'\xf2\xde\x1f\x15yaml:"source_channel"'
    _MSGTRANSFER.fields_by_name['token']._options = None
    _MSGTRANSFER.fields_by_name['token']._serialized_options = b'\xc8\xde\x1f\x00'
    _MSGTRANSFER.fields_by_name['timeout_height']._options = None
    _MSGTRANSFER.fields_by_name['timeout_height']._serialized_options = b'\xf2\xde\x1f\x15yaml:"timeout_height"\xc8\xde\x1f\x00'
    _MSGTRANSFER.fields_by_name['timeout_timestamp']._options = None
    _MSGTRANSFER.fields_by_name['timeout_timestamp']._serialized_options = b'\xf2\xde\x1f\x18yaml:"timeout_timestamp"'
    _MSGTRANSFER._options = None
    _MSGTRANSFER._serialized_options = b'\xe8\xa0\x1f\x00\x88\xa0\x1f\x00'
    _MSGTRANSFER._serialized_start = 159
    _MSGTRANSFER._serialized_end = 500
    _MSGTRANSFERRESPONSE._serialized_start = 502
    _MSGTRANSFERRESPONSE._serialized_end = 523
    _MSG._serialized_start = 525
    _MSG._serialized_end = 636
