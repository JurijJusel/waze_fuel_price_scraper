## Fuel prices crawler app

- From 'https://gas.didnt.work/?country=lt&brand=&city=Vilnius' fuel A95 and diesel prices from Vilnius city.
## Table of Contents

- [Fuel prices crawler app](#Fuel-prices-crawler-app)
- [Table of Contents](#table-of-contents)
- [General Information](#general-information)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Usage](#usage)

## General Information

This project uses [PostgreSQL](https://www.postgresql.org/), so, in order to make it working, install in your local machine or use Docker.

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Technologies Used

- Python 3.x.x
- requests
- BeautifulSoup
- PostgreSQL
- Async technics
- Docker

## Screenshots

![Example screenshot](./img/screenshot.png)

<!-- If you have screenshots you'd like to share, include them here. -->

## Setup

First step cloning project.
After cloning this project, do this steps.

Create .env file and put your project credentials
```
DATABASE_NAME = <database-name>
DATABASE_USER = <database-user>
DATABASE_PASSWORD = <database-password>
DATABASE_HOST =<host>
DATABASE_PORT = <database_port></database_port>
```
Create virtual environment and activated:
```
pip install virtualenv 
python -m venv <name_venv>
source <name_venv>/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```


What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.

## Usage

How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`