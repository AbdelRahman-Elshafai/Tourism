"""Tourism URL Configuration

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
from django.conf.urls import url , include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^Control/', include('Control.urls')),
    url(r'^LandingPage/', include('LandingPage.urls')),

||||||| merged common ancestors
    url(r'^Control/', include('Control.urls'))
=======
    url(r'^Control/', include('Control.urls')),
    url(r'^Profile/', include('Profile.urls')),

>>>>>>> 3da1828b54d6effefd078a1bb8889b8e085ebafa
]
