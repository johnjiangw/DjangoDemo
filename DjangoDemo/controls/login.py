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
from DjangoDemo.models import User

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
    request.session['code'] = code
    imgbuffer = verify.get_verify_img(code)
    return HttpResponse(imgbuffer.getvalue(), content_type='image/png')


@csrf_exempt
def check(request):
    """
    ajax登陆验证
    :param request:
    :return:
    """
    rep = {
        "code": 0,
        "msg": "请求参数为空",
    }
    data = json.loads(request.body)
    # print(request.session['code'])
    if request.session['code'] is not None and data['code'] == request.session['code']:
        user = User.objects.filter(user_name=data['username'], pwd=data['pwd'])
        if user is None:
            rep['msg'] = '用户名或密码错误'
        else:
            rep["code"] = 1
            rep['msg'] = '成功'
            request.session['username'] = user[0].user_name
            del request.session['code']
    else:
        rep['msg'] = '验证码错误'

    return JsonResponse(rep)
