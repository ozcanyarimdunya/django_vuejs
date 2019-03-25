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

migrations:
	python backend/manage.py makemigrations
	python backend/manage.py migrate

install:
	pip install -r backend/requirements.txt
	cd frontend && npm install

test:
	python backend/manage.py test apps