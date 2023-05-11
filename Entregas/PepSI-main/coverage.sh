#!/bin/bash
# Runs the coverage test utility
coverage erase
coverage run --omit="*/test*" --source=catalog manage.py test catalog.tests
coverage report -m -i
