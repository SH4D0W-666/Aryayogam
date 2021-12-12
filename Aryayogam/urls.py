"""Aryayogam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from user import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^/', include(('user.urls', ''), namespace="home")),
    # url(r'^about/', include(('user.urls', 'about'), namespace="about")),
    url(r'^profiles/', include(('user.urls', 'profiles'), namespace= "profiles")),
    url(r'^register/', include(('user.urls', 'register'), namespace= "register")),
    url(r'^register/', views.register, name="register"),
    url(r'^login/', views.login_user,name= "login"),
    url(r'^logout/', views.logout_view,name= "logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
