from .models import Movie, Director, MovieReview, Genre
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages



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


class MovieReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = MovieReview

class MovieReviewListView(LoginRequiredMixin, generic.ListView):
    model = MovieReview


### Movie review create, update, and delete functionality in 2 classes and def below ###
class WriteMovieReviewByUser(LoginRequiredMixin, CreateView):
    model = MovieReview
    fields = ['caption', 'star_rating', 'review_text']


class UpdateMovieReviewByUser(LoginRequiredMixin, CreateView):
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
### Change the base above to something review related in the future ###


### Figuring out Movie Reviews and Profiles before building admin movie/director changes

# def form_valid(self, form):
# post = form.save(commit=False)
# post.save()
# return HttpResponseRedirect(reverse('director_list'))

# class DirectorUpdate(UpdateView):
# model = Director
# fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'director_image']

# def form_valid(self, form):
# post = form.save(commit=False)
# post.save()
# return HttpResponseRedirect(reverse('director_list'))
