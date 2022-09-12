# pipeline
Django+celery+rabbitmq+redis pipeline example.


### Docker
```
docker compose --project-name "pipeline" up --build -d
```
Visit [http://localhost:16010](http://localhost:16010)


### Local
Shell 0: run `rabbit` and `redis`
```
docker compose --project-name "pipeline" up --build -d rabbit redis redis-commander
```

Shell 1: in `django/app` run django with
```
python manage.py runserver
```

Shell 2: in `django/app` run celery with
Run celery with
```
python -m celery -A app worker --loglevel=INFO
```

Visit [http://localhost:8000](http://localhost:8000)


### Celery notes
```
celery -A tasks worker --loglevel=DEBUG
celery -A tasks worker --loglevel=INFO

celery -A tasks_with_results worker --loglevel=INFO
```


### Refs
- celery+cpp [link](https://github.com/s3rvac/blog/tree/master/en-2017-06-25-consuming-and-publishing-celery-tasks-in-cpp-via-amqp)
- dramatiq

