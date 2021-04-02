from django.urls import path
from .views import *

urlpatterns = [
    path('', Quizz.as_view(), name='Quizz'),
    path('questions/<int:id>', QuizzQuestion.as_view(), name='Questions'),
    path('randomquestion/<int:id>', RandomQuestion.as_view(), name='Random Questions'),
]