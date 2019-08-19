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


class Review(models.Model):
    review_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('publish date')
    author = models.CharField(max_length=30)
    movie = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
        # , default = "the "+self.movie+" by "+self.author)

    def __str__(self):
        return self.title

