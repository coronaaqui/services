from django.db import models
from django.utils.translation import ugettext_lazy as _

from cbrasil.base import Timestamped
from cbrasil.organizations.models import Organizations
from cbrasil.places.models import Cities, Regions


class Sources(Timestamped):
    name = models.CharField(max_length=64)
    official_site = models.CharField(max_length=64)

    class Meta:
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")

    def __str__(self):
        return self.name


class News(Timestamped):
    title = models.CharField(max_length=64, null=True, blank=True)
    source = models.ForeignKey(Sources, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=120)
    link = models.URLField()

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title


class Achievements(Timestamped):

    PARTIAL_CLOSE = 'P'
    FULLY_CLOSE = 'F'
    REOPEN = 'O'
    STATUS_TYPES = (
        (PARTIAL_CLOSE, 'Partialy close'),
        (FULLY_CLOSE, 'Fully close'),
        (REOPEN, 'Reopen'),
    )

    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True, blank=True, related_name='org_archievements')
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, blank=True, related_name='cities_archievements')
    name = models.CharField(max_length=64, null=True, blank=True)
    from_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)
    undefined_ends_date = models.BooleanField(null=True, blank=True)
    source = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)
    status_type = models.CharField(max_length=1,choices=STATUS_TYPES)

    class Meta:
        verbose_name = _("Achievement")
        verbose_name_plural = _("Achievements")

    def __str__(self):
        return str(self.id)




