# Meridian Bank — projekt testowy bankowości internetowej

**Aplikacja:** https://lukasztm.github.io/MeridianBank/ — szkoleniowa bankowość internetowa
(podmiot fikcyjny, wersja 2.6.x, dane symulowane w przeglądarce, reset po odświeżeniu).
**Dane testowe:** login `jan.kowalski` · hasło `Test123!` · kod SMS `123456`

Aplikacja bankowa to dziedzina, w której błąd oznacza realne pieniądze klienta, dlatego testy
skupiają się na **poprawności kwot, autoryzacji i bezpieczeństwie sesji**.

## Zawartość

| Plik | Co zawiera |
|---|---|
| [`plan-i-raport.md`](plan-i-raport.md) | Zakres, ryzyka, podejście, wyniki i rekomendacja |
| [`przypadki-testowe.md`](przypadki-testowe.md) | 47 przypadków testowych w 10 obszarach |
| [`raporty-bledow.md`](raporty-bledow.md) | 16 zgłoszeń błędów (w tym 4 krytyczne) + obserwacje |
| [`../08-automatyzacja/tests/meridian`](../08-automatyzacja/tests/meridian) | 32 testy automatyczne PyTest + Selenium (Page Object) |

## Najważniejsze znaleziska

| ID | Błąd | Ważność |
|---|---|---|
| MB-02 | Przelew z konta oszczędnościowego obciąża konto osobiste | **Critical** |
| MB-04 | Kod BLIK ma 5 cyfr zamiast 6 — płatność BLIK niemożliwa | **Critical** |
| MB-05 | Kantor przelicza PLN→EUR po kursie kupna zamiast sprzedaży (strata banku ~3,3% na każdej wymianie) | **Critical** |
| MB-13 | Zduplikowane ID lokat — zerwanie jednej usuwa dwie, kapitał drugiej przepada | **Critical** |
| MB-01 | Blokada logowania po 2 zamiast 3 nieudanych próbach | Major |
| MB-16 | Brak limitu prób kodu SMS przy logowaniu | Major (bezpieczeństwo) |

## Jak testy automatyczne dokumentują błędy

Każdy zautomatyzowany błąd ma test oznaczony `@pytest.mark.xfail(strict=True, raises=AssertionError, reason="MB-xx: …")`:

- dziś test **oczekiwanie nie przechodzi** (xfail) — pipeline jest zielony, a raport pokazuje listę znanych błędów,
- `raises=AssertionError` sprawia, że za „znany błąd” uznawana jest tylko niespełniona asercja — zepsuty lokator czy timeout nadal zaczerwieni pipeline,
- gdy developer naprawi błąd, test zacznie przechodzić (XPASS) i przez `strict=True` **pipeline zrobi się czerwony**
  — to sygnał, żeby wykonać retest, zamknąć zgłoszenie i zdjąć znacznik `xfail`, a test staje się testem regresji.

```bash
cd portfolio-qa/08-automatyzacja
pytest -m meridian -rxX          # -rxX: podsumowanie znanych błędów (xfail) i naprawionych (xpass)
```

## Jak znalazłem błędy

1. **Testy funkcjonalne według przypadków** — porównanie z tym, co aplikacja sama deklaruje
   (panel danych testowych, FAQ, podpowiedzi przy polach, etykiety w listach).
2. **Wartości brzegowe** — kwota 0, hasło dokładnie 8-znakowe, 10 pozycji na stronę.
3. **Sprawdzanie obliczeń ręcznie** — odsetki lokaty, rata kredytu, kursy walut.
4. **Testy eksploracyjne sekwencji** — „utwórz → usuń → utwórz” (zduplikowane ID), zmiana ustawień sesji.
5. **Analiza kodu front-endu w DevTools** (aplikacja nie ma backendu — cała logika jest w JavaScript)
   do potwierdzenia przyczyny błędu i podania jej developerowi w zgłoszeniu.
