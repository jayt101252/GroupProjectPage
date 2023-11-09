from .models import Movie, Director, MovieReview, Genre
from django.shortcuts import render
from django.db.models import Avg
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """View function for home page of site."""
    num_movies = Movie.objects.all().count()
    num_reviews = MovieReview.objects.all().count()
    num_directors = Director.objects.all().count()

    # Average total star value
    num_average_rating = MovieReview.objects.aggregate(Avg('star_rating'))
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_movies': num_movies,
        'num_reviews': num_reviews,
        'num_average_rating': num_average_rating,
        'num_directors': num_directors,
        'num_visits': num_visits,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
class MovieListView(LoginRequiredMixin, generic.ListView):
    model = Movie
class MovieDetailView(LoginRequiredMixin, generic.DetailView):
    model = Movie

class DirectorListView(LoginRequiredMixin, generic.ListView):
    model = Director

class DirectorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Director
