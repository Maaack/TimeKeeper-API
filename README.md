# Time-Keeper-API
An API for managing timelines.

# Basic Idea
Store and retrieve timeline data and relationships between time, events, and actors

# Environment Setup
`docker-compose up`

You'll need to run migrations on the database to get it caught up.
(If you'd like to have docker do this automagically - by all means)
```
$> sudo docker exec -it timekeeperapi_web_1 /bin/bash
timekeeper_web_1$> python manage.py makemigrations
timekeeper_web_1$> python manage.py migrate
```

Go to `http://localhost:8000/`

# Structure
Django-based REST API

`timelines` has most of the meat. API is accessible in both readable HTML or JSON.

# Additional Resources
Writing your first Django App Tutorials: https://docs.djangoproject.com/en/1.10/intro/tutorial01/

Django REST framework Documentation: http://www.django-rest-framework.org/

API Cheatsheet: https://github.com/RestCheatSheet/api-cheat-sheet#api-design-cheat-sheet

REST API Quick Tips: http://www.restapitutorial.com/lessons/restquicktips.html
