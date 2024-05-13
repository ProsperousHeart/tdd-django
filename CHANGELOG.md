Also link to Issues where possible.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) where given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes

## [Unreleased] - RealPython Project Setup & Completion

### Added

- info on Django RESTful Framework (DRF) in main [README.md](README.md)
- [RealPython project](./RealPython/) folder setup & README update with link to site
- initial RealPython Django project setup for pet store with puppies app
- setup test section for puppies app
- create [Puppy Model](./RealPython/puppy_store/puppies/models.py) & serializer
- start test file for puppies app 
- create skeleton of puppies [Views.py](./RealPython/puppy_store/puppies/views.py) then map in [urls.py](./RealPython/puppy_store/puppies/urls.py) & [urls.py](./RealPython/puppy_store/puppy_store/urls.py)

### Updated

- RealPython's [README.md](./RealPython/README.md) to include name of venv I made, since I now have multiple projects in this main folder
- defined global [settings](http://www.django-rest-framework.org/tutorial/quickstart/#settings) for REST framework (allows unrestricted access to the API and sets default test format to JSON for all requests) ... review [here](http://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy) for more
- unit test for getting all validated Puppy items then update related view so it passes test

## [1.4.1] - 2024-05-12

### Added

- pytest and pytest-django to [requirements.txt](./TestDrivenIO/requirements.txt)
- tests folder structure
- [README.md](./TestDrivenIO/tests/README.md) for new test folder structure
- [pytest.ini](./TestDrivenIO/pytest.ini) file to define the [DJANGO_SETTINGS_MODULE](https://pytest-django.readthedocs.io/en/latest/configuring_django.html#configuring-django-settings) environment variable to point to the Django settings file and the standard test discovery rules (for explicitness)
- [conftest.py](./TestDrivenIO/conftest.py) to use a different DB during test runs
- [TestDrivenIO README](./TestDrivenIO/README.md) getting started section (e.g.: how to spin up docker)

### Updated

- main project [README](./README.md) with:
    1. info on the system this code was written on and with what tools
    2. how to test locally
    3. additional information for pytest
    4. explanation of test structure framework

## [1.3.1] - 2024-05-11

### Added

- configured volume so data can persist beyond life of container ([.docker-compose.yaml](docker-compose.yml))
- added ENV key to define a name for default DB & credentials - learn more about ENV vars [here](https://hub.docker.com/_/postgres)
- updated [requirements.txt](requirements.txt) to install [Psycopg](https://www.psycopg.org/docs/) (PostgreSQL database adapter for Python)
- TestDrivenIO [entrypoint.sh](./TestDrivenIO/movies/entrypoint.sh) since the `movies` service is dependent on container being up and running as well sa the Postgres instance being healthy

### Changed

- updated `.env.dev` to include SQL environment information
- setup `DATABASES` in [settings.py](./TestDrivenIO/drf_project/settings.py) to configure the database based on ENV vars defined
- added linux commands to ensure system is updated before installing dependencies
- updated [TestDrivenIO README](./TestDrivenIO/README.md) to:
    - include info on starting up and building Docker image after changes
    - how to migrate Django models within Docker
    - addition of explanation for bringing down volumes
    - additional commands
- locally updated file permnissions for [entrypoint.sh](./TestDrivenIO/movies/entrypoint.sh) with `chmod +x movies/entrypoint.sh`
- update [Dockerfile](./TestDrivenIO/Dockerfile) to install required dependency, copy entrypoint, and run it as Docker [entrypoint](https://docs.docker.com/engine/reference/builder/#entrypoint) command
- updated `.env.dev` to include DATABASE environment

### Fixed

- [Dockerfile](./TestDrivenIO/Dockerfile) not pulling entrypoint properly & missing command in setup

##  [1.2.0] - 2024-05-11

### Added

- new folder for what I'll learn with TEstDriven.io course
- requirements.txt for main project and TestDrivenIO

### Changed

- Updated main README with additional information (incomplete, since building multiple apps here)
- updated TestDrivenIO README with additional useful tips & link to Docker info
- updated .gitignore to include all sqlite3 items, not just the default template ones
- removed deprecated version from `docker-compose.yml`

### Removed

- TestDrivenIO requirements ... only added the two main installs (which should install the others when run)
- TestDrivenIO SQL DB - we'll be using postgres

## [1.1.0] - 2024-05-10

### Added

- basic repo setup with MIT license and python .gitignore file
- README template
- code of conduct
- PR template
- issue templates (bug, feature, documentation)
