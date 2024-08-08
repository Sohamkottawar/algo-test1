from django.urls import path
from .views import question_of_the_day

urlpatterns = [
    path('question-of-the-day/', question_of_the_day),
]
