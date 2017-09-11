#coding=utf-8
"""zqxt_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from calc import views as calc_views

urlpatterns = [
    url(r'^$', calc_views.index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^add/$', calc_views.add, name='add'), # 注意修改了这一行
    # url(r'^add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    #注意看重点 add 变成了 new_add，但是后面的 name='add2' 没改，这时 {% url 'add2' 4 5 %} 就会渲染对应的网址成 /new_add/4/5/
    url(r'^new_add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^add/(\d+)/(\d+)/$', calc_views.old_add2_redirect),#旧的url重定向了
]
