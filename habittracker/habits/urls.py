from django.urls import path

from .views import (
    list_view,
    add_habit,
    log_completion,
    habit_detail
)

urlpatterns = [
    path('', list_view, name='habit_list'),
    path('add/', add_habit, name='adding_habit'),
    path('<int:id>/log/',log_completion,name='log_completion'),
    path('<int:id>/',habit_detail,name='detail-view')

]