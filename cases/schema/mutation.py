import graphene

from .mutations import (
    AdminCaseDefinitionCreateMutation,
    AdminCaseDefinitionUpdateMutation,
    AdminStateDefinitionCreateMutation,
    AdminStateDefinitionUpdateMutation,
    AdminStateStepCreateMutation,
    AdminStateStepUpdateMutation,
    AdminStateTransitionCreateMutation,
    AdminStateTransitionUpdateMutation,
    PromoteToCaseMutation,
    ForwardStateMutation,
)


class Mutation(graphene.ObjectType):
    promote_to_case = PromoteToCaseMutation.Field()
    admin_case_definition_create = AdminCaseDefinitionCreateMutation.Field()
    admin_case_definition_update = AdminCaseDefinitionUpdateMutation.Field()
    admin_state_definition_create = AdminStateDefinitionCreateMutation.Field()
    admin_state_definition_update = AdminStateDefinitionUpdateMutation.Field()
    admin_state_step_create = AdminStateStepCreateMutation.Field()
    admin_state_step_update = AdminStateStepUpdateMutation.Field()
    admin_state_transition_create = AdminStateTransitionCreateMutation.Field()
    admin_state_transition_update = AdminStateTransitionUpdateMutation.Field()
    forward_state = ForwardStateMutation.Field()
