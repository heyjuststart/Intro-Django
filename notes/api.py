from rest_framework import serializers, viewsets
from .models import PersonalNote

# convention is to name the serializer classes after what they
# are serializing


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNote
        fields = ("title", "content")


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
