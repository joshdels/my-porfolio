FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-dev

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uv run --no-dev python manage.py collectstatic --noinput && uv run --no-dev gunicorn config.wsgi:application --bind 0.0.0.0:8000 --access-logfile - --error-logfile - --log-level debug"]