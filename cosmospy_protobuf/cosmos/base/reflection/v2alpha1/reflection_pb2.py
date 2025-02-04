
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0cosmos/base/reflection/v2alpha1/reflection.proto\x12\x1fcosmos.base.reflection.v2alpha1\x1a\x1cgoogle/api/annotations.proto"\xb0\x03\n\rAppDescriptor\x12?\n\x05authn\x18\x01 \x01(\x0b20.cosmos.base.reflection.v2alpha1.AuthnDescriptor\x12?\n\x05chain\x18\x02 \x01(\x0b20.cosmos.base.reflection.v2alpha1.ChainDescriptor\x12?\n\x05codec\x18\x03 \x01(\x0b20.cosmos.base.reflection.v2alpha1.CodecDescriptor\x12O\n\rconfiguration\x18\x04 \x01(\x0b28.cosmos.base.reflection.v2alpha1.ConfigurationDescriptor\x12P\n\x0equery_services\x18\x05 \x01(\x0b28.cosmos.base.reflection.v2alpha1.QueryServicesDescriptor\x129\n\x02tx\x18\x06 \x01(\x0b2-.cosmos.base.reflection.v2alpha1.TxDescriptor"^\n\x0cTxDescriptor\x12\x10\n\x08fullname\x18\x01 \x01(\t\x12<\n\x04msgs\x18\x02 \x03(\x0b2..cosmos.base.reflection.v2alpha1.MsgDescriptor"]\n\x0fAuthnDescriptor\x12J\n\nsign_modes\x18\x01 \x03(\x0b26.cosmos.base.reflection.v2alpha1.SigningModeDescriptor"b\n\x15SigningModeDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x05\x12+\n#authn_info_provider_method_fullname\x18\x03 \x01(\t"\x1d\n\x0fChainDescriptor\x12\n\n\x02id\x18\x01 \x01(\t"[\n\x0fCodecDescriptor\x12H\n\ninterfaces\x18\x01 \x03(\x0b24.cosmos.base.reflection.v2alpha1.InterfaceDescriptor"\xf4\x01\n\x13InterfaceDescriptor\x12\x10\n\x08fullname\x18\x01 \x01(\t\x12j\n\x1cinterface_accepting_messages\x18\x02 \x03(\x0b2D.cosmos.base.reflection.v2alpha1.InterfaceAcceptingMessageDescriptor\x12_\n\x16interface_implementers\x18\x03 \x03(\x0b2?.cosmos.base.reflection.v2alpha1.InterfaceImplementerDescriptor"D\n\x1eInterfaceImplementerDescriptor\x12\x10\n\x08fullname\x18\x01 \x01(\t\x12\x10\n\x08type_url\x18\x02 \x01(\t"W\n#InterfaceAcceptingMessageDescriptor\x12\x10\n\x08fullname\x18\x01 \x01(\t\x12\x1e\n\x16field_descriptor_names\x18\x02 \x03(\t"@\n\x17ConfigurationDescriptor\x12%\n\x1dbech32_account_address_prefix\x18\x01 \x01(\t"%\n\rMsgDescriptor\x12\x14\n\x0cmsg_type_url\x18\x01 \x01(\t"\x1b\n\x19GetAuthnDescriptorRequest"]\n\x1aGetAuthnDescriptorResponse\x12?\n\x05authn\x18\x01 \x01(\x0b20.cosmos.base.reflection.v2alpha1.AuthnDescriptor"\x1b\n\x19GetChainDescriptorRequest"]\n\x1aGetChainDescriptorResponse\x12?\n\x05chain\x18\x01 \x01(\x0b20.cosmos.base.reflection.v2alpha1.ChainDescriptor"\x1b\n\x19GetCodecDescriptorRequest"]\n\x1aGetCodecDescriptorResponse\x12?\n\x05codec\x18\x01 \x01(\x0b20.cosmos.base.reflection.v2alpha1.CodecDescriptor"#\n!GetConfigurationDescriptorRequest"n\n"GetConfigurationDescriptorResponse\x12H\n\x06config\x18\x01 \x01(\x0b28.cosmos.base.reflection.v2alpha1.ConfigurationDescriptor"#\n!GetQueryServicesDescriptorRequest"o\n"GetQueryServicesDescriptorResponse\x12I\n\x07queries\x18\x01 \x01(\x0b28.cosmos.base.reflection.v2alpha1.QueryServicesDescriptor"\x18\n\x16GetTxDescriptorRequest"T\n\x17GetTxDescriptorResponse\x129\n\x02tx\x18\x01 \x01(\x0b2-.cosmos.base.reflection.v2alpha1.TxDescriptor"j\n\x17QueryServicesDescriptor\x12O\n\x0equery_services\x18\x01 \x03(\x0b27.cosmos.base.reflection.v2alpha1.QueryServiceDescriptor"\x86\x01\n\x16QueryServiceDescriptor\x12\x10\n\x08fullname\x18\x01 \x01(\t\x12\x11\n\tis_module\x18\x02 \x01(\x08\x12G\n\x07methods\x18\x03 \x03(\x0b26.cosmos.base.reflection.v2alpha1.QueryMethodDescriptor">\n\x15QueryMethodDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x17\n\x0ffull_query_path\x18\x02 \x01(\t2\xa7\n\n\x11ReflectionService\x12\xcb\x01\n\x12GetAuthnDescriptor\x12:.cosmos.base.reflection.v2alpha1.GetAuthnDescriptorRequest\x1a;.cosmos.base.reflection.v2alpha1.GetAuthnDescriptorResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/base/reflection/v1beta1/app_descriptor/authn\x12\xcb\x01\n\x12GetChainDescriptor\x12:.cosmos.base.reflection.v2alpha1.GetChainDescriptorRequest\x1a;.cosmos.base.reflection.v2alpha1.GetChainDescriptorResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/base/reflection/v1beta1/app_descriptor/chain\x12\xcb\x01\n\x12GetCodecDescriptor\x12:.cosmos.base.reflection.v2alpha1.GetCodecDescriptorRequest\x1a;.cosmos.base.reflection.v2alpha1.GetCodecDescriptorResponse"<\x82\xd3\xe4\x93\x026\x124/cosmos/base/reflection/v1beta1/app_descriptor/codec\x12\xeb\x01\n\x1aGetConfigurationDescriptor\x12B.cosmos.base.reflection.v2alpha1.GetConfigurationDescriptorRequest\x1aC.cosmos.base.reflection.v2alpha1.GetConfigurationDescriptorResponse"D\x82\xd3\xe4\x93\x02>\x12</cosmos/base/reflection/v1beta1/app_descriptor/configuration\x12\xec\x01\n\x1aGetQueryServicesDescriptor\x12B.cosmos.base.reflection.v2alpha1.GetQueryServicesDescriptorRequest\x1aC.cosmos.base.reflection.v2alpha1.GetQueryServicesDescriptorResponse"E\x82\xd3\xe4\x93\x02?\x12=/cosmos/base/reflection/v1beta1/app_descriptor/query_services\x12\xca\x01\n\x0fGetTxDescriptor\x127.cosmos.base.reflection.v2alpha1.GetTxDescriptorRequest\x1a8.cosmos.base.reflection.v2alpha1.GetTxDescriptorResponse"D\x82\xd3\xe4\x93\x02>\x12</cosmos/base/reflection/v1beta1/app_descriptor/tx_descriptorB>Z<github.com/cosmos/cosmos-sdk/server/grpc/reflection/v2alpha1b\x06proto3')
_APPDESCRIPTOR = DESCRIPTOR.message_types_by_name['AppDescriptor']
_TXDESCRIPTOR = DESCRIPTOR.message_types_by_name['TxDescriptor']
_AUTHNDESCRIPTOR = DESCRIPTOR.message_types_by_name['AuthnDescriptor']
_SIGNINGMODEDESCRIPTOR = DESCRIPTOR.message_types_by_name['SigningModeDescriptor']
_CHAINDESCRIPTOR = DESCRIPTOR.message_types_by_name['ChainDescriptor']
_CODECDESCRIPTOR = DESCRIPTOR.message_types_by_name['CodecDescriptor']
_INTERFACEDESCRIPTOR = DESCRIPTOR.message_types_by_name['InterfaceDescriptor']
_INTERFACEIMPLEMENTERDESCRIPTOR = DESCRIPTOR.message_types_by_name['InterfaceImplementerDescriptor']
_INTERFACEACCEPTINGMESSAGEDESCRIPTOR = DESCRIPTOR.message_types_by_name['InterfaceAcceptingMessageDescriptor']
_CONFIGURATIONDESCRIPTOR = DESCRIPTOR.message_types_by_name['ConfigurationDescriptor']
_MSGDESCRIPTOR = DESCRIPTOR.message_types_by_name['MsgDescriptor']
_GETAUTHNDESCRIPTORREQUEST = DESCRIPTOR.message_types_by_name['GetAuthnDescriptorRequest']
_GETAUTHNDESCRIPTORRESPONSE = DESCRIPTOR.message_types_by_name['GetAuthnDescriptorResponse']
_GETCHAINDESCRIPTORREQUEST = DESCRIPTOR.message_types_by_name['GetChainDescriptorRequest']
_GETCHAINDESCRIPTORRESPONSE = DESCRIPTOR.message_types_by_name['GetChainDescriptorResponse']
_GETCODECDESCRIPTORREQUEST = DESCRIPTOR.message_types_by_name['GetCodecDescriptorRequest']
_GETCODECDESCRIPTORRESPONSE = DESCRIPTOR.message_types_by_name['GetCodecDescriptorResponse']
_GETCONFIGURATIONDESCRIPTORREQUEST = DESCRIPTOR.message_types_by_name['GetConfigurationDescriptorRequest']
_GETCONFIGURATIONDESCRIPTORRESPONSE = DESCRIPTOR.message_types_by_name['GetConfigurationDescriptorResponse']
_GETQUERYSERVICESDESCRIPTORREQUEST = DESCRIPTOR.message_types_by_name['GetQueryServicesDescriptorRequest']
_GETQUERYSERVICESDESCRIPTORRESPONSE = DESCRIPTOR.message_types_by_name['GetQueryServicesDescriptorResponse']
_GETTXDESCRIPTORREQUEST = DESCRIPTOR.message_types_by_name['GetTxDescriptorRequest']
_GETTXDESCRIPTORRESPONSE = DESCRIPTOR.message_types_by_name['GetTxDescriptorResponse']
_QUERYSERVICESDESCRIPTOR = DESCRIPTOR.message_types_by_name['QueryServicesDescriptor']
_QUERYSERVICEDESCRIPTOR = DESCRIPTOR.message_types_by_name['QueryServiceDescriptor']
_QUERYMETHODDESCRIPTOR = DESCRIPTOR.message_types_by_name['QueryMethodDescriptor']
AppDescriptor = _reflection.GeneratedProtocolMessageType('AppDescriptor', (_message.Message,), {'DESCRIPTOR': _APPDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(AppDescriptor)
TxDescriptor = _reflection.GeneratedProtocolMessageType('TxDescriptor', (_message.Message,), {'DESCRIPTOR': _TXDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(TxDescriptor)
AuthnDescriptor = _reflection.GeneratedProtocolMessageType('AuthnDescriptor', (_message.Message,), {'DESCRIPTOR': _AUTHNDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(AuthnDescriptor)
SigningModeDescriptor = _reflection.GeneratedProtocolMessageType('SigningModeDescriptor', (_message.Message,), {'DESCRIPTOR': _SIGNINGMODEDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(SigningModeDescriptor)
ChainDescriptor = _reflection.GeneratedProtocolMessageType('ChainDescriptor', (_message.Message,), {'DESCRIPTOR': _CHAINDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(ChainDescriptor)
CodecDescriptor = _reflection.GeneratedProtocolMessageType('CodecDescriptor', (_message.Message,), {'DESCRIPTOR': _CODECDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(CodecDescriptor)
InterfaceDescriptor = _reflection.GeneratedProtocolMessageType('InterfaceDescriptor', (_message.Message,), {'DESCRIPTOR': _INTERFACEDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(InterfaceDescriptor)
InterfaceImplementerDescriptor = _reflection.GeneratedProtocolMessageType('InterfaceImplementerDescriptor', (_message.Message,), {'DESCRIPTOR': _INTERFACEIMPLEMENTERDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(InterfaceImplementerDescriptor)
InterfaceAcceptingMessageDescriptor = _reflection.GeneratedProtocolMessageType('InterfaceAcceptingMessageDescriptor', (_message.Message,), {'DESCRIPTOR': _INTERFACEACCEPTINGMESSAGEDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(InterfaceAcceptingMessageDescriptor)
ConfigurationDescriptor = _reflection.GeneratedProtocolMessageType('ConfigurationDescriptor', (_message.Message,), {'DESCRIPTOR': _CONFIGURATIONDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(ConfigurationDescriptor)
MsgDescriptor = _reflection.GeneratedProtocolMessageType('MsgDescriptor', (_message.Message,), {'DESCRIPTOR': _MSGDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(MsgDescriptor)
GetAuthnDescriptorRequest = _reflection.GeneratedProtocolMessageType('GetAuthnDescriptorRequest', (_message.Message,), {'DESCRIPTOR': _GETAUTHNDESCRIPTORREQUEST, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetAuthnDescriptorRequest)
GetAuthnDescriptorResponse = _reflection.GeneratedProtocolMessageType('GetAuthnDescriptorResponse', (_message.Message,), {'DESCRIPTOR': _GETAUTHNDESCRIPTORRESPONSE, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetAuthnDescriptorResponse)
GetChainDescriptorRequest = _reflection.GeneratedProtocolMessageType('GetChainDescriptorRequest', (_message.Message,), {'DESCRIPTOR': _GETCHAINDESCRIPTORREQUEST, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetChainDescriptorRequest)
GetChainDescriptorResponse = _reflection.GeneratedProtocolMessageType('GetChainDescriptorResponse', (_message.Message,), {'DESCRIPTOR': _GETCHAINDESCRIPTORRESPONSE, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetChainDescriptorResponse)
GetCodecDescriptorRequest = _reflection.GeneratedProtocolMessageType('GetCodecDescriptorRequest', (_message.Message,), {'DESCRIPTOR': _GETCODECDESCRIPTORREQUEST, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetCodecDescriptorRequest)
GetCodecDescriptorResponse = _reflection.GeneratedProtocolMessageType('GetCodecDescriptorResponse', (_message.Message,), {'DESCRIPTOR': _GETCODECDESCRIPTORRESPONSE, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetCodecDescriptorResponse)
GetConfigurationDescriptorRequest = _reflection.GeneratedProtocolMessageType('GetConfigurationDescriptorRequest', (_message.Message,), {'DESCRIPTOR': _GETCONFIGURATIONDESCRIPTORREQUEST, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetConfigurationDescriptorRequest)
GetConfigurationDescriptorResponse = _reflection.GeneratedProtocolMessageType('GetConfigurationDescriptorResponse', (_message.Message,), {'DESCRIPTOR': _GETCONFIGURATIONDESCRIPTORRESPONSE, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetConfigurationDescriptorResponse)
GetQueryServicesDescriptorRequest = _reflection.GeneratedProtocolMessageType('GetQueryServicesDescriptorRequest', (_message.Message,), {'DESCRIPTOR': _GETQUERYSERVICESDESCRIPTORREQUEST, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetQueryServicesDescriptorRequest)
GetQueryServicesDescriptorResponse = _reflection.GeneratedProtocolMessageType('GetQueryServicesDescriptorResponse', (_message.Message,), {'DESCRIPTOR': _GETQUERYSERVICESDESCRIPTORRESPONSE, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetQueryServicesDescriptorResponse)
GetTxDescriptorRequest = _reflection.GeneratedProtocolMessageType('GetTxDescriptorRequest', (_message.Message,), {'DESCRIPTOR': _GETTXDESCRIPTORREQUEST, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetTxDescriptorRequest)
GetTxDescriptorResponse = _reflection.GeneratedProtocolMessageType('GetTxDescriptorResponse', (_message.Message,), {'DESCRIPTOR': _GETTXDESCRIPTORRESPONSE, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(GetTxDescriptorResponse)
QueryServicesDescriptor = _reflection.GeneratedProtocolMessageType('QueryServicesDescriptor', (_message.Message,), {'DESCRIPTOR': _QUERYSERVICESDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(QueryServicesDescriptor)
QueryServiceDescriptor = _reflection.GeneratedProtocolMessageType('QueryServiceDescriptor', (_message.Message,), {'DESCRIPTOR': _QUERYSERVICEDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(QueryServiceDescriptor)
QueryMethodDescriptor = _reflection.GeneratedProtocolMessageType('QueryMethodDescriptor', (_message.Message,), {'DESCRIPTOR': _QUERYMETHODDESCRIPTOR, '__module__': 'cosmos.base.reflection.v2alpha1.reflection_pb2'})
_sym_db.RegisterMessage(QueryMethodDescriptor)
_REFLECTIONSERVICE = DESCRIPTOR.services_by_name['ReflectionService']
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/cosmos/cosmos-sdk/server/grpc/reflection/v2alpha1'
    _REFLECTIONSERVICE.methods_by_name['GetAuthnDescriptor']._options = None
    _REFLECTIONSERVICE.methods_by_name['GetAuthnDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/base/reflection/v1beta1/app_descriptor/authn'
    _REFLECTIONSERVICE.methods_by_name['GetChainDescriptor']._options = None
    _REFLECTIONSERVICE.methods_by_name['GetChainDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/base/reflection/v1beta1/app_descriptor/chain'
    _REFLECTIONSERVICE.methods_by_name['GetCodecDescriptor']._options = None
    _REFLECTIONSERVICE.methods_by_name['GetCodecDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/cosmos/base/reflection/v1beta1/app_descriptor/codec'
    _REFLECTIONSERVICE.methods_by_name['GetConfigurationDescriptor']._options = None
    _REFLECTIONSERVICE.methods_by_name['GetConfigurationDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</cosmos/base/reflection/v1beta1/app_descriptor/configuration'
    _REFLECTIONSERVICE.methods_by_name['GetQueryServicesDescriptor']._options = None
    _REFLECTIONSERVICE.methods_by_name['GetQueryServicesDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/cosmos/base/reflection/v1beta1/app_descriptor/query_services'
    _REFLECTIONSERVICE.methods_by_name['GetTxDescriptor']._options = None
    _REFLECTIONSERVICE.methods_by_name['GetTxDescriptor']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</cosmos/base/reflection/v1beta1/app_descriptor/tx_descriptor'
    _APPDESCRIPTOR._serialized_start = 116
    _APPDESCRIPTOR._serialized_end = 548
    _TXDESCRIPTOR._serialized_start = 550
    _TXDESCRIPTOR._serialized_end = 644
    _AUTHNDESCRIPTOR._serialized_start = 646
    _AUTHNDESCRIPTOR._serialized_end = 739
    _SIGNINGMODEDESCRIPTOR._serialized_start = 741
    _SIGNINGMODEDESCRIPTOR._serialized_end = 839
    _CHAINDESCRIPTOR._serialized_start = 841
    _CHAINDESCRIPTOR._serialized_end = 870
    _CODECDESCRIPTOR._serialized_start = 872
    _CODECDESCRIPTOR._serialized_end = 963
    _INTERFACEDESCRIPTOR._serialized_start = 966
    _INTERFACEDESCRIPTOR._serialized_end = 1210
    _INTERFACEIMPLEMENTERDESCRIPTOR._serialized_start = 1212
    _INTERFACEIMPLEMENTERDESCRIPTOR._serialized_end = 1280
    _INTERFACEACCEPTINGMESSAGEDESCRIPTOR._serialized_start = 1282
    _INTERFACEACCEPTINGMESSAGEDESCRIPTOR._serialized_end = 1369
    _CONFIGURATIONDESCRIPTOR._serialized_start = 1371
    _CONFIGURATIONDESCRIPTOR._serialized_end = 1435
    _MSGDESCRIPTOR._serialized_start = 1437
    _MSGDESCRIPTOR._serialized_end = 1474
    _GETAUTHNDESCRIPTORREQUEST._serialized_start = 1476
    _GETAUTHNDESCRIPTORREQUEST._serialized_end = 1503
    _GETAUTHNDESCRIPTORRESPONSE._serialized_start = 1505
    _GETAUTHNDESCRIPTORRESPONSE._serialized_end = 1598
    _GETCHAINDESCRIPTORREQUEST._serialized_start = 1600
    _GETCHAINDESCRIPTORREQUEST._serialized_end = 1627
    _GETCHAINDESCRIPTORRESPONSE._serialized_start = 1629
    _GETCHAINDESCRIPTORRESPONSE._serialized_end = 1722
    _GETCODECDESCRIPTORREQUEST._serialized_start = 1724
    _GETCODECDESCRIPTORREQUEST._serialized_end = 1751
    _GETCODECDESCRIPTORRESPONSE._serialized_start = 1753
    _GETCODECDESCRIPTORRESPONSE._serialized_end = 1846
    _GETCONFIGURATIONDESCRIPTORREQUEST._serialized_start = 1848
    _GETCONFIGURATIONDESCRIPTORREQUEST._serialized_end = 1883
    _GETCONFIGURATIONDESCRIPTORRESPONSE._serialized_start = 1885
    _GETCONFIGURATIONDESCRIPTORRESPONSE._serialized_end = 1995
    _GETQUERYSERVICESDESCRIPTORREQUEST._serialized_start = 1997
    _GETQUERYSERVICESDESCRIPTORREQUEST._serialized_end = 2032
    _GETQUERYSERVICESDESCRIPTORRESPONSE._serialized_start = 2034
    _GETQUERYSERVICESDESCRIPTORRESPONSE._serialized_end = 2145
    _GETTXDESCRIPTORREQUEST._serialized_start = 2147
    _GETTXDESCRIPTORREQUEST._serialized_end = 2171
    _GETTXDESCRIPTORRESPONSE._serialized_start = 2173
    _GETTXDESCRIPTORRESPONSE._serialized_end = 2257
    _QUERYSERVICESDESCRIPTOR._serialized_start = 2259
    _QUERYSERVICESDESCRIPTOR._serialized_end = 2365
    _QUERYSERVICEDESCRIPTOR._serialized_start = 2368
    _QUERYSERVICEDESCRIPTOR._serialized_end = 2502
    _QUERYMETHODDESCRIPTOR._serialized_start = 2504
    _QUERYMETHODDESCRIPTOR._serialized_end = 2566
    _REFLECTIONSERVICE._serialized_start = 2569
    _REFLECTIONSERVICE._serialized_end = 3888
