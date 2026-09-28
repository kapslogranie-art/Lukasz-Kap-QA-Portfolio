import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from pages.base_page import BasePage

LOGIN = "jan.kowalski"
PASSWORD = "Test123!"
SMS_CODE = "123456"


def tid(test_id):
    """Lokator po atrybucie data-testid."""
    return (By.CSS_SELECTOR, f"[data-testid='{test_id}']")


def parse_pln(text):
    """'12 543,21 zł' / '-45,20 zł' / '+8 500,00 zł' -> float"""
    cleaned = text.replace("−", "-")
    cleaned = re.sub(r"[^\d,\-]", "", cleaned).replace(",", ".")
    return float(cleaned)


class MeridianBank(BasePage):
    """Page Object aplikacji Meridian Bank (jedna strona, wiele widoków)."""

    LOADER = tid("global-loader")
    TOAST = tid("toast")

    # ---------- ogólne ----------
    def open(self, url):
        self.driver.get(url)
        self.find(tid("login-username"))
        return self

    def wait_loader(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))

    def wait_toasts_gone(self, timeout=8):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(*self.TOAST)) == 0
        )

    def toast_texts(self):
        return [t.text for t in self.driver.find_elements(*self.TOAST)]

    def wait_toast(self, fragment):
        self.wait.until(lambda d: any(fragment in t for t in self.toast_texts()))

    def is_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return bool(elements) and elements[0].is_displayed()

    def appears_within(self, locator, seconds):
        try:
            WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def select_value(self, test_id, value):
        Select(self.find(tid(test_id))).select_by_value(value)

    def select_text(self, test_id, text):
        Select(self.find(tid(test_id))).select_by_visible_text(text)

    # ---------- logowanie ----------
    def login(self, username, password):
        self.type(tid("login-username"), username)
        self.type(tid("login-password"), password)
        self.click(tid("login-submit"))

    def enter_login_sms(self, code):
        self.type(tid("login-sms-input"), code)
        self.click(tid("login-sms-submit"))

    def login_as_default_user(self):
        self.login(LOGIN, PASSWORD)
        self.find(tid("login-sms-input"))
        self.enter_login_sms(SMS_CODE)
        self.find(tid("page-dashboard"))
        self.wait_loader()
        return self

    def login_error(self):
        return self.text_of(tid("login-error"))

    def logout(self):
        self.wait_toasts_gone()
        self.click(tid("user-menu-button"))
        self.click(tid("user-menu-logout"))
        self.confirm_modal()
        self.find(tid("login-view"))

    # ---------- nawigacja i modale ----------
    def go_to(self, page):
        self.wait_loader()
        self.click(tid(f"nav-{page}"))
        self.find(tid(f"page-{page}"))
        self.wait_loader()

    def confirm_modal(self):
        self.click(tid("modal-confirm-ok"))
        self.wait.until(EC.invisibility_of_element_located(tid("modal-confirm")))

    def authorize_sms(self, code=SMS_CODE):
        self.type(tid("sms-input"), code)
        self.click(tid("sms-confirm"))

    # ---------- pulpit ----------
    def balance(self, account_id):
        return parse_pln(self.text_of(tid(f"balance-{account_id}")))

    # ---------- przelewy ----------
    def fill_domestic_transfer(self, amount, title, from_account="ror", saved_recipient="0"):
        self.select_value("transfer-from", from_account)
        self.select_value("transfer-saved-recipient", saved_recipient)
        self.type(tid("transfer-amount"), amount)
        self.type(tid("transfer-title"), title)
        self.click(tid("transfer-submit"))

    def send_domestic_transfer(self, amount, title, from_account="ror"):
        self.fill_domestic_transfer(amount, title, from_account)
        self.find(tid("transfer-summary"))
        self.click(tid("transfer-confirm"))
        self.authorize_sms()
        self.find(tid("transfer-success"))
        return self.text_of(tid("transfer-reference"))

    def error_visible(self, test_id):
        return self.is_visible(tid(test_id))

    # ---------- historia ----------
    HISTORY_ROWS = (By.CSS_SELECTOR, "[data-testid^='h-row-']")

    def history_rows(self):
        self.find(tid("history-table-body"))
        return self.driver.find_elements(*self.HISTORY_ROWS)

    def history_amounts(self):
        return [parse_pln(r.find_elements(By.TAG_NAME, "td")[3].text) for r in self.history_rows()]

    def history_descriptions(self):
        return [r.find_elements(By.TAG_NAME, "td")[1].text for r in self.history_rows()]
