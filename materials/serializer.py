from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import URLValidator


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    is_subscribe = serializers.BooleanField(read_only=True)

    def get_lessons(self, obj):
        return [lesson.name for lesson in Lesson.objects.filter(course=obj)]

    def get_is_subscribe(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.subscribers.filter(user=user).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_amount = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    is_subscribe = serializers.BooleanField(read_only=True)

    def get_lessons(self, obj):
        return [lesson.name for lesson in Lesson.objects.filter(course=obj)]

    def get_lesson_amount(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_is_subscribe(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.subscribers.filter(user=user).exists()
        return False

    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_amount', 'lessons')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='url')]
