from rest_framework import serializers
from aluraflix_api.models import videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videos
        fields = '__all__'

