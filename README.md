# Arlight App Backend

Django Rest Framework API for the ArcLight App, currently under development.

The Arclight App is developed together with volunteers from the University of St Andrews Medical School, and is to be used to trial the Arclight Scope [http://arclightscope.com/](http://arclightscope.com/) in rural communities in India at the end of 2020.

## Running locally

1. Clone repo
2. Install dependencies with `pip install -r requirements.txt`
3. Create a local PostgreSQL database an link it to django settings
4. Migrate DB schema
5. Create a super-user
6. Start django server `python manage.py runserver`

The server is now running on `http://127.0.0.1:8000/`.

The admin panel can be accessed at `http://127.0.0.1:8000/admin`.

The graphql GUI can be accessed at `http://127.0.0.1:8000/graphql`.


## Project Structure

`/accounts`
Django app which handle all Auth operations

`/api`
 Django app which is the main API of the app. Uses graphene to create an additional GraphQL API which is use for GET requests.

`/arlightbackend`
Django project directory


`/custom_packages`
Any custom Python packages are stored here


## Endpoints

`/accounts/password_reset/*` Password reset urls

`/acounts/users/` List of users

`/accounts/current_user/` Get current user info

`/accounts/api-toke-auth/` Get/create token


`/api/upload_video/` Upload a new video screening

`/api/password_reset_redirect/<path:redirect_url>/` Used for redirecting when users resets password on smartphone app

`/api/archive_video/<int:id>/` Archiving a video


`/graphql` GraphQL routes



## CI/CD

All commits to master are automatically deployed on Heroku.
