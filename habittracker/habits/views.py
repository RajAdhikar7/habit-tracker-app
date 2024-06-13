
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
    form = HabitCompletionForm(request.POST0 or None)
