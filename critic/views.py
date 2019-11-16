from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import Question, Choice, Review, Movie, Author


def index(request):
    latest_author_list = Author.objects.order_by('-id')[:6]
    latest_movie_list = Movie.objects.order_by('-id')[:6]
    latest_review_list = Review.objects.order_by('-pub_date')[:8]
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_author_list': latest_author_list,
        'latest_movie_list': latest_movie_list,
        'latest_review_list': latest_review_list,
        'latest_question_list': latest_question_list,
    }
    # context = {}
    return render(request, 'critic/index.html', context)


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    # author.title = 'asghar'
    # author.save()
    author_review_list = Review.objects.filter(author_id=author_id)
    context = {
        'author_review_list': author_review_list,
        'author': author,
    }
    return render(request, 'critic/author.html', context)


def review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'critic/review.html', {'review': review})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'critic/detail.html', {'question': question})

# def stars(request, num_stars, review_id):
#     review = get_object_or_404(Review, pk=review_id)
#     # ...
#     review.stars = num_stars
#     review.save()
#     return json...

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'critic/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'critic/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('critic:results', args=(question.id,)))


def allreviews(request):
    all_review_list = Review.objects.order_by('-pub_date')
    context = {
        'all_review_list': all_review_list,
    }
    # context = {
    #     'all_review_list': [{
    #         'id': review.id,
    #         'movie': review.movie,
    #         'movie': review.movie,
    #         # ...
    #         'point': review.movie_rating / 20.0
    #     } for review in all_review_list],
    # }
    return render(request, 'critic/all-reviews.html', context)


def allcritics(request):
    all_critics_list = Author.objects.all()
    context = {
        'all_critics_list': all_critics_list,
    }
    return render(request, 'critic/all-critics.html', context)


def movies(request):
    all_movies_list = Movie.objects.all().order_by('title')
    context = {
        'all_movies_list': all_movies_list,
    }
    return render(request, 'critic/movies.html', context)


def get_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'critic/movie.html', {'movie': movie})


@csrf_exempt
def rate_movie(request, num_stars, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.update_rate(num_stars)
    movie.save()
    return JsonResponse({'average_rating': movie.average_rating})
