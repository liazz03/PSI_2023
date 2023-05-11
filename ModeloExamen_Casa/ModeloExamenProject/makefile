# It's a makefile!

# export DJANGOPORT := 8001
# export DEBUG := True

PSQL = psql
CMD = python3 manage.py
APP = models 
# export DATABASE_URL = postgres://enriquesaou:10hGFVANzBUs@ep-falling-dawn-283692.eu-central-1.aws.neon.tech/neondb

## delete and create a new empty database
#clear_db:
#	@echo Clear Database
#	dropdb --if-exists $(PGDATABASE)
#	createdb


# create alumnodb super user
create_super_user:
	$(CMD) shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('alumnodb', 'admin@myproject.com', 'alumnodb')"

populate:
	@echo populate database
	python3 ./manage.py populate

runserver:
	$(CMD) runserver 8001

dropdb:
	dropdb -U alumnodb -h localhost exam

createdb:
	createdb -U alumnodb -h localhost exam

update_models:
	$(CMD) makemigrations application
	$(CMD) migrate

#reset_db: clear_db update_models create_super_user

shell:
	@echo manage.py  shell
	@$(CMD) shell

dbshell:
	@echo manage.py dbshell
	@$(CMD) dbshell

addparticipants:
	@echo populate database
	python3 ./manage.py addparticipants

static:
	@echo manage.py collectstatic
	python3 ./manage.py collectstatic

fully_update_db:
	@echo del migrations and make migrations and migrate
	rm -rf */migrations
	python3 ./manage.py makemigrations $(APP) 
	python3 ./manage.py migrate

test_authentication:
	$(CMD) test models.test_authentication --keepdb

test_model:
	$(CMD) test models.test_models --keepdb

test_services:
	$(CMD) test services.test_services --keepdb

test_game:
	$(CMD) test services.test_services_game --keepdb

coverage_models:
	coverage erase
	coverage run --omit="*/test*" --source=models ./manage.py test models
	coverage report -m -i

coverage_services:
	coverage erase
	coverage run --omit="*/test*" --source=services ./manage.py test services
	coverage report -m -i
	
env_setup:
	virtualenv kahoot_env
	@echo "Install requirements with 'pip install -r requirements.txt' within the virtualenv"
		
help:
	@echo "open the makefile and see the targets"