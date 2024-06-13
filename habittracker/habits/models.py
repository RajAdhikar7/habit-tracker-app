from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habit(models.Model):

    DIFFICULTY_CHOICES = (
        (1, "Easy"),
        (2, "Medium"),
        (3, "Hard"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255);
    description = models.TextField(blank=True)
    difficulty = models.IntegerField(choices=((1,"Easy"),(2,"Medium"),(3,"Hard")))

    def __str__(self):
        return self.name
    
    # retreving the choice of difficulty.
    def get_difficulty_display(self):
        return dict(self.DIFFICULTY_CHOICES).get(self.difficulty)
    
class HabitEvent(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.habit.user.username} completed {self.habit.name} on {self.date}"