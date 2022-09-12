from celery import Celery
import time

app = Celery('tasks', backend='redis://:mindicity@localhost:40010', broker='pyamqp://localhost:40012//')

@app.task
def add(x, y, sleep):
    time.sleep(sleep)
    return x + y