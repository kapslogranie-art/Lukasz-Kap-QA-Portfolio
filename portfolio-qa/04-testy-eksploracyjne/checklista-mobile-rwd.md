# Checklista testów mobilnych i responsywności (RWD)

Oferty dla testerów często wymagają doświadczenia w testach aplikacji **webowych lub mobilnych**. Ta checklista pokazuje,
na co zwracam uwagę przy testach na urządzeniach mobilnych — zarówno dla stron responsywnych
(emulacja w Chrome DevTools / prawdziwy telefon), jak i aplikacji natywnych.

## Urządzenia / rozdzielczości

| Kategoria | Przykład | Rozdzielczość (CSS px) |
|---|---|---|
| Mały telefon | iPhone SE | 375×667 |
| Telefon | iPhone 12 Pro / Pixel 7 | 390×844 / 412×915 |
| Tablet | iPad Air | 820×1180 |
| Desktop | Laptop / monitor | 1366×768 / 1920×1080 |

## Wygląd i układ

- [ ] Brak poziomego przewijania strony
- [ ] Teksty nie są ucięte i nie nachodzą na siebie
- [ ] Obrazy skalują się i nie tracą proporcji
- [ ] Menu „hamburger” otwiera i zamyka się poprawnie
- [ ] Orientacja pionowa i pozioma — układ się dostosowuje, dane nie znikają
- [ ] Tryb ciemny systemu (jeśli wspierany)

## Interakcja

- [ ] Elementy klikalne mają odpowiedni rozmiar (min. ~44×44 px) i odstępy
- [ ] Odpowiednia klawiatura dla pola (numeryczna dla kodu pocztowego/telefonu, e-mail dla adresu)
- [ ] Klawiatura ekranowa nie zasłania aktywnego pola ani przycisku
- [ ] Gesty: przewijanie, powrót gestem / przyciskiem systemowym
- [ ] Autouzupełnianie i wklejanie w polach formularzy

## Specyficzne dla aplikacji mobilnych

- [ ] Instalacja, aktualizacja, odinstalowanie
- [ ] Przerwania: połączenie przychodzące, powiadomienie, przejście do tła i powrót
- [ ] Utrata połączenia i powrót sieci (tryb samolotowy, słaby zasięg) — komunikaty i brak utraty danych
- [ ] Uprawnienia (aparat, lokalizacja, powiadomienia) — akceptacja i odmowa
- [ ] Niski poziom baterii / tryb oszczędzania energii
- [ ] Różne wersje systemu (Android / iOS) i rozmiary ekranów

## Wydajność i sieć

- [ ] Czas ładowania na „Slow 4G” (DevTools → Network throttling)
- [ ] Zachowanie przy przerwaniu żądania (offline w DevTools)

## Wynik dla SauceDemo (emulacja iPhone 12 Pro, Chrome DevTools)

| Obszar | Wynik |
|---|---|
| Logowanie | ✔ poprawny układ |
| Lista produktów | ✔ jedna kolumna, brak poziomego scrolla |
| Menu | ✔ działa |
| Formularz checkout | ⚠ pole „Zip/Postal Code” otwiera pełną klawiaturę tekstową — sugestia UX |
| Podsumowanie i potwierdzenie | ✔ |
