#!/usr/bin/env python
# coding:utf-8
# author:john
"""
刚登录后的默认页，如各报表等
"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    content = {}
    return render(request, "desktop.html", content)
