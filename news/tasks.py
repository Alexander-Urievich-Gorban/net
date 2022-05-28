from datetime import timedelta

from django.utils import timezone

from django.core.mail import send_mail
from django.db.models import Sum
from celery import shared_task
from .models import Post
from conf.celery import app


@shared_task(bind=True)
def update_rating(self):
    for i in Post.objects.all():
        i.get_rating()
    return 'ratings is update!'


