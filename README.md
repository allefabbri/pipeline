# CELERY

### Run

```
celery -A tasks worker --loglevel=DEBUG
celery -A tasks worker --loglevel=INFO

celery -A tasks_with_results worker --loglevel=INFO
```

### Docker
```
docker compose --project-name "pipeline" up --build -d
```

### Django
Run django with
```
django/app$ python manage.py runserver
```

Run celery with
```
python -m celery -A app worker --loglevel=INFO
```

Visit [http://localhost:8000](http://localhost:8000)

### Refs
- celery+cpp [link](https://github.com/s3rvac/blog/tree/master/en-2017-06-25-consuming-and-publishing-celery-tasks-in-cpp-via-amqp)
- dramatiq
