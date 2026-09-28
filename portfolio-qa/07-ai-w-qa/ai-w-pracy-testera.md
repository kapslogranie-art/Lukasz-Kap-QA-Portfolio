# AI w pracy testera — jak z niego korzystam

Coraz więcej ofert wymienia jako atut **znajomość narzędzi AI wspierających analizę wymagań, przygotowanie
testów i codzienną pracę QA**. Na kursie *Tester oprogramowania z elementami AI* (ALX) i w pracy
nad tym portfolio używam asystentów AI (m.in. **Claude / Claude Code**, ChatGPT).

## Zasady, których się trzymam

1. **AI to pomocnik, nie wyrocznia.** Każdy wynik sprawdzam z wymaganiem i w aplikacji.
2. **Nie wklejam danych poufnych** — danych klientów, haseł, kodu i dokumentacji objętych NDA —
   do narzędzi, które nie są zatwierdzone przez firmę/klienta.
3. **Odpowiedzialność zostaje po mojej stronie.** Jeśli AI zaproponuje przypadek testowy z błędnym
   wynikiem oczekiwanym, a ja go nie zweryfikuję — to mój błąd, nie narzędzia.
4. **Konkretny kontekst = lepszy wynik.** Podaję user story, kryteria akceptacji, ograniczenia i format odpowiedzi.

## Gdzie AI realnie przyspiesza pracę

| Etap | Jak używam AI | Co weryfikuję sam |
|---|---|---|
| Analiza wymagań | Szukanie niejasności i brakujących kryteriów w user story; lista pytań do analityka | Czy pytania mają sens biznesowy; czy nie są już opisane w dokumentacji |
| Projektowanie testów | Szkic przypadków pozytywnych, negatywnych i brzegowych; tablice decyzyjne | Wyniki oczekiwane, priorytety, duplikaty, pokrycie kryteriów |
| Dane testowe | Generowanie zestawów danych (np. poprawne/niepoprawne kody pocztowe, długie ciągi, znaki specjalne) | Czy dane są realistyczne i pokrywają klasy równoważności |
| Raporty błędów | Porządkowanie notatek w czytelne zgłoszenie, poprawa języka (także po angielsku) | Fakty, kroki, środowisko — nic nie może być „dopisane” przez AI |
| SQL / API | Pomoc w zbudowaniu zapytania lub asercji w Postmanie; wyjaśnienie odpowiedzi błędu | Uruchamiam i sprawdzam wynik na prawdziwych danych |
| Automatyzacja | Claude Code: wyjaśnienie kodu testu, pomoc w debugowaniu niestabilnego lokatora, szkic testu PyTest | Czytam każdy wygenerowany kod, uruchamiam testy, rozumiem, co robią |
| Dokumentacja po angielsku | Tłumaczenie i sprawdzanie terminologii QA (przy angielskim A2 to dla mnie duże wsparcie) | Czy tłumaczenie oddaje sens techniczny |

## Przykład: od user story do przypadków testowych

**User story (wejście):**
> Jako klient chcę złożyć zamówienie, podając imię, nazwisko i kod pocztowy, aby otrzymać zakupione produkty.
> AC: wszystkie pola wymagane; po złożeniu zamówienia koszyk jest pusty.

**Prompt:**
```
Jesteś doświadczonym testerem manualnym. Na podstawie user story i kryteriów akceptacji poniżej:
1) wypisz niejasności i pytania do analityka,
2) zaproponuj przypadki testowe (pozytywne, negatywne, brzegowe) w tabeli:
   ID | Tytuł | Kroki | Dane | Oczekiwany rezultat | Priorytet,
3) zaznacz, które przypadki warto zautomatyzować i dlaczego.
Nie wymyślaj wymagań — jeśli czegoś nie wiesz, zapisz to jako pytanie.
[user story + AC]
```

**W czym taki prompt zwykle pomaga:** pytania o format kodu pocztowego, limit długości pól,
podwójne kliknięcie „Finish”; szybki szkic przypadków walidacji pól.

**Typowe poprawki, które wprowadzam po AI:**
- **Założenia podane jako fakty** — np. przyjęcie, że kod pocztowy ma format `00-000`, choć wymaganie
  tego nie mówi. Takie rzeczy zamieniam na pytanie do PO (TC-024).
- **Pominięte scenariusze wynikające ze znajomości aplikacji** — np. checkout z pustym koszykiem
  (TC-026 → BUG-005) wyszedł z mojej sesji eksploracyjnej, nie z samej analizy tekstu.
- **Priorytety „na równo”** — ustalam je sam, według ryzyka biznesowego.
- **Duplikaty i przypadki niewnoszące nic nowego** — usuwam.

➡ Efekt w tym repozytorium: [`analiza-wymagan.md`](../01-plan-testow/analiza-wymagan.md),
[`przypadki-testowe.md`](../02-przypadki-testowe/przypadki-testowe.md) (TC-022 – TC-027).

## Biblioteka promptów

Gotowe prompty, których używam: [`prompty.md`](prompty.md)
