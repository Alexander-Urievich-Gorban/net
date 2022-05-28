from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'conf.settings')
app = Celery('conf', broker='redis://redis:6379/0',
             backend='redis://redis:6379/0')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Moscow')

app.config_from_object(settings,
                       namespace='CELERY')

app.autodiscover_tasks()
