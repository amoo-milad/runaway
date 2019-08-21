from django.contrib import admin
from .models import Question, Choice, Review, Movie, Genre

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Review)
admin.site.register(Movie)
admin.site.register(Genre)