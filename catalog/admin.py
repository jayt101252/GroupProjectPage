from django.contrib import admin
from .models import Movie, Director, Genre, MovieReview, Profile

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(MovieReview)
admin.site.register(Profile)
