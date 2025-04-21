from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj):
        return [lesson.name for lesson in Lesson.objects.filter(course=obj)]

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_amount = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lessons(self, obj):
        return [lesson.name for lesson in Lesson.objects.filter(course=obj)]

    def get_lesson_amount(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_amount', 'lessons')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'



