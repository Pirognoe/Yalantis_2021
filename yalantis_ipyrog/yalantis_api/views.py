from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TrainingCourseSerializer
from .models import TrainingCourse


class TrainingCourseViewSet(viewsets.ModelViewSet):
    queryset = TrainingCourse.objects.all().order_by('name')
    serializer_class = TrainingCourseSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filterset_fields = ('start_date', 'end_date',)
    search_fields = ('name',)

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
