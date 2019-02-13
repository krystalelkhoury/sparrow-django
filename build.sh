#!/usr/bin/env bash
pip install -r requirements/production.txt
python manage.py collectstatic
python manage.py migrate