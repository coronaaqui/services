from django.db import models
from django.utils.translation import ugettext_lazy as _

from cbrasil.base import Timestamped
from cbrasil.places.models import Cities, Regions

# Create your models here.
class Sectors(Timestamped):

    name = models.CharField(max_length=32)
    mini_flag = models.ImageField(upload_to='mini_flags/', null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Sector")
        verbose_name_plural = _("Sectors")

    def __str__(self):
        return self.name


class Organizations(Timestamped):

    name = models.CharField(max_length=32)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, blank=True, null=True)
    sector = models.ForeignKey(Sectors, on_delete=models.CASCADE)
    all_sector = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name