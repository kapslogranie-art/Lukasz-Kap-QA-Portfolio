"""Meridian Bank — logowanie, SMS, wylogowanie, sesja.

Testy oznaczone xfail(strict=True) dokumentują znalezione błędy (MB-xx).
Gdy błąd zostanie naprawiony, test zacznie przechodzić i pipeline to zgłosi —
wtedy trzeba zamknąć zgłoszenie i usunąć znacznik xfail.
"""
import pytest

from pages.meridian_page import LOGIN, PASSWORD, tid

pytestmark = [pytest.mark.ui, pytest.mark.meridian]


@pytest.mark.smoke
def test_login_with_sms_opens_dashboard(meridian):
    """MB-TC-001"""
    meridian.login_as_default_user()

    assert meridian.text_of(tid("page-title")) == "Pulpit"
    assert meridian.is_visible(tid("accounts-grid"))
    meridian.wait_toast("Zalogowano pomyślnie")


def test_wrong_password_shows_remaining_attempts(meridian):
    """MB-TC-002"""
    meridian.login(LOGIN, "Zle_haslo1")

    meridian.wait.until(lambda d: meridian.is_visible(tid("login-error")))
    assert meridian.login_error() == "Nieprawidłowy login lub hasło. Pozostałe próby: 2."


def test_empty_login_form_shows_field_errors(meridian):
    """MB-TC-003"""
    meridian.click(tid("login-submit"))

    assert meridian.text_of(tid("login-username-error")) == "Podaj login."
    assert meridian.text_of(tid("login-password-error")) == "Podaj hasło."


def test_wrong_sms_code_is_rejected(meridian):
    """MB-TC-005"""
    meridian.login(LOGIN, PASSWORD)
    meridian.find(tid("login-sms-input"))
    meridian.enter_login_sms("000000")

    assert meridian.text_of(tid("login-sms-error")) == "Nieprawidłowy kod SMS. Spróbuj ponownie."
    assert not meridian.is_visible(tid("page-dashboard"))


@pytest.mark.xfail(strict=True, reason="MB-01: blokada konta już po 2. nieudanej próbie zamiast po 3.")
def test_account_is_not_locked_after_two_failed_attempts(meridian):
    """MB-TC-004"""
    meridian.login(LOGIN, "Zle_haslo1")
    meridian.wait.until(lambda d: "próby: 2" in meridian.driver.find_element(*tid("login-error")).text)

    meridian.login(LOGIN, "Zle_haslo2")
    meridian.wait.until(
        lambda d: meridian.is_visible(tid("login-lockout"))
        or "próby: 1" in d.find_element(*tid("login-error")).text
    )

    assert not meridian.is_visible(tid("login-lockout"))


@pytest.mark.xfail(strict=True, reason="MB-16: brak limitu prób kodu SMS przy logowaniu.")
def test_login_sms_step_is_blocked_after_three_wrong_codes(meridian):
    """MB-TC-006"""
    meridian.login(LOGIN, PASSWORD)
    meridian.find(tid("login-sms-input"))
    for _ in range(3):
        meridian.enter_login_sms("000000")

    meridian.enter_login_sms("123456")

    # Oczekiwane: po 3 błędnych kodach powrót do logowania, a nie wejście do aplikacji.
    assert not meridian.appears_within(tid("page-dashboard"), 4)


def test_logout(bank):
    """MB-TC-007"""
    bank.logout()

    assert bank.text_of(tid("login-info-banner")) == "Zostałeś poprawnie wylogowany. Do zobaczenia!"
    assert bank.driver.find_element(*tid("login-password")).get_attribute("value") == ""


@pytest.mark.xfail(strict=True, reason="MB-11: przy limicie 1 min ostrzeżenie o sesji pojawia się natychmiast.")
def test_one_minute_timeout_does_not_warn_immediately(bank):
    """MB-TC-009"""
    bank.go_to("settings")
    bank.select_value("session-timeout", "1")

    assert not bank.appears_within(tid("modal-session"), 4)
