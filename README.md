# TDD With Django

In order to gain better insight to TDD and Django, I need to go through a few different tutorials. In this repo, I will work on building apps related to the following:
- TDD [Read the Docs](https://test-driven-django-development.readthedocs.io/en/latest/) where you will write a well tested, Django-based blog website
- TestDrive.io's [tutorial](https://testdriven.io/courses/tdd-django/getting-started/) -- will start with this one! (creates a RESTful API using TDD)
- RealPython's [tutorial](https://realpython.com/django-1-6-test-driven-development/)
- PyMeister's [tutorial](https://dev.to/pymeister/test-driven-development-with-django-32n8)

The audience for this repo is mostly myself, but may be used in teaching my students and/or leveraging for my clients.

## Acronymns

| Acronymn | spelled out | description as needed |
| :---: | :--- | :--- |
| `TDD` | [Test Driven Development](https://testdriven.io/test-driven-development/) | a methodology in software development that focuses on an iterative development cycle where the emphasis is placed on writing test cases before the actual feature or function is written & utilizes repetition of short development cycles |

## Requirements

The [first milestone](https://github.com/ProsperousHeart/tdd-django/milestone/1) is to complete the course that TestDriven.io has. Additional information about this milestone can be found [here](TestDrivenIO/README.md).

Additional milestones will be other tutorials as needed.

# Getting Started

These instructions will provide a copy of the project & get you running on your local machine for development and testing purposes.

See [deployment](#deployment) section on how to deploy a project as a live system.

## Pre-requisites

Please see each project's README file.

# How To For ...

This section will be your general "how to" guide when using this project.

Please note that everything written in this repo done by the repo owner is done on a Windows PC that utilizes WSL and using [VS Code](https://code.visualstudio.com/) as my IDE.

Never heard of WSL? I share more on this [here](https://prosperousheart.com/windows-terminal/) when I fan girl out on the (at the time) latest version of Windows command line features that was made available to me.

## Installing

Step by step explanation on how to get a development ENV running.

## Deployment

Information on how to deploy to a live system.

## Usage

How to use this solution.

If additional documentation is stored elsewhere, it will be noted here.

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

# Support Information

## Support Contacts

The current owner of this repo is an individual. If you would like to discuss something outside of submitting an issue, please see the contact us section from [here](https://resume.prosperousheart.com/).

## Health Monitoring

Where applicable, document how the health of teh application is being monitored & how operators can be made aware of new issues.

# Contributing

See [contributing file](contributing.md).

## Authors

Currently only @prosperousheart.

## License

See [license](license.md) file.

## Acknowledgements

Thank you to anyone who helps contribute to this project!
