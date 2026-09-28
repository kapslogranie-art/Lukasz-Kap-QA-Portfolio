from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CHECKOUT = (By.CSS_SELECTOR, "[data-test='checkout']")
    ITEM_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    def item_names(self):
        return [e.text for e in self.find_all(self.ITEM_NAMES)]

    def checkout(self):
        self.click(self.CHECKOUT)


class CheckoutInfoPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "[data-test='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "[data-test='lastName']")
    POSTAL_CODE = (By.CSS_SELECTOR, "[data-test='postalCode']")
    CONTINUE = (By.CSS_SELECTOR, "[data-test='continue']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def fill(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE)

    def error_message(self):
        return self.text_of(self.ERROR)


class CheckoutOverviewPage(BasePage):
    SUBTOTAL = (By.CSS_SELECTOR, "[data-test='subtotal-label']")
    TAX = (By.CSS_SELECTOR, "[data-test='tax-label']")
    TOTAL = (By.CSS_SELECTOR, "[data-test='total-label']")
    FINISH = (By.CSS_SELECTOR, "[data-test='finish']")

    @staticmethod
    def _amount(label_text):
        # "Item total: $39.98" -> 39.98
        return float(label_text.split("$")[1])

    def subtotal(self):
        return self._amount(self.text_of(self.SUBTOTAL))

    def tax(self):
        return self._amount(self.text_of(self.TAX))

    def total(self):
        return self._amount(self.text_of(self.TOTAL))

    def finish(self):
        self.click(self.FINISH)


class CheckoutCompletePage(BasePage):
    HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")

    def header(self):
        return self.text_of(self.HEADER)
