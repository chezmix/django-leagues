django-leagues
==============

A competitive league system built with Django

Quick Setup
-----------
1. python manage.py syncdb

If you want to use the example data provided:

2. when prompted, DO NOT create a superuser account
3. python manage.py loaddata example_data


Else:

2-3. when prompted, create a superuser account
4. python manage.py runserver
5. open browser to http://localhost:8000/admin
6. login with superuser account (user: admin pass: password if using example data)

Done!