from django.db import models

class Preferences(models.Model):

    PREFERENCE_CHOICES = (
        (-3, 'must not have'),
        (-2, 'really do not like'),
        (-1, 'do not like'),
        (0, 'have no preference over'),
        (1, 'like'),
        (2, 'really like'),
        (3, 'must have')
    )
    # foodCategoryLiked
    # foodCategoryDisliked
    id = models.AutoField(primary_key=True)
    food_spicy = models.IntegerField(choices=PREFERENCE_CHOICES, default=0)
    food_vegan = models.IntegerField(choices=PREFERENCE_CHOICES, default=0)
    food_vegetarian = models.IntegerField(choices=PREFERENCE_CHOICES, default=0)
    place_loud = models.IntegerField(choices=PREFERENCE_CHOICES, default=0)
