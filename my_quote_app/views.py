# -*- coding: utf-8 -*-

from django.shortcuts import render
from my_quote_app.models import Quote

def get_quotes(request):
    return render(request, "quoteTest/home.html",
                  {'quote_list':Quote.objects.all()})