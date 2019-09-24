from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'critic'
urlpatterns = [
    path('', views.index, name='index'),

    # ex: /critic/5/
    path('<int:question_id>/', views.detail, name='detail'),
    
    # ex: /critic/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    
    # ex: /critic/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /critic/5/review/
    path('review/<int:review_id>/', views.review, name='review')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
