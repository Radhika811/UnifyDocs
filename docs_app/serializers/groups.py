from rest_framework import serializers
from docs_app.models.groups import Groups

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'