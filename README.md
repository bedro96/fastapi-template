# FastAPI Template

A complete FastAPI application template with Azure PostgreSQL support, featuring CRUD operations, Jinja2 templates, and comprehensive testing.

## Features

- 🚀 **FastAPI** - Modern, fast web framework for building APIs
- 🗄️ **SQLAlchemy** - SQL toolkit and ORM with Azure PostgreSQL support
- 📦 **UV** - Fast Python package manager
- 🎨 **Jinja2 Templates** - Server-side rendering with Bootstrap 5.3 (gray theme)
- 🔒 **Security** - Bandit security testing
- ✨ **Code Quality** - Flake8, Black, and MyPy linting
- 🐳 **Docker** - Containerized deployment
- ✅ **Testing** - Pytest with async support

## Project Structure

```
fastapi-template/
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── order.py          # Order database model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── orders.py         # API CRUD endpoints
│   │   └── web.py            # Web UI routes
│   ├── templates/
│   │   ├── base.html         # Base template
│   │   ├── index.html        # Orders list
│   │   └── order_form.html   # Create/Edit form
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── __init__.py
│   ├── config.py             # Configuration settings
│   ├── database.py           # Database connection
│   ├── main.py               # Main FastAPI app
│   └── schemas.py            # Pydantic schemas
├── tests/
│   ├── __init__.py
│   └── test_api.py           # API tests
├── .env.example              # Environment variables template
├── .flake8                   # Flake8 configuration
├── .bandit                   # Bandit configuration
├── Dockerfile                # Docker configuration
├── pyproject.toml            # Project dependencies
└── README.md
```

## Prerequisites

- Python 3.11+
- UV package manager
- Azure PostgreSQL Flexible Server (or local PostgreSQL)

## Installation

### Using UV (Recommended)

1. Install UV:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Clone the repository:
```bash
git clone https://github.com/bedro96/fastapi-template.git
cd fastapi-template
```

3. Create virtual environment and install dependencies:
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your Azure PostgreSQL credentials
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000 for the web UI or http://localhost:8000/docs for API documentation.

## Database Configuration

### Azure PostgreSQL Flexible Server

Update your `.env` file with Azure PostgreSQL credentials:

```env
DATABASE_HOST=your-server.postgres.database.azure.com
DATABASE_PORT=5432
DATABASE_NAME=fastapi_db
DATABASE_USER=your_username
DATABASE_PASSWORD=your_password
```

### Local PostgreSQL

For local development:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=fastapi_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
```

## API Endpoints

### CRUD Operations

- `POST /api/orders/` - Create a new order
- `GET /api/orders/` - Get all orders
- `GET /api/orders/{order_id}` - Get a specific order
- `PUT /api/orders/{order_id}` - Update an order
- `DELETE /api/orders/{order_id}` - Delete an order

### Web UI

- `GET /` - View all orders
- `GET /orders/new` - Create new order form
- `GET /orders/{order_id}/edit` - Edit order form

### Health Check

- `GET /health` - Application health status

## Order Model

The Order table contains the following fields:

| Field       | Type    | Description                |
|-------------|---------|----------------------------|
| id          | Integer | Primary key (auto-increment)|
| name        | String  | Order name (max 255 chars) |
| quantity    | Integer | Order quantity (min 1)     |
| description | Text    | Order description (optional)|

## Testing

Run tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=app tests/
```

## Code Quality & Security

### Flake8 (Linting)
```bash
flake8 app tests
```

### Black (Code Formatting)
```bash
black app tests
```

### MyPy (Type Checking)
```bash
mypy app
```

### Bandit (Security Scanning)
```bash
bandit -r app
```

### Run All Checks
```bash
flake8 app tests && \
black --check app tests && \
mypy app && \
bandit -r app
```

## Docker Deployment

### Build Docker Image
```bash
docker build -t fastapi-template .
```

### Run Docker Container
```bash
docker run -d \
  --name fastapi-app \
  -p 8000:8000 \
  -e DATABASE_HOST=your-server.postgres.database.azure.com \
  -e DATABASE_USER=your_username \
  -e DATABASE_PASSWORD=your_password \
  -e DATABASE_NAME=fastapi_db \
  fastapi-template
```

### Using Docker Compose (Optional)

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_HOST=db
      - DATABASE_USER=postgres
      - DATABASE_PASSWORD=postgres
      - DATABASE_NAME=fastapi_db
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=fastapi_db
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

Run with:
```bash
docker-compose up -d
```

## Development

### Adding New Dependencies

```bash
uv pip install package-name
```

Update `pyproject.toml` to persist the dependency.

### Database Migrations

For production, consider using Alembic for database migrations:

```bash
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## UI Theme

The application uses Bootstrap 5.3 with a gray color scheme:
- Background: Light gray (#e9ecef)
- Primary theme: Gray (#6c757d)
- Smaller icons using Bootstrap Icons
- Responsive design for mobile and desktop

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linters
5. Submit a pull request

## Support

For issues and questions, please open an issue on GitHub.
