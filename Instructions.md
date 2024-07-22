docker login  -u cloudyogi27

dckr_pat_ofP7cJ2YKeEy6PsgY1ile8r8UUM

ACCESS TOKEN DESCRIPTION
RESTAPI

ACCESS PERMISSIONS
Read, Write, Delete

To use the access token from your Docker CLI client:
1. Run
   docker login  -u cloudyogi27
2. At the password prompt, enter the personal access token.
   dckr_pat_ofP7cJ2YKeEy6PsgY1ile8r8UUM

DOCKERHUB_USER: cloudyogi27
DOCKERHUB_TOKEN: dckr_pat_ofP7cJ2YKeEy6PsgY1ile8r8UUM


docker build .
docker-compose build

docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "python manage.py my_wait_for_db && flake8"



# Start new project
docker-compose run --rm app sh -c "django-admin startproject app . "
docker-compose run --rm app sh -c "python manage.py startapp core"
docker-compose run --rm app sh -c "python manage.py startapp user"


# Run docker to start services
docker-compose up
docker-compose down

# Create Super user
docker-compose run --rm app sh -c "python manage.py createsuperuser"

===========
Migration
---  Cleanup old db
docker-compose down
docker volume ls
docker volume rm restapi_dev-deb-data
docker volume ls
---

docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py my_wait_for_db && python manage.py migrate"


===============
LocalRestAPI

python3 -m venv py
py/bin/pip install --upgrade pip
 py/bin/pip install -r requirements.txt
 py/bin/pip install -r requirements.dev.txt
 export PATH=$PATH:/Users/Yogesh/Documents/LocalRestAPI/py/bin
 ./activate
python manage.py runserver 0.0.0.0:8000

=========
git clone https://github.com/CloudYogi27/RestAPI.git .

git add .
git commit -am "code update."
git push origin



===========
Run on This machine




===========

