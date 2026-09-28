# Przygotowanie do rozmowy — Hiberus Poland, Tester Manualny

## 1. Co wiem o firmie i roli

- **Hiberus** — firma technologiczna z Hiszpanii, 4700+ specjalistów, 14+ krajów, projekty dla klientów
  na całym świecie. Technologie: AI, Data, Cloud, Software Development, BI, Cybersecurity.
- „Więcej niż jeden projekt. Więcej niż jeden rynek.” — po zakończeniu projektu szukają kolejnego
  w ramach Hiberus, również w innych krajach → **stabilność i długoterminowa kariera**.
- **Hiberus University** — ponad 1000 osób przeszkolonych w zeszłym roku → ważne dla mnie jako juniora.
- Biuro: pl. Teatralny 1/22, Wrocław; praca hybrydowa — **2× w miesiącu w biurze**.
- Benefity: Multisport, prywatna opieka medyczna.
- **Rola:** testy manualne + rozwój w kierunku automatyzacji; zespół zwinny, codzienna współpraca
  z analitykami, developerami i biznesem; możliwość współtworzenia **standardów jakości i regresji**.

## 2. Przedstawienie się (ok. 90 sekund)

> Nazywam się Łukasz Kap. Przebranżawiam się do IT i od ponad roku systematycznie buduję warsztat testera.
> Ukończyłem kurs Tester Automatyzujący — Python, PyTest, Selenium, Page Object — a teraz kończę kurs
> „Tester oprogramowania z elementami AI” w ALX, gdzie pracuję z przypadkami testowymi, Jirą, Postmanem,
> SQL i Scrumem.
>
> Nie mam jeszcze komercyjnego doświadczenia, dlatego pod tę ofertę przygotowałem kompletny projekt na
> GitHubie: od analizy wymagań i pytań do analityka, przez 30 przypadków testowych i raporty błędów,
> po testy API, zapytania SQL i proste testy automatyczne uruchamiane w GitHub Actions.
>
> Moje mocne strony to dokładność, konsekwencja i komunikatywność — zależy mi, żeby raport błędu był
> tak jasny, że developer nie musi dopytywać. Ta rola łączy dokładnie to, co chcę robić: solidne testy
> manualne z rozwojem w automatyzacji. Dlatego bardzo mi na niej zależy.

## 3. Pytania techniczne — krótkie odpowiedzi

**Czym jest przypadek testowy, a czym scenariusz testowy?**
Scenariusz — *co* testujemy (np. „Złożenie zamówienia”). Przypadek testowy — *jak*: ID, tytuł,
warunki wstępne, kroki, dane, oczekiwany rezultat, priorytet. Jeden scenariusz = wiele przypadków.

**Co powinno zawierać zgłoszenie błędu?**
Tytuł (co i gdzie), środowisko, warunki wstępne, kroki, wynik oczekiwany i rzeczywisty, powtarzalność,
ważność/priorytet, załączniki (screen, nagranie, logi, request z Network), link do wymagania/testu.

**Opisz cykl życia defektu.**
New → Open → In Progress → Resolved → Retest → Closed; lub Reopened, gdy retest nie przechodzi;
ewentualnie Rejected / Duplicate / Won't Fix. (Szczegóły: `portfolio-qa/03-raporty-bledow/cykl-zycia-defektu.md`.)

**Ważność vs priorytet — przykład?**
Literówka w logo na stronie głównej: niska ważność, wysoki priorytet. Awaria rzadko używanego raportu:
wysoka ważność, niski priorytet.

**Testy regresyjne vs retest?**
Retest — sprawdzam, czy *konkretny* naprawiony błąd już nie występuje. Regresja — sprawdzam, czy zmiana
nie zepsuła *innych*, działających wcześniej funkcji.

**Smoke vs sanity?**
Smoke — szybkie, szerokie sprawdzenie, czy build nadaje się do testów. Sanity — wąskie sprawdzenie
konkretnej poprawki/funkcji po zmianie.

**Czym są testy eksploracyjne?**
Równoczesne uczenie się aplikacji, projektowanie i wykonywanie testów. Robię je w sesjach z kartą
testu (charter), z limitem czasu i notatkami — to nie jest „klikanie na chybił trafił”.

**Techniki projektowania testów?**
Klasy równoważności, wartości brzegowe, tablice decyzyjne, przejścia stanów, zgadywanie błędów.
Przykład: pole wiek 18–65 → wartości 17, 18, 65, 66 + klasy: poniżej, w zakresie, powyżej, nie-liczba.

**Siedem zasad testowania (ISTQB)?**
Testowanie pokazuje obecność defektów, nie ich brak · testowanie gruntowne jest niemożliwe · wczesne
testowanie oszczędza czas i pieniądze · defekty się kumulują · paradoks pestycydów (testy się „zużywają”)
· testowanie zależy od kontekstu · błędne przekonanie o braku błędów.

**Poziomy testów?** Jednostkowe (moduł), integracyjne, systemowe, akceptacyjne (UAT).

**Testy funkcjonalne vs niefunkcjonalne?**
Funkcjonalne — *co* system robi (logowanie działa). Niefunkcjonalne — *jak* (wydajność, bezpieczeństwo,
użyteczność, dostępność, kompatybilność).

**Weryfikacja vs walidacja?**
Weryfikacja — czy budujemy produkt *poprawnie* (zgodnie ze specyfikacją). Walidacja — czy budujemy
*właściwy* produkt (spełnia potrzeby użytkownika).

**Testy API — co sprawdzasz?**
Kod statusu, nagłówki, strukturę i wartości body, czas odpowiedzi, scenariusze negatywne (brak tokenu,
złe dane, nieistniejące ID), spójność danych (POST → GET → baza). Metody: GET, POST, PUT, PATCH, DELETE.

**PUT vs PATCH?** PUT — zastępuje cały zasób. PATCH — zmienia wybrane pola.

**401 vs 403?** 401 — nie wiem, kim jesteś (brak/zły token). 403 — wiem, kim jesteś, ale nie masz uprawnień.

**SQL — JOIN-y?**
INNER JOIN — tylko pasujące rekordy z obu tabel. LEFT JOIN — wszystkie z lewej + pasujące z prawej
(brak → NULL). Przydatne do szukania „sierot”: `LEFT JOIN … WHERE prawa.id IS NULL`.

**WHERE vs HAVING?** WHERE filtruje wiersze przed grupowaniem, HAVING — grupy po `GROUP BY`.

**SQL Server — jak pobrać 10 pierwszych rekordów?** `SELECT TOP (10) * FROM tabela ORDER BY …`

**Scrum — jakie znasz wydarzenia i gdzie jest tester?**
Sprint Planning, Daily, Sprint Review, Retrospektywa (+ Refinement). Tester: na refinemencie zadaje
pytania i doprecyzowuje kryteria akceptacji, w sprincie testuje historyjki na bieżąco, pilnuje
Definition of Done, na retro proponuje usprawnienia procesu jakości.

**Co to CI/CD i jakie jest miejsce testów?**
Ciągła integracja i dostarczanie — każda zmiana w kodzie automatycznie się buduje i testuje.
Automatyczne testy (smoke, API, regresja) uruchamiane w pipeline dają szybką informację zwrotną.
W moim repozytorium testy odpalają się w GitHub Actions przy każdym pushu.

**Selenium — jak radzisz sobie z niestabilnymi testami?**
Jawne czekanie (WebDriverWait) zamiast `sleep`, stabilne lokatory (`data-test`, ID), niezależne dane
testowe, analiza, czy to problem testu czy aplikacji.

**Page Object — po co?**
Oddziela lokatory i akcje strony od logiki testu; zmiana UI = zmiana w jednym miejscu.

**Jak używasz AI w pracy testera?**
Do analizy wymagań (szukanie luk i pytań), szkiców przypadków testowych i danych, porządkowania
raportów i tłumaczenia na angielski, pomocy przy SQL/asercjach. Zasady: weryfikuję każdy wynik,
nie wklejam danych poufnych, odpowiedzialność jest moja. (Przykład: `portfolio-qa/07-ai-w-qa`.)

## 4. Zadania praktyczne, które mogą paść

**„Przetestuj długopis / windę / pole logowania.”**
Zacznij od pytań o wymagania (kto używa, do czego, jakie ograniczenia), potem: funkcjonalne,
negatywne, brzegowe, użyteczność, bezpieczeństwo, wydajność, dostępność. Pokaż strukturę, nie listę
przypadkowych pomysłów.

*Pole logowania — przykładowe przypadki:* poprawne dane; błędne hasło; nieistniejący login; puste pola;
wielkość liter; spacje; bardzo długie wartości; znaki specjalne i SQL injection (`' OR 1=1 --`);
maskowanie hasła; kopiowanie hasła; blokada po X próbach; Enter zamiast kliknięcia; nawigacja
Tab; „Zapamiętaj mnie”; zachowanie po wylogowaniu i przycisku Wstecz; komunikat nie zdradza, czy login istnieje.

**„Znalazłeś błąd, developer twierdzi, że to nie błąd.”**
Sprawdzam wymaganie/kryteria akceptacji. Jeśli są niejasne — angażuję analityka/PO, żeby zdecydował.
Rozmawiam o faktach i wpływie na użytkownika, nie o tym, kto ma rację.

**„Mało czasu przed wydaniem, dużo do przetestowania.”**
Testy oparte o ryzyko: najpierw krytyczne ścieżki biznesowe i obszary zmienione, smoke, potem reszta
wg priorytetów. Jasno komunikuję, czego nie zdążyłem przetestować.

**„Nie potrafisz odtworzyć błędu zgłoszonego przez klienta.”**
Zbieram dane: środowisko, przeglądarka, konto, dokładne kroki, czas (logi). Próbuję różnych danych
i warunków. Dokumentuję próby i konsultuję z developerem logi.

## 5. Pytania behawioralne (metoda STAR: Sytuacja – Zadanie – Działanie – Rezultat)

- **Dlaczego testowanie?** Zawsze szukałem błędów w aplikacjach i grach, lubię zagadki logiczne.
  Kursy potwierdziły, że to praca, w której dokładność i dociekliwość są wartością.
- **Twoja słaba strona?** Angielski na poziomie A2. Pracuję nad nim codziennie: czytam dokumentację
  po angielsku, uczę się słownictwa QA, piszę zgłoszenia po angielsku. Dokumentację techniczną rozumiem.
- **Brak doświadczenia komercyjnego?** Dlatego zbudowałem portfolio, które odwzorowuje realny proces.
  Szybko się uczę i jestem gotowy na zadanie próbne.
- **Praca hybrydowa i dojazd?** Mieszkam w Radzyniu Podlaskim; przyjazd do Wrocławia 2× w miesiącu
  to dla mnie żaden problem, podobnie jak częstsze wizyty na początku wdrożenia.
- **Sytuacja, w której wykazałeś się dokładnością / konsekwencją** — przygotuj 1–2 przykłady
  (z kursu, pracy, życia) w formacie STAR.

## 6. Pytania, które warto zadać

1. Jak wygląda projekt, do którego trafiłaby ta osoba — domena, aplikacja web czy mobile, wielkość zespołu?
2. Ilu testerów jest w zespole i czy jest ktoś, od kogo mogę się uczyć (mentor / senior QA)?
3. Jak wygląda proces testowy — Jira + Xray czy TestRail? Jak jest zorganizowana regresja?
4. Jakie narzędzia do automatyzacji są używane w projekcie i jak wygląda ścieżka rozwoju w tym kierunku?
5. Jakie szkolenia z Hiberus University są dostępne dla testerów na start?
6. Jak wygląda onboarding w pierwszych tygodniach?
7. Po czym poznacie po 3 miesiącach, że to był dobry wybór?
8. Jakie są kolejne etapy rekrutacji?

## 7. Kwestie formalne — przygotuj odpowiedź

- **Oczekiwania finansowe** — przed rozmową sprawdź aktualne widełki w ogłoszeniu (w wynikach
  wyszukiwania pojawiała się oferta Hiberus dla juniora QA na B2B ok. 8 400–12 600 zł netto + VAT);
  podaj kwotę w widełkach i formę umowy (UoP / B2B).
- **Dostępność** — od kiedy możesz zacząć.
- **Sprzęt** — czy laptop jest zapewniany.

## 8. Checklista dzień przed rozmową

- [ ] Repozytorium otwarte w przeglądarce — umiem pokazać: przypadek testowy, raport błędu,
      kolekcję Postmana, jeden test PyTest i uruchomiony pipeline w GitHub Actions
- [ ] **Sam odtworzyłem każdy błąd z `03-raporty-bledow`** i umiem o nim opowiedzieć
- [ ] Przećwiczone przedstawienie się (PL i EN) na głos
- [ ] Kamera, mikrofon, dobre światło, cisza, naładowany telefon
- [ ] Kartka z pytaniami do rekrutera
