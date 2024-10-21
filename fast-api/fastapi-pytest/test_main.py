import pytest
from fastapi.testclient import TestClient
from main import app # imports the FastAPI app

# pass your app to the test client instance
client = TestClient(app)

def test_add_numbers_basic():
    # testing adding the numbers
    response = client.get("/add?num1=69.0&num2=420.0")
    assert response.status_code == 200
    assert response.json() == {"result": 489.0}

def test_add_numbers_non_floats():
    # Test adding two different numbers
    response = client.get("/add?num1=10&num2=20")
    assert response.status_code == 200
    assert response.json() == {"result": 30}

def test_add_numbers_one_zero():
    # Test adding zero to a number
    response = client.get("/add?num1=7&num2=0")
    assert response.status_code == 200
    assert response.json() == {"result": 7}

def test_add_numbers_negatives():
    # Test adding negative numbers
    response = client.get("/add?num1=-2&num2=-5")
    assert response.status_code == 200
    assert response.json() == {"result": -7}

def test_invalid_input():
    # Test invalid input (non-numeric values)
    response = client.get("/add?num1=abc&num2=def")
    assert response.status_code == 422  # Expect a validation error