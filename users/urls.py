from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import PaymentViewSet, SubscribeToCourse

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [
    path('subscribe/', SubscribeToCourse.as_view(), name='subscribe-to-course'),
] + router.urls
