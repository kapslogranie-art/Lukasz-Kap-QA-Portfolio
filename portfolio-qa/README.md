# Portfolio QA — pełny proces testowy na jednym projekcie

Kolejność folderów odpowiada kolejności pracy testera w sprincie:

| Krok | Folder | Zawartość |
|---|---|---|
| 1. Analiza i planowanie | [`01-plan-testow`](01-plan-testow) | Analiza wymagań + pytania do PO, plan testów, raport z testów |
| 2. Projektowanie | [`02-przypadki-testowe`](02-przypadki-testowe) | 30 przypadków (MD + CSV do Xray/TestRail), checklista regresji |
| 3. Zgłaszanie błędów | [`03-raporty-bledow`](03-raporty-bledow) | 6 raportów w formacie Jira, cykl życia defektu |
| 4. Eksploracja | [`04-testy-eksploracyjne`](04-testy-eksploracyjne) | 3 sesje z kartami testu, checklista mobile/RWD |
| 5. API | [`05-testy-api`](05-testy-api) | 14 przypadków, kolekcja Postman z asercjami |
| 6. Dane | [`06-sql`](06-sql) | Zapytania T-SQL (Microsoft SQL Server) weryfikujące dane |
| 7. AI | [`07-ai-w-qa`](07-ai-w-qa) | Jak używam AI i jak weryfikuję wyniki, biblioteka promptów |
| 8. Automatyzacja | [`08-automatyzacja`](08-automatyzacja) | PyTest + Selenium (Page Object), testy API, CI w GitHub Actions |

**Testowane aplikacje:** [SauceDemo](https://www.saucedemo.com) (sklep — aplikacja demonstracyjna
do nauki testów) i [Restful-Booker](https://restful-booker.herokuapp.com) (API do nauki testów).
Obie są publiczne — każdy wynik można samodzielnie odtworzyć.
