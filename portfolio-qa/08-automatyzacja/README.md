# Automatyzacja — PyTest + Selenium (Page Object) + testy API

Od testera manualnego coraz częściej oczekuje się **wsparcia w przygotowaniu lub utrzymaniu prostych testów automatycznych**; oferty wymieniają
jako atut Selenium / Playwright / Cypress, Python i **CI/CD**. Ten projekt pokazuje, że potrafię
uruchomić, zrozumieć i rozwijać taki zestaw testów.

## Co tu jest

```
08-automatyzacja/
├── conftest.py            ← fixtures: przeglądarka (headless w CI), adresy aplikacji
├── pytest.ini             ← znaczniki: smoke, ui, api, meridian
├── requirements.txt
├── pages/                 ← Page Object Model
│   ├── base_page.py       ← wspólne metody z jawnym oczekiwaniem (WebDriverWait)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── checkout_pages.py
│   └── meridian_page.py   ← Meridian Bank (lokatory po data-testid)
└── tests/
    ├── ui/                ← SauceDemo: logowanie, sortowanie, koszyk, zakup E2E, walidacja formularza
    ├── api/               ← Restful-Booker: auth, CRUD rezerwacji, testy negatywne
    └── meridian/          ← Meridian Bank: 32 testy, w tym 13 dokumentujących znane błędy (xfail)
```

Każdy test ma w docstringu ID przypadku manualnego (np. `TC-022`, `API-09`) — **śledzenie od
przypadku manualnego do testu automatycznego**.

## Uruchomienie lokalne

```bash
cd portfolio-qa/08-automatyzacja
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest                      # wszystkie testy
pytest -m smoke             # tylko smoke
pytest -m api               # tylko API
pytest -m meridian -rxX     # Meridian Bank + podsumowanie znanych błędów
HEADLESS=0 pytest -m ui     # UI z widocznym oknem przeglądarki
pytest --html=raport.html --self-contained-html   # raport HTML
```

Selenium 4 sam pobiera sterownik przeglądarki (Selenium Manager) — wystarczy zainstalowany Chrome.

## CI/CD — GitHub Actions

Plik [`.github/workflows/testy.yml`](../../.github/workflows/testy.yml) uruchamia przy każdym pushu:
1. testy API (PyTest + requests),
2. testy UI (Selenium w trybie headless) — SauceDemo i osobno Meridian Bank,
3. kolekcję Postmana przez **Newman**,

a raporty HTML zapisuje jako artefakty. Dodatkowo co poniedziałek odpala się regresja.

## Dobre praktyki, których się trzymam

- **Page Object** — lokatory w jednym miejscu; zmiana w UI = poprawka w jednej klasie.
- **Stabilne lokatory** — atrybuty `data-test` zamiast długich XPath.
- **Jawne oczekiwanie** (`WebDriverWait`) zamiast `time.sleep()`.
- **Niezależne testy** — każdy test loguje się sam i nie zależy od kolejności.
- **Sprzątanie danych** — rezerwacje utworzone w testach API są usuwane (fixture z `yield`).
- **Znane błędy jako `xfail(strict=True)`** — pipeline zielony, a naprawa błędu od razu sygnalizuje potrzebę retestu.
- **Parametryzacja** — jeden test, wiele zestawów danych (`@pytest.mark.parametrize`).

## Utrzymanie — co robię, gdy test „czerwienieje”

1. Czytam komunikat błędu i raport — czy to błąd aplikacji, czy testu?
2. Odtwarzam scenariusz **ręcznie**. Jeśli aplikacja działa źle → zgłoszenie błędu.
3. Jeśli zmienił się UI → aktualizuję lokator w Page Object.
4. Jeśli test bywa niestabilny → sprawdzam czekanie na elementy i zależność od danych, nie dodaję `sleep`.

## Kierunek rozwoju

Playwright (Python / TypeScript) — podobne koncepcje (Page Object, lokatory, asercje), wbudowane
auto-czekanie i nagrywanie testów (`codegen`). To naturalny następny krok po Selenium.
