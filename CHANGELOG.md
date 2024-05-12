Also link to Issues where possible.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) where given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes

## [Unreleased]

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
