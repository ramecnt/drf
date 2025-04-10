from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=100)
    preview = models.ImageField(upload_to='images/', **NULLABLE, verbose_name="превью")
    description = models.TextField()

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    preview = models.ImageField(upload_to='images/', **NULLABLE, verbose_name='превью')
    url = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
