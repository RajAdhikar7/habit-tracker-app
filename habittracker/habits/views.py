
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import Habit,HabitEvent

def list(request):
    habit_objects = Habit.objects.filter(User=request.user)
    context = {
        "obj":habit_objects
    }
    return render(request, "habits/list.html", context=context)