from django.db import models


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
    # genre = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    length = models.DurationField()

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('publish date')
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default=movie)

    def __str__(self):
        return self.title

