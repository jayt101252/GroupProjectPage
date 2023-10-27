from django.urls import path, include, re-path
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':
    settings.MEDIA_ROOT}), #serve media files when deployed
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':
    settings.STATIC_ROOT}), #serve static files when deployed
    path('', views.index, name='index'),
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_detail/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('director_list/', views.DirectorListView.as_view(), name='director_list'),
    path('director_detail/<int:pk>', views.DirectorDetailView.as_view(), name='director_detail'),
]
