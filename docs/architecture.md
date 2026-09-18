# Architecture

The portfolio is a Django application using Wagtail as the content management system.

```text
my-portfolio/
├── config/
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
│
├── porfolio/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── docs/
│   ├── installation.md
│   └── architecture.md
│
├── .github/
│   └── workflows/
│       ├── build.yml
│       └── deploy.yml
│
├── manage.py
└── README.md
```

## Application

**Django** handles application logic, routing, forms, database access, and email.

**Wagtail** manages editable portfolio content such as the homepage and projects.

**PostgreSQL** stores application and portfolio data.

**Docker** packages and runs the application consistently across development and production.

## Content Flow

```text
Wagtail Admin
      ↓
   Django
      ↓
 PostgreSQL
      ↓
Django Templates
      ↓
  Portfolio
```

## Contact Flow

```text
Visitor
   ↓
Contact Form
   ↓
Django Form
   ↓
ContactInquiry
   ↓
Email Backend
   ↓
Portfolio Email
```

## CI/CD Flow

```text
GitHub
   ↓
Push / Pull Request
   ↓
GitHub Actions
   ↓
Docker Build
   ↓
main
   ↓
SSH Deployment
   ↓
Production Server
   ↓
Docker Compose
```

The production deployment is automated through GitHub Actions and uses Docker Compose to build and restart the application on the server.
