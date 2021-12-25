from rest_framework import serializers
from .models import File


class FileUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    profile = serializers.CharField()

    class Meta():
        model = File
        fields = '__all__'

class SaveFileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = '__all__'
