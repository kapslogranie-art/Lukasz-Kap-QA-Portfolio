# Macierz kompetencji — typowe wymagania na stanowisko testera → dowód w portfolio

Zestawienie wymagań, które najczęściej pojawiają się w ogłoszeniach na stanowiska **Tester manualny /
Junior QA / Tester oprogramowania**, wraz z miejscem w repozytorium, które je potwierdza.

## Testowanie manualne i proces

| Wymaganie | Poziom | Dowód |
|---|---|---|
| Testy manualne aplikacji webowych | ✔ projektowy (bez komercyjnego) | [Meridian Bank](../portfolio-qa/09-meridian-bank), [SauceDemo](../portfolio-qa/01-plan-testow) |
| Testy aplikacji mobilnych / RWD | ◐ podstawy | [checklista mobile/RWD](../portfolio-qa/04-testy-eksploracyjne/checklista-mobile-rwd.md) |
| Pisanie scenariuszy i przypadków testowych | ✔ | [47 przypadków — bank](../portfolio-qa/09-meridian-bank/przypadki-testowe.md), [30 przypadków — sklep](../portfolio-qa/02-przypadki-testowe/przypadki-testowe.md) |
| Techniki projektowania testów | ✔ | Klasy równoważności, wartości brzegowe, tablice decyzyjne, przejścia stanów — w przypadkach testowych |
| Raportowanie i retest błędów | ✔ | [16 błędów — bank](../portfolio-qa/09-meridian-bank/raporty-bledow.md), [6 błędów — sklep](../portfolio-qa/03-raporty-bledow/raporty-bledow.md) |
| Cykl życia defektu, STLC | ✔ | [cykl-zycia-defektu.md](../portfolio-qa/03-raporty-bledow/cykl-zycia-defektu.md) |
| Testy regresyjne | ✔ | [checklista regresji](../portfolio-qa/02-przypadki-testowe/checklista-regresji.md), testy `xfail` jako regresja po poprawce |
| Testy eksploracyjne | ✔ | [sesje z kartami testu](../portfolio-qa/04-testy-eksploracyjne/sesje-eksploracyjne.md) |
| Analiza wymagań, luki jakościowe | ✔ | [analiza wymagań + pytania do PO](../portfolio-qa/01-plan-testow/analiza-wymagan.md) |
| Plan i raport z testów | ✔ | [plan](../portfolio-qa/01-plan-testow/plan-testow-saucedemo.md), [raport — bank](../portfolio-qa/09-meridian-bank/plan-i-raport.md) |
| Agile / Scrum | ◐ kurs + teoria | [plan testów](../portfolio-qa/01-plan-testow/plan-testow-saucedemo.md), [cykl życia defektu (STLC w sprincie)](../portfolio-qa/03-raporty-bledow/cykl-zycia-defektu.md) |

## Narzędzia

| Narzędzie | Poziom | Dowód |
|---|---|---|
| Jira | ◐ kurs, format zgłoszeń | Raporty błędów w formacie Jira |
| Xray / TestRail / TestLink | ◐ struktura przypadków | [CSV do importu](../portfolio-qa/02-przypadki-testowe/przypadki-testowe-import.csv) |
| Postman / testy API (REST, JSON) | ✔ podstawy | [kolekcja + 14 przypadków](../portfolio-qa/05-testy-api) |
| SQL (MS SQL, Oracle, MySQL) | ✔ podstawy | [zapytania weryfikacyjne T-SQL](../portfolio-qa/06-sql) |
| Chrome DevTools | ✔ | Analiza żądań i kodu front-endu przy diagnozie błędów (Meridian Bank) |
| Git / GitHub | ✔ podstawy | To repozytorium |

## Automatyzacja i CI/CD (zwykle „mile widziane”)

| Wymaganie | Poziom | Dowód |
|---|---|---|
| Python | ✔ podstawy | [testy PyTest](../portfolio-qa/08-automatyzacja/tests) |
| Selenium WebDriver, Page Object | ✔ podstawy | [pages/](../portfolio-qa/08-automatyzacja/pages) |
| Playwright / Cypress | ✗ | Kolejny krok nauki (te same koncepcje co w Selenium) |
| CI/CD | ✔ podstawy | [GitHub Actions](../.github/workflows/testy.yml) — testy przy każdym pushu |
| Narzędzia AI w pracy QA | ✔ | [AI w pracy testera](../portfolio-qa/07-ai-w-qa) |

## Kompetencje miękkie

Dokładność · komunikatywność · samodzielność · analityczne myślenie · konsekwencja · wysoka kultura pracy.

## Obszary do rozwoju — i co z nimi robię

| Obszar | Plan |
|---|---|
| Brak doświadczenia komercyjnego | Portfolio odwzorowujące realny proces; gotowość do zadania rekrutacyjnego |
| Angielski A2 | Codzienna nauka słownictwa QA, zgłoszenia po angielsku — [rozmowa-po-angielsku.md](../rozmowa/rozmowa-po-angielsku.md) |
| Xray / TestRail w praktyce | Konto trial i import przygotowanego CSV |
| Playwright / Cypress | Kolejny krok po Selenium |
| ISTQB Foundation | Planowany — [plan 30-60-90](../rozmowa/plan-30-60-90.md) |

---

## Jak dopasować aplikację do konkretnej oferty (10 minut)

1. Skopiuj z ogłoszenia listę wymagań i obowiązków.
2. Dla każdego punktu znajdź wiersz w tabelach powyżej → masz gotowe argumenty do listu i rozmowy.
3. Punkty z ogłoszenia, których tu nie ma, zapisz jako pytania na rozmowę albo obszar do rozwoju
   (uczciwie: „znam podstawy / uczę się”).
4. W [liście motywacyjnym](list-motywacyjny-szablon.md) zostaw 4–5 najlepiej pasujących projektów.
5. Przed rozmową przygotuj sekcję „Research firmy” z [przygotowania do rozmowy](../rozmowa/przygotowanie-do-rozmowy.md).
