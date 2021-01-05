from rest_framework import serializers
from .group_model import Group
from api.util.decorators import deprecated_class

@deprecated_class("Use DTO")
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'created', 'name')