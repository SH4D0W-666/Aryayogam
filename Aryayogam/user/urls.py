from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
app_name= 'user'

urlpatterns = [

    url(r'^$', views.profile_list, name='list'),
    url(r'^about/$', views.about, name='about'),

    url(r'^search/$', views.profile_search_list, name='search1'),
    url(r'^search_by_id/$', views.profile_search_id, name='search2'),

    url(r'^create/$', views.profile_create, name='create'),
    url(r'^myprofile/$', views.my_profile, name='myprofile'),
    url(r'^all_profiles/$', views.profile_list_all, name='allprofiles'),

    url(r'^myprofile/edit/$', views.myprofile_update, name='myedit'),

    url(r'^(?P<slug>[\w.@+-]+)/$', views.profile_detail, name='detail'),
    url(r'^(?P<slug>[\w.@+-]+)/edit/$', views.profile_update, name='edit'),

    url(r'^(?P<slug>[\w.@+-]+)/delete/$', views.profile_delete, name="delete"),

]
