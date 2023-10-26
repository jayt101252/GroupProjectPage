from django.urls import path, include, re_path
from django.views.static import serve
<<<<<<< HEAD
from django.conf import setting
=======
from django.conf import settings
>>>>>>> ad22823ca48c50b482abb7bec6b667ee1d377bc2
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
<<<<<<< HEAD
        #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        #serve static files when deployed

]
=======
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    head,
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_detail/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
            ]

>>>>>>> ad22823ca48c50b482abb7bec6b667ee1d377bc2
