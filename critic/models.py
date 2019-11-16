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
    genres = models.ManyToManyField(Genre)
    length = models.DurationField()
    cover_image = models.ImageField(upload_to='movies/cover/', null=True)
    rate1 = models.IntegerField(default=0)
    rate2 = models.IntegerField(default=0)
    rate3 = models.IntegerField(default=0)
    rate4 = models.IntegerField(default=0)
    rate5 = models.IntegerField(default=0)
    # casts = models.ManyToManyField(Cast)

    @property
    def average_rating(self):
        rate_count = self.rate1 + self.rate2 + self.rate3 + self.rate4 + self.rate5
        rate_sum = self.rate1 + self.rate2 * 2 + self.rate3 * 3 + \
            self.rate4 * 4 + self.rate5 * 5
        return rate_sum/rate_count

    @property
    def stars(self):
        return int(self.average_rating)

    def update_rate(self, rate):
        if rate == 1:
            self.rate1 += 1
        if rate == 2:
            self.rate2 += 1
        if rate == 3:
            self.rate3 += 1
        if rate == 4:
            self.rate4 += 1
        if rate == 5:
            self.rate5 += 1
        # field = f'rate{rate}'
        # setattr(self, field, getattr(self, field) + 1)

    def __str__(self):
        return self.title
        # movie.cover_image.name == 'asghar.jpg'
        # movie.cover_image.url == 'http://www.com/media/photos/2017/5/23/asghar.jpg'
        # physical path == /home/runaway-project/media/photos/2017/5/23/asghar.jpg


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# QuerySet
# movie = Movie.objects.last()
# movie.review_set.filter()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    review_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('publish date')
    movie_rating = models.IntegerField(null=True)
    # point = models.IntegerField(default=lambda: random.randint(30, 98))

    title = models.CharField(max_length=100, default=movie)  # TODO: Remove default

    # def save(self, *args, **kwargs):
    #     if not self.title:
    #         self.title = self.movie.title
    #     return super().save(*args, **kwargs)

    @property
    def stars(self):
        return self.movie_rating / 20.0

    @property
    def star_string(self):
        return '★' * (self.movie_rating // 20)

    def __str__(self):
        return self.title

