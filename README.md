# Łukasz Kap — Tester manualny / Junior QA · portfolio

**Kontakt:** kaplukasz@gmail.com · 515 836 183 · Radzyń Podlaski (praca zdalna, hybrydowa lub stacjonarna)
**Portfolio online:** [lukasztm.github.io/Portfolio](https://lukasztm.github.io/Portfolio)

[![Testy automatyczne](https://github.com/kapslogranie-art/Lukasz-Kap-QA-Portfolio/actions/workflows/testy.yml/badge.svg)](https://github.com/kapslogranie-art/Lukasz-Kap-QA-Portfolio/actions/workflows/testy.yml)

---

## O mnie w 30 sekund

Jestem początkującym testerem oprogramowania po kursach ALX *Tester oprogramowania z elementami AI*
i *Tester Automatyzujący*. Nie mam jeszcze doświadczenia komercyjnego, dlatego to repozytorium
**pokazuje, jak pracuję**: od analizy wymagań, przez przypadki testowe i raporty błędów, po testy API,
SQL i testy automatyczne uruchamiane w CI.

Wszystkie testowane aplikacje są publiczne, więc każdy wynik można samodzielnie odtworzyć:
**[Meridian Bank](https://lukasztm.github.io/MeridianBank/)** (szkoleniowa bankowość internetowa),
**[SauceDemo](https://www.saucedemo.com)** (sklep internetowy) i
**[Restful-Booker](https://restful-booker.herokuapp.com)** (API).

## ⭐ Projekt główny: testy bankowości internetowej (Meridian Bank)

**47 przypadków testowych · 16 zgłoszonych błędów (4 krytyczne) · 32 testy automatyczne w CI**

Przykładowe znaleziska: przelew z konta oszczędnościowego obciąża konto osobiste, kantor przelicza
walutę po niewłaściwym kursie, kod BLIK ma 5 cyfr zamiast 6, blokada logowania działa po 2 zamiast
3 próbach. 13 błędów ma test automatyczny, który zaalarmuje, gdy błąd zostanie naprawiony — sygnał do retestu.
➡ [`portfolio-qa/09-meridian-bank`](portfolio-qa/09-meridian-bank)

## Co umiem → gdzie to zobaczyć

| Umiejętność | Dowód |
|---|---|
| Analiza wymagań, wykrywanie luk jakościowych | [Analiza wymagań + pytania do PO](portfolio-qa/01-plan-testow/analiza-wymagan.md) |
| Scenariusze i przypadki testowe | [47 przypadków — bank](portfolio-qa/09-meridian-bank/przypadki-testowe.md), [30 przypadków — sklep](portfolio-qa/02-przypadki-testowe/przypadki-testowe.md) + [CSV do Xray/TestRail](portfolio-qa/02-przypadki-testowe/przypadki-testowe-import.csv) |
| Zgłaszanie i retest błędów | [16 błędów — bank](portfolio-qa/09-meridian-bank/raporty-bledow.md), [raporty w formacie Jira — sklep](portfolio-qa/03-raporty-bledow/raporty-bledow.md) |
| Cykl życia defektu, proces testowy | [Cykl życia defektu + STLC](portfolio-qa/03-raporty-bledow/cykl-zycia-defektu.md) |
| Testy funkcjonalne, regresyjne, eksploracyjne | [Plan i raport — bank](portfolio-qa/09-meridian-bank/plan-i-raport.md), [checklista regresji](portfolio-qa/02-przypadki-testowe/checklista-regresji.md), [sesje eksploracyjne](portfolio-qa/04-testy-eksploracyjne/sesje-eksploracyjne.md) |
| Testy web i mobile / RWD | Projekty webowe + [checklista mobile/RWD](portfolio-qa/04-testy-eksploracyjne/checklista-mobile-rwd.md) |
| Testy API (Postman, REST, JSON) | [Przypadki API + kolekcja Postman](portfolio-qa/05-testy-api) |
| SQL | [Zapytania weryfikujące dane (T-SQL)](portfolio-qa/06-sql) |
| Automatyzacja: Python, PyTest, Selenium, Page Object | [08-automatyzacja](portfolio-qa/08-automatyzacja) |
| CI/CD | [GitHub Actions](.github/workflows/testy.yml) — testy przy każdym pushu |
| Narzędzia AI w pracy QA | [AI w pracy testera + prompty](portfolio-qa/07-ai-w-qa) |

## Struktura

```
.
├── portfolio-qa/
│   ├── 01-plan-testow/              ← analiza wymagań, plan testów, raport z testów (SauceDemo)
│   ├── 02-przypadki-testowe/        ← przypadki testowe + CSV + checklista regresji
│   ├── 03-raporty-bledow/           ← raporty defektów (Jira), cykl życia defektu
│   ├── 04-testy-eksploracyjne/      ← karty sesji + checklista mobile/RWD
│   ├── 05-testy-api/                ← kolekcja Postman + przypadki API
│   ├── 06-sql/                      ← zapytania T-SQL weryfikujące dane
│   ├── 07-ai-w-qa/                  ← jak używam AI i jak weryfikuję wyniki
│   ├── 08-automatyzacja/            ← PyTest + Selenium (Page Object) + testy API
│   └── 09-meridian-bank/            ← projekt główny: testy bankowości internetowej
├── materialy-aplikacyjne/           ← szablony: list motywacyjny, treść CV, wiadomości, macierz kompetencji
├── rozmowa/                         ← przygotowanie do rozmowy, angielski, plan pierwszych 90 dni
├── dokumenty/                       ← CV (PDF) i portfolio (HTML)
└── .github/workflows/testy.yml      ← CI: testy API, UI (SauceDemo, Meridian Bank) i Postman (Newman)
```

## Moja ścieżka

- **Kurs Tester Oprogramowania z elementami AI** (ALX, 2025): przypadki testowe, raportowanie
  błędów (Jira/Bugzilla), API (Postman, REST, JSON), SQL, SDLC, Agile/Scrum, testy eksploracyjne.
- **Kurs Tester Automatyzujący** (ALX, 2026): Python, unittest, PyTest, Selenium WebDriver, Page Object, podstawy Selenium Grid.
- **Narzędzia:** Jira, Xray, TestLink, Bugzilla, Postman, JMeter, Oracle SQL Developer, Chrome DevTools, PyCharm, Git/GitHub, Claude Code.
- **Mocne strony:** dokładność, analityczne myślenie, czytelne raporty, konsekwencja, komunikatywność.
- **Języki:** polski (ojczysty), angielski A2 (dokumentacja techniczna, terminologia QA — aktywnie się uczę).
