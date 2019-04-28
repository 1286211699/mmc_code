#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 17:08
# @Author  : Xuegod Teacher For
# @File    : adminx.py
# @Software: PyCharm
import xadmin

from .models import CityDict, CourseOrg, Teacher



class CityDictAdmin(object):
    '''城市'''

    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
xadmin.site.register(CityDict, CityDictAdmin)

class CourseOrgAdmin(object):
    '''机构'''

    list_display = ['name', 'desc', 'click_nums', 'fav_nums','add_time' ]
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums','city__name','address','add_time']

xadmin.site.register(CourseOrg, CourseOrgAdmin)
class TeacherAdmin(object):
    '''老师'''

    list_display = [ 'name','org', 'work_years', 'work_company','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org__name', 'name', 'work_years', 'work_company','click_nums', 'fav_nums', 'add_time']




xadmin.site.register(Teacher, TeacherAdmin)