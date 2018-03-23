#!/usr/bin/env python
# coding:utf-8
# author:john
"""
实体类
"""
from django.db import models
from django.utils import timezone


class User(models.Model):
    """
    用户实体
    """
    class Meta:
        db_table = 'user'
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20, blank=False)
    age = models.IntegerField()
    pwd = models.CharField(max_length=32, blank=False, default='123456')
    state = models.SmallIntegerField(blank=False, default=1)
    last_update = models.DateTimeField(default=timezone.now)


class Role(models.Model):
    """
    角色实体
    """
    class Meta:
        db_table = 'role'
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=20, blank=False)
    state = models.SmallIntegerField(blank=False, default=1)
    last_update = models.DateTimeField(default=timezone.now)
