.PHONY: all

all:
	cd frontend && npm run build
	python backend/manage.py collectstatic --noinput
	python backend/manage.py makemigrations
	python backend/manage.py migrate

coverage:
	coverage run --source='.' backend/manage.py test apps
	coverage report -m

coverage-html:
	coverage html

dockerd:
	docker-compose up -d --build

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

migrations:
	python backend/manage.py makemigrations
	python backend/manage.py migrate

run-backend:
	python backend/manage.py runserver

run-frontend:
	cd frontend && npm run serve

superuser:
	python backend/manage.py createsuperuser

test:
	python backend/manage.py test apps