# Meridian Bank — przypadki testowe

**Warunek wstępny (o ile nie podano inaczej):** zalogowany `jan.kowalski` / `Test123!` / SMS `123456`,
świeżo załadowana strona (dane startowe: konto osobiste 12 543,21 zł, oszczędnościowe 45 200,00 zł,
walutowe 3 250,50 €).
**Auto** — przypadek pokryty testem w [`08-automatyzacja/tests/meridian`](../08-automatyzacja/tests/meridian)
(w docstringu testu jest ID przypadku).

## Logowanie i sesja

| ID | Tytuł | Kroki / dane | Oczekiwany rezultat | Wynik | Auto |
|---|---|---|---|---|---|
| MB-TC-001 | Poprawne logowanie z SMS | Login i hasło poprawne → kod `123456` | Pulpit, tytuł „Pulpit”, toast „Zalogowano pomyślnie. Witaj, Jan!” | PASS | ✔ |
| MB-TC-002 | Błędne hasło | `jan.kowalski` / `Zle_haslo1` | „Nieprawidłowy login lub hasło. Pozostałe próby: 2.” | PASS | ✔ |
| MB-TC-003 | Puste pola | Kliknij „Zaloguj się” bez danych | „Podaj login.” i „Podaj hasło.” | PASS | ✔ |
| MB-TC-004 | Blokada dopiero po 3 próbach | 2× błędne hasło | Brak blokady, komunikat „Pozostałe próby: 1.” (blokada po 3. próbie — wg panelu danych testowych i FAQ) | **FAIL → MB-01** | ✔ |
| MB-TC-005 | Błędny kod SMS | Poprawny login → kod `000000` | „Nieprawidłowy kod SMS. Spróbuj ponownie.”, brak dostępu | PASS | ✔ |
| MB-TC-006 | Limit prób kodu SMS | 3× błędny kod → potem `123456` | Po 3 błędach powrót do logowania / blokada (jak w autoryzacji operacji) | **FAIL → MB-16** | ✔ |
| MB-TC-007 | Wylogowanie | Menu użytkownika → Wyloguj się → Potwierdź | Ekran logowania, „Zostałeś poprawnie wylogowany. Do zobaczenia!”, pole hasła puste | PASS | ✔ |
| MB-TC-008 | Spójna wersja aplikacji | Porównaj wersję na ekranie logowania i w stopce menu | Ten sam numer wersji | **FAIL → MB-15** | |
| MB-TC-009 | Limit sesji 1 min | Ustawienia → Automatyczne wylogowanie: 1 minuta | Ostrzeżenie o wygasaniu pojawia się dopiero po okresie bezczynności, nie natychmiast po zmianie ustawienia | **FAIL → MB-11** | ✔ |
| MB-TC-019 | „Zapamiętaj mój login” | Zaznacz checkbox → zaloguj → wyloguj | Pole loginu zawiera `jan.kowalski`, hasło puste | PASS | |

## Przelewy

| ID | Tytuł | Kroki / dane | Oczekiwany rezultat | Wynik | Auto |
|---|---|---|---|---|---|
| MB-TC-010 | Przelew krajowy E2E | Z konta osobistego, odbiorca zapisany „Anna Nowak”, 100,50 zł, tytuł → Dalej → Zatwierdź → SMS | Numer ref. `PRZ-…`, saldo konta osobistego −100,50 zł, operacja w historii | PASS | ✔ |
| MB-TC-011 | Podsumowanie przelewu | Jak wyżej, 250 zł → Dalej | Podsumowanie: odbiorca, rachunek, kwota 250,00 zł, data, tytuł, prowizja 0,00 zł | PASS | ✔ |
| MB-TC-012 | Walidacja formularza | Odbiorca `Jo`, rachunek 10 cyfr, kwota `abc`, brak tytułu | 4 komunikaty błędów, brak przejścia do podsumowania | PASS | ✔ |
| MB-TC-013 | Kwota powyżej salda | Kwota 99 999 999 | „Niewystarczające środki na rachunku.” | PASS | ✔ |
| MB-TC-014 | Kwota 0 (wartość brzegowa) | Kwota `0` | „Podaj poprawną kwotę większą od zera.” | **FAIL → MB-03** | ✔ |
| MB-TC-015 | Przelew z konta oszczędnościowego | Z rachunku: Konto oszczędnościowe, 100 zł | Saldo oszczędnościowego −100 zł, osobistego bez zmian | **FAIL → MB-02** | ✔ |
| MB-TC-016 | Przelew z przyszłą datą | Data jutrzejsza → zatwierdź | Komunikat o realizacji w dniu … o 06:00, pozycja w „Zaplanowane”, saldo bez zmian; „Anuluj” usuwa pozycję | PASS | |
| MB-TC-017 | Unikalne ID zleceń stałych | Utwórz zlecenie → usuń ST-1001 → utwórz kolejne | Każde zlecenie ma inne ID; „Usuń” usuwa tylko jedno | **FAIL → MB-12** | ✔ |
| MB-TC-018 | Przelew własny | Osobiste → oszczędnościowe, 500 zł | Osobiste −500 zł, oszczędnościowe +500 zł, operacja w historii | PASS | |

## Historia

| ID | Tytuł | Kroki / dane | Oczekiwany rezultat | Wynik | Auto |
|---|---|---|---|---|---|
| MB-TC-020 | Wyszukiwanie | Szukaj: `wynagrodzenie` | Tylko operacje „Wynagrodzenie — ACME…” | PASS | ✔ |
| MB-TC-021 | Filtr uznań | Typ: Uznania | Tylko kwoty dodatnie | PASS | ✔ |
| MB-TC-022 | Stronicowanie | Domyślnie 10 na stronę | 10 wierszy; ostatni wiersz strony 1 nie powtarza się na stronie 2 | **FAIL → MB-08** | ✔ |
| MB-TC-023 | Sortowanie po kwocie | Kliknij nagłówek „Kwota” | Kwoty malejąco wg wartości liczbowej | **FAIL → MB-07** | ✔ |
| MB-TC-024 | Eksport CSV | Filtr + „Eksportuj CSV” | Plik `wyciag_meridian_RRRR-MM-DD.csv`, liczba wierszy = licznik operacji, polskie znaki poprawne w Excelu | PASS | |
| MB-TC-025 | Szczegóły operacji | Kliknij wiersz | Modal: data, opis, kategoria, kwota, saldo po, numer ref. | PASS | |

## BLIK i karty

| ID | Tytuł | Kroki / dane | Oczekiwany rezultat | Wynik | Auto |
|---|---|---|---|---|---|
| MB-TC-030 | Generowanie i anulowanie | Generuj → Anuluj | Kod i odliczanie ≤ 120 s; po anulowaniu ekran startowy | PASS | ✔ |
| MB-TC-031 | Format kodu BLIK | Generuj kod | 6 cyfr (format `123 456`) | **FAIL → MB-04** | ✔ |
| MB-TC-032 | Wygaśnięcie kodu | Generuj i odczekaj 120 s | „Kod BLIK wygasł.” + „Generuj nowy kod” | PASS | |
| MB-TC-033 | Pokaż/ukryj numer karty | „Pokaż numer” → „Ukryj numer” | Pełny numer ↔ `•••• •••• •••• 4523` | PASS | |
| MB-TC-034 | Blokada karty | Zablokuj → Potwierdź | Status „Zablokowana”, przycisk „Odblokuj” | PASS | |

## Lokaty i kredyty

| ID | Tytuł | Kroki / dane | Oczekiwany rezultat | Wynik | Auto |
|---|---|---|---|---|---|
| MB-TC-040 | Kalkulator lokaty 6 mies. | 10 000 zł, 6 mies. (4,80%) | Brutto 240,00 zł, netto (−19%) 194,40 zł, razem 10 194,40 zł | PASS | ✔ |
| MB-TC-041 | Minimalna kwota lokaty | 999 zł | „Kwota od 1 000 do 500 000 zł.” | PASS | ✔ |
| MB-TC-042 | Lokata 12 mies. | Okres „12 miesięcy — 5,00%” | Oprocentowanie 5,00%, brutto 500,00 zł | **FAIL → MB-06** | ✔ |
| MB-TC-043 | Otwieranie i zrywanie lokat | Otwórz lokatę → zerwij DEP-2044 → otwórz kolejną → zerwij jedną | Unikalne ID; zerwanie jednej lokaty zwraca jej kapitał i nie wpływa na inne | **FAIL → MB-13** | |
| MB-TC-044 | Spójność powiadomienia o lokacie | Porównaj powiadomienie o DEP-2044 z datą końca w tabeli | Daty zgodne | **FAIL → MB-14** | |
| MB-TC-050 | Rata kredytu | 25 000 zł, 36 mies., 9,99% | Rata 806,56 zł, razem 29 036,24 zł | PASS | ✔ |
| MB-TC-051 | Wniosek — walidacja | Dochód 500 zł, bez zgody RODO | „Podaj dochód (min. 1 000 zł).” + „Ta zgoda jest wymagana.” | PASS | ✔ |

## Kantor

| ID | Tytuł | Kroki / dane | Oczekiwany rezultat | Wynik | Auto |
|---|---|---|---|---|---|
| MB-TC-060 | Ta sama waluta | EUR → EUR | Przycisk „Wykonaj wymianę” nieaktywny | PASS | ✔ |
| MB-TC-061 | Kurs PLN → EUR | 100 PLN → EUR (sprzedaż 4,38) | 22,83 € | **FAIL → MB-05** | ✔ |
| MB-TC-062 | Kurs EUR → PLN | 100 EUR → PLN (kupno 4,24) | 424,00 zł | PASS | |

## Wiadomości, ustawienia, pomoc

| ID | Tytuł | Kroki / dane | Oczekiwany rezultat | Wynik | Auto |
|---|---|---|---|---|---|
| MB-TC-070 | Licznik nieprzeczytanych | Otwórz nieprzeczytaną wiadomość → wróć | Licznik „1” znika z menu | **FAIL → MB-10** | ✔ |
| MB-TC-080 | Walidacja e-maila | Edytuj → `jan.kowalski@` → Zapisz | „Podaj poprawny adres e-mail.” | PASS | ✔ |
| MB-TC-081 | Różne hasła | Nowe ≠ powtórzone | „Hasła nie są identyczne.” | PASS | ✔ |
| MB-TC-082 | Hasło 8 znaków (brzeg) | `Abcdef1!` (8 znaków, spełnia wszystkie reguły) | Hasło zaakceptowane → okno SMS | **FAIL → MB-09** | ✔ |
| MB-TC-083 | Tryb ciemny | Ikona w nagłówku, potem przełącznik w Ustawieniach | Motyw zmienia się, oba przełączniki zsynchronizowane | PASS | |
| MB-TC-090 | Formularz kontaktowy | Wiadomość 9 znaków → błąd; poprawne dane → wyślij | „Wiadomość musi mieć min. 10 znaków.”; potem toast z numerem `ZGL-…` | PASS | |
| MB-TC-091 | FAQ | Otwórz pytanie 1, potem 2 | Otwarte jest tylko pytanie 2 | PASS | |

**Razem:** 47 przypadków · 31 PASS · 16 FAIL · 32 zautomatyzowane.

> Przypadki bez automatu wykonaj ręcznie przed rozmową i potwierdź wyniki — musisz umieć je pokazać.
