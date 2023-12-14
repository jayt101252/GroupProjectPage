from .models import Movie, Director, MovieReview, Genre
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required




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
    return render(request, 'catalog/index.html', context=context)


class MovieListView(LoginRequiredMixin, generic.ListView):
    model = Movie

class MovieDetailView(LoginRequiredMixin, generic.DetailView):
    model = Movie

class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'director', 'description', 'runtime', 'genre']

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'director', 'description', 'runtime', 'genre']

def movie_delete(request, pk):
    author = get_object_or_404(Movie, pk=pk)
    try:
        movie.delete()
        messages.success(request, (movie.title + ' ' + ' has been deleted. Associated reviews deleting.'))
    except:
        messages.success(request, (movie.title + ' ' + 'cannot be deleted.'))
    return redirect('movie_list')

class DirectorListView(LoginRequiredMixin, generic.ListView):
    model = Director

class DirectorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Director

class DirectorCreate(CreateView):
    model = Director
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'director_photo']

class DirectorUpdate(UpdateView):
    model = Director
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'director_photo']

def director_delete(request, pk):
    author = get_object_or_404(Director, pk=pk)
    try:
        director.delete()
        messages.success(request, (director.first_name + ' ' +
                                   director.last_name +" has been deleted"))
    except:
        messages.success(request, (director.first_name + ' ' + director.last_name + 'cannot be deleted. Movies exist '
                                                                                    'for the director'))
    return redirect('director_list')


class MovieReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = MovieReview

class MovieReviewListView(LoginRequiredMixin, generic.ListView):
    model = MovieReview


### Movie review create, update, and delete functionality in 2 classes and def below ###
class WriteMovieReviewByUser(CreateView):
    model = MovieReview
    fields = ['caption', 'star_rating', 'review_text']


class UpdateMovieReviewByUser(UpdateView):
    model = MovieReview
    fields = ['caption', 'star_rating', 'review_text']


def moviereview_delete(request, pk):
    moviereview = get_object_or_404(MovieReview, pk=pk)
    try:
        moviereview.delete()
        messages.success(request, (moviereview.user + "\'s review on" + moviereview.movie + " has been deleted!"))
    except:
        messages.success(request, (moviereview.user + '\'s review on' + moviereview.movie + ' cannot be deleted.'))
    return redirect('base')
@login_required
def view_profile(request):
    profile = request.user.profile
    preferences = profile.preferences.all()
    return render(request, 'catalog/profile.html', {'profile': profile, 'preferences': preferences})


@login_required
def edit_profile(request):
    profile = request.user.profile
    all_genres = Genre.objects.all()
    user_reviews = MovieReview.objects.filter(user=request.user)  # Fetch user's reviews

    if request.method == 'POST':
        bio = request.POST.get('bio')
        selected_preferences = request.POST.getlist('preferences')

        profile.about = bio
        profile.preferences.clear()
        profile.preferences.add(*Genre.objects.filter(id__in=selected_preferences))
        profile.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')  # Redirect to profile view

    return render(request, 'catalog/profile.html', {
        'profile': profile,
        'all_genres': all_genres,
        'user_reviews': user_reviews  # Include user reviews in the context
    })


