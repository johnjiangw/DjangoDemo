#!/usr/bin/env python
# coding:utf-8
# author:john
"""
登录
"""
import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


def index(request):
    """
    登录初始页面
    :param request:
    :return:
    """
    content = {
        "title": settings.APP_NAME,
        "copyright": datetime.datetime.now().year,
    }
    return render(request, "login.html", content)


def verifycode(request):
    """
    获取验证码及图片
    :param request:
    :return:
    """
    import DjangoDemo.common.verifycode as vc
    verify = vc.VerifyCode()
    code = verify.get_verify_code(length=4)
    imgbuffer = verify.get_verify_img(code)
    return HttpResponse(imgbuffer.getvalue(), content_type='image/png')


@csrf_exempt
def check(request):
    """
    ajax登陆验证
    :param request:
    :return:
    """
    response = {}
    req = json.loads(request.body)


    # return HttpResponse(json.dumps(response), content_type="application/json")
    return JsonResponse(response)
