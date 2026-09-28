import time

import pytest
import requests

HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


@pytest.fixture
def token(api_url):
    response = requests.post(
        f"{api_url}/auth",
        json={"username": "admin", "password": "password123"},
        timeout=15,
    )
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def booking_payload():
    return {
        "firstname": f"Lukasz{int(time.time())}",
        "lastname": "Kap",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-10-01", "checkout": "2026-10-05"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def booking_id(api_url, booking_payload, token):
    response = requests.post(f"{api_url}/booking", json=booking_payload,
                             headers=HEADERS, timeout=15)
    assert response.status_code == 200
    created_id = response.json()["bookingid"]
    yield created_id
    # sprzątanie po teście
    requests.delete(f"{api_url}/booking/{created_id}",
                    headers={"Cookie": f"token={token}"}, timeout=15)


@pytest.mark.api
@pytest.mark.smoke
def test_health_check(api_url):
    """API-01"""
    assert requests.get(f"{api_url}/ping", timeout=15).status_code == 201


@pytest.mark.api
def test_auth_with_wrong_password_returns_no_token(api_url):
    """API-03"""
    response = requests.post(f"{api_url}/auth",
                             json={"username": "admin", "password": "wrong"}, timeout=15)
    body = response.json()

    assert "token" not in body
    assert body["reason"] == "Bad credentials"


@pytest.mark.api
@pytest.mark.smoke
def test_create_and_get_booking(api_url, booking_id, booking_payload):
    """API-04, API-05"""
    response = requests.get(f"{api_url}/booking/{booking_id}", headers=HEADERS, timeout=15)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.json() == booking_payload


@pytest.mark.api
def test_partial_update_with_token(api_url, booking_id, token):
    """API-08"""
    response = requests.patch(
        f"{api_url}/booking/{booking_id}",
        json={"additionalneeds": "Dinner"},
        headers={**HEADERS, "Cookie": f"token={token}"},
        timeout=15,
    )

    assert response.status_code == 200
    assert response.json()["additionalneeds"] == "Dinner"
    assert response.json()["lastname"] == "Kap"


@pytest.mark.api
def test_update_without_token_is_forbidden(api_url, booking_id):
    """API-09"""
    response = requests.patch(f"{api_url}/booking/{booking_id}",
                              json={"firstname": "Hacker"}, headers=HEADERS, timeout=15)

    assert response.status_code == 403


@pytest.mark.api
def test_deleted_booking_returns_404(api_url, booking_payload, token):
    """API-10, API-11"""
    created = requests.post(f"{api_url}/booking", json=booking_payload,
                            headers=HEADERS, timeout=15).json()["bookingid"]

    delete = requests.delete(f"{api_url}/booking/{created}",
                             headers={"Cookie": f"token={token}"}, timeout=15)
    assert delete.status_code == 201

    assert requests.get(f"{api_url}/booking/{created}", timeout=15).status_code == 404


@pytest.mark.api
def test_non_existing_booking_returns_404(api_url):
    """API-12"""
    assert requests.get(f"{api_url}/booking/999999999", timeout=15).status_code == 404
