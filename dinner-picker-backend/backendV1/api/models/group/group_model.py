from django.db import models

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    meeting_time = models.DateTimeField(editable=True, blank=True)

    class Meta:
        ordering = ordering = ('created',)
