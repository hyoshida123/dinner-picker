from django.db import models
from api.models.preference.preference_model import Preferences

class FoodCategoryLiked(models.Model):
    label = models.CharField(max_length=20)
    preferences = models.ForeignKey(Preferences, on_delete=models.CASCADE)

class FoodCategoryDisliked(models.Model):
    label = models.CharField(max_length=20)
    preferences = models.ForeignKey(Preferences, on_delete=models.CASCADE)