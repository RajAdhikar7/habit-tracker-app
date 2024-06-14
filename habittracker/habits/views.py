
from django.shortcuts import render ,redirect  ,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit,HabitEvent
from .forms import HabitForm,HabitCompletionForm
from django.forms.models import modelformset_factory

@login_required
def list_view(request):
    habit_objects = Habit.objects.filter(user=request.user).prefetch_related('habitevent_set')
    context = {
        "object_list": habit_objects,
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
def habit_update_view(request, id=None):
    obj = get_object_or_404(Habit, pk=id, user=request.user)
    form = HabitForm(request.POST or None, instance=obj)
    HabitEventFormset = modelformset_factory(HabitEvent, form=HabitCompletionForm, extra=1)  # Allow 1 extra form for new HabitEvent
    qs = obj.habitevent_set.all()
    formset = HabitEventFormset(request.POST or None, queryset=qs)
    
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            if form.cleaned_data:  # Ensure the form has data before saving
                child.habit = parent
                child.save()
        context = {
            "form": form,
            "formset": formset,
            "object": obj,
            "message": "Data saved."
        }
    else:
        context = {
            "form": form,
            "formset": formset,
            "object": obj
        }

    return render(request, "habits/create-update.html", context)



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



