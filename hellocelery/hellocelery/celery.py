from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.signals import task_success
import requests

# @task_success.connect
# def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
#     # information about task are located in headers for task messages
#     # using the task protocol version 2.
#     print('Task Success')
#     url = 'http://localhost:8000'
#     requests.post(url)

from django.conf import settings
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hellocelery.settings')

app = Celery('hellocelery')
# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
