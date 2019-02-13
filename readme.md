## Activate virtualenv
`source sparrenv/bin/activate`

## Run server
`python manage.py runserver`

## Install Postgres 
`brew install postgresql`

## Create Local user & DB 
[Reference Tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

## Migrate database 
`python manage.py runserver`



# OSX dev setup
$ `source sparrenv/Scripts/activate`  
$ `pip3 install -r requirements.txt`  
$ `brew install postgresql`  
$ `pg_ctl -D /usr/local/var/postgres start`  
$ `createdb spdb`  
$ `createuser spadmin`  
$ `python3 manage.py migrate`  
$ `python3 manage.py runserver`  
