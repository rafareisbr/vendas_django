from django.db import models


class TimeStampedModel(models.Model):
    """
        Modelo abstrato, não gera migration própria.
        Objetivo: Imbutir campos de timestamp nos modelos através de herança.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
