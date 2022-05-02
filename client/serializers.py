from rest_framework import serializers
from workyspacecrm_django import settings

from .models import Client
from .models import Note
from .models import Document


# Serializer client
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        read_only_fields = (
            'created_by',
            'created_at',
            'modified_at',
        ),
        fields = (
            'id',
            'name',
            'contact_person',
            'email',
            'phone',
            'website',
            'created_at',
            'modified_at',
        )


# Serializer note
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = (
            'id',
            'name',
            'body',
        )


class DocumentSerializer(serializers.ModelSerializer):
    # file_url = serializers.SerializerMethodField('get_file_url')

    # def get_file_url(self, obj):
    #     return '%s%s' % (settings.MEDIA_URL, obj.file)

    class Meta:
        model = Document
        fields = (
            'id',
            'name',
            'type',
            'file',
            'description',
        )
