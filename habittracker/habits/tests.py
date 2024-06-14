from django.test import TestCase

# Create your tests here.
from .models import Habit 

class HabitTestCase(TestCase):
    def setUp(self):
        self.number_of_habits = 30
        for i in range(0, self.number_of_habits):
            Habit.objects.create(name='play tennis',description ='play tennis for 30 minutes',difficulty =2)

    def test_queryset_exists(self):
        qs = Habit.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Habit.objects.all()
        self.assertEqual(qs.count(),self.number_of_habits)

