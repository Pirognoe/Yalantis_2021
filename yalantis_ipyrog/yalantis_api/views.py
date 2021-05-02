from django.shortcuts import render
from rest_framework import viewsets

from .serializers import TrainingCourseSerializer
from .models import TrainingCourse


class TrainingCourseViewSet(viewsets.ModelViewSet):
    queryset = TrainingCourse.objects.all().order_by('name')
    serializer_class = TrainingCourseSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned training courses
        by filtering against a `name` query parameter in the URL.
        """
        queryset = TrainingCourse.objects.all().order_by('name')
        training_course_name = self.request.query_params.get('name')
        if training_course_name is not None:
            queryset = queryset.filter(name=training_course_name)
        return queryset
