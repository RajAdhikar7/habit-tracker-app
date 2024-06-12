from django.contrib import admin
from .models import Habit,HabitEvent
# Register your models here.

class HabitEventInline(admin.StackedInline):
    model = HabitEvent
    extra = 0

class HabitAdmin(admin.ModelAdmin):
    inlines = [HabitEventInline]
    list_display = ['name', 'description','difficulty']
    raw_id_fields = ['user']

admin.site.register(Habit,HabitAdmin)