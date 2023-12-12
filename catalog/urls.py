from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from . import views


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
    path('moviereview_detail/<int:pk>', views.MovieReviewDetailView.as_view(), name='review_detail'),
    path('moviereview_list/', views.MovieReviewListView.as_view(), name='moviereview_list'),
    path('moviereview/create/', views.WriteMovieReviewByUser.as_view(), name='moviereview_create'),
    path('moviewreview/<int:pk>/update/', views.UpdateMovieReviewByUser.as_view(), name='moviereview_update'),
    path('moviewreview/<int:pk>/delete/', views.moviereview_delete, name='moviereview_delete'),
    path('director/create/', views.DirectorCreate.as_view(), name='director_create'),
    path('director/<int:pk>/update/', views.DirectorUpdate.as_view(), name='director_update'),
    path('director/<int:pk>/delete/', views.director_delete, name='director_delete'),
    path('movie/create/', views.MovieCreate.as_view(), name='movie_create'),
    path('movie/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movie/<int:pk>/update/', views.movie_delete, name='movie_delete'),
]
