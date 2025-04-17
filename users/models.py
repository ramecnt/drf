from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=35, verbose_name="Телефон", unique=True, **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name="Страна", **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    date = models.DateTimeField(auto_now_add=True)
    payed_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments', **NULLABLE)
    payed_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payments', **NULLABLE)
    amount = models.IntegerField(default=0)
    cash_or_transfer = models.BooleanField(default=False)  # False - наличными True - перевод
