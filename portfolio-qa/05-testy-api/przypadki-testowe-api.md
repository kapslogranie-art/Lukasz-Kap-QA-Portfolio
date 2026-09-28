# Testy API — Restful-Booker

**API:** https://restful-booker.herokuapp.com · [dokumentacja](https://restful-booker.herokuapp.com/apidoc/index.html)
**Narzędzia:** Postman (kolekcja: [`restful-booker.postman_collection.json`](restful-booker.postman_collection.json)),
Newman (uruchamianie z linii poleceń / CI), Python `requests` + PyTest ([`08-automatyzacja/tests/api`](../08-automatyzacja/tests/api)).

## Jak uruchomić

1. Postman → *Import* → wybierz plik kolekcji.
2. Uruchom całą kolekcję: *Run collection* (kolejność żądań ma znaczenie — zmienne `token` i `bookingId`
   są zapisywane przez wcześniejsze żądania).
3. Z terminala: `npx newman run restful-booker.postman_collection.json`

## Przypadki testowe

| ID | Metoda i endpoint | Scenariusz | Oczekiwany rezultat |
|---|---|---|---|
| API-01 | `GET /ping` | Health check | `201 Created` |
| API-02 | `POST /auth` | Poprawne dane (`admin` / `password123`) | `200`, w body pole `token` (niepusty string) |
| API-03 | `POST /auth` | Błędne hasło | `200` i `{"reason": "Bad credentials"}` — **brak tokenu** *(uwaga: API zwraca 200 zamiast 401 — obserwacja do omówienia)* |
| API-04 | `POST /booking` | Utworzenie rezerwacji z poprawnymi danymi | `200`, `bookingid` jest liczbą, dane w odpowiedzi = dane wysłane |
| API-05 | `GET /booking/{id}` | Pobranie utworzonej rezerwacji | `200`, `firstname`, `lastname`, `totalprice`, daty zgodne z API-04 |
| API-06 | `GET /booking?firstname=…` | Filtrowanie po imieniu | `200`, lista zawiera `bookingid` z API-04 |
| API-07 | `PUT /booking/{id}` | Pełna aktualizacja z tokenem (Cookie `token=…`) | `200`, dane zaktualizowane |
| API-08 | `PATCH /booking/{id}` | Częściowa aktualizacja (tylko `firstname`) | `200`, zmienione tylko `firstname` |
| API-09 | `PUT /booking/{id}` | Aktualizacja **bez** tokenu | `403 Forbidden` |
| API-10 | `DELETE /booking/{id}` | Usunięcie z tokenem | `201` *(API zwraca 201 zamiast 200/204 — obserwacja)* |
| API-11 | `GET /booking/{id}` | Pobranie usuniętej rezerwacji | `404 Not Found` |
| API-12 | `GET /booking/999999999` | Nieistniejące ID | `404 Not Found` |
| API-13 | `POST /booking` | Brak wymaganego pola `firstname` | `4xx` z opisem błędu *(API zwraca `500` — potencjalny defekt)* |
| API-14 | `GET /booking/{id}` | Czas odpowiedzi | < 2000 ms |

## Co sprawdzam w każdym żądaniu

- **Kod statusu HTTP** (2xx sukces, 4xx błąd klienta, 5xx błąd serwera)
- **Nagłówki** — np. `Content-Type: application/json`
- **Body** — struktura (pola, typy danych) i wartości
- **Czas odpowiedzi**
- **Spójność** — dane zapisane w POST są zwracane w GET (a w prawdziwym projekcie: także w bazie → SQL)

## Kody HTTP — ściąga

| Kod | Znaczenie | Przykład |
|---|---|---|
| 200 OK | Sukces | GET zwrócił dane |
| 201 Created | Zasób utworzony | POST utworzył rekord |
| 204 No Content | Sukces bez treści | DELETE |
| 400 Bad Request | Niepoprawne dane wejściowe | Brak wymaganego pola |
| 401 Unauthorized | Brak/niepoprawne uwierzytelnienie | Brak tokenu |
| 403 Forbidden | Brak uprawnień | Token bez uprawnień do zasobu |
| 404 Not Found | Zasób nie istnieje | Nieistniejące ID |
| 500 Internal Server Error | Błąd serwera | Nieobsłużony wyjątek |

## Obserwacje (do zgłoszenia / omówienia)

1. `POST /auth` z błędnymi danymi zwraca `200` zamiast `401`.
2. `DELETE` zwraca `201 Created` zamiast `200`/`204`.
3. Brak wymaganego pola w `POST /booking` kończy się `500` zamiast `400` z czytelnym komunikatem.

> Restful-Booker to publiczne API do nauki; część niestandardowych zachowań jest w nim celowa.
