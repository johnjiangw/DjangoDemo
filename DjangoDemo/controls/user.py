#!/usr/bin/env python
# coding:utf-8
# author:john
"""
description
"""
from django.http import HttpResponse
from django.shortcuts import render
from DjangoDemo.models import User


def index(request):
    """"
    用户主界面
    """
    content = {}
    content["data"] = User.objects.all()
    return render(request, "user.html", content)


def edit(request):
    content = {}
    return render(request, content)
