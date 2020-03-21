from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from cbrasil.base import Timestamped
from cbrasil.places.models import Cities, Regions

# Create your models here.
class Sectors(Timestamped):

    name = models.CharField(max_length=32)
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
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name

    def clean(self):
        if self.region is None and self.city is None:
            raise ValidationError({
                'region': _('A organização precisa conter uma cidade ou um estado.'),
                'city': _('A organização precisa conter uma cidade ou um estado.'),
            })