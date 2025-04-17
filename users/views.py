from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from users.models import Payment
from users.serializer import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ('payed_course', 'payed_lesson', 'cash_or_transfer')
    ordering_fields = ('date')
