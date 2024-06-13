from django.urls import path

from .views import (
    list_view,
    add_habit
)

urlpatterns = [
    path('', list_view, name='habit_list'),
    path('add/', add_habit, name='adding_habit'),

]