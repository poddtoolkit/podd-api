import graphene
from graphene_django import DjangoObjectType

from accounts.models import Authority, InvitationCode


class AuthorityType(DjangoObjectType):
    class Meta:
        model = Authority
        fields = (
            "code",
            "name",
        )


class UserProfileType(graphene.ObjectType):
    id = graphene.Int(required=True)
    username = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    authority_name = graphene.String(required=False)

    def resolve_authority_name(parent, info):
        if hasattr(parent, "authority"):
            return parent.authority.name
        return ""


class CheckInvitationCodeType(DjangoObjectType):
    class Meta:
        model = InvitationCode
        fields = ("code", "authority")