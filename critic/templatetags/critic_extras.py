from django import template
register = template.Library()

from django.shortcuts import get_object_or_404
from ..models import Review



@register.filter
def times(count):
    return range(int(count))


@register.filter
def star_times(count):
    return range(int(count // 20))


@register.filter
def get_stars(review_id):
    review = get_object_or_404(Review, pk=review_id)
    return range(int(review.movie_rating // 20))