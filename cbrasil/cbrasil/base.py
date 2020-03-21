from django.db import models


class Timestamped(models.Model):
    """
        Abstract model to track creation and last update datetimes.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True