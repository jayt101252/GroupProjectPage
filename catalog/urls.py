from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import setting
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        #serve static files when deployed

]