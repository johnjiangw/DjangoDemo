#!/usr/bin/env python
# coding:utf-8
# author:john
"""
用户操作
"""
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from DjangoDemo.models import User


def index(request):
    """"
    用户主界面
    """
    return render(request, "user.html")


@csrf_exempt
def list(request):
    """
    用户列表服务端分页
    :param request:
    :return:
    """
    pageindex = 1
    pagesize = settings.PAGE_SIZE
    if request.POST["page"] is not None:
        pageindex = request.POST["page"]
    if request.POST["rows"] is not None:
        pagesize = request.POST["rows"]
    user_all = User.objects.order_by("-user_id")  # 前面加'-'表示倒序
    pager = Paginator(user_all, pagesize)
    try:
        rows = pager.page(pageindex)  # 尝试获取请求的页数
    except PageNotAnInteger:  # 请求页数错误
        rows = pager.page(1)
    except EmptyPage:
        rows = pager.page(pager.num_pages)
    # 需将对象转换一次json
    user_list = []
    for u in rows:
        user_list.append({
            "user_id": u.user_id,
            "user_name": u.user_name,
            "age": u.age,
            "last_update": u.last_update,
            "state": u.state,
        })
    rep = {
        "total": pager.count,
        "rows": user_list,
    }
    return JsonResponse(rep)


@csrf_exempt
def add(request):
    """
    添加用户的ajax处理
    :param request:
    :return:
    """
    # data = json.loads(request.body)# ajax post时取值
    user_name = request.POST["user_name"]  # 表单post时取值
    age = request.POST["age"]
    state = request.POST["state"]
    rep = {}
    try:
        #  方式1 create
        # User.objects.create(user_name=user_name, age=age, state=state)
        #  方式2 save
        # obj = User(user_name=user_name, age=age, state=state)
        # obj.save()
        #  方式3 dict
        dic = {
            'user_name': user_name,
            'age': age,
            'state': state,
        }
        User.objects.create(**dic)
        rep["code"] = 1
        rep["msg"] = '成功'
    except:
        rep["code"] = 0
        rep["msg"] = '添加失败，请稍候再试'
    return JsonResponse(rep)


@csrf_exempt
def edit(request, id):
    """
    编辑用户
    :param request:
    :param id: 用户id
    :return:
    """
    rep = {
        "code": 0,
        "msg": "请求参数为空",
    }
    if id is not None:
        try:
            #  方式1 update
            # dic = {
            #     'user_name': request.POST["user_name"],
            #     'age': request.POST["age"],
            #     'state': request.POST["state"],
            # }
            # User.objects.filter(user_id=id).update(**dic)
            #  方式2 save
            obj = User.objects.get(user_id=id)
            obj.user_name = request.POST["user_name"]
            obj.age = request.POST["age"]
            obj.state = request.POST["state"]
            obj.save()
            rep["code"] = 1
            rep["msg"] = "成功"
        except:
            rep["msg"] = "编辑失败，请稍候再试"

    return JsonResponse(rep)


@csrf_exempt
def remove(request):
    """
    删除用户
    :param request:
    :return:
    """
    rep = {
        "code": 0,
        "msg": "请求参数为空",
    }
    if request.POST["id"] is not None:
        try:
            User.objects.filter(user_id=request.POST["id"]).delete()
            rep["code"] = 1
            rep["msg"] = "成功"
        except:
            rep["msg"] = "删除失败，请稍候再试"
    return JsonResponse(rep)
