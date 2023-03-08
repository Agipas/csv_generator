from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_generator.settings')
app = Celery('csv_generator')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
