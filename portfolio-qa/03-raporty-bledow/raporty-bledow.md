# Raporty błędów — SauceDemo

Format zgodny z polami zgłoszenia typu **Bug** w Jira. Defekty znalezione podczas wykonywania
przypadków testowych i sesji eksploracyjnych.

> SauceDemo to aplikacja demonstracyjna — część błędów jest w niej celowo umieszczona dla wybranych
> użytkowników testowych (np. `problem_user`). Raporty pokazują, jak opisuję defekt, żeby developer
> mógł go odtworzyć bez dopytywania.

**Środowisko (wspólne):** https://www.saucedemo.com · Chrome 1xx (Windows 11) · rozdzielczość 1920×1080 · hasło `secret_sauce`

Cykl życia defektu: [`cykl-zycia-defektu.md`](cykl-zycia-defektu.md)

---

## BUG-001 — Wszystkie produkty wyświetlają to samo, niepoprawne zdjęcie (`problem_user`)

| Pole | Wartość |
|---|---|
| **Typ** | Bug |
| **Ważność / Priorytet** | Major / High |
| **Komponent** | Katalog produktów |
| **Powiązany test** | TC-010 |
| **Użytkownik** | `problem_user` |

**Kroki do odtworzenia**
1. Otwórz https://www.saucedemo.com
2. Zaloguj się jako `problem_user` / `secret_sauce`
3. Obejrzyj zdjęcia produktów na liście „Products”

**Rezultat oczekiwany:** każdy produkt ma zdjęcie odpowiadające nazwie (np. plecak dla „Sauce Labs Backpack”).
**Rezultat rzeczywisty:** wszystkie 6 produktów wyświetla to samo zdjęcie, niezwiązane z żadnym produktem.
**Powtarzalność:** 5/5 · **Uwagi:** dla `standard_user` zdjęcia są poprawne → problem zależny od konta.
**Załączniki:** `BUG-001_lista.png`, lista adresów `src` obrazków z DevTools.

---

## BUG-002 — Sortowanie produktów nie działa (`problem_user`)

| Pole | Wartość |
|---|---|
| **Ważność / Priorytet** | Major / Medium |
| **Komponent** | Katalog produktów — sortowanie |
| **Powiązany test** | TC-011, TC-012, TC-013 |

**Kroki do odtworzenia**
1. Zaloguj się jako `problem_user`
2. Z listy sortowania wybierz „Price (low to high)”

**Rezultat oczekiwany:** produkty ułożone od najtańszego ($7.99) do najdroższego ($49.99).
**Rezultat rzeczywisty:** kolejność produktów się nie zmienia (A–Z); ta sama sytuacja dla pozostałych opcji.
**Powtarzalność:** 5/5 · **Konsola:** brak błędów JavaScript.

---

## BUG-003 — Pole „Last Name” nadpisuje „First Name” w formularzu zamówienia (`problem_user`)

| Pole | Wartość |
|---|---|
| **Ważność / Priorytet** | **Critical / Highest** — blokuje złożenie zamówienia |
| **Komponent** | Checkout — Your Information |
| **Powiązany test** | TC-022, TC-023 |

**Kroki do odtworzenia**
1. Zaloguj się jako `problem_user`, dodaj dowolny produkt do koszyka
2. Koszyk → „Checkout”
3. W polu „First Name” wpisz `Jan`
4. Kliknij pole „Last Name” i wpisz `Kowalski`

**Rezultat oczekiwany:** „First Name” = `Jan`, „Last Name” = `Kowalski`.
**Rezultat rzeczywisty:** tekst wpisywany w „Last Name” trafia do pola „First Name”; „Last Name” pozostaje puste.
Po „Continue” pojawia się „Error: Last Name is required” — **nie da się złożyć zamówienia**.
**Powtarzalność:** 5/5 · **Obejście:** brak.
**Załączniki:** nagranie ekranu `BUG-003.mp4`.

---

## BUG-004 — Kliknięcie produktu otwiera stronę innego produktu (`problem_user`)

| Pole | Wartość |
|---|---|
| **Ważność / Priorytet** | Major / High |
| **Powiązany test** | TC-014, TC-015 |

**Kroki do odtworzenia**
1. Zaloguj się jako `problem_user`
2. Kliknij nazwę „Sauce Labs Backpack”

**Rezultat oczekiwany:** strona szczegółów „Sauce Labs Backpack”.
**Rezultat rzeczywisty:** otwiera się strona szczegółów innego produktu (inny `id` w URL `inventory-item.html?id=…`).
**Uwagi:** klient może kupić inny produkt niż zamierzał — ryzyko reklamacji.

---

## BUG-005 — Możliwe złożenie zamówienia z pustym koszykiem (`standard_user`)

| Pole | Wartość |
|---|---|
| **Ważność / Priorytet** | Major / Medium |
| **Komponent** | Koszyk / Checkout |
| **Powiązany test** | TC-026 |

**Kroki do odtworzenia**
1. Zaloguj się jako `standard_user` (pusty koszyk)
2. Kliknij ikonę koszyka → „Checkout”
3. Uzupełnij dane (Jan / Kowalski / 50-051) → „Continue” → „Finish”

**Rezultat oczekiwany:** brak możliwości przejścia do checkoutu z pustym koszykiem (przycisk nieaktywny lub komunikat).
**Rezultat rzeczywisty:** zamówienie na $0.00 zostaje „złożone”, wyświetla się „Thank you for your order!”.
**Uwagi:** przed zgłoszeniem potwierdzić z PO oczekiwane zachowanie (pytanie nr 7 w analizie wymagań).

---

## BUG-006 — „Reset App State” nie przywraca przycisków „Add to cart” (`standard_user`)

| Pole | Wartość |
|---|---|
| **Ważność / Priorytet** | Minor / Low |
| **Powiązany test** | TC-021 |

**Kroki do odtworzenia**
1. Zaloguj się jako `standard_user`, dodaj 2 produkty do koszyka
2. Menu (☰) → „Reset App State”

**Rezultat oczekiwany:** licznik koszyka znika, przy produktach przyciski „Add to cart”.
**Rezultat rzeczywisty:** licznik znika, ale przy dodanych produktach nadal widnieje „Remove” — do czasu odświeżenia strony.
**Uwagi:** stan UI niespójny ze stanem koszyka.

---

## Podsumowanie

| ID | Tytuł | Ważność | Status |
|---|---|---|---|
| BUG-001 | Te same, błędne zdjęcia produktów | Major | Open |
| BUG-002 | Sortowanie nie działa | Major | Open |
| BUG-003 | Last Name nadpisuje First Name — blokada zamówienia | Critical | Open |
| BUG-004 | Kliknięcie produktu otwiera inny produkt | Major | Open |
| BUG-005 | Zamówienie z pustym koszykiem | Major | Do potwierdzenia z PO |
| BUG-006 | Reset App State — niespójne przyciski | Minor | Open |

## Szablon zgłoszenia (do kopiowania)

```
Tytuł: [Moduł] Co nie działa — w jakich warunkach
Środowisko: URL / wersja / przeglądarka / system / użytkownik
Warunki wstępne:
Kroki do odtworzenia:
  1.
  2.
Rezultat oczekiwany:
Rezultat rzeczywisty:
Powtarzalność: x/y
Ważność / Priorytet:
Załączniki: zrzut ekranu / nagranie / log z konsoli / request z zakładki Network
Powiązany przypadek testowy / wymaganie:
```
