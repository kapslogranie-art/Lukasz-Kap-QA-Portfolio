import pytest

from pages.checkout_pages import (
    CartPage,
    CheckoutCompletePage,
    CheckoutInfoPage,
    CheckoutOverviewPage,
)
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def inventory(driver, base_url):
    LoginPage(driver).open(base_url).login("standard_user", "secret_sauce")
    return InventoryPage(driver)


@pytest.mark.ui
def test_sort_by_price_low_to_high(inventory):
    """TC-012"""
    inventory.sort_by("lohi")
    prices = inventory.item_prices()

    assert prices == sorted(prices)
    assert prices[0] == 7.99
    assert prices[-1] == 49.99


@pytest.mark.ui
def test_sort_by_name_z_to_a(inventory):
    """TC-011"""
    inventory.sort_by("za")
    names = inventory.item_names()

    assert names == sorted(names, reverse=True)


@pytest.mark.ui
def test_add_and_remove_from_cart(inventory):
    """TC-016, TC-018"""
    inventory.add_to_cart("sauce-labs-backpack")
    assert inventory.cart_count() == 1

    inventory.remove_from_cart("sauce-labs-backpack")
    assert inventory.cart_count() == 0


@pytest.mark.ui
@pytest.mark.smoke
def test_full_checkout(driver, inventory):
    """TC-022 — pełna ścieżka zakupu E2E"""
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    assert inventory.cart_count() == 2

    inventory.open_cart()
    cart = CartPage(driver)
    assert cart.item_names() == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
    cart.checkout()

    CheckoutInfoPage(driver).fill("Jan", "Kowalski", "50-051")

    overview = CheckoutOverviewPage(driver)
    assert overview.subtotal() == 39.98
    assert overview.tax() == 3.20
    assert overview.total() == pytest.approx(overview.subtotal() + overview.tax())
    overview.finish()

    assert CheckoutCompletePage(driver).header() == "Thank you for your order!"
    assert inventory.cart_count() == 0


@pytest.mark.ui
@pytest.mark.parametrize(
    "first, last, postal, expected_error",
    [
        ("", "", "", "Error: First Name is required"),
        ("Jan", "", "", "Error: Last Name is required"),
        ("Jan", "Kowalski", "", "Error: Postal Code is required"),
    ],
    ids=["no-first-name", "no-last-name", "no-postal-code"],
)
def test_checkout_form_validation(driver, inventory, first, last, postal, expected_error):
    """TC-023"""
    inventory.add_to_cart("sauce-labs-onesie")
    inventory.open_cart()
    CartPage(driver).checkout()

    form = CheckoutInfoPage(driver)
    form.fill(first, last, postal)

    assert form.error_message() == expected_error
