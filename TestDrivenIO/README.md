# What's Involved?

In this app, I will build, test, and deploy a Django app with Docker, pytest, postgres, and Django REST framework.

This course covered a wide variety of technologies and services:

## Core
1. Python
2. Django
3. [Docker](https://docs.docker.com/get-docker/)
4. Postgres
5. Django REST Framework
6. Gunicorn
7. WhiteNoise
8. Swagger/OpenAPI

## Testing and Linting
1. pytest
2. Coverage.py
3. Flake8
4. Black
5. isort
6. HTTPie

## Services
1. GitLab - free for personal projects
2. Heroku - though I will likely use Render instead

# Endpoint Overview

| Endpoint | HTTP Method | CRUD Method | Result |
|/api/movies | GET | READ | get all movies |
| /api/movies/:id | GET | READ | get a single movie |
| /api/movies | POST | CREATE | add a movie |
| /api/movies/:id | PUT | UPDATE | update a movie |
| /api/movies/:id | DELETE | DELETE | delete a movie |

# Getting Started

These instructions will provide a copy of the project & get you running on your local machine for development and testing purposes.

See [deployment](#deployment) section on how to deploy a project as a live system.

## Pre-requisites

Please see each project's README file.

### Testing Locally

#### Local Spin Up

Change into your high level directory and run:

`docker-compose up -d --build`

If you haven't already (re)built it, this will use the [docker-compose.yaml](docker-compose.yml) file to build and then bring up a detached instance.

If you can access http://localhost:8009/ then you're good.

Run in docker:

`docker-compose exec SERVICE TESTING`

... where `SERVICE` is the Django service folder you wish to test and `TESTING` is the normal pytest commands you would use.

#### Local Shut Down

`docker-compose down -v`

# Lessons Learned

It's a good idea to configure a custom User model when [starting a new Django project](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project). For more, review [Creating a Custom User Model in Django](https://testdriven.io/blog/django-custom-user-model).

## Docker Info

Be sure you are in the TestDrivenIO folder. Run the following in WSL:
1. To start Docker container:  `docker-compose up -d`
2. To bring down container & volumes:  `docker-compose down -v`

If you need to start a Docker container after updating, run:

`docker-compose up -d --build`

When running your Docker container, if you need to run migrations:

`docker-compose exec movies python manage.py migrate --noinput`

### Additional Docker Commands

Ensure Django tables created:

```
docker-compose exec movies-db psql --username=movies --dbname=movies_dev
\l
\c movies_dev
\dt
\q
```

Can also check by running:

`docker volume inspect django-tdd-docker_postgres_data`

## Postgres

Once spun up, postgres will be available on post 5432 for services running in other containers. Thus the need to update `.env.dev`.