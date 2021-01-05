from rest_framework import serializers
from .preference_model import Preferences
from api.util.decorators import deprecated_class


@deprecated_class("Use DTO")
class PreferenceSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = ('id', 'food_spicy', 'food_vegan', 'food_vegetarian', 'place_loud')