# -*- coding:utf-8 -*-
# Author:Francis
from django.contrib import admin
from django.conf.urls import url,include
from blog import views

urlpatterns=[
    # 无命名分组
    # 访问 http://127.0.0.1:8088/article/2018/02 year:2018  我是想进入2018/02，最后页面返回year:2018 month:02，可却返回了year:2018
    # 原因:article/2018/02前面的article/2018全部匹配上了，就直接进入了article_year视图，不会进入下面的article_year_month。此时正则匹配出加一个$，表示结尾，此时就不会出现上述情况了。
    # url(r'article/(\d{4})',views.article_year),
    url(r'article/(\d{4})$', views.article_year),
    # 有命名分组
    # ?P没有正则意义，只是代表要起一个命名分组
    url(r'article/(?P<year>\d{4})/(?P<month>\d{2})', views.article_year_month),
    url(r'register', views.register, name='reg'),
]
