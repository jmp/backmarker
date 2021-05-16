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
4. Set up PostgreSQL either via the package manager or using `docker compose up db`
5. Run `python manage.py migrate`
6. Run `./populate-db.sh` to populate the database (you may need to modify the credentials)

## Running with Docker Compose

1. Run `docker compose build`
2. Run `docker compose up`

The API is now reachable at `http://localhost:8000/api/`.
The OpenAPI specification can be downloaded at `http://localhost:8000/api/schema/`.
The API documentation can be viewed at `http://localhost:8000/api/schema/redoc/`.
