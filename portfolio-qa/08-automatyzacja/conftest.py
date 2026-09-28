import os

import pytest
from selenium import webdriver

BASE_URL = "https://www.saucedemo.com"
API_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def driver():
    """Przeglądarka Chrome; w CI uruchamiana bez okna (HEADLESS=1)."""
    options = webdriver.ChromeOptions()
    if os.getenv("HEADLESS", "1") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Wyłącza okno Chrome o wycieku hasła, które zasłania stronę po zalogowaniu.
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def api_url():
    return API_URL
