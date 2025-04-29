from celery import shared_task
from django.core.mail import send_mail

from materials.models import Course
from drf import settings
from users.models import Subscribe


@shared_task
def course_update(course_id):
    course = Course.objects.get(id=course_id)
    subscribes = Subscribe.objects.filter(course=course)
    users = []

    for sub in subscribes:
        users.append(sub.user.email)

    if users:
        send_mail(
            subject=f"Ваш курс '{course.name}' был обновлен",
            message=f"Ваш курс '{course.name}' был обновлен",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=users,
        )
