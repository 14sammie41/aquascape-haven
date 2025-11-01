from django.urls import path
from . import views

urlpatterns = [
    path('', views.competition_home, name='competition_home'),
    path('vote/', views.vote_page, name='competition_vote'),
    path('enter/', views.enter_competition, name='competition_enter'),
    path('like/<int:entry_id>/', views.like_entry, name='like_entry'),
]
