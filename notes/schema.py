from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import PersonalNote


# connect model to class PersonalNoteType
class PersonalNoteType(DjangoObjectType):
    class Meta:
        model = PersonalNote  # which model to export for Graphene
        interfaces = (graphene.relay.Node,)  # type of entity

# connect PersonalNoteType to query
class Query(graphene.ObjectType):

    # this class property must match the resolve methodname
    personalNotes = graphene.List(PersonalNoteType)

    # must match the property above
    # also names the resource for the graphql query
    def resolve_personalNotes(self, info):
        user = info.context.user # similar to api.py

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)

# expose query to graphene
schema = graphene.Schema(query=Query)
