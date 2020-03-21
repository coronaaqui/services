from django.db import models
from django.utils.translation import ugettext_lazy as _

from cbrasil.base import Timestamped


class Regions(Timestamped):

    name = models.CharField(max_length=32)
    official_site = models.CharField(max_length=64, null=True, blank=True, default=None)
    health_site = models.CharField(max_length=64, null=True, blank=True, default=None)
    official_site = models.CharField(max_length=64, null=True, blank=True, default=None)
    mini_flag = models.ImageField(upload_to='mini_flags/', null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name

class Cities(Timestamped):

    name = models.CharField(max_length=32)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    official_site = models.CharField(max_length=64, null=True, blank=True, default=None)
    health_site = models.CharField(max_length=64, null=True, blank=True, default=None)
    official_site = models.CharField(max_length=64, null=True, blank=True, default=None)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name