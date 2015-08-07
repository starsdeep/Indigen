#!/bin/bash
BASEDIR=$(dirname $0)
cd $BASEDIR
python ../../back_end/indigen/manage.py runserver
