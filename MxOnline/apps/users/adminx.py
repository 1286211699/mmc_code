#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 14:21
# @Author  : Xuegod Teacher For
# @File    : adminx.py
# @Software: PyCharmi
import xadmin
from .models import EmailVerifyRecord
class EmailVerifyRecordAdmin(object):
    #显示的列
    list_display = ['code','email','send_type','send_time']
    #搜索的字段，不要添加时间搜索
    search_fields = ['code','email','send_type']
    #过滤
    list_filter = ['code','email','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
from .models import Banner
class BannerAdmin(object):
    list_dispaly = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']
xadmin.site.register(Banner,BannerAdmin)
#修改主题
from xadmin import views
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)
#全局修改固定写法
class GlobalSettings(object):
    #修改title
    site_title = 'For的后台管理'
    #修改footer
    site_footer = 'For的小公司'
    #收起菜单
    menu_style = 'accordion'
xadmin.site.register(views.CommAdminView,GlobalSettings)

