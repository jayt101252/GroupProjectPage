from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movie_detail/<int:pk>', views.MovieDetailView.as_view(), name='movie_detail'),
]
=======

]
>>>>>>> 25135bc04f0bf03a9f2cbd7710bcc38667febf50
