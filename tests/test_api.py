"""API Tests"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Create test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    """Override database dependency for testing"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_database():
    """Setup and teardown test database"""
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    """Create test client"""
    return TestClient(app)


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_order(client):
    """Test creating a new order"""
    response = client.post(
        "/api/orders/",
        json={"name": "Test Order", "quantity": 5, "description": "Test description"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Order"
    assert data["quantity"] == 5
    assert data["description"] == "Test description"
    assert "id" in data


def test_read_orders(client):
    """Test reading all orders"""
    # Create test order
    client.post(
        "/api/orders/",
        json={"name": "Test Order", "quantity": 1, "description": "Test"},
    )

    # Read orders
    response = client.get("/api/orders/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["name"] == "Test Order"


def test_read_order(client):
    """Test reading a specific order"""
    # Create test order
    create_response = client.post(
        "/api/orders/",
        json={"name": "Test Order", "quantity": 1, "description": "Test"},
    )
    order_id = create_response.json()["id"]

    # Read the order
    response = client.get(f"/api/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Order"
    assert data["id"] == order_id


def test_update_order(client):
    """Test updating an order"""
    # Create test order
    create_response = client.post(
        "/api/orders/",
        json={"name": "Test Order", "quantity": 1, "description": "Test"},
    )
    order_id = create_response.json()["id"]

    # Update the order
    response = client.put(
        f"/api/orders/{order_id}",
        json={"name": "Updated Order", "quantity": 10},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Order"
    assert data["quantity"] == 10


def test_delete_order(client):
    """Test deleting an order"""
    # Create test order
    create_response = client.post(
        "/api/orders/",
        json={"name": "Test Order", "quantity": 1, "description": "Test"},
    )
    order_id = create_response.json()["id"]

    # Delete the order
    response = client.delete(f"/api/orders/{order_id}")
    assert response.status_code == 204

    # Verify order is deleted
    response = client.get(f"/api/orders/{order_id}")
    assert response.status_code == 404


def test_order_not_found(client):
    """Test accessing non-existent order"""
    response = client.get("/api/orders/99999")
    assert response.status_code == 404
