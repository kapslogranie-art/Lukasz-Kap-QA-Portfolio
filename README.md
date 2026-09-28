# Łukasz Kap — Tester Manualny · portfolio QA

> Materiały aplikacyjne i portfolio QA przygotowane pod ofertę
> **Tester Manualny / Testerka Manualna — Hiberus Poland, Wrocław** (praca hybrydowa, 2× w miesiącu w biurze).

**Kontakt:** kaplukasz@gmail.com · Radzyń Podlaski — dojazd do biura we Wrocławiu 2× w miesiącu bez problemu

[![Testy automatyczne](https://github.com/kapslogranie-art/-ukasz-Kap-Manual-Tester/actions/workflows/testy.yml/badge.svg)](https://github.com/kapslogranie-art/-ukasz-Kap-Manual-Tester/actions/workflows/testy.yml)

---

## O co chodzi w tym repozytorium

To repozytorium nie tylko opisuje, co umiem — pokazuje, **jak pracuję**. Każde wymaganie z ogłoszenia
ma tu konkretny, sprawdzalny artefakt: analizę wymagań, plan testów, przypadki testowe, raporty błędów,
sesje testów eksploracyjnych, kolekcję Postmana, zapytania SQL (Microsoft SQL Server), testy
automatyczne uruchamiane w CI oraz opis tego, jak używam AI w pracy testera.

Testowane aplikacje są publiczne, więc każdy wynik można odtworzyć:
**[SauceDemo](https://www.saucedemo.com)** (sklep internetowy do nauki testów) oraz
**[Restful-Booker](https://restful-booker.herokuapp.com)** (API do nauki testów).

## Wymagania z oferty → dowód w repozytorium

| Z oferty | Gdzie to pokazuję |
|---|---|
| Scenariusze i przypadki testowe | [30 przypadków](portfolio-qa/02-przypadki-testowe/przypadki-testowe.md) + [CSV do Xray/TestRail](portfolio-qa/02-przypadki-testowe/przypadki-testowe-import.csv) |
| Testy funkcjonalne, regresyjne, eksploracyjne | [Raport z testów](portfolio-qa/01-plan-testow/raport-z-testow.md), [checklista regresji](portfolio-qa/02-przypadki-testowe/checklista-regresji.md), [sesje eksploracyjne](portfolio-qa/04-testy-eksploracyjne/sesje-eksploracyjne.md) |
| Zgłaszanie, opisywanie i retest błędów | [Raporty w formacie Jira](portfolio-qa/03-raporty-bledow/raporty-bledow.md) |
| Cykl życia defektu i proces testowy | [Cykl życia defektu + STLC](portfolio-qa/03-raporty-bledow/cykl-zycia-defektu.md) |
| Analiza wymagań i luki jakościowe | [Analiza wymagań + pytania do PO](portfolio-qa/01-plan-testow/analiza-wymagan.md) |
| Jira, Xray, TestRail | Format zgłoszeń Jira, import CSV |
| Testy web / mobile | Projekt SauceDemo + [checklista mobile/RWD](portfolio-qa/04-testy-eksploracyjne/checklista-mobile-rwd.md) |
| Podstawy testowania API | [Przypadki API + kolekcja Postman](portfolio-qa/05-testy-api) |
| Podstawy SQL (Microsoft SQL) | [Zapytania T-SQL](portfolio-qa/06-sql) |
| *Mile widziane:* Selenium, Python | [PyTest + Selenium, Page Object](portfolio-qa/08-automatyzacja) |
| *Mile widziane:* CI/CD | [GitHub Actions](.github/workflows/testy.yml) — testy przy każdym pushu |
| *Mile widziane:* narzędzia AI w QA | [AI w pracy testera + prompty](portfolio-qa/07-ai-w-qa) |

Szczegółowa macierz: [`aplikacja/dopasowanie-do-oferty.md`](aplikacja/dopasowanie-do-oferty.md)

## Struktura

```
.
├── aplikacja/                       ← list motywacyjny, CV, wiadomości, dopasowanie do oferty
├── portfolio-qa/
│   ├── 01-plan-testow/              ← analiza wymagań, plan testów, raport z testów
│   ├── 02-przypadki-testowe/        ← przypadki testowe + CSV + checklista regresji
│   ├── 03-raporty-bledow/           ← raporty defektów (Jira), cykl życia defektu
│   ├── 04-testy-eksploracyjne/      ← karty sesji + checklista mobile/RWD
│   ├── 05-testy-api/                ← kolekcja Postman + przypadki API
│   ├── 06-sql/                      ← zapytania T-SQL weryfikujące dane
│   ├── 07-ai-w-qa/                  ← jak używam AI i jak weryfikuję wyniki
│   └── 08-automatyzacja/            ← PyTest + Selenium (Page Object) + testy API
├── rozmowa/                         ← przygotowanie do rozmowy, angielski, plan 30-60-90
├── dokumenty/                       ← CV (PDF) i portfolio (HTML)
└── .github/workflows/testy.yml      ← CI: testy API, UI i Newman
```

## Moja ścieżka

- **Kurs Tester Oprogramowania z elementami AI** (ALX, 2025 — w trakcie): przypadki testowe, raportowanie
  błędów (Jira/Bugzilla), API (Postman, REST, JSON), SQL, SDLC, Agile/Scrum, testy eksploracyjne.
- **Kurs Tester Automatyzujący:** Python, unittest, PyTest, Selenium WebDriver, Page Object, podstawy Selenium Grid.
- **Mocne strony:** dokładność, analityczne myślenie, czytelne raporty, konsekwencja, komunikatywność.
