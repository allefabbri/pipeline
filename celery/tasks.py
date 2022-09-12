from celery import Celery
import time

app = Celery('tasks', broker='pyamqp://127.0.0.1:40012//')

@app.task
def add(x, y, sleep):
    #time.sleep(sleep)
    return x + y