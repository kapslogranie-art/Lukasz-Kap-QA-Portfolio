"""Meridian Bank — przelewy krajowe i zlecenia stałe."""
import pytest
from selenium.webdriver.common.by import By

from pages.meridian_page import tid

pytestmark = [pytest.mark.ui, pytest.mark.meridian]


@pytest.mark.smoke
def test_domestic_transfer_debits_personal_account(bank):
    """MB-TC-010 — przelew E2E: formularz → podsumowanie → SMS → potwierdzenie"""
    before = bank.balance("ror")

    bank.go_to("transfers")
    reference = bank.send_domestic_transfer("100,50", "Test automatyczny")

    assert reference.startswith("PRZ-")
    bank.go_to("dashboard")
    assert bank.balance("ror") == pytest.approx(before - 100.50)


def test_transfer_summary_shows_entered_data(bank):
    """MB-TC-011"""
    bank.go_to("transfers")
    bank.fill_domestic_transfer("250", "Czynsz")

    assert bank.text_of(tid("summary-recipient")) == "Anna Nowak"
    assert bank.text_of(tid("summary-amount")).startswith("250,00")


def test_transfer_form_validation(bank):
    """MB-TC-012"""
    bank.go_to("transfers")
    bank.type(tid("transfer-recipient"), "Jo")
    bank.type(tid("transfer-account"), "6110901014")
    bank.type(tid("transfer-amount"), "abc")
    bank.click(tid("transfer-submit"))

    assert bank.error_visible("transfer-recipient-error")
    assert bank.error_visible("transfer-account-error")
    assert bank.error_visible("transfer-amount-error")
    assert bank.error_visible("transfer-title-error")
    assert not bank.is_visible(tid("transfer-summary"))


def test_transfer_above_balance_is_rejected(bank):
    """MB-TC-013"""
    bank.go_to("transfers")
    bank.fill_domestic_transfer("99999999", "Za dużo")

    assert bank.text_of(tid("transfer-amount-error")) == "Niewystarczające środki na rachunku."


@pytest.mark.xfail(strict=True, reason="MB-03: przelew na kwotę 0,00 zł przechodzi walidację.")
def test_transfer_with_zero_amount_is_rejected(bank):
    """MB-TC-014"""
    bank.go_to("transfers")
    bank.fill_domestic_transfer("0", "Zero")

    assert bank.error_visible("transfer-amount-error")


@pytest.mark.xfail(strict=True, reason="MB-02: przelew z konta oszczędnościowego obciąża konto osobiste.")
def test_transfer_from_savings_debits_savings_account(bank):
    """MB-TC-015"""
    ror_before, sav_before = bank.balance("ror"), bank.balance("sav")

    bank.go_to("transfers")
    bank.send_domestic_transfer("100", "Z oszczędności", from_account="sav")
    bank.go_to("dashboard")

    assert bank.balance("sav") == pytest.approx(sav_before - 100)
    assert bank.balance("ror") == pytest.approx(ror_before)


def _create_standing_order(bank, name):
    bank.click(tid("standing-new"))
    bank.type(tid("standing-recipient"), name)
    bank.type(tid("standing-title"), "Abonament")
    bank.type(tid("standing-amount"), "50")
    bank.click(tid("standing-save"))
    bank.wait.until(lambda d: not bank.is_visible(tid("modal-standing")))


@pytest.mark.xfail(strict=True, reason="MB-12: po usunięciu zlecenia nowe zlecenia dostają zduplikowane ID.")
def test_standing_orders_have_unique_ids(bank):
    """MB-TC-017"""
    bank.go_to("transfers")
    bank.click(tid("tab-standing"))

    _create_standing_order(bank, "Siłownia")          # dostaje ST-1002
    bank.click((By.CSS_SELECTOR, "[data-st-del='ST-1001']"))
    bank.confirm_modal()
    _create_standing_order(bank, "Internet")          # oczekiwane ST-1003, jest ST-1002

    toggles = bank.driver.find_elements(By.CSS_SELECTOR, "[data-testid='standing-list'] [data-st-toggle]")
    ids = [t.get_attribute("data-st-toggle") for t in toggles]
    assert len(ids) == 2
    assert len(set(ids)) == len(ids)
