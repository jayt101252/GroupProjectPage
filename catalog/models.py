from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User # Used to authenticate User identity against Django default User model
import uuid  # Required for unique book instances

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a movie genre (e.g. Sci-Fi or Horror)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Director(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    director_photo = models.URLField(blank=False)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('director_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Movie(models.Model):
    """Model representing a movie made by a director."""
    title = models.CharField(max_length=200)

    # Foreign Key used because movie can only have one director, but directors can have multiple books
    director = models.ForeignKey('Director', on_delete=models.RESTRICT, null=True)

    description = models.TextField(max_length=1000, help_text='Enter a summary of the movie')
    # runtime used for formatting the run time of movie as ’00:00:00’
    runtime = models.TimeField()

    # ManyToManyField used because genre can contain many movies. Movies can cover many genres.
    genre = models.ManyToManyField(Genre, help_text='Select a genre(s) for this movie')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('movie_detail', args=[str(self.id)])


class MovieReview(models.Model):
    """Model representing a review for a specific movie; to include a star rating out of 5."""
    caption = models.CharField(max_length=100)
    star_rating = models.IntegerField(default=0)  # add star image functionality
    review_text = models.TextField(max_length=300) # Review text

    # Foreign Keys to match movie review to a movie, and the profile leaving the review
    movie = models.ForeignKey('Movie', on_delete=models.RESTRICT, null=True)
    user = models.ForeignKey('Profile', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.caption}: ({str(self.star_rating)} {self.review_text})'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('review_detail', args=[str(self.id)])


class Profile(models.Model):
    # Pulls profile associated with user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Attribute to store profile picture, and default to baseline .jpg file
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Area to write about the user on their profile
    about = models.CharField(max_length=300)
    # Set profile preferences
    preferences = models.ManyToManyField(Genre, help_text='Select your favorite genres of movies')

    def __str__(self):
        return f'{self.user.username} Profile'