from django import template
register = template.Library()

# from django.shortcuts import get_object_or_404
# from ..models import Review


@register.filter
def times(count):
    return range(int(count))


# @register.filter
# def star_times(movie_rating):
#     '''
#     {% for item in review.movie_rating|star_times %}
#     '''
#     return range(int(movie_rating // 20))


# @register.filter
# def get_stars(review_id):
#     '''
#     {% for star in review.id|get_stars %}
#     '''
#     review = get_object_or_404(Review, pk=review_id)
#     return range(int(review.movie_rating // 20))