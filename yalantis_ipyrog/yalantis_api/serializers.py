from rest_framework import serializers

from .models import TrainingCourse

class TrainingCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingCourse
        fields = ('name', 'alias')