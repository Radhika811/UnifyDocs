from rest_framework import serializers
from docs_app.models.tags import Tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'