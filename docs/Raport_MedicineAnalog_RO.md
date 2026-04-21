# REALIZARE

În calitate de limbaj de programare a fost selectat Python. Acest limbaj îşi păstrează popularitatea în lumea programării de mulţi ani datorită sintaxei sale intuitive şi universalităţii sale. Flexibilitatea lui permite aplicarea a diverse stiluri de programare, inclusiv abordarea orientată pe obiecte, funcţională şi procedurală. Datorită ecosistemului bogat de biblioteci şi comunităţii active, Python a găsit o utilizare largă în cele mai diverse domenii: de la construirea aplicaţiilor web şi a sistemelor analitice, până la automatizarea proceselor şi dezvoltarea programelor cu elemente de învăţare automată. Datorită caracterului multi-platformă, programele scrise în Python pot fi executate pe diferite sisteme de operare fără modificări semnificative în cod.

Python se distinge prin simplitatea sintaxei şi prin claritatea acesteia, fapt ce contribuie la adaptarea rapidă a dezvoltatorilor noi şi accelerează procesul de învăţare. Tiparea sa dinamică şi gestionarea automată a memoriei fac limbajul comod pentru soluţionarea celor mai diverse sarcini – de la scripturi simple până la aplicaţii de amploare. Dezvoltatorii web apreciază Python pentru posibilitatea de a crea prototipuri şi de a implementa modificări fără cicluri îndelungate de compilare. Toate aceste calităţi fac din Python o alegere ideală pentru realizarea proiectelor cu cerinţe ce se schimbă rapid şi cu un nivel înalt de complexitate.

Pentru dezvoltarea software-ului în cadrul prezentei lucrări a fost utilizată mediul de dezvoltare PyCharm Professional. Această IDE, elaborată de compania JetBrains, oferă un set larg de funcţii pentru lucrul comod cu limbajul de programare Python. PyCharm Professional susţine autocompletarea codului, analiza erorilor în timp real şi navigarea inteligentă, ceea ce accelerează semnificativ procesul de dezvoltare. Funcţionalitatea încorporată pentru lucrul cu bazele de date permite executarea şi editarea interogărilor SQL, precum şi gestionarea structurilor de tabele direct în mediul de dezvoltare, fără necesitatea utilizării unor programe suplimentare.

Unul dintre punctele forte ale acestei medii de dezvoltare îl constituie susţinerea instrumentelor populare de programare web, inclusiv Django, Flask şi FastAPI, ceea ce lărgeşte posibilităţile la crearea logicii de server a aplicaţiilor. În plus, PyCharm oferă mijloace flexibile pentru gestionarea mediilor virtuale şi instalarea dependenţelor, permiţând lucrul cu pachetele Python direct prin interfaţa încorporată, fără a fi nevoie să configurezi manual mediul prin terminal.

PyCharm Professional posedă capacităţi încorporate pentru efectuarea testării modulare: sunt susţinute bibliotecile populare, precum pytest şi unittest, ceea ce contribuie la verificarea rapidă a corectitudinii codului. Integrarea cu sistemele de control al versiunilor, inclusiv Git, permite urmărirea comodă a modificărilor, crearea commiturilor şi lucrul în echipă asupra unui proiect. Diversitatea parametrilor de configurare disponibili permite adaptarea mediului la preferinţele şi stilul de lucru al fiecărui dezvoltator în parte.

## 3.1 Tehnologii utilizate

În prezentul subcapitol sunt analizate principalele tehnologii utilizate la dezvoltarea aplicaţiei. Sunt descrise alegerea framework-ului, a bazei de date, a instrumentelor pentru colectarea datelor de pe paginile web, precum şi pentru determinarea substanţei active a medicamentelor.

### Django

Django reprezintă un framework elaborat în Python şi orientat spre realizarea rapidă a platformelor web complete. Arhitectura sa contribuie la simplificarea dezvoltării prin reutilizarea componentelor şi printr-o structură strictă. Datorită documentaţiei detaliate şi comunităţii active, însuşirea Django devine considerabil mai simplă chiar şi pentru dezvoltatorii începători.

Unul dintre avantajele notabile ale Django îl constituie interfaţa generată automat pentru gestionarea datelor, bazată pe modelele descrise. Această parte administrativă simplifică semnificativ lucrul cu conţinutul fără a fi nevoie să se dezvolte manual interfaţa de administrare. Pe lângă aceasta, framework-ul implementează şablonul arhitectural Model-View-Template, care contribuie la delimitarea logică a componentelor aplicaţiei şi sporeşte lizibilitatea codului.

Abordarea obiect-relaţională, implementată în Django, oferă posibilitatea interacţionării cu bazele de date folosind sintaxa Python, ceea ce scuteşte dezvoltatorul de necesitatea de a scrie manual interogări SQL. Framework-ul este compatibil cu diverse sisteme de gestiune a bazelor de date, precum PostgreSQL, MySQL, SQLite şi Oracle, ceea ce asigură flexibilitate în alegerea depozitului de date în funcţie de cerinţele proiectului. În cadrul prezentei lucrări a fost aleasă baza de date SQLite, deoarece este convenabilă pentru un proiect MVP (Minimum Viable Product), nu necesită configurare suplimentară a serverului şi este inclusă în mod implicit în Django.

În Django este implementat un sistem flexibil de rutare, care permite alocarea cu uşurinţă a adreselor de cereri către manipulatorii corespunzători. Aceasta contribuie la o organizare mai logică a logicii aplicaţiei şi sporeşte lizibilitatea codului. Suplimentar, framework-ul oferă module gata pregătite pentru gestionarea utilizatorilor, inclusiv mecanisme de autentificare şi delimitare a drepturilor de acces. O atenţie deosebită în Django este acordată aspectelor de securitate: mecanismele încorporate protejează proiectul de cele mai răspândite ameninţări, precum injecţiile SQL, XSS, CSRF etc.

Django este dotat cu instrumente pentru gestionarea modificărilor în structura bazei de date – migrările, care permit urmărirea şi aplicarea modificărilor modelelor fără necesitatea de a schimba manual baza de date, ceea ce simplifică semnificativ procesul de mentenanţă a proiectului. Pentru optimizarea vitezei de răspuns şi reducerea încărcării serverului, framework-ul susţine implementarea mecanismelor de caching, inclusiv integrarea cu soluţii externe, precum Redis.

Django reprezintă o platformă susţinută activ, cu o comunitate profesională extinsă, ceea ce garantează actualizări regulate şi o dezvoltare stabilă a ecosistemului. Existenţa unui număr mare de module adiţionale permite adaptarea flexibilă a framework-ului la cele mai diverse sarcini. Datorită stabilităţii şi scalabilităţii sale, Django este aplicat cu succes în dezvoltarea celor mai variate sisteme web – de la platforme comerciale şi servicii sociale, până la portale informaţionale şi CMS-uri corporative.

### Scrapy

Scrapy este un framework open-source pentru Python, destinat colectării automatizate a datelor de pe paginile web (web scraping) şi extragerii informaţiilor structurate. Framework-ul asigură un randament înalt graţie prelucrării asincrone a cererilor, bazate pe biblioteca Twisted, ceea ce permite procesarea paralelă a mai multor pagini concomitent. Aceasta reduce semnificativ timpul necesar pentru colectarea volumelor mari de date.

Arhitectura Scrapy este construită pe conceptul de "spideri" (spiders) – clase specializate, care descriu logica navigării pe site şi extragerea datelor. Fiecare spider este un obiect autonom, responsabil de prelucrarea unui anumit resurs web. Astfel, framework-ul permite organizarea comodă a codului, separând logica colectării datelor de pe diferite surse.

Scrapy oferă un set bogat de instrumente pentru selectarea elementelor de pe pagina HTML. Sunt susţinute atât selectoarele CSS, cât şi expresiile XPath, ceea ce îi oferă dezvoltatorului flexibilitate la alegerea metodei de parsare. Selectoarele CSS se caracterizează prin sintaxa mai simplă şi mai familiară pentru dezvoltatorii web, în timp ce XPath oferă posibilităţi mai largi pentru navigarea prin arborele DOM.

Un avantaj important al Scrapy îl constituie susţinerea încorporată a diverselor formate de export al datelor, inclusiv JSON, CSV, XML. Aceasta permite salvarea rapidă a rezultatelor parsării în formatul necesar pentru prelucrarea ulterioară. În prezenta lucrare este utilizat formatul JSON, deoarece se integrează uşor cu Django şi permite păstrarea structurii ierarhice a datelor.

Framework-ul susţine, de asemenea, mecanismul pipelines, care permite prelucrarea suplimentară a datelor după extragere: curăţarea, validarea, filtrarea duplicatelor şi salvarea în baza de date. Pentru gestionarea comportamentului spider-ilor sunt disponibile middleware-uri – componente intermediare, care permit modificarea cererilor şi răspunsurilor la diferite etape ale prelucrării.

Scrapy include şi mecanisme pentru navigarea automată pe paginile site-urilor cu paginare, fapt ce este deosebit de important la colectarea datelor de pe cataloagele online. Framework-ul gestionează automat cozile de cereri, urmăreşte adresele deja vizitate şi previne ciclurile. Aceste posibilităţi fac Scrapy un instrument ideal pentru construirea sistemelor complexe de parsare.

### BeautifulSoup şi lxml

Pentru analiza suplimentară a documentelor HTML au fost utilizate bibliotecile BeautifulSoup şi lxml. BeautifulSoup oferă o interfaţă comodă, la nivel înalt, pentru parsarea HTML-ului, permiţând accesarea uşoară a elementelor prin metode simple. Biblioteca susţine diverse parsere, inclusiv lxml, ceea ce asigură viteza sporită a prelucrării.

Biblioteca lxml este o implementare rapidă şi puternică a analizei XML şi HTML pe baza bibliotecilor C libxml2 şi libxslt. Ea oferă un suport deplin al expresiilor XPath, ceea ce permite extragerea precisă a elementelor după căi xpath complexe. Combinarea BeautifulSoup şi lxml asigură un compromis optim între simplitatea utilizării şi performanţă.

### SQLite

SQLite este un sistem încorporat de gestiune a bazelor de date relaţionale, care păstrează toate datele într-un fişier unic. Spre deosebire de bazele de date la nivel de server, precum PostgreSQL sau MySQL, SQLite nu necesită pornirea unui proces de server separat, ceea ce simplifică semnificativ dezvoltarea şi distribuirea aplicaţiei. Acest aspect este îndeosebi convenabil pentru etapa MVP a proiectului.

Baza de date SQLite susţine tranzacţiile ACID, garantând integritatea datelor chiar şi în cazul opririlor de urgenţă a sistemului. SQLite se integrează eficient cu Django ORM şi este cea mai potrivită alegere pentru prezenta aplicaţie în faza de dezvoltare. În caz de necesitate, proiectul poate fi transferat uşor pe PostgreSQL sau pe o altă bază de date, prin simpla modificare a parametrilor de configurare.

### OpenAI API

Pentru determinarea inteligentă a substanţei active a medicamentului pe baza denumirii sale, proiectul utilizează integrarea cu API-ul OpenAI. Aceasta permite folosirea modelelor moderne de limbaj (Large Language Models), precum GPT-4o-mini, pentru extragerea informaţiei farmaceutice din denumirile comerciale.

Abordarea bazată pe AI oferă avantaje semnificative faţă de metodele tradiţionale: modelul poate gestiona variaţii de scriere, forme prescurtate, denumiri în limbi diferite şi poate distinge substanţa activă principală de componentele auxiliare. În cazul în care cheia API nu este configurată, sistemul foloseşte o metodă alternativă offline bazată pe expresii regulate (fallback).

## 3.2 Partea de server

Partea de server reprezintă componenta centrală a sistemului, responsabilă de prelucrarea cererilor, gestionarea datelor şi interacţiunea cu partea de client. În prezentul subcapitol vor fi analizate principalele componente ale părţii de server, inclusiv modelele de date, funcţiile de vizualizare, rutarea, panoul administrativ, comenzile de management, precum şi serviciile auxiliare.

### Modele

Modelele în Django descriu structura bazei de date şi definesc modul în care datele vor fi păstrate şi vor interacţiona. Fiecare model corespunde unui tabel din baza de date, iar câmpurile modelului reprezintă coloanele tabelului. Pentru lucrul comod cu datele sunt utilizate metodele şi funcţiile încorporate ale ORM (Object-Relational Mapping), ceea ce permite interacţionarea cu uşurinţă cu baza de date fără a scrie nicio linie de SQL.

Modelul `Medicine` reprezintă informaţia despre un medicament concret al unei farmacii concrete. Modelul include câmpuri pentru stocarea denumirii, preţului, link-ului către produs, imaginii, producătorului, farmaciei, precum şi substanţei active. Fiecare articol în baza de date reprezintă o propunere separată a unei farmacii anumite.

```python
class Medicine(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(max_length=255)
    img = models.URLField(max_length=255, blank=True, default='')
    manufacturer = models.CharField(max_length=255, blank=True, default='-')
    pharmacy = models.CharField(max_length=255)
    active_ingredient = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
```

În Django, câmpurile modelului pot fi configurate cu ajutorul a diverşi modificatori. De exemplu, `CharField` foloseşte `max_length` pentru limitarea lungimii şirului, parametrul `blank=True` indică faptul că câmpul poate fi lăsat nepopulat la formulare, iar `default` setează valoarea implicită. Câmpul `price` are tipul `DecimalField` cu parametrii `max_digits=10` şi `decimal_places=2`, ceea ce permite păstrarea preţurilor cu exactitate de două zecimale şi corespunde cel mai bine necesităţilor financiare. Câmpurile `link` şi `img` au tipul `URLField` pentru stocarea adreselor URL către pagina produsului şi imaginea lui.

Metoda `__str__` returnează reprezentarea şir a obiectului, ce este denumirea medicamentului. Aceasta este folosită în panoul de administrare Django pentru o afişare comodă a articolelor şi este utilă, de asemenea, în procesul de depanare.

Modelul `SearchQuery` este destinat pentru stocarea istoricului interogărilor de căutare. Acesta permite salvarea cererilor utilizatorilor pentru afişarea ulterioară a acestora sub formă de sugestii şi pentru îmbunătăţirea experienţei utilizatorului.

```python
class SearchQuery(models.Model):
    MODE_TITLE = "title"
    MODE_INGREDIENT = "ingredient"
    MODE_CHOICES = [
        (MODE_TITLE, "title"),
        (MODE_INGREDIENT, "ingredient"),
    ]

    query = models.CharField(max_length=255)
    query_norm = models.CharField(max_length=255, db_index=True)
    mode = models.CharField(max_length=32, choices=MODE_CHOICES,
                            default=MODE_TITLE, db_index=True)
    session_key = models.CharField(max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=["mode", "query_norm", "-created_at"]),
            models.Index(fields=["session_key", "-created_at"]),
        ]

    def __str__(self):
        return f"{self.query} ({self.mode})"
```

Câmpul `query` stochează textul original al interogării, aşa cum a fost introdus de utilizator, iar câmpul `query_norm` – forma normalizată (lowercase), care este folosită pentru căutarea rapidă şi compararea. Câmpul `mode` indică regimul de căutare – după denumire sau după substanţa activă – şi poate accepta doar valorile definite în `MODE_CHOICES`.

Câmpul `session_key` conţine identificatorul sesiunii utilizatorului, ceea ce permite afişarea istoricului personal fără a fi necesară înregistrarea utilizatorului în sistem. Câmpul `created_at` este completat automat la crearea articolului datorită parametrului `auto_now_add=True`. Clasa internă `Meta` defineşte indecşii pentru optimizarea interogărilor frecvente către baza de date: căutarea după modul şi interogarea normalizată, precum şi selectarea istoricului după sesiune cu ordonare după data creării.

### Funcţiile View

Funcţiile View sunt baza logicii de server a aplicaţiei web. Ele prelucrează cererile utilizatorilor, interacţionează cu modelele şi transmit datele către şabloane pentru afişare. Anume aici este implementată logica de business principală, inclusiv prelucrarea formularelor, filtrarea datelor, paginarea rezultatelor şi gestionarea sesiunilor.

Funcţia `home` este cea mai complexă funcţie view din aplicaţie şi îndeplineşte mai multe roluri: afişarea paginii de pornire cu statistici, procesarea interogărilor de căutare, afişarea rezultatelor filtrate după farmacie şi paginarea rezultatelor. Decoratorul `@ensure_csrf_cookie` garantează că cookie-ul CSRF va fi setat în răspuns, ceea ce este necesar pentru cererile AJAX ulterioare.

```python
@ensure_csrf_cookie
def home(request):
    query = request.GET.get("query", "")
    active_pharmacy = (request.GET.get("pharmacy") or "all").strip() or "all"
    page_number = request.GET.get("page") or "1"
    ui = get_ui_strings(get_language(request))

    analogs = []
    landing = {}
    total_count = 0
    pharmacy_tabs = []
    page_obj = None

    if query:
        medicines = (
            Medicine.objects.filter(
                Q(title__icontains=query) | Q(active_ingredient__icontains=query)
            )
            .order_by("price", "id")
        )
        total_count = medicines.count()
```

La începutul funcţiei se extrage parametrul `query` din cererea GET – textul căutat de utilizator, parametrul `pharmacy` – filtrul după farmacia aleasă, precum şi numărul paginii `page` pentru paginare. Variabila `ui` stochează dicţionarul de şiruri traduse pentru limba curentă a interfeţei.

Dacă utilizatorul a introdus o interogare, se efectuează o căutare în baza de date. Aici este folosit un obiect `Q` din Django, care permite construirea de interogări complexe cu operatorii logici `OR`. Filtrul caută potriviri atât după denumirea medicamentului (`title__icontains`), cât şi după substanţa activă (`active_ingredient__icontains`). Sufixul `__icontains` asigură căutarea insensibilă la mărimea literelor. Rezultatele sunt sortate după preţ în ordine crescătoare, ceea ce permite utilizatorului să vadă imediat cele mai ieftine oferte.

```python
if not request.session.session_key:
    request.session.create()

query_clean = query.strip()
if query_clean and active_pharmacy == "all" and str(page_number) == "1":
    SearchQuery.objects.create(
        query=query_clean,
        query_norm=query_clean.lower(),
        mode=SearchQuery.MODE_TITLE,
        session_key=request.session.session_key or "",
    )
```

Acest fragment asigură crearea unei sesiuni pentru utilizator, dacă aceasta încă nu există. Ulterior, dacă este prezentă o interogare corectă şi utilizatorul se află pe prima pagină a tab-ului "toate", interogarea este salvată în istoric. Condiţia cu numărul paginii şi cu farmacia aleasă împiedică duplicarea articolelor în istoric la navigarea pe pagini sau la comutarea filtrelor.

```python
pharmacy_stats = list(
    medicines.values("pharmacy")
    .annotate(count=Count("id"), min_price=Min("price"))
    .order_by("-count", "min_price", "pharmacy")
)

pharmacy_tabs = [
    {
        "id": "all",
        "label": ui["all_label"],
        "count": total_count,
        "is_active": active_pharmacy == "all",
    }
]
pharmacy_tabs.extend(
    {
        "id": row["pharmacy"],
        "label": row["pharmacy"],
        "count": row["count"],
        "is_active": row["pharmacy"] == active_pharmacy,
    }
    for row in pharmacy_stats
)
```

Acest cod construieşte lista tab-urilor cu farmacii pentru filtrarea rezultatelor. Metoda `values("pharmacy").annotate()` grupează medicamentele după farmacie şi calculează pentru fiecare grup numărul de oferte (`count`) şi preţul minim (`min_price`). Rezultatele sunt sortate după numărul de oferte descrescător, astfel încât farmaciile cu cele mai multe oferte să fie afişate primele. Se construieşte o listă de dicţionare, fiecare descriind un tab cu informaţii despre farmacie, numărul de oferte şi starea de activitate.

```python
active_medicines = (
    medicines if active_pharmacy == "all" else medicines.filter(pharmacy=active_pharmacy)
)
page_obj = Paginator(active_medicines, 10).get_page(page_number)
```

Dacă a fost selectată o farmacie concretă, rezultatele sunt filtrate suplimentar. Paginarea este implementată cu ajutorul clasei `Paginator` din Django, cu 10 articole per pagină. Metoda `get_page()` returnează pagina solicitată, gestionând corect valorile incorecte ale numărului paginii.

```python
ingredients = (
    medicines.exclude(active_ingredient__isnull=True)
    .exclude(active_ingredient__exact="")
    .values("active_ingredient")
    .annotate(min_price=Min("price"))
    .order_by("min_price")[:10]
)
analogs = list(ingredients)
```

Pentru lista analogilor sunt selectate primele 10 substanţe active unice cu preţurile minime ale medicamentelor ce le conţin. Metoda `exclude()` este utilizată pentru a exclude articolele cu substanţa activă goală sau null. Această abordare permite utilizatorului să treacă rapid la analoagii ieftini după substanţa activă.

Funcţia `medicine_detail` este destinată afişării paginii detaliate a medicamentului. În cadrul acesteia se construieşte compararea preţurilor după substanţa activă pe diferite farmacii, precum şi lista de analogi mai ieftini.

```python
@ensure_csrf_cookie
def medicine_detail(request, medicine_id: int):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    price_compare = []
    if medicine.active_ingredient:
        price_compare = list(
            Medicine.objects.filter(active_ingredient=medicine.active_ingredient)
            .values("pharmacy", "link")
            .annotate(min_price=Min("price"))
            .order_by("min_price")
        )

    cheap_analogs = []
    if medicine.active_ingredient:
        cheap_analogs = list(
            Medicine.objects.filter(active_ingredient=medicine.active_ingredient)
            .exclude(id=medicine.id)
            .order_by("price")[:5]
        )
```

Funcţia primeşte identificatorul medicamentului prin URL şi foloseşte `get_object_or_404` pentru a obţine obiectul din baza de date. Dacă medicamentul cu identificatorul dat nu există, este returnat automat răspunsul 404.

Pentru blocul comparării preţurilor se selectează toate medicamentele cu aceeaşi substanţă activă, grupate după farmacie, cu selectarea preţului minim. Aceasta permite utilizatorului să vadă dintr-o privire în care farmacie substanţa activă căutată este cea mai ieftină.

Pentru lista analogilor ieftini se aleg primele 5 medicamente cu aceeaşi substanţă activă, dar diferite de cel curent (este exclus medicamentul însuşi prin `exclude(id=medicine.id)`). Rezultatele sunt sortate după preţ în ordine crescătoare.

```python
if len(cheap_analogs) < 5:
    existing_ids = {medicine.id} | {analog.id for analog in cheap_analogs}
    first_word = medicine.title.split()[0] if medicine.title else ""
    if first_word and len(first_word) >= 3:
        name_matches = (
            Medicine.objects.filter(title__istartswith=first_word)
            .exclude(id__in=existing_ids)
            .order_by("price")[: 5 - len(cheap_analogs)]
        )
        cheap_analogs.extend(name_matches)
```

Dacă lista analogilor s-a obţinut mai scurtă de 5 articole (de exemplu, pentru o substanţă activă rară), se efectuează o căutare suplimentară după primul cuvânt al denumirii. Aceasta permite găsirea unor medicamente cu denumiri asemănătoare, care pot fi de fapt analogi chiar dacă substanţa activă la ele nu este completată. Verificarea lungimii primului cuvânt `len(first_word) >= 3` previne rezultatele false la cuvinte prea scurte.

Funcţia `analogs` afişează pagina cu analogi după o substanţă activă concretă. Este folosită, de exemplu, la apăsarea denumirii substanţei active pe pagina medicamentului.

```python
@ensure_csrf_cookie
def analogs(request):
    ingredient = request.GET.get("ingredient", "").strip()
    results = []

    if ingredient:
        queryset = Medicine.objects.filter(active_ingredient__iexact=ingredient)
        results = list(
            queryset.values("title", "manufacturer", "img")
            .annotate(min_price=Min("price"))
            .order_by("min_price")
        )

    return render(request, "meds/analogs.html",
                  {"ingredient": ingredient, "results": results})
```

Aici este folosită căutarea cu potrivire exactă a substanţei active (`iexact`), deoarece pagina afişează anume toţi analogii unei substanţe concrete. Rezultatele sunt grupate după denumirea medicamentului, producător şi imagine pentru a preveni duplicatele, iar preţurile minime sunt determinate prin agregarea `Min("price")`.

Funcţia `suggest` este un endpoint AJAX pentru autocompletarea la căutare. Ea returnează un JSON cu sugestii bazate pe denumirile medicamentelor şi substanţelor active, precum şi pe istoricul recent al utilizatorului.

```python
def suggest(request):
    q = (request.GET.get("q") or "").strip()

    if not q or len(q) < 2:
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key or ""
        return JsonResponse({"suggestions": _recent_search_suggestions(session_key)})

    suggestions = []

    ingredient_rows = (
        Medicine.objects.exclude(active_ingredient__isnull=True)
        .exclude(active_ingredient__exact="")
        .filter(active_ingredient__icontains=q)
        .values("active_ingredient")
        .annotate(cnt=Count("id"), min_price=Min("price"))
        .order_by("-cnt")[:6]
    )
```

La începutul funcţiei se verifică dacă interogarea este prea scurtă (mai puţin de 2 caractere) – în acest caz se returnează sugestii bazate pe istoricul recent. Altfel, se efectuează căutarea în două iteraţii: mai întâi după substanţele active, apoi după denumirile medicamentelor. Pentru fiecare sugestie se calculează numărul de rezultate potenţiale şi preţul minim, ceea ce permite afişarea unor metadate utile în interfaţă.

```python
seen = set()
deduped = []
for suggestion in suggestions:
    key = (suggestion.get("text") or "").strip().lower()
    if not key or key in seen:
        continue
    seen.add(key)
    deduped.append(suggestion)

return JsonResponse({"suggestions": deduped[:10]})
```

La final este aplicată deduplicarea, deoarece substanţa activă şi denumirea medicamentului pot coincide (de exemplu, "Paracetamol"). Setul `seen` păstrează cheile deja adăugate în formă lowercase pentru compararea insensibilă la mărimea literelor. Sunt returnate maxim 10 sugestii.

Funcţiile `delete_search_history_item` şi `clear_search_history` sunt destinate gestionării istoricului căutărilor utilizatorului. Acestea sunt accesibile numai prin metoda POST datorită decoratorului `@require_POST`, ceea ce protejează aplicaţia de operaţiunile de modificare a datelor prin cereri GET.

```python
@require_POST
def delete_search_history_item(request):
    session_key = request.session.session_key or ""
    query = (request.POST.get("query") or "").strip()

    if session_key and query:
        SearchQuery.objects.filter(
            session_key=session_key, query_norm=query.lower()
        ).delete()

    return JsonResponse({"suggestions": _recent_search_suggestions(session_key)})


@require_POST
def clear_search_history(request):
    session_key = request.session.session_key or ""

    if session_key:
        SearchQuery.objects.filter(session_key=session_key).delete()

    return JsonResponse({"suggestions": []})
```

Prima funcţie şterge un articol concret din istoricul utilizatorului, iar a doua – curăţă în întregime tot istoricul. După ştergere, este returnată lista actualizată a sugestiilor, ceea ce permite interfeţei să se actualizeze imediat fără o cerere suplimentară.

Funcţia `set_language` este responsabilă de comutarea limbii interfeţei. Ea foloseşte sesiunea şi cookie-urile pentru stocarea alegerii utilizatorului.

```python
@require_POST
def set_language(request):
    language = normalize_language((request.POST.get("language") or "").strip())
    next_url = (request.POST.get("next") or request.META.get("HTTP_REFERER") or "").strip()

    if not next_url or not url_has_allowed_host_and_scheme(
        next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure(),
    ):
        next_url = reverse("home")

    request.session["language"] = language
    response = HttpResponseRedirect(next_url)
    response.set_cookie(LANGUAGE_COOKIE_NAME, language,
                        max_age=60 * 60 * 24 * 365, samesite="Lax")
    return response
```

Funcţia `normalize_language` aduce limba primită la una dintre cele admise, ceea ce previne salvarea unor valori incorecte. Utilizarea `url_has_allowed_host_and_scheme` este un mecanism de securitate al Django, care protejează de atacurile de tipul Open Redirect – redirecţionează utilizatorul doar la URL-uri admise.

Limba este salvată atât în sesiune, cât şi într-un cookie cu durata de un an. Acest fapt asigură păstrarea alegerii chiar şi după terminarea sesiunii browserului. Parametrul `samesite="Lax"` sporeşte securitatea cookie-ului împotriva atacurilor CSRF.

### Funcţiile auxiliare

În afară de funcţiile view principale, în modul sunt prezente funcţii auxiliare pentru formatare şi paginare.

```python
def _fmt_price(value):
    if value is None:
        return ""
    return f"{float(value):.2f}"
```

Funcţia `_fmt_price` formatează preţul cu două zecimale pentru afişarea corectă în interfaţă. În cazul valorii `None`, returnează şir gol, ceea ce previne erorile la afişare.

```python
def _pagination_items(page_obj):
    total_pages = page_obj.paginator.num_pages
    current_page = page_obj.number

    if total_pages <= 7:
        return list(range(1, total_pages + 1))

    items = [1]
    start = max(2, current_page - 1)
    end = min(total_pages - 1, current_page + 1)

    if start > 2:
        items.append(None)

    items.extend(range(start, end + 1))

    if end < total_pages - 1:
        items.append(None)

    items.append(total_pages)
    return items
```

Funcţia `_pagination_items` construieşte lista elementelor de paginare cu afişarea inteligentă a elipselor (reprezentate de `None`). Dacă numărul total de pagini este 7 sau mai mic, sunt returnate toate numerele de pagină. Altfel este construită o structură de forma `[1, ..., current-1, current, current+1, ..., total]`, ceea ce face paginarea compactă şi comodă pentru utilizator.

### Rutarea

Rutarea în Django leagă URL-urile cu funcţiile de vizualizare corespunzătoare, asigurând o prelucrare corectă a cererilor utilizatorilor. Acest mecanism permite organizarea structurii aplicaţiei, făcând-o comodă pentru mentenanţă şi scalare.

În proiectul dat, URL-urile sunt împărţite între fişierul central `MedicineAnalog/urls.py` şi fişierul modulului `meds/urls.py`. Fişierul principal include URL-urile modulului meds prin funcţia `include()`, precum şi conectează panoul administrativ.

```python
# MedicineAnalog/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('meds.urls')),
]
```

Fişierul `meds/urls.py` conţine rutele concrete ale aplicaţiei. Fiecare URL este legat de o funcţie view corespunzătoare şi are un nume unic pentru apelarea inversă în şabloane şi în redirecţionări.

```python
# meds/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),
    path('analogs/', views.analogs, name='analogs'),
    path('suggest/', views.suggest, name='suggest'),
    path('search-history/delete/', views.delete_search_history_item,
         name='delete_search_history_item'),
    path('search-history/clear/', views.clear_search_history,
         name='clear_search_history'),
    path('set-language/', views.set_language, name='set_language'),
]
```

Ruta `medicine/<int:medicine_id>/` foloseşte convertorul de tip `int`, care asigură că parametrul `medicine_id` va fi transmis în funcţie ca un număr întreg, şi nu ca un şir. Aceasta simplifică validarea datelor în funcţia view şi sporeşte securitatea.

Rutele `search-history/delete/` şi `search-history/clear/` sunt endpoint-uri AJAX pentru gestionarea istoricului căutărilor. Ele funcţionează doar cu metoda POST şi returnează JSON. Ruta `set-language/` este, de asemenea, POST, deoarece modifică starea aplicaţiei.

### Panoul de administrare

Panoul administrativ al Django reprezintă o puternică interfaţă web pentru gestionarea conţinutului şi datelor. Acesta este generat automat pe baza modelelor şi oferă administratorilor comoditatea editării înregistrărilor, căutării şi filtrării datelor fără a fi nevoie să se dezvolte o interfaţă separată.

```python
from django.contrib import admin
from .models import Medicine


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'manufacturer', 'pharmacy')
    search_fields = ('title', 'manufacturer', 'pharmacy')
    list_filter = ('manufacturer', 'pharmacy')
    ordering = ('title',)
```

Decoratorul `@admin.register(Medicine)` înregistrează modelul `Medicine` în panoul administrativ şi leagă de acesta clasa de configurare `MedicineAdmin`. Atributul `list_display` defineşte care câmpuri vor fi afişate în lista de articole – denumirea, preţul, producătorul şi farmacia. Acest lucru permite administratorului să vadă dintr-o privire informaţiile cheie despre fiecare medicament.

Atributul `search_fields` activează bara de căutare în vârful listei, care va căuta după denumire, producător şi farmacie. Atributul `list_filter` adaugă un panou lateral cu filtre după producător şi farmacie, ceea ce face comodă lucrarea cu volume mari de date. Atributul `ordering` setează sortarea implicită după denumire în ordine alfabetică.

Prin intermediul panoului administrativ, administratorul poate adăuga manual medicamente, edita informaţia existentă, şterge articolele învechite şi monitoriza starea generală a bazei de date. Aceasta este deosebit de util în situaţiile în care parsarea automată nu reuşeşte să colecteze complet toate datele necesare, sau dacă sunt necesare corectări manuale.

### Comenzi de management

Framework-ul Django oferă un mecanism puternic pentru crearea propriilor comenzi de management, care pot fi rulate prin utilitarul `manage.py`. În proiect sunt implementate patru comenzi de management, responsabile de încărcarea datelor, de actualizarea şi de gestionarea lor.

Comanda `load2db` realizează încărcarea datelor din fişierele JSON, obţinute prin parsare, în baza de date Django. Ea acceptă parametrii calea către fişier, numele farmaciei şi steagurile pentru gestionarea prelucrării.

```python
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, required=True,
                            help='Calea către fișierul JSON cu date')
        parser.add_argument('--pharmacy', type=str, required=True,
                            help='Numele farmaciei')
        parser.add_argument('--manufacturer', type=bool, default=False)
        parser.add_argument('--extract-active', action='store_true',
                            help='Completează active_ingredient la încărcare '
                                 '(OpenAI dacă este configurat, altfel fallback)')

    def handle(self, *args, **kwargs):
        json_path = os.path.join(settings.BASE_DIR, kwargs['path'])
        pharmacy = kwargs['pharmacy']
        manufacturer = kwargs['manufacturer']
        extract_active = kwargs['extract_active']

        with open(json_path, 'r', encoding='utf-8') as file:
            products = json.load(file)
```

Metoda `add_arguments` defineşte argumentele liniei de comandă. Parametrii `--path` şi `--pharmacy` sunt obligatorii şi nu pot fi omise. Parametrul `--manufacturer` indică dacă fişierul JSON conţine câmpul cu producătorul (acest lucru depinde de site-ul de la care au fost colectate datele). Steagul `--extract-active` activează extragerea automată a substanţei active prin API-ul OpenAI sau prin metoda offline.

```python
if manufacturer:
    for product in products:
        active_ingredient = ""
        if extract_active:
            active_ingredient = extract_active_ingredient(product.get('title', ''))
        Medicine.objects.create(
            title=product['title'],
            price=float(product['price'].replace(',', '')),
            link=product['link'],
            img=product['img'],
            manufacturer=product['manufacturer'],
            pharmacy=pharmacy,
            active_ingredient=active_ingredient,
        )
```

Prelucrarea produselor depinde de prezenţa câmpului `manufacturer` în JSON. Metoda `Medicine.objects.create()` creează un nou articol în baza de date. Preţul este convertit din şir în număr în virgulă mobilă cu înlăturarea virgulelor (care pot fi folosite ca separatori ai miilor). În cazul steagului `--extract-active`, pentru fiecare articol este invocată funcţia `extract_active_ingredient`, care determină substanţa activă pe baza denumirii medicamentului.

Comanda `refresh_data` este o comandă combinată, care actualizează integral toate datele proiectului: rulează parserii Scrapy, curăţă tabelul în baza de date şi reîncarcă informaţia. Această comandă simplifică semnificativ procesul de actualizare a datelor.

```python
class Command(BaseCommand):
    help = "Fetch fresh data via Scrapy and load into DB."

    def add_arguments(self, parser):
        parser.add_argument("--skip-scrapy", action="store_true",
                            help="Nu porni Scrapy, doar încarcă JSON în BD")
        parser.add_argument("--extract-active", action="store_true",
                            help="Completează active_ingredient la încărcare/actualizare")

    def handle(self, *args, **kwargs):
        skip_scrapy = bool(kwargs.get("skip_scrapy"))
        extract_active = bool(kwargs.get("extract_active"))

        base_dir = str(settings.BASE_DIR)
        scraper_dir = os.path.join(base_dir, "meds_scraper")

        outputs = {
            "apteka_md": os.path.join(scraper_dir, "apteka_md.json"),
            "farmacie_md": os.path.join(scraper_dir, "farmacie_md.json"),
            "farmacia_familiei": os.path.join(scraper_dir, "farmacia_familiei.json"),
            "hippocrates": os.path.join(scraper_dir, "hippocrates.json"),
        }
```

La începutul comenzii sunt formate căile către fişierele JSON pentru fiecare spider. Dicţionarul `outputs` stabileşte corespondenţa dintre numele spider-ului şi calea către fişierul său de ieşire.

```python
if not skip_scrapy:
    for spider, out_path in outputs.items():
        self.stdout.write(f"Scraping {spider} ...")
        subprocess.run(
            ["scrapy", "crawl", spider, "-O", out_path],
            cwd=scraper_dir,
            check=True,
        )
```

Dacă steagul `--skip-scrapy` nu este activat, comanda rulează succesiv fiecare spider prin modulul `subprocess`. Steagul `-O` semnifică rescrierea fişierului de ieşire (spre deosebire de `-o`, care adaugă informaţia). Parametrul `check=True` va genera o excepţie la eroare, ceea ce împiedică continuarea lucrului cu date incorecte.

```python
mapping = [
    ("apteka_md", "AptekaMD", True),
    ("farmacie_md", "FarmacieMD", False),
    ("farmacia_familiei", "FarmaciaFamiliei", True),
    ("hippocrates", "Hippocrates", True),
]

for spider, pharmacy_name, has_manufacturer in mapping:
    json_path = outputs[spider]
    self.stdout.write(f"Reloading {pharmacy_name} from {json_path} ...")
    call_command("clear_medicines", pharmacy=pharmacy_name)
    call_command(
        "load2db",
        path=os.path.relpath(json_path, base_dir),
        pharmacy=pharmacy_name,
        manufacturer=has_manufacturer,
        extract_active=extract_active,
    )
```

Lista `mapping` conţine tripleţi: numele spider-ului, numele farmaciei şi flagul existenţei câmpului producător. Pentru fiecare farmacie sunt executate secvenţial două comenzi: `clear_medicines` pentru ştergerea înregistrărilor vechi şi `load2db` pentru încărcarea datelor noi. Funcţia `call_command` permite invocarea altor comenzi Django în mod programatic. Această abordare asigură o actualizare atomică a datelor – întâi se şterge totul, apoi se încarcă datele noi.

Comanda `clear_medicines` este o comandă simplă pentru ştergerea tuturor medicamentelor unei farmacii concrete din baza de date.

```python
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--pharmacy', type=str, required=True,
                            help='Numele farmaciei')

    def handle(self, *args, **kwargs):
        pharmacy = kwargs['pharmacy']
        count, _ = Medicine.objects.filter(pharmacy=pharmacy).delete()
        self.stdout.write(self.style.SUCCESS(
            f'Tabelul a fost curățat, au fost șterse {count} înregistrări'))
```

Metoda `delete()` a QuerySet-ului returnează un tuple: numărul total de articole şterse şi un dicţionar cu numărul şterselor pe fiecare model. Numărul total este afişat în consolă cu formatare succes, ceea ce oferă feedback util pentru utilizator.

Comanda `fill_active_ingredients` este destinată completării ulterioare (backfill) a substanţei active pentru medicamentele existente. Aceasta este utilă dacă datele iniţial nu au fost încărcate cu `--extract-active`, sau dacă a fost obţinută o cheie API OpenAI şi este necesar de a reprelucra articolele existente.

```python
class Command(BaseCommand):
    help = "Backfill active_ingredient for medicines."

    def add_arguments(self, parser):
        parser.add_argument("--pharmacy", type=str, required=False,
                            help="Filtru după farmacie (opțional)")
        parser.add_argument("--overwrite", action="store_true",
                            help="Rescrie active_ingredient chiar dacă este deja completat")
        parser.add_argument("--limit", type=int, default=0,
                            help="Limitează numărul de actualizări (0 = fără limită)")

    def handle(self, *args, **kwargs):
        pharmacy = kwargs.get("pharmacy")
        overwrite = bool(kwargs.get("overwrite"))
        limit = int(kwargs.get("limit") or 0)

        qs = Medicine.objects.all().order_by("id")
        if pharmacy:
            qs = qs.filter(pharmacy=pharmacy)

        updated = 0
        for med in qs.iterator(chunk_size=200):
            if med.active_ingredient and not overwrite:
                continue
            med.active_ingredient = extract_active_ingredient(med.title)
            med.save(update_fields=["active_ingredient"])
            updated += 1
            if limit and updated >= limit:
                break

        self.stdout.write(self.style.SUCCESS(f"Updated {updated} medicines"))
```

Comanda este construită astfel încât să fie maximal eficientă faţă de memorie. Metoda `iterator(chunk_size=200)` încarcă articolele în porţii de 200 de bucăţi, ceea ce evită încărcarea întregului tabel în memorie la un moment dat – lucru important pentru baze de date mari. Parametrul `update_fields=["active_ingredient"]` la apelul `save()` face ca Django să genereze un SQL UPDATE doar pentru un singur câmp, ceea ce accelerează operaţiunea şi reduce încărcarea pe baza de date.

Parametrul `--overwrite` permite rescrierea valorilor deja existente ale substanţei active – acesta este util dacă anterior a fost folosit un fallback, iar acum este disponibilă o cheie API mai precisă. Parametrul `--limit` limitează numărul de actualizări, ceea ce este convenabil pentru testarea pe un volum mic de date sau pentru gestionarea cheltuielilor pentru API-ul OpenAI.

### Serviciul de extragere a substanţei active

Modulul `services.py` conţine logica de extragere a substanţei active pe baza denumirii medicamentului. Implementarea foloseşte o abordare hibridă: dacă cheia API OpenAI este configurată, apelează modelul de limbaj, altfel se execută algoritmul offline bazat pe expresii regulate.

```python
_DOSAGE_RE = re.compile(
    r"(?i)\b(\d+([.,]\d+)?\s?(mg|g|mcg|\u00b5g|ui|iu|ml|l))\b"
)
_FORM_WORDS_RE = re.compile(
    r"(?i)\b(comprimat\w*|capsul\w*|sirop\w*|pulber\w*|solu[tț]i\w*|"
    r"spray\w*|unguent\w*|crem\w*|gel\w*|fiol\w*|plic|pic[ăa]tur\w*|"
    r"suspens\w*|supozit\w*|ovul\w*|emulsi\w*|past\w*|drajeu\w*)\b"
)
_PACK_RE = re.compile(r"(?i)\b(n\d+|nr\.?\s?\d+|\d+\s?buc\.?|\d+\s?x|x\s?\d+)\b")
```

La începutul modulului sunt definite trei expresii regulate, compilate pentru a spori performanţa: `_DOSAGE_RE` pentru identificarea dozajelor (de exemplu, "500 mg", "2,5 mcg", "100 ui"), `_FORM_WORDS_RE` pentru formele farmaceutice în limba română (comprimate, capsule, sirop, pulbere, soluție, unguent, cremă, gel, fiole, plic, picături, suspensie, supozitoare, ovule, emulsie, pastă, drajeuri) şi `_PACK_RE` pentru ambalaj (N20, nr. 30, 10 buc., 2x etc.). Steagul `(?i)` asigură insensibilitatea la mărimea literelor, iar barierele de cuvinte `\b` previn potrivirile parţiale. Terminaţia `\w*` permite potrivirea cu diferite forme gramaticale ale cuvintelor (de exemplu, `comprimat\w*` se potriveşte cu "comprimat", "comprimate", "comprimatelor"). Claselor de caractere `[tț]` şi `[ăa]` permit potrivirea cu variantele cu şi fără diacritice, deoarece în denumirile medicamentelor diacriticele pot fi omise.

```python
def _fallback_extract_active_ingredient(title: str) -> str:
    """
    Heuristic fallback: strip dosage/form/pack tokens, keep first 1-3 words.
    """
    if not title:
        return ""

    s = title.strip()
    s = _DOSAGE_RE.sub(" ", s)
    s = _FORM_WORDS_RE.sub(" ", s)
    s = _PACK_RE.sub(" ", s)
    s = re.sub(r"[(){}\[\];:,/\\|+*<>=\"'`~]", " ", s)
    s = re.sub(r"\s+", " ", s).strip().lower()

    if not s:
        return ""

    parts = s.split(" ")
    return " ".join(parts[:3]).strip()
```

Funcţia de fallback lucrează pe principiul "curăţă şi scurtează". Mai întâi din denumire sunt înlăturate dozajele, formele dozate, ambalajele şi semnele de punctuaţie. Apoi sunt normalizate spaţiile consecutive şi este aplicat lowercase. În cele din urmă, sunt preluate primele 3 cuvinte, deoarece denumirea substanţei active, de regulă, constă din 1 până la 3 cuvinte (de exemplu, "acid ascorbic", "paracetamol", "diclofenac sodiu"). Această metodă nu este ideală, dar funcţionează rezonabil pentru majoritatea cazurilor tipice.

```python
def extract_active_ingredient(title: str) -> str:
    """
    Best-effort extraction. If OPENAI_API_KEY is configured, uses OpenAI to extract
    the active ingredient; otherwise falls back to a heuristic extractor.
    """
    api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return _fallback_extract_active_ingredient(title)

    try:
        from openai import OpenAI
    except Exception:
        return _fallback_extract_active_ingredient(title)

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Ești un asistent farmaceutic. "
                        "Extrage substanța activă din denumirea medicamentului. "
                        "Răspunde doar cu substanța activă, fără explicații."
                    ),
                },
                {"role": "user", "content": title},
            ],
        )
        content = (response.choices[0].message.content or "").strip().lower()
        return content
    except Exception:
        return _fallback_extract_active_ingredient(title)
```

Funcţia principală `extract_active_ingredient` implementează strategia "graceful degradation": la orice eroare se trece la metoda offline. Prima verificare – existenţa cheii API în variabilele mediului. Dacă cheia nu este setată, se revine imediat la fallback.

A doua verificare – importul bibliotecii OpenAI. Dacă biblioteca nu este instalată sau este ruptă, funcţia, de asemenea, va reveni la fallback. Aceasta face sistemul robust la problemele de configurare a mediului.

În cazul în care toate verificările sunt trecute, se creează un client OpenAI şi se efectuează o cerere la modelul `gpt-4o-mini` (sau la alt model indicat prin variabila de mediu `OPENAI_MODEL`). Parametrul `temperature=0` reduce la minimum caracterul aleator în răspuns, ceea ce este important pentru extragerea consistentă a aceloraşi valori pentru aceleaşi denumiri. Mesajul de sistem este formulat în limba română şi indică clar modelului rolul său ("asistent farmaceutic") şi formatul aşteptat al răspunsului – doar substanţa activă, fără explicaţii. Această formulare concisă limitează răspunsul modelului doar la datele necesare, ceea ce economiseşte resursele (token-urile) şi simplifică prelucrarea ulterioară a rezultatului.

Răspunsul este normalizat: sunt înlăturate spaţiile şi este adus la lowercase. Orice erori la apelul la API (problemele de reţea, limitele, eşecurile serverului) sunt capturate, iar funcţia revine la metoda offline, garantând astfel ca sistemul să-şi păstreze funcţionalitatea.

### Internaţionalizarea

Aplicaţia susţine trei limbi ale interfeţei: română (implicită), engleză şi rusă. Spre deosebire de mecanismul încorporat de traduceri al Django cu fişierele `.po`, în prezentul proiect este folosită o abordare mai simplă – un dicţionar de traduceri în codul Python.

```python
# meds/i18n.py
DEFAULT_LANGUAGE = "ro"
LANGUAGE_COOKIE_NAME = "ma_language"
LANGUAGE_OPTIONS = (
    ("ro", "Română"),
    ("en", "English"),
    ("ru", "Русский"),
)

TRANSLATIONS = {
    "ro": {
        "home_page_title": "Căutare medicamente",
        "search_placeholder": "Introdu numele medicamentului...",
        "search_button": "Caută",
        # ... alte şiruri
    },
    "ru": {
        "home_page_title": "Поиск лекарств",
        "search_placeholder": "Введите название лекарства...",
        # ...
    },
    "en": {
        "home_page_title": "Search Medicines",
        "search_placeholder": "Enter the medicine name...",
        # ...
    },
}
```

Constanta `DEFAULT_LANGUAGE` defineşte limba implicită (română), iar `LANGUAGE_COOKIE_NAME` – numele cookie-ului pentru păstrarea alegerii utilizatorului. Tuple-ul `LANGUAGE_OPTIONS` conţine codurile şi denumirile locale ale limbilor pentru afişarea lor în interfaţă.

```python
def normalize_language(language):
    supported = {code for code, _ in LANGUAGE_OPTIONS}
    return language if language in supported else DEFAULT_LANGUAGE


def get_language(request):
    session_language = getattr(getattr(request, "session", None),
                               "get", lambda *_: None)("language")
    cookie_language = getattr(request, "COOKIES", {}).get(LANGUAGE_COOKIE_NAME)
    return normalize_language(
        session_language or cookie_language or DEFAULT_LANGUAGE
    )


def get_ui_strings(language):
    return TRANSLATIONS[normalize_language(language)]
```

Funcţia `normalize_language` asigură că va fi returnat doar un cod de limbă susţinut, prevenind erorile la intrarea datelor incorecte. Funcţia `get_language` stabileşte limba curentă după următoarea ierarhie de priorităţi: întâi se verifică sesiunea, apoi cookie-ul şi, la final, se foloseşte limba implicită. Aceasta permite păstrarea alegerii utilizatorului atât în cadrul sesiunii curente, cât şi între sesiuni.

Funcţia `get_ui_strings` returnează dicţionarul cu şirurile traduse pentru limba indicată. Pentru integrarea cu şabloanele Django este folosit un context processor:

```python
# meds/context_processors.py
from .i18n import LANGUAGE_OPTIONS, get_language, get_ui_strings


def ui_i18n(request):
    current_language = get_language(request)
    language_options = [
        {"code": code, "label": label} for code, label in LANGUAGE_OPTIONS
    ]
    current_language_label = next(
        (opt["label"] for opt in language_options if opt["code"] == current_language),
        current_language.upper(),
    )

    return {
        "current_language": current_language,
        "current_language_label": current_language_label,
        "language_options": language_options,
        "ui": get_ui_strings(current_language),
    }
```

Context processor-ul adaugă automat în contextul fiecărui şablon variabila `ui` cu şirurile traduse, precum şi informaţia despre limba curentă. Aceasta permite utilizarea în şabloane a unor construcţii de tipul `{{ ui.search_button }}`, ceea ce face codul mai lizibil şi comod pentru mentenanţă.

## 3.3 Modulul de colectare a datelor

Pentru completarea bazei de date cu medicamente, în proiect este elaborat un modul separat pentru web scraping, bazat pe framework-ul Scrapy. Modulul se găseşte în directorul `meds_scraper/` şi reprezintă un proiect autonom Scrapy cu patru spideri pentru diferite farmacii online ale Moldovei.

### Structura proiectului Scrapy

Structura tipică a proiectului Scrapy include mai multe fişiere şi directoare cu o destinaţie strictă. Fişierul `settings.py` conţine setările globale ale framework-ului, `items.py` – clasele pentru date structurate, `pipelines.py` – pipeline-urile pentru prelucrarea elementelor, iar directorul `spiders/` – codul spider-ilor înşişi.

```python
# meds_scraper/meds_scraper/settings.py
BOT_NAME = "meds_scraper"

SPIDER_MODULES = ["meds_scraper.spiders"]
NEWSPIDER_MODULE = "meds_scraper.spiders"

ROBOTSTXT_OBEY = False

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
```

Parametrul `BOT_NAME` defineşte numele botului, care va fi folosit în header-ul User-Agent. Listele `SPIDER_MODULES` şi `NEWSPIDER_MODULE` indică Scrapy unde să caute spiderii. Parametrul `ROBOTSTXT_OBEY = False` este setat pentru dezactivarea verificării automate a robots.txt – aceasta este necesar, deoarece unele site-uri interzic complet parsarea chiar şi pentru datele publice, în timp ce noi ne asumăm responsabilitatea pentru respectarea limitelor rezonabile.

Setarea `TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"` activează utilizarea reactorului asincron modern, care îmbunătăţeşte performanţa. `FEED_EXPORT_ENCODING = "utf-8"` asigură salvarea corectă a caracterelor Unicode în fişierele JSON, ceea ce este important pentru datele în română, rusă şi alte limbi.

### Spider-ul apteka_md

Spider-ul pentru site-ul apteka.md este cel mai complex dintre cei patru din proiect, deoarece site-ul foloseşte clase CSS dinamice în stilul Tailwind, ceea ce cere selectoare mai complicate. Codul spider-ului demonstrează lucrul cu mai multe URL-uri de start, extragerea datelor prin combinaţia CSS şi XPath, precum şi gestionarea paginării.

```python
import scrapy


class AptekaMdSpider(scrapy.Spider):
    name = "apteka_md"

    def start_requests(self):
        urls = [
            'https://www.apteka.md/category/vitamine',
            'https://www.apteka.md/category/plante-medicinale',
            'https://www.apteka.md/category/produse-igienice',
            'https://www.apteka.md/category/tehnica-medicala',
            'https://www.apteka.md/category/mama-si-copilul',
            'https://www.apteka.md/category/produse-ortopedice',
            'https://www.apteka.md/category/cosmetica',
            'https://www.apteka.md/category/medicamente',
            'https://www.apteka.md/category/nursing-ingrijirea-bolnavilor',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
```

Atributul `name` defineşte numele unic al spider-ului, după care acesta va fi invocat prin comanda `scrapy crawl apteka_md`. Metoda `start_requests` este punctul de pornire al spider-ului – ea generează cererile iniţiale pentru fiecare categorie a site-ului. Folosirea a mai multor URL-uri de start permite acoperirea completă a catalogului farmaciei.

Operatorul `yield` creează un generator, ceea ce este convenabil pentru lucrul cu volume mari de date – Scrapy primeşte cererile pe măsură ce devin disponibile, fără a aştepta crearea tuturor în memorie. Parametrul `callback=self.parse` indică care metodă va prelucra răspunsul serverului.

```python
def parse(self, response):
    product_table = response.css(
        "div[class*='mt-6 mb-10 grid gap-x-6 gap-y-10 grid-cols-1 "
        "lg:grid-cols-2 xl:grid-cols-4']")
    for product in product_table.css("a"):
        title = product.xpath(
            ".//div[contains(@class, 'line-clamp-3') "
            "and contains(@class, 'font-semibold')]/text()").get()
        try:
            price = product.xpath(
                ".//div[contains(@class, 'text-xl') "
                "and contains(@class, 'font-semibold')]/text()"
            ).get().replace("Lei", "").strip()
        except:
            price = None

        link = "https://www.apteka.md/" + product.css("a").attrib["href"]
        img = product.css("img::attr(src)").get()
        manufacturer = product.xpath(
            ".//div[contains(@class, 'text-xs') "
            "and contains(@class, 'font-normal')]/text()").get()

        yield {
            "title": title,
            "price": price,
            "link": link,
            "img": img,
            "manufacturer": manufacturer,
        }
```

Metoda `parse` prelucrează HTML-ul paginii categoriei. Mai întâi se selectează containerul cu produsele prin atributul `class*=`, care caută un substring în clasă. Această abordare este mai stabilă la modificările minore din clasele Tailwind.

Pentru fiecare produs sunt folosite expresii XPath cu operatorul `contains()` în loc de selectoare CSS stricte. Aceasta permite găsirea elementelor chiar şi atunci când pe ele sunt specificate clase suplimentare. Metoda `.get()` returnează prima potrivire sau `None`, dacă nu există rezultate.

Preţul este curăţat de textul "Lei" şi de spaţii. Construcţia `try/except` protejează de erorile în cazul în care produsul nu are preţ (este în afara stocului). Operatorul `yield` returnează un dicţionar, care va fi salvat în fişierul JSON de ieşire.

```python
next_page = response.css("a[aria-label='Go to next page']::attr(href)").get()
page_param = '?page='
if next_page:
    if page_param in response.url:
        link_parts = response.url.split(page_param)
        next_page = link_parts[0] + next_page
    else:
        next_page = response.url + next_page

    yield scrapy.Request(url=next_page, callback=self.parse)
```

Logica paginării este construită pe căutarea link-ului către pagina următoare după atributul `aria-label`, care este un atribut de accesibilitate standard. Dacă link-ul a fost găsit, este format URL-ul absolut al paginii următoare. Verificarea prezenţei `?page=` în URL-ul curent este necesară pentru a preveni duplicarea parametrului la navigarea prin pagini. Scrapy va continua procesul recursiv, prelucrând toate paginile categoriei.

### Spider-ul farmacie_md

Spider-ul pentru site-ul farmacie.md are o logică mai simplă datorită claselor CSS stabile, dar conţine o optimizare importantă pentru economisirea timpului de parsare.

```python
import scrapy


class MedsSpider(scrapy.Spider):
    name = "farmacie_md"

    def start_requests(self):
        urls = [
            'https://farmacie.md/ro/cosmetica',
            'https://farmacie.md/ro/mama-si-copilul',
            'https://farmacie.md/ro/raceala-si-gripa',
            'https://farmacie.md/ro/antineoplazice-si-imunomodulatoare',
            'https://farmacie.md/ro/aparatul-respirator',
            'https://farmacie.md/ro/digestie-si-metabolism',
            'https://farmacie.md/ro/sistemul-nervos-central',
            'https://farmacie.md/ro/sistemul-cardiovascular',
            'https://farmacie.md/ro/preparate-dermatologice',
            'https://farmacie.md/ro/sistemul-musculo-scheletic',
            # ... alte categorii
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
```

Lista URL-urilor de start acoperă toate categoriile principale ale farmaciei: de la cosmetică şi produse pentru mame, până la medicamente specializate pentru sistemul nervos central şi sistemul cardiovascular. Aceasta asigură o acoperire maximă a gamei de produse a farmaciei.

```python
def parse(self, response):
    for product in response.css('div.product-cart__inner'):
        lei = product.css("span.product-cart__price-new--lei::text").get()
        if lei:
            ban = product.css("span.product-cart__price-new--ban::text").get()
            price = lei + "." + ban
        else:
            return

        """
        - un produs fără preț înseamnă că nu este în stoc
        - produsele sunt sortate astfel încât mai întâi apar cele în stoc, apoi cele fără stoc
        - dacă încep produsele fără stoc, putem întrerupe parsarea
        - acest lucru economisește timp și evită munca inutilă
        """

        yield {
            "title": product.css("h3.product-cart__title::text").get().strip(),
            "price": price,
            "link": "https://farmacie.md" + product.css(
                "a.product-cart__image").attrib['href'],
            "img": product.css(
                "a.product-cart__image img::attr(src)").get(),
        }
```

Aici este demonstrat un detaliu interesant al site-ului farmacie.md – preţul este despărţit în două elemente separate: leii întregi (`--lei`) şi bani (`--ban`). Codul combină aceste părţi într-un număr zecimal, folosind punctul ca separator.

Un element cheie important este condiţia `if lei: ... else: return`. Pe site-ul farmacie.md, produsele cu preţ sunt afişate înaintea celor fără preţ (adică fără stoc). De îndată ce spider-ul întâlneşte primul produs fără preţ, el execută `return`, întrerupând parsarea paginii curente. Aceasta este o optimizare semnificativă, care reduce timpul de parsare şi volumul datelor colectate, deoarece produsele fără stoc nu sunt relevante pentru utilizatori.

```python
page_param = '?page='
if page_param in response.url:
    link_parts = response.url.split(page_param)
    current_page = int(link_parts[-1])
    next_page = link_parts[0] + page_param + str(current_page + 1)
else:
    next_page = response.url + page_param + '2'

yield response.follow(next_page, callback=self.parse)
```

Paginarea este realizată prin incrementarea explicită a numărului paginii. Spre deosebire de apteka_md, aici nu se caută link-ul "Pagina următoare" – în schimb se adună 1 la numărul paginii curente. Metoda `response.follow()` este o prescurtare pentru crearea cererii absolute din link-ul relativ. Condiţia de oprire este implicită: dacă pagina nu conţine produse, metoda `parse` se va termina fără generare de cereri noi.

### Spider-ul farmacia_familiei

Spider-ul pentru site-ul ff.md (Farmacia Familiei) demonstrează lucrul cu date structurate încorporate în pagină, inclusiv atribute cu JSON. De asemenea, aici este implementat filtrul după disponibilitatea în stoc.

```python
import scrapy
import json


class FarmaciaFamilieiSpider(scrapy.Spider):
    name = "farmacia_familiei"

    def start_requests(self):
        urls = [
            'https://ff.md/collections/sanatate',
            'https://ff.md/collections/vitamine-si-minerale',
            'https://ff.md/collections/cuplu-si-sex',
            'https://ff.md/collections/frumusete-si-igiena',
            'https://ff.md/collections/dermatocosmetica',
            'https://ff.md/collections/mama-si-copilul',
            'https://ff.md/collections/optica',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
```

Importul `json` este necesar pentru parsarea datelor structurate de pe pagină. URL-urile de start acoperă principalele colecţii ale farmaciei.

```python
def parse(self, response):
    product_list = response.css(
        "div.product-list.product-list--collection.product-list--with-sidebar")

    for product in product_list.css(
            "div[class*='product-item product-item--vertical']"):
        in_stock = product.css(
            "span[class='product-item__inventory inventory "
            "inventory--high']::text").get() == "Disponibil"
        if not in_stock:
            continue
        title = product.css(
            "a[class='product-item__title text--strong link']::text").get()
        link = 'https://ff.md' + product.css(
            "a[class='product-item__title text--strong link']::attr(href)").get()
        price = product.css(
            "span[class*='price']::text").get().replace(' MDL', '')
        manufacturer = product.css(
            "a[class='product-item__vendor link']::text").get()
```

Filtrarea după disponibilitate este realizată prin verificarea textului în spanul indicatorului de stoc. Dacă textul nu este egal cu "Disponibil", produsul este sărit prin `continue`. Aceasta permite includerea în JSON doar a produselor realmente disponibile pentru cumpărare, ceea ce sporeşte calitatea datelor.

```python
widths = product.css("img::attr(data-widths)").get()
if widths:
    width = json.loads(widths)[-1]
    img = 'https:' + product.css(
        "img::attr(data-src)").get().replace('{width}', str(width))
else:
    img = 'https://ff.md/cdn/shop/files/105202_600x.webp?v=1734088438'

yield {
    "title": title,
    "price": price,
    "link": link,
    "img": img,
    "manufacturer": manufacturer,
}
```

Aici este demonstrată prelucrarea imaginilor responsive. Site-ul foloseşte atributul `data-widths` cu un array JSON al lăţimilor disponibile (de exemplu, `[150, 300, 600, 1200]`). Codul alege valoarea maximă `[-1]` – cea mai mare rezoluţie disponibilă – şi o inserează în şablonul URL-ului care conţine placeholder-ul `{width}`. Dacă atributul `data-widths` nu este găsit, se utilizează o imagine placeholder implicită. Această abordare asigură calitate înaltă a imaginilor medicamentelor în baza de date.

```python
next_page = response.css("a[class='pagination__next link']::attr(href)").get()

if next_page:
    next_page = 'https://ff.md' + next_page
    yield scrapy.Request(next_page, callback=self.parse)
else:
    return
```

Paginarea pe ff.md foloseşte link-uri explicite "Pagina următoare" cu clasa `pagination__next`. Dacă link-ul este găsit, spider-ul creează o cerere nouă şi continuă parsarea. Returul `return` explicit nu este strict necesar aici, dar face logica mai transparentă.

### Spider-ul hippocrates

Spider-ul pentru site-ul hippocrates.md este cel mai compact dintre patru, deoarece site-ul are o structură HTML relativ simplă şi stabilă. Spider-ul foloseşte parametrul URL `show_by=60` pentru afişarea a 60 de produse pe pagină, reducând astfel numărul de cereri.

```python
import scrapy


class HippocratesSpider(scrapy.Spider):
    name = "hippocrates"

    def start_requests(self):
        urls = [
            'https://hippocrates.md/ro/catalog/medicamente?show_by=60',
            'https://hippocrates.md/ro/catalog/mama_si_copilul?show_by=60',
            'https://hippocrates.md/ro/catalog/cosmetica_si_igiena?show_by=60',
            'https://hippocrates.md/ro/catalog/vitamine_si_suplimente?show_by=60',
            'https://hippocrates.md/ro/catalog/echipament_medical?show_by=60',
            'https://hippocrates.md/ro/catalog/cuplu_si_sex?show_by=60',
            'https://hippocrates.md/ro/catalog/produse_non-medicale?show_by=60',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        product_table = response.css(
            "div.result-search__content.content-result-search")
        for product in product_table.css(
                "div.content-result-search__item.item-product"):
            price = product.css("div.item-product__price span::text").get()
            # dacă nu există preț, produsul nu este în stoc, se sare iterația
            if not price:
                continue
            title = product.css("a[class='item-product__name']::text").get()
            link = 'https://hippocrates.md/' + product.css(
                "a[class='item-product__name']::attr(href)").get()
            img = 'https://hippocrates.md/' + product.css("img::attr(src)").get()
            manufacturer = product.css("p.item-product__brand::text").get()

            yield {
                "title": title,
                "price": price,
                "link": link,
                "img": img,
                "manufacturer": manufacturer,
            }
        next_page = response.xpath(
            '//div[@class="pagging__arrow"]/a[span[text()="Înainte"]]/@href').get()
        if next_page:
            next_page = 'https://hippocrates.md' + next_page
            yield scrapy.Request(next_page, callback=self.parse)
```

Verificarea `if not price: continue` filtrează produsele fără preţ, care, de regulă, înseamnă absenţa în stoc. O trăsătură interesantă este XPath pentru pagina următoare – se caută anume link-ul, al cărui nod-copil `span` conţine textul "Înainte" (textul butonului paginării pe versiunea română a site-ului). Construcţia `a[span[text()="Înainte"]]` îi permite lui XPath să filtreze link-urile după textul copilului lor, ceea ce este imposibil în selectoarele CSS standard.

Concatenarea rutelor printr-o bară oblică (`/`) este caracteristică pentru acest site, deoarece linkurile relative nu încep cu `/`. Aceasta diferenţiază spider-ul hippocrates de alţi spideri din proiect.

### Integrarea Scrapy cu Django

Una dintre trăsăturile importante ale proiectului este integrarea dintre Scrapy şi Django. Scrapy este rulat ca un subproces separat din comanda Django `refresh_data`, iar apoi JSON-urile obţinute sunt încărcate în baza de date prin comanda `load2db`. Această abordare are mai multe avantaje:

În primul rând, Scrapy şi Django au cicluri de viaţă diferite şi funcţionează mai eficient ca procese separate. Scrapy foloseşte Twisted pentru I/O asincron, în timp ce Django este orientat pe cererile HTTP sincronice. Încercarea integrării lor într-un proces ar crea probleme cu event loop.

În al doilea rând, formatul JSON intermediar permite depanarea uşoară – dacă parsarea a decurs nereuşit, se poate studia JSON-ul înainte de a încărca în baza de date. De asemenea, JSON-urile pot fi salvate ca backup-uri sau folosite pentru testarea comenzii `load2db` separat.

În al treilea rând, o astfel de arhitectură simplifică scalarea: în viitor, spideri pot fi rulaţi pe un server separat prin Scrapyd, iar JSON-urile pot fi transmise la serverul Django prin reţea sau prin sistemul de fişiere partajat.

## 3.4 Testarea

Testarea reprezintă o parte integrantă a procesului de dezvoltare software. Ea permite identificarea erorilor, verificarea corespondenţei sistemului cu cerinţele prestabilite şi asigurarea funcţionării stabile a acestuia. Această etapă este esenţială pentru îmbunătăţirea calităţii produsului şi a experienţei utilizatorului.

În prezentul proiect este utilizată abordarea testării automate bazate pe Django TestCase. Testele automate acoperă scenariile principale de lucru cu modelele, funcţiile view şi endpoint-urile API, verifică corectitudinea creării, salvării şi afişării datelor, precum şi prelucrarea erorilor şi a cazurilor limită. Automatizarea a permis accelerarea verificării funcţionalităţii şi asigurarea repetabilităţii testelor fără participarea omului.

Clasa `SearchViewsTestCase` moşteneşte de la `TestCase` din Django şi este destinată verificării funcţionalităţii principale de căutare şi a funcţiilor auxiliare. Django TestCase încapsulează fiecare test într-o tranzacţie a bazei de date, care este anulată după efectuarea testului. Aceasta asigură izolarea testelor – modificările făcute în cadrul unui test, nu influenţează alte teste.

```python
from decimal import Decimal

from django.test import Client, TestCase
from django.urls import reverse

from .models import Medicine, SearchQuery


class SearchViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.primary_medicine = Medicine.objects.create(
            title="Nurofen Forte",
            active_ingredient="Ibuprofen",
            price=Decimal("45.50"),
            link="https://example.com/nurofen",
            img="https://example.com/nurofen.png",
            manufacturer="Reckitt",
            pharmacy="Farmacia 1",
        )
        Medicine.objects.create(
            title="Ibuprofen Bios",
            active_ingredient="Ibuprofen",
            price=Decimal("22.10"),
            link="https://example.com/ibuprofen-bios",
            img="https://example.com/ibuprofen-bios.png",
            manufacturer="Bios",
            pharmacy="Farmacia 2",
        )
        cls.no_image_medicine = Medicine.objects.create(
            title="Paracetamol 500mg comp.",
            active_ingredient="Paracetamol",
            price=Decimal("8.35"),
            link="https://example.com/paracetamol",
            img="",
            manufacturer="Eurofarmaco SA",
            pharmacy="FarmaciaFamiliei",
        )
```

Metoda `setUpTestData` este invocată o singură dată pentru toată clasa de teste (înainte de toate metodele de test). Decoratorul `@classmethod` indică că metoda lucrează cu clasa, nu cu instanţa. Aceasta este o optimizare importantă a performanţei: în loc să se creeze date de test înainte de fiecare test (aşa cum s-ar fi întâmplat la `setUp`), datele sunt create o singură dată şi sunt reutilizate. Django se ocupă de izolare la nivelul tranzacţiilor bazei de date.

Sunt create trei medicamente de test cu caracteristici diferite: două cu substanţa activă Ibuprofen în farmacii diferite (pentru testarea grupării după farmacii) şi unul cu un câmp gol al imaginii (pentru testarea placeholder-ului). Pentru preţuri este utilizat tipul `Decimal`, pentru a evita erorile de exactitate a calculelor în virgulă mobilă.

Testul `test_home_search_matches_title_and_active_ingredient` verifică funcţia cheie – căutarea care găseşte medicamente atât după denumire, cât şi după substanţa activă. Acesta este scenariul principal pentru utilizator.

```python
def test_home_search_matches_title_and_active_ingredient(self):
    response = self.client.get(reverse("home"), {"query": "ibuprofen"})

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["total_count"], 2)
    self.assertContains(response, 'class="search-clear"')

    titles = {medicine.title for medicine in response.context["page_obj"].object_list}
    self.assertEqual(titles, {"Nurofen Forte", "Ibuprofen Bios"})
```

Clientul de test `self.client` (o instanţă a `django.test.Client`) execută o cerere HTTP GET spre endpoint-ul "home" cu parametrul `query=ibuprofen`. Funcţia `reverse("home")` construieşte URL-ul după numele rutei, ceea ce face testul rezistent la modificările din URL-urile aplicaţiei.

Sunt efectuate trei verificări: codul statutului trebuie să fie 200 (OK), numărul total de rezultate trebuie să fie 2 (ambele medicamente cu Ibuprofen – unul în denumire, altul în substanţa activă), iar în HTML trebuie să fie prezentă clasa butonului de curăţare a căutării. Ultima verificare asigură că denumirile medicamentelor găsite corespund exact cu cele aşteptate. Utilizarea setului (`set`) pentru compararea denumirilor face testul indiferent la ordinea rezultatelor.

Testul `test_suggest_returns_title_and_ingredient_matches` verifică endpoint-ul AJAX de autocompletare, care lucrează în modul JSON. Aceasta este o verificare importantă a integrării backend-JavaScript.

```python
def test_suggest_returns_title_and_ingredient_matches(self):
    response = self.client.get(reverse("suggest"), {"q": "ibu"})

    self.assertEqual(response.status_code, 200)
    payload = response.json()

    suggestion_texts = {item["text"] for item in payload["suggestions"]}
    suggestion_kinds = {item["kind"] for item in payload["suggestions"]}

    self.assertIn("Ibuprofen", suggestion_texts)
    self.assertIn("Ibuprofen Bios", suggestion_texts)
    self.assertIn("ingredient", suggestion_kinds)
    self.assertIn("title", suggestion_kinds)
```

Metoda `response.json()` deserializează răspunsul JSON într-un dicţionar Python. Apoi se extrag două seturi: textele sugestiilor şi tipurile (`kind`) lor. Sunt utilizate asocierile `assertIn` pentru a verifica prezenţa sugestiilor aşteptate, fără a verifica ordinea lor. Se verifică că sugestiile includ atât substanţa activă "Ibuprofen", cât şi denumirea medicamentului "Ibuprofen Bios", şi că tipurile de sugestii acoperă ambele categorii – "ingredient" şi "title".

Testul `test_suggest_recent_history_can_delete_single_item` verifică funcţia ştergerii unui articol separat din istoricul căutărilor.

```python
def test_suggest_recent_history_can_delete_single_item(self):
    session_key = self._ensure_session_key()
    SearchQuery.objects.create(
        query="paracetamol",
        query_norm="paracetamol",
        session_key=session_key,
    )
    SearchQuery.objects.create(
        query="vitamin c",
        query_norm="vitamin c",
        session_key=session_key,
    )

    response = self.client.post(
        reverse("delete_search_history_item"),
        {"query": "paracetamol"})

    self.assertEqual(response.status_code, 200)
    self.assertFalse(
        SearchQuery.objects.filter(
            session_key=session_key, query_norm="paracetamol").exists()
    )
    self.assertTrue(
        SearchQuery.objects.filter(
            session_key=session_key, query_norm="vitamin c").exists()
    )
    self.assertEqual(response.json()["suggestions"],
                     [{"text": "vitamin c", "kind": "recent"}])
```

Testul începe cu pregătirea mediului: este invocată metoda auxiliară `_ensure_session_key()`, care garantează existenţa sesiunii utilizatorului. Apoi sunt create două articole în istoric cu session_key identic.

Urmează cererea POST spre endpoint-ul ştergerii cu parametrul `query=paracetamol`. După executarea cererii sunt efectuate trei verificări: răspunsul trebuie să fie succes (200), articolul "paracetamol" nu trebuie să mai existe în baza de date, iar articolul "vitamin c" trebuie să fie încă acolo. Este verificat, de asemenea, şi conţinutul răspunsului JSON – trebuie să conţină o listă cu un singur articol – "vitamin c". Această logică verifică că este şters exact articolul solicitat, şi nu toată istoria.

Metoda `_ensure_session_key` este auxiliară şi se pregăteşte pentru crearea sesiunii:

```python
def _ensure_session_key(self):
    session = self.client.session
    session["history_seed"] = "1"
    session.save()
    return session.session_key
```

Adăugarea unei chei fictive `history_seed` este necesară pentru a forţa Django să creeze o sesiune cu un identificator unic. Altfel, sesiunea va fi "goală" şi nu va primi session_key.

Testul `test_suggest_recent_history_can_be_cleared` verifică ştergerea completă a istoricului. Aceasta este o operaţiune mai simplă decât ştergerea unui articol separat, dar extrem de importantă.

```python
def test_suggest_recent_history_can_be_cleared(self):
    session_key = self._ensure_session_key()
    SearchQuery.objects.create(
        query="paracetamol",
        query_norm="paracetamol",
        session_key=session_key,
    )
    SearchQuery.objects.create(
        query="vitamin c",
        query_norm="vitamin c",
        session_key=session_key,
    )

    response = self.client.post(reverse("clear_search_history"))

    self.assertEqual(response.status_code, 200)
    self.assertFalse(
        SearchQuery.objects.filter(session_key=session_key).exists())
    self.assertEqual(response.json()["suggestions"], [])
```

După apelul endpoint-ului de curăţare sunt verificate că nu mai există niciun articol pentru session_key-ul dat, precum şi că răspunsul conţine o listă goală de sugestii.

Testul `test_delete_history_endpoint_accepts_post_with_csrf_cookie_from_page` este deosebit de important – el verifică respectarea protecţiei CSRF pe endpoint-urile de modificare a datelor. Aceasta este o componentă critică de securitate.

```python
def test_delete_history_endpoint_accepts_post_with_csrf_cookie_from_page(self):
    csrf_client = Client(enforce_csrf_checks=True)
    page_response = csrf_client.get(reverse("home"))
    csrf_token = page_response.cookies["csrftoken"].value

    session = csrf_client.session
    session["history_seed"] = "1"
    session.save()
    session_key = session.session_key

    SearchQuery.objects.create(
        query="paracetamol",
        query_norm="paracetamol",
        session_key=session_key,
    )

    response = csrf_client.post(
        reverse("delete_search_history_item"),
        {"query": "paracetamol"},
        HTTP_X_CSRFTOKEN=csrf_token,
    )

    self.assertEqual(response.status_code, 200)
    self.assertFalse(
        SearchQuery.objects.filter(
            session_key=session_key, query_norm="paracetamol").exists()
    )
```

Aici este creat un client special `Client(enforce_csrf_checks=True)` cu verificările CSRF activate (ele sunt implicit dezactivate în testele Django pentru comoditate). Clientul efectuează mai întâi o cerere GET la pagina de pornire pentru a primi cookie-ul CSRF, apoi scoate token-ul din cookie.

În cererea POST token-ul este transmis prin header-ul `X-CSRFToken` (aceasta este exact ceea ce face JavaScript-ul client prin fetch API). Dacă token-ul lipseşte sau este incorect, Django va returna statusul 403 Forbidden. Testul verifică că implementarea funcţionează corect cu token-ul corect.

Testele `test_language_switch_to_english_changes_home_ui` şi `test_language_switch_to_russian_changes_home_ui` verifică funcţionalitatea comutării limbii interfeţei.

```python
def test_language_switch_to_english_changes_home_ui(self):
    response = self.client.post(
        reverse("set_language"),
        {"language": "en", "next": reverse("home")},
        follow=True,
    )

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Search medicines and analogs")
    self.assertContains(response, "Search")
    self.assertEqual(self.client.session["language"], "en")


def test_language_switch_to_russian_changes_home_ui(self):
    response = self.client.post(
        reverse("set_language"),
        {"language": "ru", "next": reverse("home")},
        follow=True,
    )

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "\u041f\u043e\u0438\u0441\u043a \u043b\u0435"
                                  "\u043a\u0430\u0440\u0441\u0442\u0432 \u0438 "
                                  "\u0430\u043d\u0430\u043b\u043e\u0433\u043e\u0432")
    self.assertContains(response, "\u041f\u043e\u0438\u0441\u043a")
    self.assertEqual(self.client.session["language"], "ru")
```

Parametrul `follow=True` permite clientului de test să execute automat redirecţionările – după POST-ul la `/set-language/`, serverul execută redirect la pagina de pornire, iar testul capturează conţinutul anume al acesteia.

Pentru limba engleză se verifică prezenţa frazelor "Search medicines and analogs" şi "Search" în HTML. Pentru limba rusă sunt folosite secvenţele Unicode, care se extind în "Поиск лекарств и аналогов" şi "Поиск". Aceasta reprezintă un simbol de caractere chirilice în cod Python. În plus, este verificat că limba este salvată corect în sesiune.

Testul `test_medicine_detail_page_renders` verifică că pagina detaliată a medicamentului se deschide cu succes.

```python
def test_medicine_detail_page_renders(self):
    response = self.client.get(
        reverse("medicine_detail", args=[self.primary_medicine.id]))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "MedicineAnalog")
```

Parametrul `args=[self.primary_medicine.id]` transmite ID-ul medicamentului la construirea URL-ului. Verificarea prezenţei "MedicineAnalog" în răspuns confirmă că şablonul s-a randat corect şi conţine elementul tipic al aplicaţiei (de exemplu, titlul).

Similar, testul `test_analogs_page_renders` verifică că pagina analogilor se încarcă cu succes:

```python
def test_analogs_page_renders(self):
    response = self.client.get(reverse("analogs"), {"ingredient": "Ibuprofen"})

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "MedicineAnalog")
```

Testul `test_missing_image_uses_placeholder_on_detail_page` verifică că în lipsa imaginii medicamentului, interfaţa afişează un placeholder implicit.

```python
def test_missing_image_uses_placeholder_on_detail_page(self):
    response = self.client.get(
        reverse("medicine_detail", args=[self.no_image_medicine.id]))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response,
                        "/static/meds/img/medicine-placeholder.svg")
```

Se utilizează medicamentul `no_image_medicine`, creat în `setUpTestData` cu câmpul gol `img=""`. Testul confirmă că, în lipsa URL-ului imaginii, în HTML apare calea către fişierul SVG-placeholder. Aceasta ne protejează de imagini deteriorate în interfaţă.

Testul `test_home_search_paginates_results_server_side` este cel mai complex şi verifică funcţionarea corectă a paginării cu un număr mare de rezultate.

```python
def test_home_search_paginates_results_server_side(self):
    for idx in range(12):
        Medicine.objects.create(
            title=f"Paracetamol extra {idx}",
            active_ingredient="Paracetamol",
            price=Decimal("10.00") + Decimal(idx),
            link=f"https://example.com/paracetamol-{idx}",
            img="",
            manufacturer="Extra Pharma",
            pharmacy="FarmaciaFamiliei" if idx < 8 else "Hippocrates",
        )

    first_page = self.client.get(reverse("home"), {"query": "paracetamol"})
    second_page = self.client.get(reverse("home"),
                                  {"query": "paracetamol", "page": 2})

    self.assertEqual(first_page.status_code, 200)
    self.assertEqual(first_page.context["page_obj"].paginator.per_page, 10)
    self.assertEqual(len(first_page.context["page_obj"].object_list), 10)
    self.assertContains(first_page, 'class="medicine-card"', count=10)
    self.assertContains(first_page, "\u00cenainte")

    self.assertEqual(second_page.status_code, 200)
    self.assertEqual(second_page.context["page_obj"].number, 2)
    self.assertEqual(len(second_page.context["page_obj"].object_list), 3)
    self.assertContains(second_page, "\u00cenapoi")
```

Testul creează 12 medicamente suplimentare cu substanţa activă Paracetamol, distribuindu-le între două farmacii (primele 8 – FarmaciaFamiliei, restul 4 – Hippocrates). În total în baza de date există 13 medicamente cu Paracetamol (cu adăugarea medicamentului iniţial din `setUpTestData`).

Pentru prima pagină se verifică: statutul 200, mărimea paginii 10 articole (setare în cod), prezenţa a 10 cărduri în HTML (atributul `count=10` cere numărul exact) şi prezenţa butonului "Înainte" pentru paginile următoare. Secvenţa Unicode `\u00cenainte` reprezintă cuvântul românesc "Înainte" cu o literă majusculă Î.

Pentru pagina a doua se verifică statutul 200, numărul paginii 2, numărul de articole rămase (3 = 13 - 10) şi prezenţa butonului "Înapoi" pentru întoarcerea la pagina anterioară. Acest test cuprinde logica completă a paginării server-side.

Testul `test_home_search_shows_empty_state_when_nothing_found` verifică afişarea stării "Nimic găsit" la interogările fără rezultate.

```python
def test_home_search_shows_empty_state_when_nothing_found(self):
    response = self.client.get(reverse("home"), {"query": "zzznothingmatch"})

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Niciun rezultat")
    self.assertContains(response, "Nu am găsit nimic pentru")
```

Ca interogare se foloseşte şirul "zzznothingmatch", care nu poate fi conţinut în denumiri reale. Se verifică că statutul răspunsului este 200 (pagina se afişează, nu se returnează o eroare), precum şi prezenţa frazelor specifice despre absenţa rezultatelor în română. Acest test asigură că utilizatorul primeşte un feedback util chiar şi la absenţa datelor.

Sumarizând cele 11 teste automate implementate, acoperirea include:
- Căutarea pe denumiri şi substanţe active (1 test);
- Endpoint-ul AJAX de sugestii şi autocompletare (1 test);
- Gestionarea istoricului căutărilor – ştergerea unui articol şi curăţarea completă (2 teste);
- Protecţia CSRF pe endpoint-urile API (1 test);
- Comutarea limbii interfeţei – engleză şi rusă (2 teste);
- Randarea paginilor detaliate şi a paginii analogilor (2 teste);
- Folosirea placeholder-ului în lipsa imaginii (1 test);
- Paginarea server-side (1 test);
- Afişarea stării goale (1 test).

Utilizarea abordării automate a testării, în locul celei manuale, oferă mai multe avantaje. În primul rând, testele automate sunt rulate rapid – setul complet se execută în câteva secunde, în timp ce verificarea manuală a aceloraşi scenarii ar fi durat multe minute. În al doilea rând, testele automate sunt repetabile: de fiecare dată ele verifică aceleaşi lucruri, fără a "uita" nimic şi fără a introduce erori umane. În al treilea rând, testele servesc drept documentaţie – prin citirea lor, dezvoltatorul poate înţelege care este comportamentul aşteptat al aplicaţiei.

Testele automate sunt deosebit de valoroase la refactoring şi la adăugarea funcţionalului nou. Dacă la modificarea codului există un test eşuat, aceasta este un indicator imediat de regresie. Fără teste, astfel de erori ar fi putut să ajungă în producţie şi să fie găsite de utilizatori, ceea ce ar fi scăzut încrederea în produs.

Pentru rularea testelor se utilizează comanda standard Django: `python manage.py test meds`. Framework-ul creează o bază de date de test separată, execută migrările, rulează toate testele şi la final şterge baza de date. Aceasta garantează faptul că testele nu afectează datele de producţie.

În concluzie, abordarea automată a testării permite menţinerea calităţii înalte a codului pe tot parcursul ciclului de viaţă al proiectului. Chiar dacă o testare manuală suplimentară ar putea detecta probleme cu UX-ul sau cu aspecte vizuale, testele automate creează un fundament solid de încredere că funcţionalitatea de business a aplicaţiei va funcţiona corect la orice modificare a codului.
