from django.db import models
import datetime
# Create your models here.
class Exercises(models.Model):
    EXERCISES = [
        ('pullup','pullup'),
        ('pushup','pushup'),
        ('row','row'),
        ('squat','squat'),
    ]
    exercise = models.CharField(default="pullup", max_length=100, choices=EXERCISES)
    reps = models.PositiveIntegerField(default=0)
    date = models.DateField(blank=False, default=datetime.date.today)
    #creationdate = models.DateField(default=datetime.date.today, auto_now=False, auto_now_add=False)

    def __str__(self):
        return (str(self.date) + ": " + str(self.exercise) + "s: " + str(self.reps))