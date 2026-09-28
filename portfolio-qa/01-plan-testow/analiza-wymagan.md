# Analiza wymagań — SauceDemo (sklep internetowy)

**Aplikacja:** https://www.saucedemo.com
**Cel dokumentu:** zrozumieć wymagania przed testami, wskazać niejasności i ryzyka, przygotować pytania
do analityka / Product Ownera.

## 1. User stories (odtworzone na podstawie działania aplikacji)

| ID | User story | Kryteria akceptacji |
|---|---|---|
| US-01 | Jako klient chcę zalogować się do sklepu, aby móc robić zakupy | AC1: poprawne dane → strona „Products”. AC2: błędne dane → komunikat błędu. AC3: zablokowany użytkownik → komunikat o blokadzie. AC4: puste pola → komunikat „Username is required” / „Password is required” |
| US-02 | Jako klient chcę przeglądać i sortować produkty | AC1: widoczna lista 6 produktów ze zdjęciem, nazwą, opisem i ceną. AC2: sortowanie A–Z, Z–A, cena rosnąco, cena malejąco |
| US-03 | Jako klient chcę dodawać i usuwać produkty z koszyka | AC1: licznik na ikonie koszyka odzwierciedla liczbę produktów. AC2: przycisk zmienia się z „Add to cart” na „Remove” |
| US-04 | Jako klient chcę złożyć zamówienie | AC1: formularz wymaga imienia, nazwiska, kodu pocztowego. AC2: podsumowanie pokazuje sumę, podatek i razem. AC3: po „Finish” komunikat potwierdzenia i pusty koszyk |
| US-05 | Jako klient chcę się wylogować | AC1: po wylogowaniu powrót do strony logowania. AC2: brak dostępu do stron sklepu przez bezpośredni URL |

## 2. Niejasności — pytania do analityka / PO

1. **US-01:** Czy po X nieudanych próbach logowania konto powinno być blokowane? Czy wielkość liter w loginie ma znaczenie?
2. **US-01:** Czy komunikaty błędów mają być wielojęzyczne? Jaki jest docelowy tekst komunikatów?
3. **US-02:** Czy wybrana opcja sortowania ma być zapamiętana po odświeżeniu strony / po powrocie z koszyka?
4. **US-03:** Czy jest limit ilości sztuk jednego produktu? Czy koszyk ma być zachowany po wylogowaniu?
5. **US-04:** Jaki jest format kodu pocztowego (tylko cyfry? kraj?) i maksymalna długość imienia/nazwiska?
6. **US-04:** Jaka stawka podatku ma być naliczana i jak zaokrąglamy kwoty (do 2 miejsc, w górę/w dół)?
7. **US-04:** Czy można złożyć zamówienie z pustym koszykiem? *(obecnie aplikacja na to pozwala — patrz BUG-005)*
8. **US-05:** Czy sesja wygasa po czasie bezczynności? Po jakim?
9. **Ogólne:** Jakie przeglądarki i urządzenia są wspierane? Czy obowiązuje WCAG (dostępność)?

## 3. Ryzyka produktowe

| Ryzyko | Prawdopodobieństwo | Wpływ | Priorytet testów |
|---|---|---|---|
| Nie da się złożyć zamówienia (utrata przychodu) | Średnie | Krytyczny | **Wysoki** |
| Błędne wyliczenie sumy / podatku | Średnie | Wysoki | **Wysoki** |
| Logowanie nie działa / obejście logowania | Niskie | Krytyczny | **Wysoki** |
| Błędy sortowania i prezentacji produktów | Średnie | Średni | Średni |
| Problemy wydajnościowe (wolne ładowanie) | Średnie | Średni | Średni |
| Problemy wyglądu na urządzeniach mobilnych | Wysokie | Średni | Średni |
| Literówki / drobne błędy UI | Wysokie | Niski | Niski |

## 4. Wnioski do planu testów

- Najwięcej uwagi: ścieżka zakupowa (login → koszyk → checkout → potwierdzenie) i obliczenia kwot.
- Testy negatywne formularzy logowania i checkoutu.
- Różni użytkownicy testowi (`standard_user`, `locked_out_user`, `problem_user`,
  `performance_glitch_user`, `error_user`, `visual_user`) pozwalają sprawdzić różne zachowania systemu.
