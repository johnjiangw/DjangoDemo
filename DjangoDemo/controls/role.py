#!/usr/bin/env python
# coding:utf-8
# author:john
"""
角色操作
"""
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from DjangoDemo.models import Role


def index(request):
    """"
    角色主界面
    """
    return render(request, "role.html")


@csrf_exempt
def list(request):
    """
    角色列表服务端分页
    :param request:
    :return:
    """
    pageindex = 1
    pagesize = settings.PAGE_SIZE
    if request.POST["page"] is not None:
        pageindex = request.POST["page"]
    if request.POST["rows"] is not None:
        pagesize = request.POST["rows"]
    role_all = Role.objects.order_by("-role_id")# 前面加'-'表示倒序
    pager = Paginator(role_all, pagesize)
    try:
        # 尝试获取请求的页数
        rows = pager.page(pageindex)
        # 请求页数错误
    except PageNotAnInteger:
        rows = pager.page(1)
    except EmptyPage:
        rows = pager.page(pager.num_pages)
    # 需将对象转换一次json
    role_list = []
    for u in rows:
        role_list.append({
            "role_id": u.role_id,
            "role_name": u.role_name,
            "last_update": u.last_update,
            "state": u.state,
        })
    rep = {
        "total": pager.count,
        "rows": role_list,
    }
    return JsonResponse(rep)


@csrf_exempt
def add(request):
    """
    添加角色的ajax处理
    :param request:
    :return:
    """
    # data = json.loads(request.body)# ajax post时取值
    role_name = request.POST["role_name"]#表单post时取值
    state = request.POST["state"]
    rep = {}
    try:
        #方式1 create
        # Role.objects.create(role_name=role_name, state=state)
        #方式2 save
        # obj = Role(role_name=role_name, state=state)
        # obj.save()
        #方式3 dict
        dic = {
            'role_name': role_name,
            'state': state,
        }
        Role.objects.create(**dic)
        rep["code"] = 1
        rep["msg"] = '成功'
    except:
        rep["code"] = 0
        rep["msg"] = '添加失败，请稍候再试'
    return JsonResponse(rep)


@csrf_exempt
def edit(request, id):
    """
    编辑角色
    :param request:
    :param id: id
    :return:
    """
    rep = {
        "code": 0,
        "msg": "请求参数为空",
    }
    if id is not None:
        try:
            #方式1 update
            # dic = {
            #     'role_name': request.POST["role_name"],
            #     'state': request.POST["state"],
            # }
            # Role.objects.filter(role_id=id).update(**dic)
            #方式2 save
            obj = Role.objects.get(role_id=id)
            obj.role_name = request.POST["role_name"]
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
    删除角色
    :param request:
    :return:
    """
    rep = {
        "code": 0,
        "msg": "请求参数为空",
    }
    if request.POST["id"] is not None:
        try:
            Role.objects.filter(role_id=request.POST["id"]).delete()
            rep["code"] = 1
            rep["msg"] = "成功"
        except:
            rep["msg"] = "删除失败，请稍候再试"
    return JsonResponse(rep)
