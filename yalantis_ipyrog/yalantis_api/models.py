from django.db import models
from django_filters import rest_framework as filters


# Create your models here.

class TrainingCourse(models.Model):
    """
    Basic model in our app, represents a training course
    """
    name = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()
    number_of_lectures = models.IntegerField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class TrainingCourseFilter(filters.FilterSet):
    start_date = filters.DateFromToRangeFilter()
    end_date = filters.DateFromToRangeFilter()

    class Meta:
        model = TrainingCourse
        fields = ['start_date', 'end_date']
