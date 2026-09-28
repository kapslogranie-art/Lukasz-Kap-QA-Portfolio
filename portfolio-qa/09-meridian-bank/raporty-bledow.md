# Meridian Bank — raporty błędów

**Środowisko (wspólne):** https://lukasztm.github.io/MeridianBank/ · Chrome (Windows 11 / Ubuntu, CI) ·
1920×1080 · użytkownik `jan.kowalski` / `Test123!` / SMS `123456` · świeżo załadowana strona.

Każdy błąd ma test automatyczny `xfail(strict=True)` — kolumna **Test** w podsumowaniu.
Pole **Przyczyna (analiza)** to wynik analizy kodu JavaScript w DevTools (aplikacja nie ma backendu);
w zgłoszeniu ułatwia developerowi szybką poprawkę.

## Podsumowanie

| ID | Tytuł | Ważność | Test |
|---|---|---|---|
| MB-02 | Przelew z konta oszczędnościowego obciąża konto osobiste | Critical | `test_transfer_from_savings_debits_savings_account` |
| MB-04 | Kod BLIK ma 5 cyfr zamiast 6 | Critical | `test_blik_code_has_six_digits` |
| MB-05 | Kantor: PLN→EUR po kursie kupna zamiast sprzedaży | Critical | `test_fx_pln_to_eur_uses_sell_rate` |
| MB-13 | Zduplikowane ID lokat — zerwanie jednej usuwa dwie | Critical | — (manualny) |
| MB-01 | Blokada logowania po 2 zamiast 3 próbach | Major | `test_account_is_not_locked_after_two_failed_attempts` |
| MB-03 | Przelew na kwotę 0,00 zł przechodzi walidację | Major | `test_transfer_with_zero_amount_is_rejected` |
| MB-06 | Lokata 12 mies.: 5,00% w ofercie, 4,80% w wyliczeniu | Major | `test_twelve_month_deposit_uses_advertised_rate` |
| MB-07 | Sortowanie historii po kwocie jest tekstowe | Major | `test_history_sort_by_amount_is_numeric` |
| MB-08 | Historia: 11 wierszy na stronie „10”, duplikat na kolejnej stronie | Major | `test_history_shows_ten_rows_per_page` |
| MB-12 | Zduplikowane ID zleceń stałych | Major | `test_standing_orders_have_unique_ids` |
| MB-16 | Brak limitu prób kodu SMS przy logowaniu | Major | `test_login_sms_step_is_blocked_after_three_wrong_codes` |
| MB-09 | Hasło 8-znakowe odrzucane mimo reguły „min. 8 znaków” | Minor | `test_password_with_exactly_eight_chars_is_accepted` |
| MB-10 | Licznik nieprzeczytanych wiadomości nie znika | Minor | `test_unread_badge_disappears_after_reading` |
| MB-11 | Limit sesji 1 min — ostrzeżenie od razu | Minor | `test_one_minute_timeout_does_not_warn_immediately` |
| MB-14 | Powiadomienie o końcu lokaty niezgodne z datą lokaty | Minor | — (manualny) |
| MB-15 | Różne numery wersji aplikacji (2.6.0 / 2.6.1) | Trivial | — (manualny) |

---

## MB-02 — Przelew z konta oszczędnościowego obciąża konto osobiste

| Ważność / Priorytet | **Critical / Highest** | Moduł | Przelewy → Przelew krajowy |
|---|---|---|---|

**Kroki**
1. Pulpit — zanotuj salda: osobiste 12 543,21 zł, oszczędnościowe 45 200,00 zł.
2. Przelewy → „Z rachunku”: **Konto oszczędnościowe**; odbiorca zapisany „Anna Nowak”; kwota `100`; tytuł `Test`.
3. Dalej → Zatwierdź i autoryzuj → kod `123456`.
4. Wróć na Pulpit.

**Oczekiwany:** oszczędnościowe 45 100,00 zł, osobiste bez zmian.
**Rzeczywisty:** oszczędnościowe 45 200,00 zł (bez zmian), **osobiste 12 443,21 zł** (−100 zł).
Ekran potwierdzenia twierdzi przy tym: „Środki zostały pobrane z rachunku: Konto oszczędnościowe”.
**Powtarzalność:** 3/3.
**Przyczyna (analiza):** `executeTransfer()` zawsze wywołuje `addTxn()`, które modyfikuje saldo `acc('ror')`, niezależnie od `p.from`.

---

## MB-04 — Kod BLIK ma 5 cyfr zamiast 6

| Ważność / Priorytet | **Critical / Highest** | Moduł | BLIK |
|---|---|---|---|

**Kroki:** BLIK → Generuj kod BLIK.
**Oczekiwany:** 6-cyfrowy kod (tak opisuje go ekran i FAQ), format `123 456`.
**Rzeczywisty:** kod ma **5 cyfr**, np. `482 17` — nie da się go użyć w terminalu/sklepie.
**Powtarzalność:** 10/10.
**Przyczyna (analiza):** `Math.floor(10000 + Math.random() * 90000)` generuje zakres 10000–99999; powinno być `100000 + … * 900000`.

---

## MB-05 — Kantor: PLN→EUR przeliczany po kursie kupna zamiast sprzedaży

| Ważność / Priorytet | **Critical / Highest** | Moduł | Kantor |
|---|---|---|---|

**Kroki:** Kantor → kwota `100`, Sprzedaję `PLN`, Kupuję `EUR`.
**Oczekiwany:** 100 / 4,38 (kurs sprzedaży EUR, pokazany pod wynikiem i w tabeli) = **22,83 €**.
**Rzeczywisty:** **23,58 €** (100 / 4,24 — kurs kupna). Pod wynikiem widnieje „Sprzedaż EUR: 4,38 zł”, więc
wynik jest niezgodny z informacją wyświetlaną klientowi. Po „Wykonaj wymianę” na konto walutowe trafia 23,58 €.
**Wpływ:** bank traci ok. 3,3% wartości każdej wymiany PLN→EUR.
**Przyczyna (analiza):** `fxCalc()` używa `RATES[to].buy` zamiast `RATES[to].sell`.

---

## MB-13 — Zduplikowane ID lokat: zerwanie jednej lokaty usuwa dwie

| Ważność / Priorytet | **Critical / Highest** | Moduł | Lokaty |
|---|---|---|---|

**Kroki**
1. Lokaty → 1 000 zł, 3 mies. → Otwórz lokatę → Potwierdź (powstaje **DEP-2045**).
2. Zerwij lokatę **DEP-2044** → Potwierdź.
3. Otwórz kolejną lokatę 1 000 zł → Potwierdź.
4. Obserwuj listę „Twoje lokaty”, a następnie zerwij jedną z lokat.

**Oczekiwany:** nowa lokata ma unikalne ID (DEP-2046); zerwanie jednej zwraca 1 000 zł i nie dotyka drugiej.
**Rzeczywisty:** w kroku 3 powstaje druga lokata **DEP-2045**. W kroku 4 znikają **obie** lokaty, a na konto
wraca tylko 1 000 zł — **1 000 zł klienta przepada**.
**Przyczyna (analiza):** ID liczone jako `2044 + liczba lokat` zamiast kolejnego numeru; zerwanie filtruje po ID.
Ten sam wzorzec: zlecenia stałe (MB-12).

---

## MB-01 — Blokada logowania po 2 zamiast 3 nieudanych próbach

| Ważność / Priorytet | Major / High | Moduł | Logowanie |
|---|---|---|---|

**Kroki:** 2× zaloguj się z błędnym hasłem.
**Oczekiwany:** po 1. próbie „Pozostałe próby: 2.”, po 2. „Pozostałe próby: 1.”, blokada dopiero po 3. próbie
(zgodnie z panelem „Dane testowe” i FAQ: „Blokada po 3 błędnych próbach”).
**Rzeczywisty:** po 2. próbie konto zostaje zablokowane na 30 s z komunikatem „…po 3 nieudanych próbach”.
Komunikat po 1. próbie („Pozostałe próby: 2.”) wprowadza w błąd.
**Przyczyna (analiza):** warunek `if (left <= 1) lockLogin()` — powinno być `left <= 0`.

---

## MB-03 — Przelew na kwotę 0,00 zł przechodzi walidację

| Ważność / Priorytet | Major / Medium | Moduł | Przelewy |
|---|---|---|---|

**Kroki:** Przelew krajowy, poprawne dane, kwota `0` → Dalej → Zatwierdź → SMS.
**Oczekiwany:** błąd „Podaj poprawną kwotę większą od zera.” (ten tekst istnieje w aplikacji).
**Rzeczywisty:** przejście do podsumowania, przelew 0,00 zł zostaje „przyjęty do realizacji” z numerem referencyjnym.
**Przyczyna (analiza):** `validateTransfer()` sprawdza `amt < 0` zamiast `amt <= 0` (przelew własny i zlecenia stałe robią to poprawnie).

---

## MB-06 — Lokata 12-miesięczna: 5,00% w ofercie, 4,80% w wyliczeniu

| Ważność / Priorytet | Major / High | Moduł | Lokaty |
|---|---|---|---|

**Kroki:** Lokaty → kwota 10 000 → okres „12 miesięcy — 5,00%”.
**Oczekiwany:** oprocentowanie 5,00%, odsetki brutto 500,00 zł (asystent Meri też podaje 5,00%).
**Rzeczywisty:** oprocentowanie **4,80%**, brutto 480,00 zł; otwarta lokata zapisuje się z 4,80%.
**Wpływ:** klient dostaje mniej niż w ofercie — ryzyko reklamacji i regulacyjne (wprowadzanie w błąd).
**Przyczyna (analiza):** `DEP_RATES = { …, 12: 4.8, … }` zamiast `5.0`.

---

## MB-07 — Sortowanie historii po kwocie jest tekstowe, nie liczbowe

| Ważność / Priorytet | Major / Medium | Moduł | Historia |
|---|---|---|---|

**Kroki:** Historia → kliknij nagłówek „Kwota”.
**Oczekiwany:** kwoty malejąco wg wartości: …, −84,44, −86,42, −87,96, −92,14, …
**Rzeczywisty:** kolejność „alfabetyczna”: np. −92,14 przed −87,96; kwoty ujemne z różną liczbą cyfr przemieszane.
**Przyczyna (analiza):** `hFiltered()` porównuje `String(a.amount)` zamiast liczb.

---

## MB-08 — Historia: 11 wierszy przy ustawieniu „10 na stronę”

| Ważność / Priorytet | Major / Medium | Moduł | Historia |
|---|---|---|---|

**Kroki:** Historia (domyślnie 10 na stronę) → policz wiersze → przejdź na stronę 2.
**Oczekiwany:** 10 wierszy; informacja „pozycje 1–10”; strona 2 zaczyna się od 11. pozycji.
**Rzeczywisty:** **11 wierszy** przy informacji „pozycje 1–10”; ostatni wiersz strony 1 jest też pierwszym na stronie 2 —
klient widzi operację dwukrotnie. Dotyczy też 25 i 50 na stronę.
**Przyczyna (analiza):** `slice(start, start + H.per + 1)` — błąd „o jeden” (off-by-one).

---

## MB-12 — Zduplikowane ID zleceń stałych

| Ważność / Priorytet | Major / High | Moduł | Przelewy → Zlecenia stałe |
|---|---|---|---|

**Kroki:** Zlecenia stałe → utwórz zlecenie (ST-1002) → usuń „Czynsz” (ST-1001) → utwórz kolejne → na jednym z nich kliknij „Usuń”.
**Oczekiwany:** nowe zlecenie ma ID ST-1003; usunięcie dotyczy jednego zlecenia.
**Rzeczywisty:** dwa zlecenia mają ID **ST-1002**; „Usuń” usuwa **oba**, a „Wstrzymaj” na drugim wstrzymuje pierwsze.
**Przyczyna (analiza):** ID = `1000 + liczba zleceń + 1` (jak w MB-13).

---

## MB-16 — Brak limitu prób kodu SMS przy logowaniu

| Ważność / Priorytet | Major / High (bezpieczeństwo) | Moduł | Logowanie |
|---|---|---|---|

**Kroki:** poprawny login i hasło → wpisz błędny kod SMS 10 razy → wpisz `123456`.
**Oczekiwany:** po 3 błędnych kodach przerwanie logowania (tak działa autoryzacja SMS przelewów: „Autoryzacja odrzucona po 3 błędnych próbach”).
**Rzeczywisty:** liczba prób nieograniczona; po dowolnej liczbie błędów poprawny kod loguje do aplikacji.
**Wpływ:** 6-cyfrowy kod można odgadnąć metodą prób (brute force).

---

## MB-09 — Hasło 8-znakowe odrzucane mimo reguły „min. 8 znaków”

| Ważność / Priorytet | Minor / Medium | Moduł | Ustawienia → Zmiana hasła |
|---|---|---|---|

**Kroki:** Obecne `Test123!`, nowe i powtórzone `Abcdef1!` (8 znaków: wielka litera, cyfra, znak specjalny) → Zmień hasło.
**Oczekiwany:** hasło zaakceptowane (wartość brzegowa reguły „Min. 8 znaków…”), okno SMS.
**Rzeczywisty:** „Hasło nie spełnia wymagań bezpieczeństwa.”, choć wskaźnik siły hasła pokazuje 100% (zielony).
**Przyczyna (analiza):** walidacja `np.length > 8` zamiast `>= 8` (wskaźnik siły używa `>= 8` — niespójność).

---

## MB-10 — Licznik nieprzeczytanych wiadomości nie znika po przeczytaniu

| Ważność / Priorytet | Minor / Low | Moduł | Wiadomości |
|---|---|---|---|

**Kroki:** Wiadomości (licznik „1”) → otwórz „Nowe zasady bezpieczeństwa logowania” → Wróć do listy.
**Oczekiwany:** wiadomość oznaczona jako przeczytana, licznik w menu znika.
**Rzeczywisty:** na liście znika znacznik „●”, ale licznik „1” w menu zostaje (do czasu przelogowania).
**Przyczyna (analiza):** `openMessage()` nie wywołuje `updateMsgBadge()`.

---

## MB-11 — Limit sesji 1 min: ostrzeżenie o wygasaniu pojawia się natychmiast

| Ważność / Priorytet | Minor / Low | Moduł | Ustawienia → Sesja |
|---|---|---|---|

**Kroki:** Ustawienia → Automatyczne wylogowanie: **1 minuta**.
**Oczekiwany:** ostrzeżenie dopiero po okresie bezczynności.
**Rzeczywisty:** w ciągu 1 s pojawia się okno „Twoja sesja wkrótce wygaśnie” z odliczaniem od 60 s — użytkownik
nie ma ani chwili pracy bez ostrzeżenia; kliknięcia na stronie nie resetują licznika, gdy okno jest otwarte.
**Przyczyna (analiza):** ostrzeżenie wyświetlane, gdy `idle >= limit - 60`; przy limicie 60 s to warunek `idle >= 0`.

---

## MB-14 — Powiadomienie o końcu lokaty niezgodne z datą lokaty

| Ważność / Priorytet | Minor / Low | Moduł | Powiadomienia / Lokaty |
|---|---|---|---|

**Kroki:** Dzwonek → „Za 3 dni kończy się Twoja lokata DEP-2044” (5 dni temu) → Lokaty → data końca DEP-2044.
**Oczekiwany:** lokata kończy się ok. 2 dni temu (lub dane są spójne).
**Rzeczywisty:** data końca DEP-2044 to ok. **92 dni od dziś**.

---

## MB-15 — Różne numery wersji aplikacji

| Ważność / Priorytet | Trivial / Low | Moduł | Logowanie / Menu |
|---|---|---|---|

**Rzeczywisty:** ekran logowania „Wersja 2.6.0”, stopka menu „v2.6.1”, wiadomość powitalna „Meridian 2.6”.
**Oczekiwany:** jeden numer wersji — ważne przy zgłaszaniu błędów (w której wersji wystąpił błąd?).

---

## Obserwacje i sugestie (nie błędy funkcjonalne)

1. **UX:** komunikaty (toasty) wyświetlane w prawym górnym rogu przez ~4,5 s **mogą zasłaniać menu użytkownika**
   (np. zaraz po zalogowaniu nie da się kliknąć „Jan” → Wyloguj). Sugestia: toasty na dole ekranu.
2. **Walidacja NRB:** sprawdzana jest tylko liczba cyfr (26), bez sumy kontrolnej IBAN (mod 97) —
   literówka w numerze rachunku przejdzie walidację.
3. **Autoryzacja:** przelew i zmiana limitów karty wymagają SMS, a otwarcie lokaty i wymiana walut — nie.
   Do potwierdzenia z PO, czy to zamierzone.
4. **Data końca lokaty** liczona jako `liczba miesięcy × 30 dni` (np. lokata 12 mies. kończy się po 360 dniach).
5. **Telefon w profilu** akceptuje litery (`abc601234789`) — liczone są tylko cyfry.
