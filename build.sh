#!/usr/bin/env bash
pip install -r requirements.txt
nvm run build
python manage.py collectstatic
python manage.py migrate
