# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

# Create your views here.


def test(request):
    return HttpResponse('welcome my per_blog...')
