#!/bin/bash
# Runs database migrations
python3 manage.py makemigrations
python3 manage.py migrate

