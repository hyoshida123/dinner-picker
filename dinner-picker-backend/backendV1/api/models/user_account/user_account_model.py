from django.db import models

from api.models.preference.preference_model import Preferences
from api.models.group.group_model import Group

class User(models.Model):
    id = models.AutoField(primary_key=True)
    # TODO remove unique later once you create an access token field
    name = models.CharField(max_length=20, null=False, unique=True, blank=False)
    preferences = models.OneToOneField(Preferences, on_delete=models.CASCADE, null=False)
    groups = models.ManyToManyField(Group, blank=False)

    def save(self, *args, **kwargs):
        """
        @override
        """
        # name is always lowercase
        self.name = self.name.lower()
        super(User, self).save(*args, **kwargs)
