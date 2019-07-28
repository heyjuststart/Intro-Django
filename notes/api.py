from rest_framework import serializers, viewsets
from .models import PersonalNote

# convention is to name the serializer classes after what they
# are serializing


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        # import pdb
        #
        # pdb.set_trace()
        # pass

        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

    class Meta:
        model = PersonalNote
        fields = ("title", "content")


class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.all()
