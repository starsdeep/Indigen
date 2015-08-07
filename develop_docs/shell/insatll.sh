#!/bin/bash

# change work directory to this file' dir
BASEDIR=$(dirname $0)
cd $BASEDIR
# drop the database and create a new database
cat ../sql/create_database.sql | mysql -u root -p
python ../../back_end/indigen/manage.py makemigrations
python ../../back_end/indigen/manage.py migrate
