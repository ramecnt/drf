from rest_framework import viewsets, generics, status

from materials.models import Course, Lesson
from materials.paginators import CoursePaginator
from materials.serializer import CourseSerializer, LessonSerializer, CourseDetailSerializer
from materials.tasks import course_update

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            course_update.delay(instance.id)
        return response


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
