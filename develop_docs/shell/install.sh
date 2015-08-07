#!/bin/bash

# change work directory to this file' dir
BASEDIR=$(dirname $0)
cd $BASEDIR
echo "next you need input mysql root password"
# drop the database and create a new database
cat ../sql/create_database.sql | mysql -u root -p
python ../../back_end/indigen/manage.py makemigrations
python ../../back_end/indigen/manage.py migrate

echo "you can use default user(username:username, password:password ) to login"
