# lc_questions/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question-list'),
    path('add/', views.add_question, name='add-question'),
]
