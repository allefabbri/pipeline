from api.models import Dummy
from time import sleep

from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def count_dummy():
    sleep(5)
    return Dummy.objects.count()

@shared_task(bind=True)
def progress_task(self):

    data = {}
    tot_time = 5
    step_n = 20
    for i in range(step_n):
        data[f'step{i:03d}'] = i
        self.update_state(state='PROGRESS', meta={'done': i, 'total': step_n})
        sleep(tot_time/step_n)

    return {'done': i, 'total': step_n}