.PHONY: help makemigrations migrate build bash load up down dump createsuperuser reset shell

make shell:
	cd src && poetry shell && cd ..

migrations:
	docker compose run -it src poetry run python manage.py makemigrations

migrate: makemigrations
	docker compose run -it src poetry run python manage.py migrate

build: migrate
	docker build -t src -f ops/src.Dockerfile ./src

bash:
	docker compose exec -it src bash

load:
	docker compose exec -it src poetry run python manage.py loaddata /app/data.json

up:
	docker compose up $(if $(DETACH),-d) --build

down:
	docker compose down --remove-orphans --volumes

dump:
	docker compose exec -it src poetry run python manage.py dumpdata -o data.json
	docker cp netic-src-1:/app/data.json ./src/data.json

createsuperuser:
	docker compose run -it src poetry run python manage.py createsuperuser --noinput --username Admin --email netic_admin@eticalgarve.com
	docker compose exec -it src poetry run python manage.py shell -c "\
from django.contrib.auth import get_user_model; \
User = get_user_model(); \
user = User.objects.get(username='Admin'); \
user.set_password('Password'); \
user.save(); \
from app.models import UserProfile; \
UserProfile.objects.create(user=user, first_name='Admin', last_name='Admin', email='netic_admin@eticalgarve.com')"

make setup:
	make up DETACH=true
	sleep 20
	make load

reset: down up migrate dump
	make down
	make up DETACH=true
	sleep 5
	make load