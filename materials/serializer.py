from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.Serializer):
    class Meta:
        model = Lesson
        fields = '__all__'

