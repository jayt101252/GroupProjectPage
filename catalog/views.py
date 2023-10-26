from .models import Movie, Director, MovieReview, Genre
from django.shortcuts import render
from django.db.models import Avg
<<<<<<< HEAD
from django.views import generic


=======

>>>>>>> 25135bc04f0bf03a9f2cbd7710bcc38667febf50
def index(request):
    """View function for home page of site."""
    num_movies = Movie.objects.all().count()
    num_reviews = MovieReview.objects.all().count()
    num_directors = Director.objects.all().count()

    # Average total star value
    num_average_rating = MovieReview.objects.aggregate(Avg('star_rating'))

    context = {
        'num_movies': num_movies,
        'num_reviews': num_reviews,
        'num_average_rating': num_average_rating,
        'num_directors': num_directors,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
<<<<<<< HEAD


class MovieListView(generic.ListView):
    model = Movie


class MovieDetailView(generic.DetailView):
    model = Movie
=======
>>>>>>> 25135bc04f0bf03a9f2cbd7710bcc38667febf50
