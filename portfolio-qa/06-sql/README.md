# SQL w pracy testera (Microsoft SQL Server)

Najczęściej spotykane w ofertach bazy to **Microsoft SQL Server**, Oracle i PostgreSQL. Plik [`zapytania-weryfikacyjne.sql`](zapytania-weryfikacyjne.sql)
jest napisany w T-SQL i sam tworzy przykładowe tabele, więc można go uruchomić na czystej bazie
(SQL Server Express, Docker `mcr.microsoft.com/mssql/server` albo https://dbfiddle.uk → SQL Server).

## Po co testerowi SQL

- **Weryfikacja zapisu** — czy to, co widzę w UI / odpowiedzi API, jest poprawnie zapisane w bazie.
- **Szukanie niespójności** — sumy, podatki, rekordy osierocone, braki danych.
- **Przygotowanie danych testowych** — w transakcji z `ROLLBACK`, żeby nie zostawiać śmieci.
- **Diagnoza błędu** — dołączenie do zgłoszenia zapytania i wyniku przyspiesza pracę developera.

## Co pokazuje skrypt

| # | Zapytanie | Elementy SQL |
|---|---|---|
| 1 | Ostatnie zamówienie użytkownika | `JOIN`, `TOP`, `ORDER BY` |
| 2 | Pozycje zamówienia | `JOIN` 3 tabel, wyrażenia |
| 3 | Suma pozycji ≠ `item_total` | `GROUP BY`, `HAVING`, `SUM` |
| 4–5 | Poprawność sumy i podatku | `ROUND`, porównania |
| 6 | Zamówienia bez pozycji | `LEFT JOIN … IS NULL` |
| 7 | Niekompletne dane klientów | `NULLIF`, `LTRIM/RTRIM` |
| 8 | Zablokowany użytkownik z zamówieniami | `COUNT`, filtr |
| 9 | Przychód per klient | `LEFT JOIN`, `COALESCE` |
| 10 | Duplikaty loginów | `LOWER`, `HAVING COUNT(*) > 1` |
| 11 | Produkty bez sprzedaży | `NOT EXISTS` |
| 12 | Dane testowe w transakcji | `BEGIN TRAN` / `ROLLBACK` |

Dane są przygotowane tak, żeby zapytania 4, 6 i 7 **znalazły** celowo wprowadzone niespójności
(błędna suma zamówienia nr 3, zamówienie bez pozycji, klient bez nazwiska), a zapytania 3, 5, 8 i 10
zwróciły pusty wynik (dane poprawne)
— tak wygląda praca testera z bazą: zapytanie kontrolne zwracające wiersze = sygnał do analizy.

## Różnice T-SQL vs. MySQL/PostgreSQL, o których pamiętam

| | SQL Server | MySQL / PostgreSQL |
|---|---|---|
| Ograniczenie wyników | `SELECT TOP (10) …` | `… LIMIT 10` |
| Auto-numeracja | `IDENTITY(1,1)` | `AUTO_INCREMENT` / `SERIAL` |
| Bieżąca data | `GETDATE()`, `SYSDATETIME()` | `NOW()` |
| Zamiana NULL | `ISNULL()` / `COALESCE()` | `IFNULL()` / `COALESCE()` |
| Tekst Unicode | `N'tekst'`, `NVARCHAR` | `'tekst'`, `VARCHAR` (UTF-8) |
