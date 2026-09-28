# Cykl życia defektu i proces testowy

## Cykl życia defektu (typowy workflow w Jira)

```
            ┌──────────── Rejected / Won't Fix / Duplicate ─────────┐
            │                                                        ▼
  New ──► Open ──► In Progress ──► Resolved (Fixed) ──► Retest ──► Closed
                        ▲                                  │
                        └────────────── Reopened ◄─────────┘  (retest nie przeszedł)
```

| Status | Kto | Co się dzieje |
|---|---|---|
| **New** | Tester | Zgłoszenie utworzone: kroki, wynik oczekiwany/rzeczywisty, środowisko, załączniki |
| **Open / Triaged** | PO / Lead | Potwierdzenie, nadanie priorytetu, przypisanie developera |
| **Rejected / Duplicate / Won't Fix** | PO / Dev | To nie błąd (zgodne z wymaganiem), duplikat lub świadoma decyzja o nienaprawianiu — z uzasadnieniem |
| **In Progress** | Developer | Analiza i poprawka |
| **Resolved / Ready for QA** | Developer | Poprawka wdrożona na środowisko testowe, podana wersja buildu |
| **Retest** | Tester | Odtworzenie kroków na nowej wersji + testy obszarów powiązanych (regresja) |
| **Closed** | Tester | Poprawka działa |
| **Reopened** | Tester | Błąd nadal występuje — komentarz z wersją, krokami i dowodem |

### Ważność vs priorytet

- **Ważność (severity)** — jak bardzo błąd wpływa na system (ocenia tester): Blocker, Critical, Major, Minor, Trivial.
- **Priorytet (priority)** — jak szybko trzeba naprawić (decyduje PO/biznes).
- Przykład: literówka w nazwie firmy na stronie głównej → ważność **Trivial**, priorytet **High**.
- Przykład: awaria rzadko używanego raportu dla 1 klienta → ważność **Major**, priorytet może być **Low**.

## Proces testowy (STLC) — jak pracuję w sprincie

1. **Analiza wymagań** — czytam user story i kryteria akceptacji, zadaję pytania na refinemencie
   (*luki jakościowe* wychwycone przed kodowaniem są najtańsze).
2. **Planowanie** — zakres, ryzyka, środowisko, dane testowe.
3. **Projektowanie** — scenariusze i przypadki testowe w Xray/TestRail, powiązanie z wymaganiem (traceability).
4. **Przygotowanie środowiska i danych.**
5. **Wykonanie** — testy funkcjonalne, eksploracyjne; zgłaszanie defektów.
6. **Retest i regresja** — po poprawkach; aktualizacja zestawu regresji o nowe przypadki.
7. **Zamknięcie** — raport z testów, wnioski, propozycje do automatyzacji (powtarzalne, stabilne przypadki).

## Zasady dobrego zgłoszenia

- Jeden błąd = jedno zgłoszenie.
- Tytuł odpowiada na pytanie: *co* nie działa i *gdzie*.
- Minimalne kroki potrzebne do odtworzenia.
- Fakty zamiast opinii („przycisk nie reaguje” zamiast „przycisk jest zepsuty”).
- Dowód: zrzut ekranu, nagranie, log z konsoli, request/response z zakładki Network.
- Przed zgłoszeniem: sprawdź, czy nie ma duplikatu, i czy zachowanie nie wynika z wymagania.
