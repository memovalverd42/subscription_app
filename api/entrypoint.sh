#!/bin/sh

if [ "$DATABASE" = "POSTGRES" ]
then
    echo "Waiting for POSTGRES..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "POSTGRES started"
fi

exec "$@"