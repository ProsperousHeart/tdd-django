This project is based on [this RealPython page](https://realpython.com/test-driven-development-of-a-django-restful-api/).

Locally, I have created a virtual machine called:  `RealPython-DRFTDD`

# What's Involved?

In this app, I will build, test, and deploy a Django app with pytest, sqlite3, and Django REST framework.

This course covered a wide variety of technologies and services:

## Core
1. Python
2. Django
3. Postgres
4. Django REST Framework
5. Swagger/OpenAPI

## Testing and Linting
1. pytest
2. Flake8
3. Black

Test first approach of TDD:
1. add a unit test - just enough code to fail
2. update code to make it pass the test
3. when test passes, start over with same process for a new test

## Services
N/A

# Endpoint Overview

| Endpoint | HTTP Method | CRUD Method | Result |
| puppies | GET | READ | get all puppies |
| puppies/:id | GET | READ | get a single puppy |
| puppies | POST | CREATE | add a single puppy |
| puppies/:id | PUT | UPDATE | update a single puppy |
| puppies/:id | DELETE | DELETE | delete a single puppy |

# Getting Started

These instructions will provide a copy of the project & get you running on your local machine for development and testing purposes.

See [deployment](#deployment) section on how to deploy a project as a live system.

## Pre-requisites

Please see each project's README file.

## Testing Locally

TBD

# Deployment

TBD

# Lessons Learned

TBD