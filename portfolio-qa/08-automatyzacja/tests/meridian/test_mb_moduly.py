"""Meridian Bank — historia, BLIK, lokaty, kredyty, kantor, wiadomości, ustawienia."""
import re

import pytest

from pages.meridian_page import parse_pln, tid

pytestmark = [pytest.mark.ui, pytest.mark.meridian]


# ---------- historia ----------
def test_history_search_filters_rows(bank):
    """MB-TC-020"""
    bank.go_to("history")
    bank.type(tid("history-search"), "wynagrodzenie")

    descriptions = bank.history_descriptions()
    assert descriptions
    assert all("Wynagrodzenie" in d for d in descriptions)


def test_history_incoming_filter_shows_only_positive_amounts(bank):
    """MB-TC-021"""
    bank.go_to("history")
    bank.select_value("history-type", "in")

    amounts = bank.history_amounts()
    assert amounts
    assert all(a > 0 for a in amounts)


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-08: przy 10 pozycjach na stronę wyświetla się 11 wierszy.")
def test_history_shows_ten_rows_per_page(bank):
    """MB-TC-022"""
    bank.go_to("history")

    assert len(bank.history_rows()) == 10


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-07: sortowanie po kwocie jest tekstowe, a nie liczbowe.")
def test_history_sort_by_amount_is_numeric(bank):
    """MB-TC-023"""
    bank.go_to("history")
    bank.click(tid("history-sort-amount"))   # pierwsze kliknięcie: malejąco

    amounts = bank.history_amounts()
    assert amounts == sorted(amounts, reverse=True)


# ---------- BLIK ----------
def test_blik_code_can_be_generated_and_cancelled(bank):
    """MB-TC-030"""
    bank.go_to("blik")
    bank.click(tid("blik-generate"))

    assert 0 < int(bank.text_of(tid("blik-countdown"))) <= 120
    bank.click(tid("blik-cancel"))
    assert bank.is_visible(tid("blik-generate"))


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-04: kod BLIK ma 5 cyfr zamiast 6.")
def test_blik_code_has_six_digits(bank):
    """MB-TC-031"""
    bank.go_to("blik")
    bank.click(tid("blik-generate"))

    digits = re.sub(r"\D", "", bank.text_of(tid("blik-code")))
    assert len(digits) == 6


# ---------- lokaty ----------
def test_deposit_calculator_six_months(bank):
    """MB-TC-040 — 10 000 zł × 4,80% × 6/12 = 240,00 zł brutto; netto po 19% = 194,40 zł"""
    bank.go_to("deposits")

    assert parse_pln(bank.text_of(tid("deposit-profit"))) == pytest.approx(240.00)
    assert parse_pln(bank.text_of(tid("deposit-net"))) == pytest.approx(194.40)


def test_deposit_amount_below_minimum_shows_error(bank):
    """MB-TC-041"""
    bank.go_to("deposits")
    bank.type(tid("deposit-amount"), "999")

    assert bank.text_of(tid("deposit-amount-error")) == "Kwota od 1 000 do 500 000 zł."


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-06: lokata 12 mies. — w ofercie 5,00%, w wyliczeniu 4,80%.")
def test_twelve_month_deposit_uses_advertised_rate(bank):
    """MB-TC-042"""
    bank.go_to("deposits")
    bank.select_value("deposit-period", "12")

    # 10 000 zł × 5,00% × 12/12 = 500,00 zł brutto
    assert parse_pln(bank.text_of(tid("deposit-profit"))) == pytest.approx(500.00)


# ---------- kredyty ----------
def test_loan_installment_default_values(bank):
    """MB-TC-050 — 25 000 zł, 36 mies., 9,99% → rata annuitetowa 806,56 zł"""
    bank.go_to("loans")

    assert parse_pln(bank.text_of(tid("loan-installment"))) == pytest.approx(806.56)


def test_loan_application_requires_consent(bank):
    """MB-TC-051"""
    bank.go_to("loans")
    bank.click(tid("loan-apply"))
    bank.type(tid("loan-income"), "500")
    bank.click(tid("loan-submit"))

    assert bank.error_visible("loan-income-error")
    assert bank.error_visible("loan-consent-error")


# ---------- kantor ----------
def test_fx_same_currency_disables_exchange(bank):
    """MB-TC-060"""
    bank.go_to("fx")
    bank.select_text("fx-from", "EUR")
    bank.select_text("fx-to", "EUR")

    assert not bank.find(tid("fx-execute")).is_enabled()


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-05: PLN→EUR przeliczane po kursie kupna 4,24 zamiast sprzedaży 4,38.")
def test_fx_pln_to_eur_uses_sell_rate(bank):
    """MB-TC-061 — 100 PLN / 4,38 = 22,83 EUR"""
    bank.go_to("fx")

    assert "22,83" in bank.text_of(tid("fx-result"))


# ---------- wiadomości ----------
@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-10: licznik nieprzeczytanych nie znika po przeczytaniu wiadomości.")
def test_unread_badge_disappears_after_reading(bank):
    """MB-TC-070"""
    assert bank.text_of(tid("messages-badge")) == "1"

    bank.go_to("messages")
    bank.click(tid("message-M-3"))
    bank.find(tid("message-detail"))
    bank.click(tid("message-back"))

    assert not bank.is_visible(tid("messages-badge"))


# ---------- ustawienia ----------
def test_profile_invalid_email_is_rejected(bank):
    """MB-TC-080"""
    bank.go_to("settings")
    bank.click(tid("profile-edit"))
    bank.type(tid("profile-email"), "jan.kowalski@")
    bank.click(tid("profile-save"))

    assert bank.error_visible("profile-email-error")


def test_password_change_with_mismatched_repeat(bank):
    """MB-TC-081"""
    bank.go_to("settings")
    bank.type(tid("password-current"), "Test123!")
    bank.type(tid("password-new"), "NoweHaslo1!")
    bank.type(tid("password-repeat"), "InneHaslo1!")
    bank.click(tid("password-save"))

    assert bank.error_visible("password-repeat-error")


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-09: hasło 8-znakowe odrzucane mimo wymagania „min. 8 znaków”.")
def test_password_with_exactly_eight_chars_is_accepted(bank):
    """MB-TC-082 — wartość brzegowa: 8 znaków"""
    bank.go_to("settings")
    bank.type(tid("password-current"), "Test123!")
    bank.type(tid("password-new"), "Abcdef1!")
    bank.type(tid("password-repeat"), "Abcdef1!")
    bank.click(tid("password-save"))

    assert not bank.error_visible("password-new-error")
    assert bank.is_visible(tid("modal-sms"))
