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

When writing test, the goal is to utilize the [given-when-then](https://martinfowler.com/bliki/GivenWhenThen.html) framework.

| **State** | **Explanation** | **Code** |
| :---: | :--- | :--- |
| Given | the state of the application before the test runs | setup code, fixtures, database state |
| When | the behavior/logic being tested | code under test |
| Then | the expected changes based on the behavior | asserts |

# Getting Started

These instructions will provide a copy of the project & get you running on your local machine for development and testing purposes.

See [deployment](#deployment) section on how to deploy a project as a live system.

## Pre-requisites

Please see each project's README file.

# How To For ...

This section will be your general "how to" guide when using this project.

Please note that everything written in this repo done by the repo owner is done on a Windows PC that utilizes WSL and using [VS Code](https://code.visualstudio.com/) as my IDE.

Never heard of WSL? I share more on this [here](https://prosperousheart.com/windows-terminal/) when I fan girl out on the (at the time) latest version of Windows command line features that was made available to me.

See [here](./TestDrivenIO/README.md#getting-started) for **TestDrivenIO** getting started.

## Installing

Step by step explanation on how to get a development ENV running.

## Deployment

Information on how to deploy to a live system.

## Usage

How to use this solution.

If additional documentation is stored elsewhere, it will be noted here.

Since using pytest, check out the following for more info:
- [All You Need to Know to Start Using Fixtures in Your pytest Code](https://pybit.es/articles/pytest-fixtures/)
- the [Fixtures section](https://testdriven.io/blog/pytest-for-beginners/#fixtures) from [Pytest for Beginners](https://testdriven.io/blog/pytest-for-beginners/)
- [Fixture finalization / executing teardown code](https://docs.pytest.org/en/latest/explanation/fixtures.html#improvements-over-xunit-style-setup-teardown-functions)

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
