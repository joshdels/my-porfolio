.PHONY: run

run:
	uv run python manage.py runserver

lint:
	uv run djlint . --reformat