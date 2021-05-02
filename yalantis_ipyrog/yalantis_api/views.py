from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TrainingCourseSerializer
from .models import TrainingCourse


class TrainingCourseViewSet(viewsets.ModelViewSet):
    queryset = TrainingCourse.objects.all().order_by('name')
    serializer_class = TrainingCourseSerializer
