from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course
from users.models import Payment, User, Subscribe
from users.serializer import PaymentSerializer, SubscribeSerializer
from users.services import create_product, create_price, create_session


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('payed_course', 'payed_lesson', 'cash_or_transfer')
    ordering_fields = ('date')


class SubscribeToCourseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data.get('user', None)
        course_id = request.data.get('course', None)
        payment_id = request.data.get('payment', None)

        if user_id is None or course_id is None or payment_id is None:
            return Response(
                {"error": "Необходимо указать 'user', 'course' и 'payment'"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = get_object_or_404(User, id=user_id)
        course = get_object_or_404(Course, id=course_id)
        payment = get_object_or_404(Payment, id=payment_id)

        subs_item = Subscribe.objects.filter(user=user, course=course, payment=payment)
        if subs_item.exists():
            subs_item.delete()
            return Response(
                {"message": "Подписка удалена"},
                status=status.HTTP_200_OK
            )
        else:

            if payment.payed_lesson:
                return Response(
                    {"error": "Подписку можно оформить только на курс"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            new_sub = Subscribe.objects.create(user=user, course=course, payment=payment)
            serializer = SubscribeSerializer(new_sub)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save()
        if payment.lesson:
            product = create_product(payment.lesson.name)
        else:
            product = create_product(payment.course.name)
        amount = create_price(payment.amount, product)
        session_id, payment_url = create_session(amount)
        payment.session_id = session_id
        payment.url = payment_url
        payment.save()
