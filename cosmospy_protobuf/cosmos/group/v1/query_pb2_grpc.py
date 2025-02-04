
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.group.v1 import query_pb2 as cosmos_dot_group_dot_v1_dot_query__pb2

class QueryStub(object):
    'Query is the cosmos.group.v1 Query service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.GroupInfo = channel.unary_unary('/cosmos.group.v1.Query/GroupInfo', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupInfoRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupInfoResponse.FromString)
        self.GroupPolicyInfo = channel.unary_unary('/cosmos.group.v1.Query/GroupPolicyInfo', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPolicyInfoRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPolicyInfoResponse.FromString)
        self.GroupMembers = channel.unary_unary('/cosmos.group.v1.Query/GroupMembers', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupMembersRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupMembersResponse.FromString)
        self.GroupsByAdmin = channel.unary_unary('/cosmos.group.v1.Query/GroupsByAdmin', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByAdminRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByAdminResponse.FromString)
        self.GroupPoliciesByGroup = channel.unary_unary('/cosmos.group.v1.Query/GroupPoliciesByGroup', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByGroupRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByGroupResponse.FromString)
        self.GroupPoliciesByAdmin = channel.unary_unary('/cosmos.group.v1.Query/GroupPoliciesByAdmin', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByAdminRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByAdminResponse.FromString)
        self.Proposal = channel.unary_unary('/cosmos.group.v1.Query/Proposal', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalResponse.FromString)
        self.ProposalsByGroupPolicy = channel.unary_unary('/cosmos.group.v1.Query/ProposalsByGroupPolicy', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalsByGroupPolicyRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalsByGroupPolicyResponse.FromString)
        self.VoteByProposalVoter = channel.unary_unary('/cosmos.group.v1.Query/VoteByProposalVoter', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVoteByProposalVoterRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVoteByProposalVoterResponse.FromString)
        self.VotesByProposal = channel.unary_unary('/cosmos.group.v1.Query/VotesByProposal', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByProposalRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByProposalResponse.FromString)
        self.VotesByVoter = channel.unary_unary('/cosmos.group.v1.Query/VotesByVoter', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByVoterRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByVoterResponse.FromString)
        self.GroupsByMember = channel.unary_unary('/cosmos.group.v1.Query/GroupsByMember', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByMemberRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByMemberResponse.FromString)
        self.TallyResult = channel.unary_unary('/cosmos.group.v1.Query/TallyResult', request_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryTallyResultRequest.SerializeToString, response_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryTallyResultResponse.FromString)

class QueryServicer(object):
    'Query is the cosmos.group.v1 Query service.\n    '

    def GroupInfo(self, request, context):
        'GroupInfo queries group info based on group id.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GroupPolicyInfo(self, request, context):
        'GroupPolicyInfo queries group policy info based on account address of group policy.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GroupMembers(self, request, context):
        'GroupMembers queries members of a group\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GroupsByAdmin(self, request, context):
        'GroupsByAdmin queries groups by admin address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GroupPoliciesByGroup(self, request, context):
        'GroupPoliciesByGroup queries group policies by group id.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GroupPoliciesByAdmin(self, request, context):
        'GroupsByAdmin queries group policies by admin address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Proposal(self, request, context):
        'Proposal queries a proposal based on proposal id.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProposalsByGroupPolicy(self, request, context):
        'ProposalsByGroupPolicy queries proposals based on account address of group policy.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VoteByProposalVoter(self, request, context):
        'VoteByProposalVoter queries a vote by proposal id and voter.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VotesByProposal(self, request, context):
        'VotesByProposal queries a vote by proposal.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VotesByVoter(self, request, context):
        'VotesByVoter queries a vote by voter.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GroupsByMember(self, request, context):
        'GroupsByMember queries groups by member address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TallyResult(self, request, context):
        'TallyResult returns the tally result of a proposal. If the proposal is\n        still in voting period, then this query computes the current tally state,\n        which might not be final. On the other hand, if the proposal is final,\n        then it simply returns the `final_tally_result` state stored in the\n        proposal itself.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'GroupInfo': grpc.unary_unary_rpc_method_handler(servicer.GroupInfo, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupInfoRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupInfoResponse.SerializeToString), 'GroupPolicyInfo': grpc.unary_unary_rpc_method_handler(servicer.GroupPolicyInfo, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPolicyInfoRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPolicyInfoResponse.SerializeToString), 'GroupMembers': grpc.unary_unary_rpc_method_handler(servicer.GroupMembers, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupMembersRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupMembersResponse.SerializeToString), 'GroupsByAdmin': grpc.unary_unary_rpc_method_handler(servicer.GroupsByAdmin, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByAdminRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByAdminResponse.SerializeToString), 'GroupPoliciesByGroup': grpc.unary_unary_rpc_method_handler(servicer.GroupPoliciesByGroup, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByGroupRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByGroupResponse.SerializeToString), 'GroupPoliciesByAdmin': grpc.unary_unary_rpc_method_handler(servicer.GroupPoliciesByAdmin, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByAdminRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByAdminResponse.SerializeToString), 'Proposal': grpc.unary_unary_rpc_method_handler(servicer.Proposal, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalResponse.SerializeToString), 'ProposalsByGroupPolicy': grpc.unary_unary_rpc_method_handler(servicer.ProposalsByGroupPolicy, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalsByGroupPolicyRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalsByGroupPolicyResponse.SerializeToString), 'VoteByProposalVoter': grpc.unary_unary_rpc_method_handler(servicer.VoteByProposalVoter, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVoteByProposalVoterRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVoteByProposalVoterResponse.SerializeToString), 'VotesByProposal': grpc.unary_unary_rpc_method_handler(servicer.VotesByProposal, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByProposalRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByProposalResponse.SerializeToString), 'VotesByVoter': grpc.unary_unary_rpc_method_handler(servicer.VotesByVoter, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByVoterRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByVoterResponse.SerializeToString), 'GroupsByMember': grpc.unary_unary_rpc_method_handler(servicer.GroupsByMember, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByMemberRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByMemberResponse.SerializeToString), 'TallyResult': grpc.unary_unary_rpc_method_handler(servicer.TallyResult, request_deserializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryTallyResultRequest.FromString, response_serializer=cosmos_dot_group_dot_v1_dot_query__pb2.QueryTallyResultResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.group.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query is the cosmos.group.v1 Query service.\n    '

    @staticmethod
    def GroupInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/GroupInfo', cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupInfoRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GroupPolicyInfo(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/GroupPolicyInfo', cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPolicyInfoRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPolicyInfoResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GroupMembers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/GroupMembers', cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupMembersRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupMembersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GroupsByAdmin(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/GroupsByAdmin', cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByAdminRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByAdminResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GroupPoliciesByGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/GroupPoliciesByGroup', cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByGroupRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByGroupResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GroupPoliciesByAdmin(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/GroupPoliciesByAdmin', cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByAdminRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupPoliciesByAdminResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Proposal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/Proposal', cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProposalsByGroupPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/ProposalsByGroupPolicy', cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalsByGroupPolicyRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryProposalsByGroupPolicyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VoteByProposalVoter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/VoteByProposalVoter', cosmos_dot_group_dot_v1_dot_query__pb2.QueryVoteByProposalVoterRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryVoteByProposalVoterResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VotesByProposal(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/VotesByProposal', cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByProposalRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByProposalResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VotesByVoter(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/VotesByVoter', cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByVoterRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryVotesByVoterResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GroupsByMember(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/GroupsByMember', cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByMemberRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryGroupsByMemberResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TallyResult(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.group.v1.Query/TallyResult', cosmos_dot_group_dot_v1_dot_query__pb2.QueryTallyResultRequest.SerializeToString, cosmos_dot_group_dot_v1_dot_query__pb2.QueryTallyResultResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
