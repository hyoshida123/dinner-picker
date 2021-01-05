from rest_framework import serializers
from .user_account_model import User
from api.util.decorators import deprecated_class

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'preferences', 'groups')
