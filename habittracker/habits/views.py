
from django.shortcuts import render ,redirect  ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit,HabitEvent
from .forms import HabitForm,HabitCompletionForm

@login_required
def list_view(request):
    habit_objects = Habit.objects.filter(user=request.user)
    #habit_objects = get_object_or_404(Habit,user=request.user)
    context = {
        "object_list":habit_objects
    }
    return render(request, "habits/list-view.html", context=context) 

@login_required
def add_habit(request):
    form = HabitForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        habit = form.save(commit=False)
        habit.user=request.user
        habit.save()
        return redirect("habit_list")
    return render(request,"habits/add-habits.html",context)


@login_required
def log_completion(request , id):
    habit = get_object_or_404(Habit ,pk = id,user=request.user)
    form = HabitCompletionForm(request.POST or None)
    context = {
        "form":form,
        "habit":habit
    }
    if form.is_valid():
        habit_event=form.save(commit=False)
        habit_event.habit=habit
        habit_event.habit.user=request.user
        return redirect("habit_list")
    return render(request,"habits/log_completion.html",context=context)


@login_required
def habit_detail(request , id):
    habit = get_object_or_404(Habit ,pk = id)
    context={
        "habit":habit
    }
    return render(request,"habits/detail.html",context=context)

from django.contrib.auth.models import User
from .models import HabitEvent
from datetime import date

