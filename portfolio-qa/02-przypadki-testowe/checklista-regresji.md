# Checklista regresji — SauceDemo

Używana po każdej poprawce błędu lub nowej wersji. Zakres dobierany wg ryzyka:
**Smoke (P1)** zawsze → **P2** przy zmianach w danym module → **P3** przed wydaniem.

## Smoke (≈10 min)

- [ ] Logowanie `standard_user` działa (TC-001)
- [ ] Błędne dane → komunikat (TC-002)
- [ ] Brak dostępu do `/inventory.html` bez logowania (TC-008)
- [ ] Lista 6 produktów wyświetla się poprawnie (TC-010)
- [ ] Dodanie do koszyka zmienia licznik (TC-016)
- [ ] Pełna ścieżka zakupu kończy się potwierdzeniem (TC-022)
- [ ] Wylogowanie (TC-028)

## Regresja modułowa

| Zmiana w module… | Uruchom dodatkowo |
|---|---|
| Logowanie / sesja | TC-003 – TC-009, TC-028 |
| Katalog / sortowanie | TC-011 – TC-015 |
| Koszyk | TC-017 – TC-021, TC-025 |
| Checkout / ceny | TC-023 – TC-027 |
| CSS / layout | TC-030 + szybki przegląd wizualny wszystkich stron |

## Retest zgłoszonych błędów

- [ ] Wykonaj kroki z raportu błędu na nowej wersji
- [ ] Sprawdź obszary sąsiednie (np. poprawka w sortowaniu → sprawdź też stronę szczegółów produktu)
- [ ] Wynik: **Closed** (działa) lub **Reopened** (z komentarzem, wersją, zrzutem ekranu)

## Przeglądarki

- [ ] Chrome (aktualna) · [ ] Firefox (aktualna) · [ ] Edge (aktualna) · [ ] Widok mobilny (DevTools)

## Rejestr wykonania

| Data | Wersja / build | Zakres | Wynik | Uwagi |
|---|---|---|---|---|
| RRRR-MM-DD | … | Smoke | PASS / FAIL | … |
