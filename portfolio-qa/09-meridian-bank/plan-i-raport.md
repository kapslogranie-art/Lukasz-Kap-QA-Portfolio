# Meridian Bank — plan testów i raport

## 1. Zakres

| Moduł | W zakresie |
|---|---|
| Logowanie | Login + hasło, weryfikacja SMS, blokada po nieudanych próbach, „Zapamiętaj login”, wylogowanie |
| Sesja | Automatyczne wylogowanie, ostrzeżenie o wygasaniu, przedłużenie sesji |
| Pulpit | Salda rachunków, ostatnie operacje, kursy walut, wykres wydatków |
| Przelewy | Krajowy (walidacja, podsumowanie, SMS, potwierdzenie), własny, zaplanowany, zlecenia stałe |
| Historia | Wyszukiwanie, filtry, sortowanie, stronicowanie, eksport CSV, szczegóły operacji |
| Karty | Pokaż/ukryj numer, blokada/odblokowanie, limity z autoryzacją SMS |
| BLIK | Generowanie, odliczanie 120 s, kopiowanie, anulowanie, wygaśnięcie |
| Lokaty / Kredyty | Kalkulatory, otwieranie i zrywanie lokaty, wniosek kredytowy |
| Kantor | Przelicznik, wymiana PLN ⇄ EUR |
| Wiadomości / Ustawienia / Pomoc | Licznik nieprzeczytanych, profil, zmiana hasła, powiadomienia, FAQ, formularz kontaktowy |

**Poza zakresem:** wydajność, prawdziwe bezpieczeństwo (aplikacja nie ma backendu), dostępność w pełnym zakresie WCAG.

## 2. Ryzyka i priorytety

| Ryzyko | Wpływ | Priorytet |
|---|---|---|
| Błędne kwoty / obciążenie złego rachunku | Strata finansowa klienta lub banku | **Najwyższy** |
| Obejście autoryzacji (SMS, blokada logowania) | Przejęcie konta | **Najwyższy** |
| Nieprawidłowe kursy / odsetki | Strata finansowa, reklamacje, ryzyko regulacyjne | Wysoki |
| Błędna prezentacja historii | Klient nie znajduje operacji, reklamacje | Średni |
| UI / komunikaty | Frustracja, zgłoszenia na infolinię | Niski |

## 3. Podejście

- Przypadki testowe dla każdego modułu (techniki: wartości brzegowe, klasy równoważności, przejścia stanów).
- Obliczenia weryfikowane niezależnie (arkusz / Python): odsetki, rata annuitetowa, przewalutowanie.
- Sesje eksploracyjne: sekwencje operacji, dane nietypowe, zmiana ustawień w trakcie działania.
- Automatyzacja krytycznych ścieżek i 13 z 16 znalezionych błędów (PyTest + Selenium, Page Object),
  uruchamiana w GitHub Actions.
- Środowisko: Chrome (desktop 1920×1080), Chrome DevTools — emulacja telefonu.

## 4. Wyniki

| | Liczba |
|---|---|
| Przypadki testowe | 47 |
| Zaliczone | 31 |
| Niezaliczone (błąd) | 16 |
| Zgłoszone błędy | 16 (Critical 4 · Major 7 · Minor 4 · Trivial 1) |
| Obserwacje / sugestie | 5 |
| Testy automatyczne | 32 (19 przechodzi, 13 dokumentuje znane błędy jako xfail) |

## 5. Rekomendacja

**Wersja nie nadaje się do wydania.** Blokujące są błędy finansowe (MB-02, MB-05, MB-13)
i niedziałający BLIK (MB-04). Przed wydaniem należy też poprawić bezpieczeństwo logowania
(MB-01, MB-16). Po poprawkach: retest zgłoszeń + pełna regresja automatyczna (`pytest -m meridian`)
+ regresja manualna modułów Przelewy, Lokaty, Kantor.
