# CAPITOLUL 1. ANALIZA DOMENIULUI DE APLICARE

## 1.1 Actualitatea temei alese

Digitalizarea sectorului medical si farmaceutic reprezinta una dintre directiile esentiale ale transformarii societatii contemporane. In Republica Moldova, cresterea accesului la internet, dezvoltarea serviciilor electronice si diversificarea platformelor de comert online au schimbat semnificativ modul in care populatia cauta informatii despre produse si servicii medicale. Cu toate acestea, procesul de identificare a unui medicament potrivit ramane, in practica, dificil pentru multi utilizatori, in special in situatiile in care este necesara compararea rapida a preturilor intre mai multe farmacii sau gasirea unor produse analoge.

In contextul cresterii preturilor la medicamente si al variatiilor semnificative intre lanturile farmaceutice, utilizatorul final se confrunta cu o problema reala: lipsa unei imagini centralizate asupra ofertei disponibile in piata. De regula, pentru a gasi un produs la un pret convenabil, pacientul trebuie sa viziteze manual mai multe site-uri, sa introduca aceeasi interogare de cautare, sa compare denumiri comerciale similare si sa verifice disponibilitatea. Acest proces este consumator de timp, predispus la erori si incomod, mai ales pentru persoanele varstnice sau pentru utilizatorii fara competente digitale avansate.

Necesitatea dezvoltarii aplicatiei **MedicineAnalog** apare exact in acest punct critic: este nevoie de un sistem informatic unic care sa colecteze, sa structureze si sa prezinte intr-un mod clar datele despre medicamente din mai multe surse farmaceutice. Aplicatia propusa raspunde la mai multe provocari concrete:

- lipsa unui instrument unic de comparare a preturilor medicamentelor in farmaciile online din Republica Moldova;
- dificultatea identificarii rapide a analogilor dupa substanta activa;
- fragmentarea informatiilor privind producatorul, farmacie, pret si link-ul catre produs;
- riscul de alegere suboptimala a medicamentului din punct de vedere economic.

Din perspectiva socio-economica, problema are impact direct asupra bugetului familial si asupra accesului la tratament. Pentru pacientii cu tratamente de lunga durata, diferenta de pret intre produse similare poate fi semnificativa in timp. O aplicatie care permite compararea rapida a variantelor disponibile si identificarea alternativelor poate reduce costurile personale si poate creste accesibilitatea terapiei.

Din perspectiva tehnologica, tema este actuala deoarece implica integrarea mai multor directii moderne:

- agregarea datelor din surse eterogene (platforme farmaceutice diferite);
- prelucrarea semi-automata a informatiei (normalizare, structurare, clasificare);
- dezvoltarea unei aplicatii web cu interfata intuitiva si timp de raspuns redus;
- extinderea functionala spre cautare orientata semantic (dupa substanta activa).

In plus, tema este relevanta si academic, deoarece ofera un cadru potrivit pentru aplicarea conceptelor de analiza a domeniului, proiectare software, modelare de date, arhitectura pe straturi, securitate aplicativa si optimizare a interactiunii om-calculator. Astfel, realizarea sistemului nu este doar o implementare tehnica, ci si o contributie practica la rezolvarea unei probleme reale de interes public.

Prin urmare, actualitatea temei este justificata de intersectia dintre nevoia sociala (acces facil la informatii farmaceutice), necesitatea economica (compararea preturilor), oportunitatea tehnologica (dezvoltarea de agregatoare specializate) si valoarea didactica (aplicarea integrata a cunostintelor acumulate in procesul de studiu).

## 1.2 Analiza analogilor existenti si comparatia cu aplicatia propusa

Pentru evaluarea nivelului de noutate si utilitate al sistemului **MedicineAnalog**, este necesara analiza unor platforme existente care ofera functionalitati apropiate. In cadrul acestui subcapitol sunt examinate trei exemple relevante:

1. platforme farmaceutice online locale (Republica Moldova);
2. agregatoare/comparatoare internationale de medicamente;
3. platforme orientate pe informatie medicala si disponibilitate.

Scopul analizei consta in identificarea avantajelor si limitarilor acestora si in evidentierea modului in care aplicatia propusa adreseaza golurile functionale.

### 1.2.1 Analog 1: Apteka.md (Republica Moldova)

**Apteka.md** este una dintre cele mai cunoscute platforme farmaceutice online locale. Sistemul permite utilizatorului sa caute medicamente dupa denumire comerciala, sa vizualizeze pretul, producatorul si descrierea produsului.

**Puncte forte:**
- interfata cunoscuta si relativ simpla;
- catalog extins de produse;
- informatii utile despre produs (in functie de pagina);
- prezenta pe piata locala si orientare spre utilizatorii din Moldova.

**Limitari:**
- datele sunt limitate la oferta propriei retele/surse;
- nu exista comparare directa cu alte farmacii in acelasi ecran;
- identificarea analogilor dupa substanta activa este limitata sau neuniforma;
- utilizatorul trebuie sa repete cautarea pe alte platforme pentru comparatie reala.

**Raportare la MedicineAnalog:**
Aplicatia propusa nu inlocuieste platforma Apteka.md ca magazin online, ci functioneaza ca strat de agregare si comparare intre surse multiple. Astfel, avantajul principal este perspectiva unificata asupra pietei, nu doar asupra unui singur operator.

### 1.2.2 Analog 2: Farmacie.md / Farmacia Familiei (Republica Moldova)

Platformele locale precum **Farmacie.md** sau **Farmacia Familiei** ofera, la randul lor, functionalitati de cautare si prezentare a produselor farmaceutice. Aceste sisteme sunt utile pentru achizitie directa in cadrul ecosistemului propriu.

**Puncte forte:**
- acces rapid la oferta lantului farmaceutic respectiv;
- informatii comerciale clare (pret, denumire, imagini);
- integrare cu procese logistice interne (disponibilitate in retea, promotii etc., in functie de platforma).

**Limitari:**
- imposibilitatea compararii transparente cu preturile concurentei in acelasi flux de utilizare;
- orientare predominanta spre vanzare, nu spre analiza comparativa;
- dificultate in identificarea substituentilor cu aceeasi substanta activa din alte surse;
- date neomogene intre platforme (formatare diferita, denumiri diferite, structura variabila).

**Raportare la MedicineAnalog:**
In timp ce platformele locale sunt eficiente ca puncte individuale de comercializare, **MedicineAnalog** are un obiectiv diferit: suport decizional pentru utilizator prin centralizarea ofertelor si compararea acestora. Astfel, sistemul propus completeaza ecosistemul existent, nu concureaza direct pe logica de magazin.

### 1.2.3 Analog 3: GoodRx (SUA) / modele internationale de comparare

Pe pietele internationale exista platforme de tip **GoodRx** (SUA), care ofera comparare de preturi, cupoane si recomandari pentru medicamente. Aceste solutii demonstreaza maturitatea conceptului de agregator farmaceutic.

**Puncte forte:**
- comparare structurata a preturilor intre mai multe puncte de vanzare;
- interfete moderne si experienta de utilizare optimizata;
- functionalitati avansate (alerte, discounturi, recomandari).

**Limitari in raport cu contextul local:**
- orientare spre alte piete si reglementari;
- neadaptare la specificul farmaciilor online din Republica Moldova;
- posibil acces limitat pentru utilizatorii locali la unele servicii.

**Raportare la MedicineAnalog:**
Aceste platforme internationale pot servi drept model conceptual, insa aplicabilitatea directa pe piata moldoveneasca este redusa. **MedicineAnalog** valorifica aceeasi idee de baza (comparare si transparenta), dar o adapteaza la surse locale concrete si la nevoile reale ale utilizatorilor din Republica Moldova.

### 1.2.4 Sinteza comparativa

Analiza arata ca platformele existente rezolva partial problema: ele permit cautarea in interiorul unei singure surse, dar nu ofera o viziune agregata, comparativa, simplu de utilizat. Solutia propusa adreseaza exact acest deficit prin:

- colectarea datelor din mai multe farmacii;
- normalizarea informatiei relevante (denumire, pret, producator, farmacie, substanta activa);
- prezentarea comparativa a rezultatelor;
- posibilitatea identificarii analogilor pe baza substantei active.

### 1.2.5 Tabel comparativ

| Criteriu | Apteka.md | Farmacie.md / Farmacia Familiei | GoodRx (model international) | MedicineAnalog (proiect propus) |
|---|---|---|---|---|
| Acoperire geografica | Moldova (locala) | Moldova (locala) | International (SUA) | Moldova (adaptat local) |
| Cautare dupa denumire | Da | Da | Da | Da |
| Comparare intre mai multe farmacii in acelasi ecran | Limitat/nu | Limitat/nu | Da | Da (obiectiv central) |
| Cautare dupa substanta activa | Partial | Partial | Da (in forme avansate) | Da (focus functional) |
| Unificare date din surse multiple | Nu | Nu | Da | Da |
| Adaptare la contextul local (surse MD) | Da | Da | Nu | Da |
| Suport decizional pentru alegere economica | Mediu | Mediu | Ridicat | Ridicat |
| Dependenta de un singur operator | Ridicata | Ridicata | Redusa | Redusa |

Pe baza acestui tabel se poate concluziona ca proiectul propus ocupa o nisa functionala justificata: agregarea si compararea locala a datelor farmaceutice, cu accent pe analogi si optimizare economica pentru utilizator.

## 1.3 Scopul lucrarii si cerintele sistemului

### 1.3.1 Scopul general al lucrarii

Scopul principal al lucrarii este proiectarea si dezvoltarea unui sistem informatic web denumit **MedicineAnalog**, destinat cautarii, compararii si analizarii medicamentelor din mai multe farmacii online, cu suport pentru identificarea analogilor pe baza substantei active.

Obiectivul practic este oferirea unui instrument usor de utilizat, care reduce timpul de cautare si creste transparenta informatiei privind preturile, contribuind la luarea unei decizii informate de catre utilizator.

### 1.3.2 Obiective specifice

Pentru realizarea scopului general, au fost formulate urmatoarele obiective:

1. analiza domeniului farmaceutic online si identificarea cerintelor reale ale utilizatorilor;
2. colectarea datelor din surse farmaceutice multiple prin mecanisme automate de extragere;
3. modelarea bazei de date pentru stocarea unitara a informatiilor despre medicamente;
4. implementarea unui mecanism de cautare dupa denumire si dupa substanta activa;
5. implementarea compararii preturilor intre farmacii;
6. dezvoltarea unei interfete web intuitive, clare si responsive;
7. asigurarea unor conditii minime de securitate si fiabilitate.

### 1.3.3 Cerinte functionale

Sistemul trebuie sa indeplineasca un set de cerinte functionale de baza:

- **CF1. Cautare medicamente:** utilizatorul introduce denumirea si obtine lista de rezultate relevante.
- **CF2. Afisare detalii:** pentru fiecare rezultat se afiseaza pretul, farmacia, producatorul, imaginea si link-ul catre sursa.
- **CF3. Grupare/comparare:** rezultatele pot fi comparate intre farmacii dupa pret si caracteristici.
- **CF4. Analogi dupa substanta activa:** sistemul permite identificarea produselor cu aceeasi substanta activa.
- **CF5. Actualizare date:** datele pot fi reimprospatate periodic prin rularea proceselor de colectare si incarcare.
- **CF6. Administrare continut:** exista posibilitatea gestionarii datelor in panoul administrativ.

### 1.3.4 Cerinte nefunctionale

Pe langa functionalitate, sistemul trebuie sa respecte cerinte nefunctionale esentiale:

- **Usabilitate:** interfata simpla, clara, cu flux logic de utilizare.
- **Performanta:** timp de raspuns redus la cautare, chiar la volume moderate de date.
- **Securitate:** protectia cheilor API si a configuratiilor sensibile prin variabile de mediu; validarea datelor de intrare.
- **Scalabilitate:** posibilitatea adaugarii de noi surse farmaceutice fara rescriere majora.
- **Fiabilitate:** functionare stabila in conditii normale si tratarea erorilor de colectare.
- **Mentenabilitate:** cod structurat pe module, usor de extins si testat.

### 1.3.5 Cerinte privind interfata front-end

Componenta front-end trebuie sa asigure:

- pagina de start cu formular de cautare intuitiv;
- afisare organizata a rezultatelor (carduri sau tabel);
- separare vizuala clara pe farmacii;
- elemente de comparare rapida a preturilor;
- acces simplu la pagina de detalii a medicamentului;
- design responsive pentru utilizare pe desktop si dispozitive mobile.

### 1.3.6 Cerinte privind componenta back-end

Back-end-ul trebuie sa ofere:

- logica de cautare si filtrare in baza de date;
- structurare si persistenta a datelor colectate;
- endpoint-uri interne/view-uri pentru afisarea continutului;
- procese de incarcare periodica a datelor din fisierele generate de scrapers;
- mecanisme de logare si tratare a exceptiilor.

### 1.3.7 Instrumente tehnologice utilizate (prezentare succinta)

In implementarea sistemului sunt utilizate urmatoarele tehnologii:

- **Django** - framework principal pentru back-end si managementul datelor;
- **SQLite** (sau alta baza relationala compatibila) - stocarea persistenta a informatiilor;
- **Scrapy** - colectarea automata a datelor din surse farmaceutice online;
- **HTML/CSS + template-uri Django** - constructia interfetei web;
- **Python** - limbajul de implementare pentru logica aplicatiei;
- **JSON** - format intermediar pentru transferul datelor colectate.

Acest set de instrumente este adecvat pentru un produs software de tip MVP, permitand dezvoltare rapida, claritate arhitecturala si extindere ulterioara.

---

# CAPITOLUL 2. PROIECTAREA SI MODELAREA SISTEMULUI

## 2.1 Descriere structurala a sistemului

Descrierea structurala prezinta organizarea componentelor sistemului, relatiile dintre acestea si fluxurile majore de date. Pentru proiectul **MedicineAnalog**, arhitectura poate fi descrisa ca o arhitectura modulara pe straturi, compusa din:

1. stratul de colectare a datelor;
2. stratul de persistenta si prelucrare;
3. stratul de prezentare;
4. stratul de administrare si mentenanta.

### 2.1.1 Arhitectura generala

Arhitectura sistemului urmeaza un model logic de tip **Data Ingestion -> Data Storage -> Business Logic -> Presentation**:

- datele sunt extrase din surse externe (site-uri farmaceutice);
- datele brute sunt transformate in format standardizat;
- informatia este incarcata in baza de date a aplicatiei;
- utilizatorul interogheaza aplicatia prin interfata web;
- rezultatele sunt afisate intr-un format comparativ.

Aceasta separare pe straturi reduce dependentele intre componente si faciliteaza extinderea ulterioara (de exemplu, adaugarea unui nou scraper sau a unei noi functionalitati de filtrare).

### 2.1.2 Componenta de colectare a datelor

Componenta de colectare are rolul de a extrage informatii despre medicamente din mai multe farmacii online. In mod practic, aceasta este implementata prin spider-e Scrapy dedicate fiecarui site tinta.

Responsabilitati principale:

- accesarea paginilor sursa;
- identificarea elementelor relevante (denumire, pret, link, producator, imagine);
- curatarea primara a datelor textuale;
- serializarea rezultatelor in fisiere JSON.

Prin separarea acestei componente de restul sistemului se obtine independenta fata de front-end si de baza de date. Daca structura unui site sursa se modifica, interventia este localizata la nivelul spider-ului respectiv.

### 2.1.3 Componenta de persistenta si modelul de date

Dupa colectare, datele sunt importate in baza de date relationala prin comenzi dedicate de management. Elementul central al modelului de date este entitatea **Medicine**, care include atribute precum:

- `title` (denumirea medicamentului);
- `price` (pretul);
- `pharmacy` (farmacia/sursa);
- `manufacturer` (producator);
- `active_ingredient` (substanta activa);
- `link` (URL catre produsul original);
- `img` (imagine reprezentativa).

La nivel structural, modelul este conceput pentru interogari rapide dupa denumire si pentru grupare dupa substanta activa. In viitor, structura poate fi extinsa prin entitati suplimentare (de exemplu, `Pharmacy`, `Category`, `PriceHistory`) pentru normalizare avansata.

### 2.1.4 Componenta de logica aplicativa

Logica aplicativa este implementata in backend-ul Django si include:

- procesarea cererilor HTTP de cautare;
- validarea parametrilor de intrare;
- interogarea eficienta a bazei de date;
- ordonarea si gruparea rezultatelor;
- pregatirea contextului pentru template-uri.

Aceasta componenta reprezinta nucleul functional al sistemului, deoarece transforma datele brute in informatie utila pentru decizie.

### 2.1.5 Componenta de prezentare (UI)

Stratul de prezentare este responsabil de interactiunea directa cu utilizatorul. Interfata este construita cu template-uri Django, HTML si CSS, urmarind principiile de claritate vizuala si usurinta de utilizare.

Structura tipica a interactiunii:

1. utilizatorul introduce termenul de cautare;
2. sistemul afiseaza lista de rezultate;
3. utilizatorul compara variantele disponibile;
4. utilizatorul acceseaza detalii si link-ul catre farmacia sursa.

Prin aceasta abordare, aplicatia ramane simpla si accesibila, chiar pentru utilizatorii fara experienta tehnica.

### 2.1.6 Componenta de administrare

Pentru mentenanta si controlul datelor, sistemul include o componenta administrativa bazata pe panoul standard Django Admin. Aceasta permite:

- vizualizarea inregistrarilor existente;
- filtrarea si cautarea rapida;
- corectarea manuala a unor date daca este necesar;
- gestionarea continutului fara modificari directe in baza de date.

Existenta unui modul administrativ simplifica operatiunile de suport si reduce costurile de mentenanta.

### 2.1.7 Fluxul structural al datelor

Fluxul de date al sistemului poate fi descris textual astfel:

1. sursele externe publica date despre produse;
2. spider-ele colecteaza datele si le stocheaza in JSON;
3. comanda de import preia JSON-ul si populeaza baza relationala;
4. utilizatorul lanseaza cautari din interfata web;
5. backend-ul returneaza rezultate structurate;
6. utilizatorul compara si decide produsul optim.

Acest flux asigura decuplarea intre colectare si consumul datelor, oferind flexibilitate in actualizarea periodica.

### 2.1.8 Aspecte de securitate la nivel structural

Desi sistemul este orientat in principal pe agregare de date publice, arhitectura ia in calcul masuri de securitate de baza:

- eliminarea secretelor din codul sursa (chei API in variabile de mediu);
- validarea datelor introduse de utilizator in formularul de cautare;
- limitarea expunerii datelor interne in interfata;
- utilizarea mecanismelor oferite de framework (protectie CSRF, management sesiuni, configurare DEBUG adecvata mediului).

### 2.1.9 Posibilitati de extindere arhitecturala

Structura sistemului permite evolutie in mai multe directii:

- adaugarea unui API REST pentru consum extern;
- introducerea de cache pentru optimizarea interogarilor;
- monitorizarea istoricului preturilor si analiza tendintelor;
- recomandari inteligente pe baza similaritatii produselor;
- integrarea cu alte surse locale sau regionale.

Aceasta capacitate de extindere confirma alegerea unei arhitecturi modulare, potrivite atat pentru MVP, cat si pentru dezvoltare ulterioara.

## 2.2 Descriere functionala a sistemului

Descrierea functionala evidentiaza comportamentul sistemului din perspectiva actorilor si a scenariilor de utilizare. Pentru **MedicineAnalog**, actorul principal este utilizatorul final interesat de compararea medicamentelor, iar actorul secundar este administratorul care actualizeaza datele.

### 2.2.1 Actori si roluri

**Actor 1: Utilizator final**
- cauta medicamente dupa denumire;
- analizeaza rezultatele din mai multe farmacii;
- identifica analogi dupa substanta activa;
- selecteaza varianta convenabila si acceseaza farmacia sursa.

**Actor 2: Administrator**
- actualizeaza periodic datele colectate;
- verifica consistenta informatiilor;
- gestioneaza inregistrarile prin interfata administrativa.

### 2.2.2 Cazuri principale de utilizare

Din punct de vedere functional, sistemul include urmatoarele cazuri de utilizare:

1. **UC1 - Cautare medicament dupa denumire**
   - intrare: text introdus de utilizator;
   - proces: interogare in baza de date;
   - iesire: lista de produse relevante.

2. **UC2 - Vizualizare rezultate comparative**
   - intrare: setul de produse gasite;
   - proces: ordonare/grupare pe farmacii si pret;
   - iesire: afisare comparativa intr-un format usor de interpretat.

3. **UC3 - Identificare analogi dupa substanta activa**
   - intrare: produs selectat sau substanta activa;
   - proces: cautare produse cu acelasi ingredient activ;
   - iesire: lista de alternative disponibile.

4. **UC4 - Vizualizare detalii produs**
   - intrare: selectarea unui produs din lista;
   - proces: preluare detalii complete;
   - iesire: pagina de detalii cu date relevante si link extern.

5. **UC5 - Actualizare baza de date**
   - actor: administrator;
   - proces: rulare scraping + import in baza;
   - iesire: date actualizate pentru interogarile utilizatorilor.

### 2.2.3 Scenariul functional principal

Scenariul de baza al sistemului poate fi redat in urmatorii pasi:

1. utilizatorul acceseaza pagina principala;
2. introduce denumirea unui medicament in campul de cautare;
3. sistemul valideaza intrarea si executa interogarea;
4. rezultatele sunt afisate cu pret, farmacie, producator si alte detalii;
5. utilizatorul compara ofertele si, optional, acceseaza lista de analogi;
6. utilizatorul deschide detalii pentru produsul preferat;
7. utilizatorul este directionat prin link catre farmacia sursa pentru informatii suplimentare sau achizitie.

### 2.2.4 Reguli functionale de baza

Pentru functionare corecta, sistemul aplica un set de reguli:

- cautarea se realizeaza fara sensibilitate la litere mari/mici;
- rezultatele fara pret valid pot fi tratate separat sau prioritizate inferior;
- compararea se bazeaza pe campuri standardizate;
- analogii se determina pe baza campului `active_ingredient` atunci cand este disponibil;
- fiecare rezultat trebuie sa contina sursa farmaceutica pentru trasabilitate.

### 2.2.5 Performanta functionala si experienta utilizatorului

Experienta utilizatorului este un criteriu central in evaluarea functionala. Aplicatia trebuie sa ofere:

- raspuns rapid la cautari uzuale;
- rezultate lizibile si ordonate;
- minim de pasi pana la luarea deciziei;
- consistenta vizuala intre pagini.

Din perspectiva functionala, performanta nu inseamna doar viteza tehnica, ci si claritate in prezentarea informatiei.

### 2.2.6 Tratarea erorilor si exceptiilor

Sistemul trebuie sa gestioneze robust situatiile neprevazute:

- lipsa rezultatelor pentru o interogare;
- date incomplete provenite din sursele externe;
- indisponibilitate temporara a unor pagini sursa la colectare;
- erori de format in fisierele intermediare.

In astfel de cazuri, aplicatia trebuie sa furnizeze mesaje clare, fara a expune detalii interne sensibile.

### 2.2.7 Aspecte de modelare recomandate pentru capitolul grafic

Desi in acest subcapitol descrierea este textuala, proiectul se preteaza la includerea urmatoarelor diagrame in varianta finala a lucrarii:

- diagrama de context a sistemului (actori externi si fluxuri principale);
- diagrama de cazuri de utilizare (utilizator, administrator);
- diagrama de componente (scrapers, backend, baza de date, UI);
- diagrama de secventa pentru scenariul de cautare si comparare;
- diagrama entitate-relatie pentru modelul de date.

Aceste reprezentari grafice pot completa argumentarea tehnica si pot creste claritatea expunerii in documentul final.

### 2.2.8 Validarea functionala a sistemului

Validarea functionala urmareste confirmarea faptului ca aplicatia raspunde cerintelor definite in capitolul anterior. Criteriile de validare pot include:

- corectitudinea rezultatelor la cautari cu termeni diferiti;
- acuratetea compararii preturilor intre surse;
- prezenta analogilor acolo unde substanta activa este disponibila;
- stabilitatea interfetei la utilizare repetata;
- consistenta datelor dupa cicluri de actualizare.

Rezultatele obtinute in etapa de validare ofera baza pentru concluziile finale ale lucrarii si pentru directiile de dezvoltare ulterioara.

### 2.2.9 Concluzii pentru proiectare si modelare

Proiectarea structurala si functionala a sistemului **MedicineAnalog** confirma fezabilitatea unei platforme locale de agregare farmaceutica orientate spre utilizator. Arhitectura modulara asigura separarea clara a responsabilitatilor, iar modelul functional sustine scenariile reale de utilizare: cautare, comparare, identificare de analogi si acces la sursa.

Prin combinarea componentelor de colectare automata a datelor cu un backend robust si o interfata simpla, sistemul ofera un echilibru intre utilitate practica, complexitate tehnica rezonabila si potential de extindere. Acest echilibru face proiectul potrivit pentru obiectivele unei lucrari de diploma aplicative, cu relevanta atat academica, cat si sociala.

