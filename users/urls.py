from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import PaymentViewSet, SubscribeToCourseAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('subscribe/', SubscribeToCourseAPIView.as_view(), name='subscribe-to-course'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
] + router.urls
