"""django_lesson URL Configuration

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
from django.conf.urls import url,include
from blog import views
'''
   r 开头的python字符串是 raw 字符串，所以里面的所有字符都不会被转义，
   比如r'\n'这个字符串就是一个反斜杆加上一字母n，而'\n'我们知道这是个换行符。
   因此，上面的'\\\\'你也可以写成r'\\'，这样，应该就好理解很多了。可以看下面这段：
  '''
urlpatterns = [
    url(r'admin/',admin.site.urls),
    url(r'show_time/',views.show_time),
    # 路由分发
    url(r'blog/',include('blog.urls')),
]
