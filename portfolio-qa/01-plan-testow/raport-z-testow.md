# Raport z testów — SauceDemo v1

| | |
|---|---|
| **Tester** | Łukasz Kap |
| **Zakres** | Zgodnie z [planem testów](plan-testow-saucedemo.md) |
| **Środowisko** | https://www.saucedemo.com · Chrome, Firefox, Edge · emulacja iPhone 12 Pro |

## 1. Podsumowanie dla zespołu

Główna ścieżka zakupowa dla `standard_user` działa poprawnie (logowanie → koszyk → zamówienie →
potwierdzenie, obliczenia kwot zgodne). Wykryto **6 defektów**, w tym **1 krytyczny** blokujący
złożenie zamówienia dla `problem_user` (BUG-003). Wymagają decyzji PO: składanie zamówienia
z pustym koszykiem (BUG-005) oraz brak walidacji formatu kodu pocztowego.

**Rekomendacja:** wydanie możliwe dla ścieżki podstawowej po naprawie BUG-003 i decyzji w sprawie BUG-005.

## 2. Wykonanie przypadków testowych (użytkownik `standard_user`)

| Moduł | Liczba | Pass | Fail | Blocked / Do decyzji PO |
|---|---|---|---|---|
| Logowanie | 9 | 7 | 0 | 2 (TC-005, TC-006 — oczekiwane zachowanie niezdefiniowane) |
| Produkty | 6 | 6 | 0 | 0 |
| Koszyk | 6 | 5 | 1 (TC-021 → BUG-006) | 0 |
| Zamówienie | 6 | 4 | 1 (TC-026 → BUG-005) | 1 (TC-024 — limity pól) |
| Menu | 2 | 2 | 0 | 0 |
| UI / RWD | 1 | 1 | 0 | 0 |
| **Razem** | **30** | **25** | **2** | **3** |

Dodatkowo te same przypadki kluczowe wykonane dla `problem_user` → BUG-001 – BUG-004.

## 3. Defekty

| Ważność | Liczba | ID |
|---|---|---|
| Critical | 1 | BUG-003 |
| Major | 4 | BUG-001, BUG-002, BUG-004, BUG-005 |
| Minor | 1 | BUG-006 |

## 4. Testy eksploracyjne

3 sesje (łącznie 2 h 45 min) — szczegóły w [sesje-eksploracyjne.md](../04-testy-eksploracyjne/sesje-eksploracyjne.md).
Wnioski: brak walidacji długości i formatu pól, możliwość pominięcia formularza danych przez bezpośredni URL,
sesja oparta o niezabezpieczone ciasteczko (obserwacja).

## 5. Testy API (Restful-Booker)

14 przypadków, 3 obserwacje niezgodne z konwencjami REST (kody 200/201/500 zamiast 401/204/400).

## 6. Ryzyka i rekomendacje

1. Dodać walidację formatu i długości pól formularza zamówienia (po decyzji PO).
2. Zablokować checkout z pustym koszykiem.
3. Włączyć smoke test automatyczny (PyTest + Selenium) do pipeline CI, uruchamiany dla kilku typów kont.
4. Dodać testy wizualne dla `visual_user` (porównanie zrzutów ekranu).
