# pull official base image
FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# install dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt
# copy project
COPY . .
RUN apk add dos2unix
COPY ./entrypoint.sh /usr/src/entrypoint.sh
RUN dos2unix /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh
ENTRYPOINT ["/usr/src/entrypoint.sh"]
EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000
