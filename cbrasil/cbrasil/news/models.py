from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from cbrasil.base import Timestamped
from cbrasil.organizations.models import Organizations
from cbrasil.places.models import Cities, Regions
from cbrasil.organizations.models import Sectors


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


class Events(Timestamped):

    PARTIAL_CLOSE = 'P'
    FULLY_CLOSE = 'F'
    REOPEN = 'O'
    STATUS_TYPES = (
        (PARTIAL_CLOSE, 'Partialy close'),
        (FULLY_CLOSE, 'Fully close'),
        (REOPEN, 'Open'),
    )

    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    sector = models.ForeignKey(Sectors, on_delete=models.CASCADE, null=True, blank=True, related_name='events')
    name = models.CharField(max_length=64, null=True, blank=True)
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    undefined_ends_date = models.BooleanField(null=True, blank=True)
    source = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True)
    status_type = models.CharField(max_length=1,choices=STATUS_TYPES)
    estimated_impact = models.IntegerField(default=1, help_text='Número estimado de estabelecimentos/serviços atingidos')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name if self.name else str(self.id)

    def clean(self):
        if self.region is None and self.city is None:
            raise ValidationError({
                'region': _('O evento precisa conter uma cidade ou um estado.'),
                'city': _('O evento precisa conter uma cidade ou um estado.'),
            })






