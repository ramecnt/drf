from datetime import timedelta

from celery import shared_task
from celery.utils.time import timezone

from users.models import User


@shared_task
def block_user():
    month = timezone.now() - timedelta(days=30)
    users = User.objects.filter(is_active=True, is_superuser=False, last_login__gte=month)
    users.update(is_active=False)
    return users.count()
