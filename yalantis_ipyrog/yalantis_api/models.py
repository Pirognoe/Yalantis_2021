from django.db import models


# Create your models here.

class TrainingCourse(models.Model):
    """
    Basic model in our app, represents a training course
    """
    name = models.CharField(max_length=60, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_lectures = models.IntegerField()

    def __str__(self):
        return self.name
