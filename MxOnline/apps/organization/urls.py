#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 14:14
# @Author  : Xuegod Teacher For
# @File    : urls.py
# @Software: PyCharm
from organization.views import OrgView, AddUserAskView,OrgCourseView
from django.urls import path,re_path
#写上app的名字
app_name = 'organization'
from .views import *
urlpatterns = [
    path('list/',OrgView.as_view(),name = 'org_list'),
    path('add_ask/',AddUserAskView.as_view(),name = 'add_ask'),
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
    re_path('course/(?P<org_id>\d+)/',OrgCourseView.as_view(),name = 'org_course'),
]