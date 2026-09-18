# Installation

## Requirements

- Python 3.14+
- PostgreSQL
- Git
- Docker (optional)

## Local Development

Clone the repository:

```bash
git clone <repository-url>
cd my-portfolio
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment configuration:

```bash
cp .env.example .env
```

Configure the database and other required settings in `.env`.

Run migrations:

```bash
python manage.py migrate
```

Create a Wagtail administrator:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open the portfolio at:

```text
http://127.0.0.1:8000/
```

Wagtail admin:

```text
http://127.0.0.1:8000/admin/
```

## Wagtail Setup

After logging into Wagtail:

1. Create the **Home Page**.
2. Add the homepage content.
3. Set the Home Page as the site's root page.
4. Publish the page.

## Projects

Create projects through the Wagtail admin.

For each project, add the available project information such as:

- Title
- Description
- Project image
- Tools / technologies
- Project links
- Project status or category

Publish the project when complete.

## Docker

The production application can be built and started with:

```bash
docker compose -f .docker/docker-compose.yml up -d --build
```

GitHub Actions automatically builds the Docker image and deploys the `main` branch to the production server.
