# Testy eksploracyjne — karty sesji i raporty

Podejście: **Session-Based Test Management** — każda sesja ma kartę (charter), ograniczony czas,
notatki na bieżąco i krótki raport. Format karty: *Eksploruj [obszar] z użyciem [zasoby/techniki],
aby odkryć [rodzaj informacji].*

---

## Sesja 1 — Proces zamówienia

| | |
|---|---|
| **Charter** | Eksploruj proces checkout z użyciem nietypowych danych i nawigacji (Wstecz, odświeżanie, bezpośrednie URL), aby odkryć problemy z walidacją i spójnością stanu zamówienia |
| **Czas** | 60 min |
| **Użytkownik** | `standard_user` |

**Pomysły testowe (heurystyki):** puste / bardzo długie / specjalne znaki w polach, przycisk Wstecz
w trakcie zamówienia, odświeżenie na każdym kroku, wejście bezpośrednio na `/checkout-step-two.html`,
pusty koszyk, dwukrotne kliknięcie „Finish”.

**Notatki z sesji**
- Kod pocztowy przyjmuje litery i znaki specjalne → brak walidacji formatu (pytanie do PO).
- Pola przyjmują bardzo długie wartości (sprawdzone ~500 znaków) — brak limitu.
- Wejście bezpośrednio na `/checkout-step-two.html` z produktami w koszyku pomija formularz danych
  → do zgłoszenia jako potencjalna luka (pytanie do PO).
- Checkout możliwy z pustym koszykiem → **BUG-005**.
- `<script>alert(1)</script>` w polu imienia — skrypt się nie wykonuje ✔.

**Wynik:** 1 błąd, 3 pytania do PO. **Pokrycie:** formularz, nawigacja, stany koszyka.

---

## Sesja 2 — Porównanie użytkowników testowych

| | |
|---|---|
| **Charter** | Eksploruj katalog i koszyk dla `problem_user`, `error_user`, `visual_user`, porównując z `standard_user`, aby odkryć błędy zależne od konta |
| **Czas** | 60 min |

**Notatki z sesji**
- `problem_user`: te same zdjęcia wszystkich produktów (**BUG-001**), sortowanie nie działa (**BUG-002**),
  złe pole w checkoutcie (**BUG-003**), kliknięcie produktu otwiera inny (**BUG-004**), dla części
  produktów „Add to cart” nie reaguje.
- `error_user`: część akcji kończy się błędem (m.in. przy sortowaniu i koszyku) — do opisania w osobnych zgłoszeniach.
- `visual_user`: różnice wizualne względem `standard_user` (m.in. położenie elementów, zdjęcia) —
  kandydat do testów wizualnych (porównanie zrzutów ekranu).

**Wniosek:** warto mieć w regresji smoke uruchamiany na kilku typach kont, bo błędy zależą od danych użytkownika.

---

## Sesja 3 — Sesja, nawigacja i bezpieczeństwo podstawowe

| | |
|---|---|
| **Charter** | Eksploruj zarządzanie sesją (wylogowanie, Wstecz, wiele kart, ciasteczka w DevTools), aby odkryć możliwość dostępu do sklepu bez logowania |
| **Czas** | 45 min |

**Notatki z sesji**
- Po wylogowaniu przycisk Wstecz nie daje dostępu do listy produktów ✔.
- Bezpośredni URL `/inventory.html` bez logowania → komunikat i brak dostępu ✔.
- DevTools → Application → Cookies: sesja przechowywana w ciasteczku `session-username`
  z nazwą użytkownika w czystym tekście; ręczne ustawienie ciasteczka daje dostęp do sklepu
  → **obserwacja do omówienia z zespołem** (w aplikacji demonstracyjnej to świadome uproszczenie,
  w prawdziwym systemie byłby to poważny problem bezpieczeństwa).

**Wynik:** 0 błędów funkcjonalnych, 1 obserwacja bezpieczeństwa.

---

## Szablon karty sesji

```
Charter: Eksploruj … z użyciem …, aby odkryć …
Tester:            Data:            Czas trwania:
Środowisko / wersja:
Notatki (co testowałem, co zauważyłem):
Znalezione błędy (ID):
Pytania / wątpliwości:
Pomysły na kolejne sesje:
Podział czasu: projektowanie i wykonanie __% · analiza i zgłaszanie błędów __% · konfiguracja __%
```
