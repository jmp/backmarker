# Backmarker

A fun little project where I build a REST API for an F1 database backed by Django.

Some facts:

* The backend is written in Python using the Django framework
* The database is PostgreSQL
* The data is from [Ergast](http://ergast.com/mrd/db/), under Creative Commons
  [BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)

## Requirements

* Python 3.9
* PostgreSQL 13 or Docker

## Installation

1. Install [Poetry](https://python-poetry.org)
2. Create a virtual environment and activate it
3. Run `poetry install` to install all the dependencies
4. Set up PostgreSQL with e.g. `docker compose up db`
5. Run `python manage.py migrate`

## Populating the database

To fill the database with some data, you can use the `populate-db.sh` script in the repository.
It is a very basic script that downloads the latest Ergast MySQL database dump and attempts to
convert it such that the rows can be inserted to the PostgreSQL database.

You may need to modify the credentials in the script if you are not using Docker Compose to run
the database.

## Running with Docker Compose

1. Run `docker compose build`
2. Run `docker compose up`

The API is now reachable at `http://localhost:8000/api/`.
The OpenAPI specification can be downloaded at `http://localhost:8000/api/schema/`.
The API documentation can be viewed at `http://localhost:8000/api/schema/redoc/`.
