"""TOURISM URL Configuration

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
from django.conf.urls import url, include
from Profile import views
import django.contrib.auth.views as auth_view

urlpatterns = [
    url(r'^register/$', views.signupUser),  ### visitor moved from home to register
    # url(r'^login/$', auth_profile.login ),
    # url('accounts/', include('django.contrib.auth.urls')),
    # url(r'^home/logout$', auth_profile.logout),
    # url(r'^home$', views.temphome),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html'}),
    url(r'^login/account/$', views.viewAccount),
    # url(r'^register/login/account/$', views.viewAccount),

]
