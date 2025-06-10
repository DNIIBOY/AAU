
# Produktudvikling

#### SP1:
* Hvad er det primære formål med opportunity identification processen og hvad er de vigtigste output? Beskriv/eksemplificer hvordan man kan udføre processen.
	* Formålet er at at finde muligheder
	* Forskel på ide og mulighed: Mulighed er en ide der passer til markedet, og kan lade sig gøre
	* Vurdere risiki
 ![[Pasted image 20250608191524.png]]
	3 Horisonter: 
	1. Noget der er samme marked som virksomheden, og bruger eksisterende teknologi
	2. Noget der er næste generation, en udvikling, måske ind i et markede, som virksomheden ikke har været i før
	3. Helt nyt, skaber et nyt markede, som ingen har været i før
	Steps:
	4. Innovation charter: et "scope" eller kategori man skal lave en løsning indenfor
	5. Idegenering: Mange muligheder, indhent via kolleger, studee markedet/konkurenter, find fejl i nuværende løsninger
	6. Screen ideas: Fjern dem der ikke kan lade sig gøre, eller ikke giver mening, feks spørgeskema eller intern afstemning.
	7. Develop promising opportunities: Undersøg markedet, krav for fremstilling, evt prototype
	8. Select Product Candidates: Vælg den/de ideer der er mest lovende.
	Output: Mission statement: Alt viden man har fået

* Er det radikalt nye produkter altid det bedste mål? Hvad er fordelen og ulempen ved radikalt nye produkter?
	* Horisont 3 er radikalt nye ting, og det er en meget større risiko, men med potentiale for mere success

#### SP2:
* Hvad kan vanskeliggøre indhentningen af customer needs? Hvorfor er indhentningen af disse et særligt vigtigt step i produktudviklingsprocessen?
	* Vigtigt for at opstille krav, der tager udgangspunkt i markedet.
	* Forskellige kunder "elitekunder" vs normale kunder
	* Manglende kilder
	* Stor spredning i ønsker
* Hvilke andre interessenter kunne være relevante at indhente krav til produktet fra? Hvordan vil du gøre det?
	* Interne afdelinger (hr til ansættelse af inginører hvis det skal bruge, marketing, osv)
	* Eksterne partnere (fabrik har krav til hvad der kan fremstilles)
	![[Pasted image 20250608193019.png]]
#### SP3:
* Hvilke typer af modularitet findes der for en modulær produktarkitektur? Giv et par eksempler fra konkrete produkter.
	* Integreret vs modulær
	* Slotbaseret: Hver ting passer kun ét sted, men alt samles ud fra en fælles bund
	* Busbaseret: Hver ting sidder på en fælles bund, men kan sidde forskellige steder, de har samme interface.
	* Sektionsbaseret: Hver ting sider fast i en anden ting, og samler sidst en hel løsning
* Er en modulær produktarkitektur altid en fordel? Er det tilfælde hvor en integreret arkitektur er en fordel? Giv gerne eksempler.
	* Nej
	* Integreret arkitektur kan være billigere at udvikle/fremstille og optimere det færdige produkt ved at gøre det mindre/lettere.
#### SP4:
* I kurset har vi anvendt en ”screening & scoring” matrix til at udvælge et endeligt koncept. Hvad er styrken ved denne metode? Hvad kunne alternative metoder være til at vælge et koncept?
![[Pasted image 20250608205837.png]]
	* Styrken er at de orginale krav kommer med ind i matricen, og bruges til at vurdere konceptet
	* Kriterier kan ikke altid evalueres uafhængigt
	* Nogle kriterier er meget kvalitative/subjektive
	* Vurdering af kost
* Hvad kunne du gøre for at øge troværdigheden af de enkelte scorer i matrixen?
	* Bruge kunderne til at vurdere scorene, under koncepttesting
	* Screen kunden før de bruges til at vurdere matricen
#### SP5:
* Hvad er fordelene ved at følge en struktureret metode til produktudvikling? Hvad risikerer man ved ikke at gøre det?
	* Det kan hjælpe med at skabe en struktur, at man fremstiller et realistisk produkt, at man ikke overser vigtige detaljer, og at produktet faktisk er noget der er nogen der gerne vil bruge.
* Hvad er nogle af de største faldgruber som produktudviklingsteam i forbindelse med processen?
	* Man skal passe på ikke at indsnævre sig for meget, for tidligt, og man skal være forberedt på at kravene skal kunne ændre sig, når ny viden opdages


# Kravsspecifikation og system design

#### SP6:
* Hvad er et use case diagram? Hvilke elementer består det af? Hvad bruger man det til? Hvornår anvender man use case diagrammer? Tegn eller vis eksempel/eksempler.
	* Et diagram der binder brugere til et system med usecases, som er fundet gennem kravene
	* Består af brugere, system(er), og usecases.
	* Bruges til at definere scope, udvikle krav, identificere systeminteraktioner
		![[Pasted image 20250610234203.png]]
* Hvad er en use case beskrivelse? Hvad er vigtigt i en sådan beskrivelse? Hvordan relaterer disse sig til krav specifikationerne? Hvornår udarbejder man beskrivelserne? Hvem udarbejder dem? Giv eksempler.
	* En udvidet beskrivelse af en usecase, udvikles efter usecase diagramet, for at gå mere i detaljerne med en usecase
	![[Pasted image 20250609125924.png]]
#### SP7:
* Hvad karakteriserer gode krav? Giv eksempler på gode og dårlige krav. Hvor i V- modellen finder vi hvilke typer af krav? Med hvem udarbejder vi krav og på hvilke måde sikrer vi at vi får samtlige vigtige krav med i kravspecifikationen?
	* Korrekt
	* Utvetydigt
	* Komplet
	* Konsistent
	* Organiseret efter prioritet
	* Verificerbart
	* Modificerbart
![[Pasted image 20250609130113.png]]
* Hvilke krav har vi til vores kravspecifikation? Hvordan sikrer vi at krav til krav er opfyldt? Hvordan bruger vi krav i efterfølgende udviklingsproces? Hvordan forholder vi os til at skulle lave ændringer i krav i de efterfølgende tidsperioder i en udviklingsproces f.eks. hen mod slutningen af projektet? Giv eksempler.

* Korrekthed
* Utvetydig
* Komplet
* Konsistent
* Organiseret efter prioritet/vigtighed
* Verificerbar
* Modificerbar
* Sporbar

Modificerbarhed skal tænkes ind fra starten, kravene skal laves uafhængige, og være seperate. Struktur som indeksering og nummerering kan hjælpe med overblik når krav skal ændres.

#### SP8:
* Hvordan deler man effektivt krav op i funktionelle moduler? Hvad definerer et modul? Hvad kan vi bruge modulariseringen til? Giv eksempler, gerne på tavle.
	* Et modul er en isoleret del af et system, som har nogle inputs og outputs. Implementeringen skjules.
	* Enkelgør testfasen, da moduler kan testes individuelt
* Hvad er en grænseflade? Hvordan bliver man enig om en grænseflade? Hvem er involveret i at definere grænseflader? Hvilke fordele/ulemper er der ved at definere grænseflader tidligt/sent i et projektforløb? Giv eksempler
	* Et sæt af regler der skal følges for en bestemt kommunikation
	* Defineres ofte internt, hvis de kun skal bruges internt, kan defineres med kunden osv, hvis det er en ekstern grænseflade.
	* Hvis de defineres for tidligt kan det låse designet fast for at passe med en grænseflade, hvis de defineres for sent kan det være svært at udvikle, specielt parallelt arbejde.

# Implementering og test

#### SP9:
* Hvad er kodestil og kodestruktur? For hvem er dette vigtigt? Hvad har I gjort i jeres projekt? Hvordan bliver man enige om f.eks. brug af white space eller tab’s? Giv eksempler på forskellige kodestilarter der kan øge læsevenligheden, og eksempler på det modsatte (der mindsker læsevenligheden).
* Hvad er objekt orienteret programmering? Hvad er en klasse i forhold til et objekt? Hvad er et klassediagram? Tegn gerne et simpelt et på tavlen og diskuter ud fra det tegnede diagram.
#### SP10:
* Hvad er white boks test? Hvornår anvender vi white boks test og i hvilke sammenhæng. Hvad er en path test og hvorfor er en 100% path testing stort set altid umulig at gennemføre? Tegn et flowgraph diagram på tavlen og forklar hvad en branch test er.
	* Path testing er test af alle kombinationer af veje gennem programmet
	* Branch testing skal man bare teste hver linje kode.
* Hvad er debugning? Hvordan bruger man en debugger (princippet)? Hvornår bruger man en debugger? Forklar ud fra et af de tre kodestumper givet på moodle, hvordan du vil white boks teste koden. Vis gerne på laptop hvis du har den med.
#### SP11:
* Hvad er en black box test? Forklar princippet bag black box tests. Er det realistisk at risikere at en komplet test skal gennemføre 10^100 kombinationsmuligheder af input værdier – hvorfor/hvorfor ikke? Antag det er, hvordan sikrer du så at testen kan gennemføres på realistisk kort tid? Argumenter for hvorfor din metode vil være bullet- proof. Ved sidste spørgsmål, tag gerne udgangspunkt i en løsning fra opgave 1.
	* 
* Hvis noget kode ser ud til at virke, er du så helt sikker? Hvordan sikrer du dig, at du også vil have den kode til at være ansvarlig for næste flytur du selv skal på? Beskriv hvordan du fandt fejlen i det kode der blev givet i opgave 2. Er du sikker på du fandt ALLE fejl? Argumenter hvorfor du er sikker.