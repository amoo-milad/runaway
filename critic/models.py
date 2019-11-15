from django.db import models
import random


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('publish date')

    def __str__(self):
        # return 'question: {self.question_text}'.format(self=self)
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Genre(models.Model):
    genre_name = models.CharField(max_length=30)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    screen_writer = models.CharField(max_length=100)
    # casts = models.ManyToManyField(Cast)
    genres = models.ManyToManyField(Genre)
    length = models.DurationField()
    cover_image = models.ImageField(upload_to='movies/cover/', null=True)

    def __str__(self):
        # movie.cover_image.name == 'asghar.jpg'
        # movie.cover_image.url == 'http://www.com/media/photos/2017/5/23/asghar.jpg'
        # physical path == /home/runaway-project/media/photos/2017/5/23/asghar.jpg
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    review_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('publish date')
    # point = models.IntegerField(default=lambda: random.randint(30, 98))

    # movie_rating = models.IntegerField(null=True)

    title = models.CharField(max_length=100, default=movie)  # TODO: Remove default

    # def save(self, *args, **kwargs):
    #     if not self.title:
    #         self.title = self.movie.title
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

