FROM python:3.8

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install Django==4.0
RUN pip install celery
RUN pip install redis

# copy project
COPY ./app /app

ENTRYPOINT [ "/entrypoint.sh" ]
