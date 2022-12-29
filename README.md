# Q School

This project is intended to replace the scheduling system used by F3 organizations worldwide. It should work better (and faster) than spreadsheets and piecemail automation.

## Features

* Multiple region support (can handle one or all)

* Permissions based on role assignments (not implemented)

* PAX import by CSV (not implemented)

* Automatic PAX account generation (not implemented)

* Email notifications through gmail (not implemented)

* Python (Django)/PostgreSQL/Javascript

* Bootstrap 5  and Datatables

## Requirements

* Docker

## Starting the project

1. Start the project with the command `docker compose up`. All container will be retrieved and built.
2. Once the project is running, you'll need to open a shell to the application server `docker exec -it <container ID> /bin/bash`
3. Use the django [migrate](https://docs.djangoproject.com/en/4.1/topics/migrations/) management command to populate the database
4. Use the django [createsuperuser](https://docs.djangoproject.com/en/4.1/ref/django-admin/#createsuperuser) management command to create the super user account
5. Log in and go