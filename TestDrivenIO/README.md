# What's Involved?

In this app, I will build, test, and deploy a Django app with Docker, pytest, postgres, and Django REST framework.

This course covered a wide variety of technologies and services:

## Core
1. Python
2. Django
3. Docker
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