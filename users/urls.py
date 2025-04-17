from django.urls import path
from rest_framework import routers

from users.apps import UsersConfig
from users.views import PaymentViewSet

app_name = UsersConfig.name

router = routers.DefaultRouter()
router.register(r'payments', PaymentViewSet, basename='payments')

urlpatterns = [

] + router.urls
