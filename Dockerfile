# syntax=docker/dockerfile:1
FROM python:3.10.7-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /var/log/webapp
RUN touch /var/log/webapp/debug.log
RUN touch /var/log/webapp/info.log

RUN apt-get update
RUN apt-get install xz-utils
RUN apt-get -y install curl

WORKDIR /tmp
RUN curl https://deb.nodesource.com/setup_12.x | bash
RUN curl https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install -y nodejs yarn

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python3 manage.py collectstatic --no-input
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN ls -lah

ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]