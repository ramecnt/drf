from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course


class LessonTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.course = Course.objects.create(
            name="Test",
            preview=None,
            description="test",
        )
        self.lesson = Lesson.objects.create(
            name="Test",
            description="test",
            preview=None,
            url=None,
            course=self.course
        )
        self.data = {
            'name': 'Test',
            'description': 'test',
            'course': self.course.pk
        }

    def test_LessonList(self):
        response = self.client.get('/lesson/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [
            {'id': self.lesson.pk,
             'name': 'Test',
             'description': 'test',
             'preview': None,
             'url': None,
             'course': self.course.pk}
        ])

    def test_LessonRetrieve(self):
        response = self.client.get(f'/lesson/{self.lesson.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': self.lesson.pk,
            'name': 'Test',
            'description': 'test',
            'preview': None,
            'url': None,
            'course': self.course.pk
        })

    def test_LessonCreate(self):
        response = self.client.post('/lesson/create/', self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {
            'id': response.json()['id'],
            'name': 'Test',
            'description': 'test',
            'preview': None,
            'url': None,
            'course': self.course.pk
        })

    def test_LessonUpdate(self):
        response = self.client.patch(f'/lesson/update/{self.lesson.id}/', {'name': 'Test2'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'id': self.lesson.pk,
            'name': 'Test2',
            'description': 'test',
            'preview': None,
            'url': None,
            'course': self.course.pk
        })

    def test_LessonDestroy(self):
        response = self.client.delete(f'/lesson/delete/{self.lesson.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)