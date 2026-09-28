# Plan testów — SauceDemo v1

| | |
|---|---|
| **Autor** | Łukasz Kap |
| **Wersja dokumentu** | 1.0 |
| **Aplikacja** | SauceDemo — https://www.saucedemo.com |
| **Typ** | Aplikacja webowa e-commerce |

## 1. Cel

Ocena gotowości aplikacji do wydania poprzez weryfikację kluczowych funkcji biznesowych
(logowanie, katalog produktów, koszyk, zamówienie) oraz wykrycie i raportowanie defektów.

## 2. Zakres

**W zakresie:**
- Logowanie i wylogowanie (w tym użytkownicy o różnych rolach/stanach)
- Lista produktów, szczegóły produktu, sortowanie
- Koszyk: dodawanie, usuwanie, licznik
- Checkout: formularz danych, podsumowanie, obliczenia, potwierdzenie
- Menu boczne (All Items, About, Logout, Reset App State)
- Podstawowa responsywność (desktop, tablet, telefon — emulacja w DevTools)
- Testy API na osobnej usłudze Restful-Booker (ćwiczeniowo — patrz `05-testy-api`)

**Poza zakresem:**
- Testy wydajnościowe i bezpieczeństwa (poza obserwacjami z testów eksploracyjnych)
- Płatności rzeczywiste (aplikacja ich nie obsługuje)

## 3. Rodzaje testów i podejście

| Rodzaj | Podejście |
|---|---|
| Smoke | 5 krytycznych przypadków (P1) przed każdą sesją testów |
| Funkcjonalne | Przypadki testowe z `02-przypadki-testowe`, techniki: klasy równoważności, wartości brzegowe, tablice decyzyjne |
| Eksploracyjne | Sesje 45–60 min z kartą testu (charter), notatki i raport z sesji |
| Regresyjne | Checklista regresji po każdej poprawce; retest zgłoszonych błędów |
| UI / RWD | Chrome DevTools — iPhone 12, Pixel 7, iPad; 1920×1080 |
| Cross-browser | Chrome, Firefox, Edge (aktualne wersje) |
| Automatyczne (wsparcie) | Smoke w PyTest + Selenium (`08-automatyzacja`) |

## 4. Środowisko i dane testowe

- System: Windows 11 / Linux; przeglądarki: Chrome, Firefox, Edge
- Użytkownicy testowi: `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`,
  `error_user`, `visual_user` — hasło `secret_sauce`
- Narzędzia: Jira (zgłoszenia), Xray/TestRail (przypadki — import CSV), Chrome DevTools, Postman, Git

## 5. Kryteria wejścia i wyjścia

**Wejście:** aplikacja dostępna, wymagania przeanalizowane, pytania do PO zadane, przypadki testowe gotowe.

**Wyjście:**
- 100% przypadków P1 i P2 wykonanych
- Brak otwartych błędów o ważności *Critical* / *Blocker*
- Wszystkie błędy *Major* opisane i zaakceptowane przez PO lub naprawione
- Raport z testów przekazany zespołowi

## 6. Klasyfikacja defektów

| Ważność (Severity) | Opis |
|---|---|
| Blocker | Brak możliwości kontynuowania testów / kluczowa funkcja nie działa |
| Critical | Błąd w kluczowym procesie biznesowym, brak obejścia |
| Major | Istotny błąd funkcjonalny, istnieje obejście |
| Minor | Drobny błąd funkcjonalny lub wizualny |
| Trivial | Kosmetyka, literówki |

Priorytet (Highest–Lowest) ustala PO na podstawie ważności i wpływu biznesowego.

## 7. Cykl życia błędu (Jira)

`Open → In Progress → Resolved → Retest → Closed` (lub `Reopened`, gdy retest nie przechodzi).

## 8. Komunikacja

- Daily: status testów, blokery
- Nowy błąd *Critical/Blocker* — zgłoszenie w Jira + natychmiastowa informacja do developera / PO
- Wątpliwości co do wymagań — pytanie do analityka **przed** zgłoszeniem błędu

## 9. Ryzyka projektu testowego

| Ryzyko | Mitygacja |
|---|---|
| Niestabilne środowisko | Zgłoszenie, testy innych obszarów, powtórzenie smoke |
| Niejasne wymagania | Lista pytań do PO (`analiza-wymagan.md`) |
| Brak czasu na pełną regresję | Regresja oparta o ryzyko — najpierw P1/P2 |

## 10. Artefakty

Analiza wymagań · Przypadki testowe · Checklista regresji · Raporty błędów · Raporty z sesji
eksploracyjnych · [Raport z testów](raport-z-testow.md)
