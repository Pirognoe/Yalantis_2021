from rest_framework import serializers

from .models import TrainingCourse

class TrainingCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingCourse
        fields = ('id', 'name', 'start_date', 'end_date', 'number_of_lectures')