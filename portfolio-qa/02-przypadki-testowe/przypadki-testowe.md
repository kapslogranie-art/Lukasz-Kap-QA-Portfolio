# Przypadki testowe — SauceDemo

**Hasło dla wszystkich użytkowników testowych:** `secret_sauce`
**Priorytety:** P1 — krytyczny (smoke), P2 — wysoki, P3 — średni
**Techniki:** KR — klasy równoważności, WB — wartości brzegowe, TD — tablica decyzyjna, PS — przejścia stanów, EG — zgadywanie błędów

Wersja do importu w Xray / TestRail: [`przypadki-testowe-import.csv`](przypadki-testowe-import.csv)

---

## Moduł: Logowanie (US-01)

### TC-001 — Logowanie poprawnymi danymi · P1 · KR
**Warunki wstępne:** użytkownik jest na stronie logowania.
| # | Krok | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Wpisz login | `standard_user` | Login widoczny w polu |
| 2 | Wpisz hasło | `secret_sauce` | Hasło zamaskowane |
| 3 | Kliknij „Login” | — | Przekierowanie na `/inventory.html`, nagłówek „Products”, lista 6 produktów |

### TC-002 — Logowanie błędnym hasłem · P1 · KR
| # | Krok | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Wpisz login i błędne hasło, kliknij „Login” | `standard_user` / `wrong_pass` | Komunikat: „Epic sadface: Username and password do not match any user in this service”; użytkownik pozostaje na stronie logowania; pola podświetlone na czerwono |

### TC-003 — Logowanie zablokowanego użytkownika · P1 · KR
| # | Krok | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Zaloguj się | `locked_out_user` / `secret_sauce` | Komunikat: „Epic sadface: Sorry, this user has been locked out.”; brak dostępu do sklepu |

### TC-004 — Logowanie z pustymi polami · P2 · TD
| # | Login | Hasło | Oczekiwany rezultat |
|---|---|---|---|
| 1 | puste | puste | „Epic sadface: Username is required” |
| 2 | `standard_user` | puste | „Epic sadface: Password is required” |
| 3 | puste | `secret_sauce` | „Epic sadface: Username is required” |

### TC-005 — Wielkość liter w loginie · P3 · KR
| # | Krok | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Zaloguj się loginem pisanym wielkimi literami | `STANDARD_USER` / `secret_sauce` | Komunikat o niepoprawnych danych (login rozróżnia wielkość liter) — *do potwierdzenia z PO* |

### TC-006 — Spacje przed/po loginie · P3 · EG
| # | Krok | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Zaloguj się loginem ze spacją na końcu | `standard_user␣` / `secret_sauce` | Zachowanie zgodne z wymaganiem (przycięcie spacji lub komunikat o błędzie) — *pytanie do PO* |

### TC-007 — Zamknięcie komunikatu błędu · P3
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Wywołaj błąd logowania (TC-002) | Komunikat widoczny |
| 2 | Kliknij „X” w komunikacie | Komunikat znika, czerwone podświetlenie pól znika |

### TC-008 — Dostęp do sklepu bez logowania (bezpośredni URL) · P1 · EG
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | W nowej karcie incognito otwórz `https://www.saucedemo.com/inventory.html` | Przekierowanie na stronę logowania z komunikatem „You can only access '/inventory.html' when you are logged in.” |

### TC-009 — Logowanie użytkownika z opóźnieniem · P3
| # | Krok | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Zaloguj się, zmierz czas do wyświetlenia listy | `performance_glitch_user` | Lista produktów wyświetla się w akceptowalnym czasie (np. < 3 s — *wartość do ustalenia z PO*). Zmierzony czas zapisz w wyniku |

## Moduł: Produkty i sortowanie (US-02)

### TC-010 — Wyświetlenie listy produktów · P1
**Warunki wstępne:** zalogowany `standard_user`.
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Sprawdź listę produktów | 6 produktów; każdy ma zdjęcie, nazwę, opis, cenę i przycisk „Add to cart”; zdjęcia odpowiadają nazwom |

### TC-011 — Sortowanie po nazwie Z→A · P2
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Wybierz „Name (Z to A)” | Pierwszy produkt: „Test.allTheThings() T-Shirt (Red)”, ostatni: „Sauce Labs Backpack” |

### TC-012 — Sortowanie po cenie rosnąco · P2
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Wybierz „Price (low to high)” | Pierwsza cena $7.99, ostatnia $49.99; ceny w porządku niemalejącym |

### TC-013 — Sortowanie po cenie malejąco · P2
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Wybierz „Price (high to low)” | Pierwsza cena $49.99, ostatnia $7.99; ceny w porządku nierosnącym |

### TC-014 — Szczegóły produktu · P2
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Kliknij nazwę „Sauce Labs Backpack” | Strona szczegółów tego samego produktu: nazwa, opis, cena $29.99, zdjęcie plecaka |
| 2 | Kliknij „Back to products” | Powrót do listy produktów |

### TC-015 — Spójność danych lista ↔ szczegóły · P3 · EG
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Dla każdego z 6 produktów porównaj nazwę, cenę i zdjęcie na liście i na stronie szczegółów | Dane identyczne |

## Moduł: Koszyk (US-03)

### TC-016 — Dodanie produktu do koszyka · P1 · PS
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Kliknij „Add to cart” przy „Sauce Labs Backpack” | Przycisk zmienia się na „Remove”; licznik koszyka = 1 |
| 2 | Otwórz koszyk | Produkt widoczny z ilością 1 i ceną $29.99 |

### TC-017 — Dodanie wszystkich produktów · P2 · WB
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Dodaj wszystkie 6 produktów | Licznik = 6; w koszyku 6 pozycji |

### TC-018 — Usunięcie produktu z listy produktów · P2 · PS
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Dodaj produkt, kliknij „Remove” na liście | Przycisk wraca do „Add to cart”; licznik znika (0) |

### TC-019 — Usunięcie produktu w koszyku · P2
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Dodaj 2 produkty, otwórz koszyk, usuń jeden | W koszyku 1 pozycja; licznik = 1 |

### TC-020 — Koszyk po odświeżeniu strony · P3
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Dodaj 2 produkty, odśwież stronę (F5) | Licznik = 2; produkty nadal w koszyku |

### TC-021 — Reset App State · P3 · EG
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Dodaj 2 produkty | Licznik = 2 |
| 2 | Menu → „Reset App State” | Licznik znika; **przyciski przy produktach wracają do „Add to cart”** |

## Moduł: Zamówienie (US-04)

### TC-022 — Pełna ścieżka zakupu (E2E) · P1
**Warunki wstępne:** zalogowany `standard_user`, pusty koszyk.
| # | Krok | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Dodaj „Sauce Labs Backpack” i „Sauce Labs Bike Light” | — | Licznik = 2 |
| 2 | Koszyk → „Checkout” | — | Formularz „Checkout: Your Information” |
| 3 | Uzupełnij dane, „Continue” | Jan / Kowalski / 50-051 | Strona „Checkout: Overview” |
| 4 | Sprawdź podsumowanie | — | Item total: $39.98; Tax: $3.20; Total: $43.18 |
| 5 | Kliknij „Finish” | — | „Thank you for your order!”; licznik koszyka znika |

### TC-023 — Walidacja pól formularza checkout · P2 · TD
| # | Imię | Nazwisko | Kod | Oczekiwany rezultat |
|---|---|---|---|---|
| 1 | puste | puste | puste | „Error: First Name is required” |
| 2 | Jan | puste | puste | „Error: Last Name is required” |
| 3 | Jan | Kowalski | puste | „Error: Postal Code is required” |
| 4 | Jan | Kowalski | 50-051 | Przejście do podsumowania |

### TC-024 — Pola formularza — wartości brzegowe i znaki specjalne · P3 · WB/EG
| # | Pole | Dane | Oczekiwany rezultat |
|---|---|---|---|
| 1 | Imię | 1 znak: `J` | Akceptowane |
| 2 | Imię | 256 znaków | Zgodnie z wymaganiem (limit długości) — *pytanie do PO* |
| 3 | Nazwisko | `Łukasz-Żółć` | Polskie znaki i myślnik akceptowane |
| 4 | Kod | `abc!@#` | Walidacja formatu kodu — *pytanie do PO* |
| 5 | Imię | `<script>alert(1)</script>` | Brak wykonania skryptu; tekst traktowany jako zwykły tekst |

### TC-025 — Anulowanie zamówienia · P2
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Na stronie „Checkout: Overview” kliknij „Cancel” | Powrót do listy produktów; produkty nadal w koszyku |

### TC-026 — Zamówienie z pustym koszykiem · P2 · EG
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Przy pustym koszyku otwórz koszyk i kliknij „Checkout” | Przycisk nieaktywny lub komunikat „Koszyk jest pusty” — nie można złożyć zamówienia |

### TC-027 — Poprawność obliczeń dla wszystkich produktów · P2
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Dodaj 6 produktów i przejdź do podsumowania | Item total = $129.94; Tax (8%) = $10.40; Total = $140.34 |

## Moduł: Menu i wylogowanie (US-05)

### TC-028 — Wylogowanie · P1
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Menu → „Logout” | Strona logowania; pola puste |
| 2 | Użyj przycisku „Wstecz” przeglądarki | Brak dostępu do listy produktów — komunikat o konieczności zalogowania |

### TC-029 — Link „About” · P3
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | Menu → „About” | Otwiera się strona https://saucelabs.com |

## Moduł: UI / RWD

### TC-030 — Widok mobilny (375×812) · P3
| # | Krok | Oczekiwany rezultat |
|---|---|---|
| 1 | DevTools → iPhone 12 Pro; przejdź pełną ścieżkę TC-022 | Wszystkie elementy widoczne i klikalne; brak poziomego przewijania; teksty nie nachodzą na siebie |

---

## Pokrycie wymagań

| User story | Przypadki |
|---|---|
| US-01 Logowanie | TC-001 – TC-009 |
| US-02 Produkty | TC-010 – TC-015 |
| US-03 Koszyk | TC-016 – TC-021 |
| US-04 Zamówienie | TC-022 – TC-027 |
| US-05 Wylogowanie / menu | TC-028 – TC-029 |
| Niefunkcjonalne (UI/RWD) | TC-030 |
