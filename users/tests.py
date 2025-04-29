from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User, Payment


class SubscribeTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.course = Course.objects.create(
            name="Test",
            description="test",
        )
        self.user = User.objects.create(
            email='test@test.com',
            password='test'
        )
        self.payment = Payment.objects.create(
            user=self.user,
            payed_course=self.course,
            amount=10,
            cash_or_transfer=True
        )

        self.data = {
            'user': self.user.pk,
            'course': self.course.pk,
            'payment': self.payment.pk
        }

    def test_SubscribeToCourse(self):
        print(self.data)
        response = self.client.post('/subscribe/', self.data)

        self.assertEqual(response.json(), {
            'id': 1,
            'user': self.user.pk,
            'course': self.course.pk,
            'payment': self.payment.pk
        })

        response = self.client.post('/subscribe/', self.data)

        self.assertEqual(response.json(), {'message': 'Подписка удалена'})