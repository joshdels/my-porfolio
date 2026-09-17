.PHONY: run

run:
	uv run python manage.py runserver

lint:
	uv run djlint . --reformat

migrate:
	uv run python manage.py makemigrations && \
	uv run python manage.py migrate && \
	uv run python manage.py showmigrations