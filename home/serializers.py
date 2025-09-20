from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'   # include all fields in the model
        read_only_fields = ['owner']  # owner cannot be set manually
