# coding=utf-8
'''
Created on 2015年3月23日

@author: Administrator
'''
from django.conf.urls import patterns,url
from evernote_web import views

urlpatterns = patterns('',
                       url(r'^$',views.index,name='index'),
                       url(r'^(?P<user_id>\d+)/$',views.notebooks,name='notebooks'),
                       url(r'^(?P<user_id>\d+)/(?P<notebook_id>\d+)/$',views.notes,name='notes')
                       )