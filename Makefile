DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env
APP_PROD_FILE = compose/app.prod.yaml
APP_DEV_FILE = compose/app.dev.yaml
STORAGES_FILE = compose/storages.yaml
APP_CONTAINER = prerecover.api
LOCALY =
PY = poetry

app-prod:
	${DC} -f ${APP_PROD_FILE} ${ENV} up --build

app-dev:
	${DC} -f ${APP_DEV_FILE} ${ENV} up --build

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
