import pytest

from pages.meridian_page import MeridianBank

MERIDIAN_URL = "https://lukasztm.github.io/MeridianBank/"


@pytest.fixture
def meridian(driver):
    """Strona logowania Meridian Bank."""
    return MeridianBank(driver).open(MERIDIAN_URL)


@pytest.fixture
def bank(meridian):
    """Zalogowany użytkownik jan.kowalski na pulpicie."""
    return meridian.login_as_default_user()
