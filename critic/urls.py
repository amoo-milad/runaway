from django.urls import path

from . import views

app_name = 'critic'

urlpatterns = [
    path('', views.index, name='index'),

    # ex: /critic/author/5/
    path('author/<int:author_id>', views.author, name='author'),

    # ex: /critic/5/
    path('<int:question_id>/', views.detail, name='detail'),
    
    # ex: /critic/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    
    # ex: /critic/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /critic/review/5/
    path('review/<int:review_id>/', views.review, name='review'),

    # ex: /critic/allreviews/
    path('all-reviews/', views.allreviews, name='all-reviews'),

    # ex: /critic/allcritics/
    path('all-critics/', views.allcritics, name='all-critics'),

    # ex: /critic/movies/

    # path('movie/<int:movie_id>/rate/<int:num_stars>/', views.stars, name='stars'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_id>/', views.get_movie, name='movie_detail'),
    path('movies/<int:movie_id>/rate/<int:num_stars>/', views.rate_movie, name='movie_rate'),

]
