from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255);
    description = models.TextField(blank=True)
    difficulty = models.IntegerField(choices=((1,"Easy"),(2,"Medium"),(3,"Hard")))

    def __str__(self):
        return self.name


class HabitEvent(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} completed {self.habit.name} on {self.date}"