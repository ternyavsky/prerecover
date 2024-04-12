package_dir := "src"

help:
    just -l

install:
	poetry install --with dev,test,lint

lint:
	just _py pre-commit run --all-files


test *args:
    just _py pytest {{args}}

run:
	poetry run python -m {{package_dir}}

_py *args:
    poetry run {{args}}
