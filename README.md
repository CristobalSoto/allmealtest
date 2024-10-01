# AllMeal - Online Menu and Order System

AllMeal is an online menu and ordering system that allows employees to receive daily menus via Slack, select their meal choices, and manage their orders. The system is fully integrated with Slack and uses Celery for task scheduling to automate the process of sending menus and reminders.

## Features

- **Daily Menu Management**: Admins can create, update, and delete menus for specific days.
- **Slack Integration**: Employees receive daily menus via Slack and can order directly through Slack buttons.
- **Order Scheduling**: Menus are automatically sent at 12:00 PM every day, and employees can place orders between 12:00 PM and 12:30 PM.
- **Celery & Redis Integration**: Celery is used to schedule daily menu sending and reminders.
- **Reminder System**: Employees who haven't placed their orders will receive reminders via Slack.

---

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Tasks](#tasks)
- [Environment Variables](#environment-variables)
- [License](#license)

---

## Installation

### Prerequisites

- Docker
- Docker Compose

### Clone the Repository

```bash
git clone https://github.com/your-username/allmeal.git
cd allmeal
```

### Install Dependencies

All dependencies are managed via requirements.txt. The Docker container will handle installing them.

### Project Structure

Here is the project structure for the project.

```
allmeal/
├── allmeal_backend/         # Django project folder
│   ├── __init__.py          # Celery app initialized here
│   ├── settings.py          # Django settings
│   └── urls.py              # URL routing
├── menu/                    # Menu app (Handles menu creation and Slack interaction)
│   ├── models.py            # Models (Menu, Order)
│   ├── tasks.py             # Celery tasks (sending menus, reminders)
│   ├── slack.py             # Slack-related functions (sending messages)
│   ├── views.py             # Views (handles Slack interactions)
│   ├── serializers.py       # DRF serializers
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Dockerfile for building the app
└── requirements.txt         # Dependencies
```

#### Step 1: Environment Variables

Create a .env file in the project root and add the following environment variables:

```bash
DATABASE_URL=postgres://postgres:postgres@db:5432/allmeal_db
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_SIGNING_SECRET=your-slack-signing-secret
```

#### Step 2: Build and Run Containers

Build and run the project using Docker Compose:

```bash
docker-compose up --build
```

This command will:

Build the Django web service.
Run a PostgreSQL database.
Run a Redis instance to be used by Celery for task queuing.

#### Step 3: Apply Migrations

After the containers are running, apply database migrations:

```bash
docker-compose exec web python manage.py migrate
```

#### Step 4: Create a Superuser (for Admin access)

Create a superuser to access the Django admin dashboard:

```bash
docker-compose exec web python manage.py createsuperuser
```

## Usage

### Admins

Create Menus: Log in to the Django Admin interface (http://localhost:8000/admin/) and create daily menus.
View Orders: Admins can view all orders submitted by employees from the Django Admin dashboard.

### Employees (Slack Users)

Receive Menu: Every day at 12:00 PM, a menu will be sent to the Slack channel.
Place Orders: Employees can order via Slack between 12:00 PM and 12:30 PM by clicking on the menu options in the Slack message.
Receive Confirmation: Employees will receive a confirmation message once they place their order.

### Features:

Employees will receive a reminder if they haven't placed their orders before 12:30 PM.
Orders will be rejected if placed after 12:30 PM.

## Tasks

### Celery & Periodic Tasks

The project uses Celery for scheduling tasks like sending daily menus and reminders. To run Celery:

Start Celery Worker:

```bash
docker-compose exec web celery -A allmeal_backend worker -l info
```

Start Celery Beat (for scheduling periodic tasks):

```bash
Start Celery Beat (for scheduling periodic tasks):
```

## Environment Variables

- DATABASE_URL: PostgreSQL database connection string.
- SLACK_BOT_TOKEN: Slack bot token for interacting with the Slack API.
- SLACK_SIGNING_SECRET: Slack signing secret for validating requests from Slack.
- CELERY_BROKER_URL: URL for Redis (used by Celery for task queuing).
- CELERY_RESULT_BACKEND: Redis URL to store task results.