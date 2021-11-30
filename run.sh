#!/bin/bash

# Path to our manage.py
DJANGO_MANAGER="./website/manage.py"

# First, lets create/update db
$DJANGO_MANAGER makemigrations
$DJANGO_MANAGER migrate

# Now lets populate it
$DJANGO_MANAGER update_db

# Finally, running test server
$DJANGO_MANAGER runserver
