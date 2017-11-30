# -*- coding: utf-8 -*-

from django.db import models
class Quote(models.Model):

    class Meta:
        app_label = "my_quote_app"

    aQuote = models.CharField(max_length=255)
    aQuoter = models.CharField(max_length=50)