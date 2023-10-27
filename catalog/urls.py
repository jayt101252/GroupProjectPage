from django.urls import path, re-path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_detail/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('director_list/', views.DirectorListView.as_view(), name='director_list'),
    path('director_detail/<int:pk>', views.DirectorDetailView.as_view(), name='director_detail'),
]
