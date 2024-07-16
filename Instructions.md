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

# Start new project
docker-compose run --rm app sh -c "django-admin startproject app . "

# Run docker to start services
docker-compose up









