"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from DjangoDemo.controls import login, index, desktop, user, role

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login', login.index),#登录默认页
    path('verifycode', login.verifycode),#验证码图片
    path('login/check', login.check),#登录验证
    path('index', index.index),#登录后主页
    path('desktop', desktop.index),
    path('user', user.index),
    path('user/list', user.list),#用户列表ajax用
    path('user/add', user.add),
    # path('user/edit', user.edit),
    re_path(r'^user/edit/(\d+)?$', user.edit),#编辑用户
    path('user/remove', user.remove),
    path('role', role.index),
    path('role/list', role.list),#角色列表ajax用
    path('role/add', role.add),
    re_path(r'^role/edit/(\d+)?$', role.edit),#编辑角色
    path('role/remove', role.remove),

]
