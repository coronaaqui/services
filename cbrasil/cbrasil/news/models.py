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
        verbose_name = _("Fonte")
        verbose_name_plural = _("Fontes")

    def __str__(self):
        return self.name


class News(Timestamped):
    title = models.CharField(max_length=64, null=True, blank=True)
    source = models.ForeignKey(Sources, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=300)
    link = models.URLField()

    class Meta:
        verbose_name = _("Notícia")
        verbose_name_plural = _("Notícias")

    def __str__(self):
        return self.title


class Events(Timestamped):

    PARTIAL_CLOSE = 'P'
    FULLY_CLOSE = 'F'
    REOPEN = 'O'
    STATUS_TYPES = (
        (PARTIAL_CLOSE, 'Funcionamento limitado'),
        (FULLY_CLOSE, 'Totalmente fechado'),
        (REOPEN, 'Aberto'),
    )

    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE, null=True, blank=True, related_name='events', help_text='Selecione SOMENTE caso o evento afete uma organização/empresa especificamente.')
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, null=True, blank=True, help_text='Selecione um estado SOMENTE se a medida afeta todo estado.')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True, blank=True, related_name='events', help_text='Selecione uma cidade SOMENTE se a medida afeta exclusivamente uma cidade.')
    sector = models.ForeignKey(Sectors, on_delete=models.CASCADE, null=True, blank=True, related_name='events', help_text='Selecione um setor caso todo o grupo seja afetado.')
    name = models.CharField(max_length=64, help_text='Nome do serviço/estabelecimento/grupo afetado.')
    from_date = models.DateField(help_text='Início da validade do decreto.')
    to_date = models.DateField(null=True, blank=True, help_text='Fim da validade do decreto. Caso não haja, deixar em branco.')
    undefined_ends_date = models.BooleanField(null=True, blank=True, help_text='O evento tem uma data de término indefinida?')
    source = models.ForeignKey(News, on_delete=models.CASCADE, null=True, blank=True, help_text='Se possível, selecione sempre a notícia associada ao evento. Você pode selecionar uma existente ou criar clicando no +.')
    status_type = models.CharField(max_length=1,choices=STATUS_TYPES, help_text='Escolha o  impacto do evento.')
    estimated_impact = models.IntegerField(default=1, help_text='Número estimado de estabelecimentos/serviços atingidos')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=300, null=True, blank=True, help_text='Na ordem de exibição buscamos exibir o texto do evento, caso não haja, exibiremos o texto da notícia atrelada ao mesmo.')


    class Meta:
        verbose_name = _("Evento")
        verbose_name_plural = _("Eventos")

    def __str__(self):
        return self.name if self.name else str(self.id)

    def clean(self):
        if self.region is None and self.city is None:
            raise ValidationError({
                'region': _('O evento precisa conter uma cidade ou um estado.'),
                'city': _('O evento precisa conter uma cidade ou um estado.'),
            })






