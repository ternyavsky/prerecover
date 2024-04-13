DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_FILE = compose/app.yaml
STORAGES_FILE = compose/storages.yaml
APP_CONTAINER = prerecover.api
PY = poetry

app:
	${DC} -f ${APP_FILE} ${ENV} up --build

storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

all:
	${DC} -f ${STORAGES_FILE} -f ${APP_FILE} ${ENV} up --build -d

app-down:
	${DC} -f ${APP_FILE} down

app-logs:
	${LOGS} ${APP_CONTAINER} -f

test:
	${EXEC} ${APP_CONTAINER} pytest


app-shell:
	${EXEC} ${APP_CONTAINER} bash

install:
	${PY} install --with dev,test,lint

lint:
	${PY} run pre-commit run --all-files


ipython:
	${PY} run ipython
