#!/usr/bin/env python
# coding:utf-8
# author:john
"""
description
"""
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def index(request):
    """"主页"""
    content = {
        "title": settings.APP_NAME,
    }
    content["username"] = request.session['username']
    return render(request, "index.html", content)

