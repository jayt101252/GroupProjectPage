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

    path('moviereview_detail/<int:pk>', views.MovieReviewDetailView.as_view(), name='movieReview_detail'),
    path('moviereview_list/', views.MovieReviewListView.as_view(), name='movieReview_list'),
    path('moviereview/create/', views.WriteMovieReviewByUser.as_view(), name='write_review'),
    path('moviewreview/<int:pk>/update/', views.UpdateMovieReviewByUser.as_view(), name='update_review'),
    path('moviewreview/<int:pk>/delete/', views.moviereview_delete, name='review_delete'),
]
