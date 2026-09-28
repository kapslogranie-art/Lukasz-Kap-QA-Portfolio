# Biblioteka promptów dla testera

Wszystkie prompty zakładają, że **nie wklejam danych poufnych** i że każdy wynik weryfikuję.

## 1. Analiza wymagań — luki jakościowe

```
Przeanalizuj poniższą user story i kryteria akceptacji jako tester.
Wypisz:
- niejasności i sprzeczności,
- brakujące kryteria akceptacji (walidacje, komunikaty błędów, uprawnienia, stany brzegowe),
- ryzyka biznesowe i techniczne,
- pytania do analityka (maks. 10, od najważniejszego).
Nie dopisuj wymagań od siebie.
[treść]
```

## 2. Przypadki testowe z technik projektowania

```
Dla pola/funkcji: [opis, np. "pole wiek: liczba całkowita 18–65"]
zastosuj klasy równoważności i analizę wartości brzegowych.
Zwróć tabelę: Klasa/granica | Wartość testowa | Oczekiwany rezultat.
```

## 3. Tablica decyzyjna

```
Zbuduj tablicę decyzyjną dla reguł: [reguły biznesowe, np. rabat zależny od statusu klienta i kwoty].
Wypisz wszystkie kombinacje warunków, akcje i zaznacz kombinacje niemożliwe.
```

## 4. Karta sesji eksploracyjnej

```
Zaproponuj 5 kart sesji testów eksploracyjnych (charter) dla modułu: [moduł].
Format: "Eksploruj <obszar> z użyciem <technika/zasoby>, aby odkryć <rodzaj problemów>".
Do każdej dodaj 5 pomysłów testowych i heurystyk.
```

## 5. Raport błędu z notatek

```
Na podstawie moich notatek przygotuj zgłoszenie błędu w formacie Jira:
Tytuł, Środowisko, Warunki wstępne, Kroki, Rezultat oczekiwany, Rezultat rzeczywisty,
Ważność (z uzasadnieniem). Używaj wyłącznie faktów z notatek — niczego nie dopisuj.
Następnie przetłumacz zgłoszenie na angielski.
[notatki]
```

## 6. Zapytanie SQL

```
Mam tabele (SQL Server): [struktura tabel].
Napisz zapytanie T-SQL, które znajdzie [np. zamówienia, których suma pozycji różni się od item_total].
Wyjaśnij zapytanie krok po kroku.
```

## 7. Asercje w Postmanie

```
Odpowiedź API wygląda tak: [przykładowy JSON bez danych wrażliwych].
Napisz testy Postmana (pm.test) sprawdzające: kod 200, typy pól, wymagane pola, czas < 2 s.
```

## 8. Analiza niestabilnego testu automatycznego

```
Test Selenium czasami kończy się błędem: [traceback].
Kod testu: [kod]. Jakie są możliwe przyczyny (lokator, czekanie, dane, środowisko)
i jak to sprawdzić krok po kroku? Zaproponuj poprawkę z jawnym oczekiwaniem (WebDriverWait).
```

## 9. Dobór zestawu regresji

```
Zmiana w wydaniu: [opis zmiany]. Lista przypadków testowych: [lista ID + tytuły + moduły].
Zaproponuj zestaw regresji oparty o ryzyko: co uruchomić obowiązkowo, co opcjonalnie, uzasadnij.
```
