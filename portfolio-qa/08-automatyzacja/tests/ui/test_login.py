import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"


@pytest.mark.ui
@pytest.mark.smoke
def test_login_with_valid_credentials(driver, base_url):
    """TC-001"""
    LoginPage(driver).open(base_url).login("standard_user", PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.title() == "Products"
    assert "/inventory.html" in driver.current_url
    assert inventory.item_count() == 6


@pytest.mark.ui
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "wrong_pass",
         "Epic sadface: Username and password do not match any user in this service"),
        ("locked_out_user", PASSWORD,
         "Epic sadface: Sorry, this user has been locked out."),
        ("", "", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
    ],
    ids=["wrong-password", "locked-user", "empty-fields", "empty-password"],
)
def test_login_negative(driver, base_url, username, password, expected_error):
    """TC-002, TC-003, TC-004"""
    page = LoginPage(driver).open(base_url)
    page.login(username, password)

    assert page.error_message() == expected_error
    assert "/inventory.html" not in driver.current_url


@pytest.mark.ui
@pytest.mark.smoke
def test_inventory_not_accessible_without_login(driver, base_url):
    """TC-008"""
    driver.get(f"{base_url}/inventory.html")

    error = LoginPage(driver).error_message()
    assert "You can only access '/inventory.html' when you are logged in" in error
