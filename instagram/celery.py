import os
from celery import Celery
from django.conf import settings



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram_rest.settings')

app = Celery('instagram',broker='redis://0.0.0.0:6379')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule={
    'check_data': {
        'task':'apps.stories.tasks.stories',
        'schedule': 3600
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.timezone = 'Asia/Bishkek'