from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    ITEM_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    SORT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def title(self):
        return self.text_of(self.TITLE)

    def item_count(self):
        return len(self.find_all(self.ITEMS))

    def item_names(self):
        return [e.text for e in self.find_all(self.ITEM_NAMES)]

    def item_prices(self):
        return [float(e.text.replace("$", "")) for e in self.find_all(self.ITEM_PRICES)]

    def sort_by(self, value):
        """value: az, za, lohi, hilo"""
        Select(self.find(self.SORT)).select_by_value(value)

    def add_to_cart(self, product_slug):
        """product_slug np. 'sauce-labs-backpack'."""
        self.click((By.CSS_SELECTOR, f"[data-test='add-to-cart-{product_slug}']"))

    def remove_from_cart(self, product_slug):
        self.click((By.CSS_SELECTOR, f"[data-test='remove-{product_slug}']"))

    def cart_count(self):
        if not self.is_present(self.CART_BADGE):
            return 0
        return int(self.text_of(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)
