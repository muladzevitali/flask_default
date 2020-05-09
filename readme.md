# Minimal Flask Application
> Application includes: Login and Landing pages.

## Introduction
The main goal of this repository is to provide the very basics of flask large application including: Login, Register, Landing and Admin pages.
The flask application has already installed 3 apps as blueprints:
* Admin - App contains views for index, role and user management.
* Auth - App contains database models for users, roles and their relation. Also views for login and logout. Form for login and templates and statics folders.
* Landing - App contains view for landing page, templates and statics folders.

Application uses SQLite as database. If you want to change it, modify the uri variable in [config file](src/config/config_parser.py) ApplicationDatabase class.
Server runs on port 8080 as default. You can change it in manage.py file.
For running server in a production mode use the [readme](https://github.com/muladzevitali/faiss_server).

## Installation
For installing dependencies run:
```bash
pip install -r requirements.txt
```
After installing create database tables with command:
```bash
python manage.py create_db
```
For reset database run:
```bash
python manage.py reset_db
```
After installing dependencies and creating tables for running the server type:
```bash
python manage.py runserver
```
and check the url: [http://localhost:8080](http://localhost:8080)
