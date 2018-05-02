# User Requirement Specification

## 1. Einleitung

In diesem Dokument werden die User Requirements für das Projekt "Social Life eines Bots" festgehalten.
Bei dem Projekt handelt es sich um die Erstellung eines Bots für das soziale Netzwerk "Twitter".
Die Bots sollen automatisiert bestimmte Funktionen ausführen und dabei beobachtet werden können.
Die Anforderungen an diese Bots werden im Folgenden genauer dokumentiert.

### 1.1 Zweck des Dokuments

In diesem Dokument werden die User Requirements für den Kundenauftrag zu dem Projekt "Social Life eines Bots" festgelegt. 
Die Kundenansprüche werden festgehalten, um einen Überblick zu erschaffen und den Umfang des Projekts zu definieren.
Die Anforderungen definieren die zu erledigende Arbeit und definieren den Umfang, der geleistet werden muss.

### 1.2 Gültigkeit des Dokuments

Erstellung des Dokuments: 11.04.2018
Umänderung des Dokument: 18.04.2018

### 1.3 Begriffsbestimmung und Abkürzungen

--

### 1.4 Zusammenhang mit anderen Dokumenten

UseCase.svg = Use Case Diagramm

## 2. Allgemeine Beschreibung des gewünschten Systems

Das Projekt besteht aus dem Erstellen einer Software zur Erstellung von Bots für das soziale Netzwerk "Twitter".
Die Bots sollen die wichtigsten Aktionen in "Twitter" automatisiert ausführen und auf vordefinierte "Tweets" automatisiert reagieren.
Der Nutzer kann die Aktionen, Reaktionen und die Stichwörter der "Tweetes" im Vorfeld selbst definieren und ändern.
In einem Log sollen alle Aktionen des Bots einsehbar sein.
Jeder "Tweet" des Bots, jede Reaktion auf einen "Tweet" und jegliche andere Aktivität des Bots soll im Log zusammen mit den Reaktionen anderer Nutzer beobachtbar sein.

### 2.1 Zweck des gewünschten Systems

Der Zweck des Projekts besteht aus der Beobachtung des sozialen Aspekts eines Bots in einem Sozialen Netzwerk.
Als soziales Netzwerk wird die Plattform "Twitter" eingesetzt.
Die soziale Plattform "Twitter" ist eine Internetseite, auf der Personen miteinander kommunizieren und Meinungen miteinander teilen können.
Die Personen haben ein eigenes Profil und können über mehrere Möglichkeiten mit anderen Nutzern in Kontakt treten.
Die Interaktion des Bots mit anderen Nutzern, eventuell auch dargestellt durch andere Bots, soll beobachtet werden.
Die Interaktion mit anderen Nutzern in Form von Menschen steht im Mittelpunkt der Beobachtung.
Besonders die Reaktionen der anderen Nutzer auf den Bot sind der Haupt-Beobachtungsaspekt.
Ursprünglich war die Plattform "FaceBook" als soziales Netzwerk angestrebt.
Die Aktionen bei "Twitter" haben Äquivalente Aktionen bei "FaceBook".
Das Äquivalent zu "Tweeten" ist "Posten", "Liken", "Kommentieren" und "Persönliche Nachrichten" werden in beiden sozialen Netzwerken gleich gehandhabt.
Das Äquivalent zu "Re-Tweeten" in "Twitter" ist "Teilen" in "FaceBook" und zu "Folgen" ist das Äquivalent eine "Freundschaft".
Flexibilität des Bots ist wichtig, um unterschiedliche soziale Einstellungen des Bots gewährleisten zu können und umfangreiche Reaktionen anderer Nutzer hervorzurufen.
Der Bot soll unterschiedliche Aktionen, abhängig von seinen im Vorfeld getätigten Einstellungen, ausführen und verschiedene Reaktionen bei den Nutzern hervorrufen.
Zu den wichtigsten Aktionen der Interaktion zwischen Nutzern zählen "Tweeten", "Liken", "Kommentieren", "Nachrichten schreiben", "Re-Tweeten" und "Folgen". 
Die Aktionen des Bots und die Reaktionen anderer Nutzer sollen im Log einsehbar sein.
Aus den erfassten Daten soll das soziale Leben des Bots beurteilt werden und anschließend in die Studie der Kunden übernommen werden. 

### 2.2 Überblick über die geforderte Funktionalität

Als Anforderung an die Funktionalität ist die Erstellung unterschiedlicher Bots gesetzt.
Ein Bot für das soziale Netzwerk soll erstellt werden können.
Die Erstellung eines Bots soll dabei nicht automatisiert sein.
Die Bots sollen die grundlegensten Aktionen, bestehend aus "Tweeten", "Liken", "Kommentieren", "Nutzer Folgen", "Re-Tweeten" und "Direkte Nachrichten senden" automatisiert durchführen.
Die Bots sollen einen vorgefertigten Text "Tweeten" können, ein "Like" auf bestimmte, vorher definierte "Tweets" geben können und unter ausgewählten "Tweets" einen festgelegten Text in Form eines Kommentars "kommentieren" können.
Jede Aktivität des Bots und die Reaktionen anderer Nutzer sollen in einem Aktivitäten-Log festgehalten werden.
Die Reaktionen anderer Nutzer müssen abgespeichert werden und mit der entsprechenden Aktion des Bots in Verbindung gebracht werden können.
Die Daten aus dem Aktivitäten-Log sollen in einer Übersicht in der Nutzeroberfläche angezeigt werden.
Die Einstellungen für das Verhalten des Bots sollen vom Nutzer getätigt werden können.
Explizit sollen die Nutzer die Texte des Bots und die Stichwörter auf die der Bot reagieren soll einstellen können.
Der Algorithmus für die Zuordnung der Texte des Bots zu den Stichwörtern in Tweets soll austauschbar sein, um in Zukunft andere Relationen zuzulassen.
Standardmäßig soll eine 1-zu-1-Relation von den Texten des Bots zu Stichwörtern geschaffen werden.
Die Relation von Texten zu Stichwörtern soll in Zukunft durch einen anderen Algorithmus austauschbar sein.
Der Algorithmus des Bots muss folglich in einer gesonderten Form gehalten werden, um in Zukunft eine reibunglose Einbindung eines neuen Algorithmus zu gewährleisten.
Die Benutzeroberfläche und die Funktionen des Bots sollen mit jedem Algorithmus, der Daten im selben Format verwendet, arbeiten können.
Die Einstellungen für das Verhalten des Bots sollen über die Stichwörter, auf die der Bot reagieren soll, in Verbindung mit den zugeordneten Texten, getätigt werden.
Außerdem können allgemeine Funktionen wie "Suchen" und "Streaming" zu einem Thema in der Benutzeroberfläche getätigt werden.

### 2.3 Abgrenzung und Einbettung des gewünschten Systems

Das Projekt soll ein einfach zu handhabendes Programm hervorbringen, das ausgeführt werden muss.
Alle wichtigen Funktionalitäten und Daten sollen in der Benutzeroberfläche vereint werden.
Die Funktionalitäten sollen in der Benutzeroberfläche aufrufbar sein und die Daten sollen in einer Übersicht angezeigt werden.
Das Programm soll Betriebssystem unabhängig agieren, um eine Plattform unabhängige Arbeitsweise zu gewährleisten.
Als priorisierte Betriebssysteme werden Windows und MacOS angestrebt.
Die Datenspeicherung soll in einem Format ermöglicht werden, dass, unabhängig vom Betriebssystem, verwendbar ist.
Die Anbindung an das soziale Netzwerk "Twitter" soll vom Programm intern gelöst werden.
Die Verbindung der Software Komponenten untereinander wird vom Programm intern gelöst.

### 2.4 Allgemeine Einschränkungen

Die Software soll das Verhalten des Bots in einer eigenen Datei halten, um das Verhalten in Zukunft austauschbar zu halten. 
Nutzer können durch die Kapselung die Datei mit dem Verhalten, in Zukunft, einfacher austauschen.
Der ursprüngliche Ansatz, den Bot für das soziale Netzwerk "FaceBook" zu entwerfen, wurde aufgrund der Richtlinien von "FaceBook" verworfen.
Die Richtlinien von "FaceBook" verhindern die Umsetzung der geforderten Funktionalitäten. (Siehe "5. Durchführbarkeitsuntersuchungen")

Die automatische Erstellung von Bots für "Twitter" ist nicht möglich und muss händisch durchgeführt werden. 

Die Software muss auf "OpenSource"-Basis gehalten werden und soll bei Bedarf auch nur auf "OpenSource" Software zurückgreifen.
Die verwendete Software soll keine direkten Kosten erzeugen und bei Bedarf nur auf kostenlose Software zurückgreifen.
Das Endprodukt soll keine Lizenz-Eingrenzungen erhalten und für alle Nutzer in vollem Umfang zur Verfügung stehen.
Das Endprodukt wird auschließlich zur nicht kommerziellen Nutzung verwendet.

### 2.5 Vorgaben zu Hardware und Software

Das Programm soll Betriebssystem unabhängig sein, auf OpenSource-Software basieren und keine Kosten verursachen.
An die Hardware sind keine besonderen Anforderungen gestellt.
Die Grundlegenden Eigenschaften zum Ausführen des Bots sind vorausgesetzt.
Zu den grundlegenden Voraussetzungen zählen ein lauffähiger Computer mit Internet-Anbindung.
An den Nutzer sind die Anforderungen gestellt, mit dem Umgang von Software auf dem Computer Erfahrung zu haben.
Das Wissen um die Bedienung von "Twitter" wird als Anforderung gesetzt, um die Funktionalität des Programms verstehen zu können.

Als weitere Software die zum Einsatz kommt wird die offiziele "Twitter" API als anbindung an das soziale Netzwerk "Twitter" verwendet.
Als Programmierumgebung wird "PyCharm" von "JetBrains" in der Version "PyCharm 2018.1.1 (Professional Edition) , Build #Py-181.4445.76".
Für den Datenaustausch wird "GitHub" verwendet. 
Die Dateien zu diesem Projekt werden alle unter dem Repository "SocialBot" unter dem Link "https://github.com/weberval/SocialBot" gesammelt.


### 2.6 Anforderungsquellen / Zielgruppen

Das Hauptziel ist die Auswertung der sozialen Interaktionen zwischen dem Bot und der Umwelt.
Die Hauptnutzer werden durch Studentinnen und Studenten der Universität Basel dargstellt.
Die Hauptnutzer beziehen die Daten für ihre Analyse aus den Daten des Programms.
Die Studienrichtung der Studentinnen und Studenten sind die Sozialwissenschaften.
Explizit sind die Kunden der Kulturanthropologie zugeschrieben.
Weitere Zielgruppen können in Zukunft hinzukommen, sind aber keine geplanten Nutzer des Programms und werden nicht weiter aufgeführt.
Das Programm soll unabhängig vom Nutzer und weiteren Gegebenheiten funktionieren und eine einfach Handhbung garantieren.
Weder Software-technische noch Hardware-technische Einschränkungen sollen auftreten.
Das Programm soll unabhängig von allen Eigenschaften eines beliebigen Computers funktionieren.

## 3. Detailierte Beschreibung der Anforderung (Leistungsmerkmale)

### 3.1 Lieferumfang

Zu der Lieferung gehört ein Programm mit allen zugehörigen Komponenten, eine Dokumentation der implementierten Funktionen und eine Einweisung in die Funktionen der Software.
Die Komponenten des Programms bestehen aus der Benutzeroberfläche, dem Programmteil für die Abwicklung der Funktionen und dem austauschbaren Algorithmus.
Bei Auslieferung des Programms sollen alle benötigten Programmteile, soweit sie in ihrer Entwicklung bis zu diesem Zeitpunkt sind, in einem Paket ausgeliefert werden.
Die Programmteile werden schon eingerichtet und aufeinander abgestimmt an den Kunden geliefert.
Die Dokumentation des Vorgehens und des Ablaufs des Projekts werden in Form eines oder mehrerer Dokumente geliefert.
In den Dokumenten wird festgehalten wie das Projekt verlaufen ist, welche Funktionalitäten implementiert sind, welche Funktionen nicht umsetzbar sind und wie das Programm erstellt wurde.
Außerdem wird ein "End User License Agreement" beigelegt, um die Nutzungsbdeingungen zu klären.
Als letztes wird bei der Auslieferung eine Schrittweise Anleitung mitgeliefert, wie das Programm, für den vorgesehenen Zweck, zu nutzen ist.
In der Anleitung werden Punkte geklärt, wie die Einrichtung des Programms, sofern dies noch notwendig ist, die Erstellung eines "Twitter"-Accounts, die Aktivierung eines "Twitter"-Profils und eine Erklärung aller Funktionen, zusammen mit der jeweiligen Benutzung im Programm.

### 3.2 Abläufe (Szenarien) von Interaktionen mit der Umgebung
> Typische Abläufe z.B. mit Anwendungsfall-Diagrammen darstellen.

'UseCase.svg'

### 3.3 Geforderte Funktionen des Produkts
> Das Produkt wird aus funktionaler Sicht anhand von Anwendungsfällen (Use Cases) beschrieben. Jeder Anwendungsfall wird in Form einer Tabelle spezifiziert:

Die grundlegenden Funktionen im Use Case Diagramm werden genauer beschrieben.
Die Aufgabe "Bot erstellen" beschreibt das Erstellen eines Bots.
Zum Erstellen eines Bots gehört das Anlegen einer App und das Verbinden des Accounts mit der entsprechenden App. 
Die Aufgabe "Bot erstellen" inkludiert die Aufgabe "Botinfo einpflegen". 
Die Aufgabe "Botinfo einflegen" bezeichnet das initiale Festlegen vom Verhalten.
Beim Erstellen des Bots wird das Verhalten des Bots festgelegt.
Außerdem wird die Aufgabe "Twitter Account erstellen" von der Aufgabe "Bot erstellen" inkludiert.
Bei der Aufgabe "Twitter Account erstellen" wird der Account bei "Twitter" angelegt, der fortan verwendet wird.
Bei der Aufgabe "Bot löschen" wird ein bereits erstellter Bot wieder entfernt.
Das Verhalten des Bots wird durch die Aufgabe "Botverhalten anpassen" dargestellt.
Bei der Aufgabe wird das momentane Verhalten des Bots angepasst oder durch ein anderes Verhalten ersetzt.
Die Aufgabe "Begrenzungen setzen" erweitert die Aufgabe "Botverhalten anpassen".
Die Aufgabe legt fest, wieviele Aktionen in einer bestimmten Zeit durchgeführt werden können.
Die Aufgabe "Botprotokoll betrachten" beschreibt die Funktion, das Log des Bots anzuzeigen.
Die Aufgabe "Export Protokoll" erweitert die Aufgabe "Botprotokoll betrachten", um den Export des Logs eines Bots.
Bei der Aufgabe "Bot starten/stoppen" handelt es sich um die Funktion einen Bot starten oder stoppen zu lassen.
Die Aufgabe "Login Twitter" erweitert die Aufgabe "Bot starten/stoppen" um die Funktion den Account von Twitter einzuloggen. 
Die Aufgabe "Logout Twitter" erweitert die Aufgabe "Bot starten/stoppen" um die Funktion den Account von Twitter auszuloggen.

Bot erstellen
-> Botinfo einpflegen 
-> Twitter Account erstellen
Bot löschen
Botverhalten anpassen
Botprotokoll anpassen
<- Begrenzung setzen
Botprotokoll betrachten
<- Export Protokoll
Bot start/stop
<- Logout Twitter
-> Login Twitter

| Bezeichnung      		   | XXX |
| Zusammenfassung		   | XXX |
| Akteure  			   | XXX |
| Vorbedingung 			   | XXX |
| Ablaufbeschreibung 		   | XXX |
| Verwendungen (Include-Beziehung) | XXX |
| Erweiterungen (Extend-Beziehung) | XXX |
| Alternativen  		   | XXX |
| Nachbedingung 		   | XXX |
| Fehlschlag    		   | XXX |

### 3.4 Struktur und Verhalten des Systems
> Beschreibung der verschiedenen statischen Strukturaspekte des Systems (Klassen-, Paket-, Komponenten-, Verteilungsdiagramm) sowie Beschreibung der Dynamik, der internen Abläufe und des Zusammenspiels der Systemteile (Aktivität-, Sequenz-, Zustand-, Timingdiagramm).

*Klassendiagramm*

### 3.5 Schnittstellen des gewünschten System
> Beschreibung der Benutzerschnittstellen; Beschreibung der Schnittstellen zu anderen Soft- und Hardwaresystemen. Zu berücksichtigende Normen

Der Grundbaustein der Anwendung besteht aus einer inoffizielen "Phyton-Twitter"-API. 
Aufgrundlage dieser "Twitter-Phyton"-API wird die Anwendung aufgebaut.
Das Programm erweitert jede Funktion der "Twitter-Phyton"-API, um das geforderte Log und weitere zusätzliche Funktionen. 
Für jeden Bot wird ein neues Log angelegt, das für jeden Bot tageweise gespeichert wird.
Änderungen am Verhalten des Bots und ausgeführte Aktionen des Bots werden in das entsprechende Log des Bots eingetragen.
Das Log kann jederzeit im Programm angezeigt und ausgelesen werden oder die entsprechende Datei kann außerhalb des Programms geöffnet werden.
Die Funktionen für den Nutzer werden in einem Nutzer Interface bereit gestellt.
Das Nutzer Interface stellt die meisten Funktionen für die Nutzer über Buttons zur Verfügung.
Die möglichen Funktionen, die über einen Button Klick ausführbar sind, beschränken sich auf "Bot erstellen", "Bot löschen", "Botverhalten anpassen", "Botprotokoll betrachten", und "Bot starten/stoppen".
Um einen neuen Bot anzulegen, wird die Funktion "Bot erstellen" über den entsprechenden Button ausgeführt.
Anschließend wird der Bot erstellt und das Verhalten für den Bot wird eingestellt.
Um einen bereits erstellten Bot zu entfernen, wird über den Button "Bot löschen" die entsprechende Funktion ausgeführt.
Um die bereits erstellten Bots in ihrem Verhalten anzupassen, wird die Funktion, zum Verändern des Verhaltens, über den Button "Botverhalten anpassen" ausgeführt.
Um einen bereits erstellten Bot in Betrieb zu nehmen oder ihn anschließend wieder zu stoppen, wird der Button "Bot starten/stoppen" verwendet.
Der Button startet den ausgewählten Bot oder stoppt ihn wieder, sollte er bereits aktiv sein.
Nachdem ein Bot in Betrieb genommen wurde und der Bot die gewünschten Aktivitäten ausgeführt hat, kann das Log für den Bot angezeigt werden.
Das Log kann über den Button "Botprotokoll betrachten" angezeigt werden.

### 3.6 Zu berücksichtigende Normen

Für das Projekt sind keine Normen zu beachten. 
Die Nutzung der Software ist nur für die private Nutzung innerhalb der Universität Basel ausgelegt.
Die AGBs von Twitter geben den Rahmen für das Programm vor.

Die Software behandelt keine Lebensbedrohlichen Systeme oder kann zur direkten Gefährdung von Menschen führen.
Die Software ist an die allgemeinen Geschäftsbedingungen des sozialen Netzwerks gebunden.
Die durch das Programm enstehenden Gefahren für Nutzer und andere involvierte Personen unterliegen nicht den Entwicklern.
Die Benutzer der Software müssen sich der Gefahr, die ein Bot in einem sozialen Netzwerk hat, bewusst sein.
Die durch einen Bot enstandenen Veränderungen und Auswirkungen unterliegen nicht den Entwicklern, vielmehr dem Nutzer.
Der Nutzer ist selbst verantwortlich und trägt selbst jegliche Konsequenzen für die Auwirkungen eines Bots.
Die Entwickler behalten sich vor, die Daten zur späteren Auswertung von den Nutzern einzuziehen.
Die Entwickler haften nicht für den Missbrauch der Software.
Für den Einsatz der Software entgegen den ursprünglichen Nutzungbestimmungen haftet der Nutzer.
Der Wiederverkauf der Software ist nicht genehmigt und Strafbar.
Die Entwickler übernehemen keine Haftung für Schäden jeglicher Art.

### 3.7 Qualitätsanforderungen / sonstige Entwicklerorientierte Anforderungen

Spezifikation von Anforderungen hinsichtlich Performance, Ressourcen, Safety (Schutz und Sicherheit), Datensicherheit, Portabilität, Reliability, Wartung, Wiederverwendung, Usability, Serviceability

## 4. Vorgaben des Auftraggebers an die Projektabwicklung

### 4.1 Anforderungen an die Realisierung
> z. B. Angaben über zu verwendende Software, Hardware, Entwicklungsmethode, Termine, Ausbaustufen, zugekaufte Produkte

Als Vorgaben an das Projekt sind die Entwicklungsmethode und der Zeitraum gesetzt.
Die eingesetzte Entwicklungsmethode ist Kanban.
Bei Kanban handelt es sich um eine agile Entwicklungsmethode.
Die Aufgaben werden in Form von Backlog Items festgehalten und durch die einzelnen Bearbeitungsschritte durchgeführt.
Die Bearbeitungsschritte bestehen aus Product Backlog, Bereit, Entwicklung, Release und Fertig.
Ein Product Backlog Item wird von einem Mitarbeiter oder von mehreren durch die gesamten Bearbeitungsschritte geführt.
Die einzelnen Bearbeitungsschritte sind auf eine bestimmte Anzahl an Items beschränkt, die sich maximal in diesem Schritt befinden dürfen.
Es können dynamisch neue Product Backlog Items in das Product Backlog hinzugefügt werden und die Aufgaben können dynamisch bearbeitet werden.
Es gibt keine zeitliche Vorgabe für die Bearbeitung eines Product Backlog Items, noch eine mindest Anforderung an der Anzahl die ein Mitarbeiter bearbeiten muss.
Insgesamt wird dadurch Agil entwickelt.
Als terminliche Vorgabe ist der Zeitraum des Semesters gesetzt.
Das Projekt soll vom ersten Vorlesungstermin bis zum letzte Vorlesungstermin laufen.
Als genauer Zeitraum ist 04.04.2018 bis 13.06.2018 gesetzt.
Die eingesetzten Versionen der Software werden im folgenden aufgelistet.
> PyCharm -- PyCharm 2018.1.1 (Professional Edition) , Build #Py-181.4445.76
> Python3 -- Python 3.6.3
> TwitterAPI -- TwitterAPI 3.0
> 
Zur Entwicklung wurden die aufgelisteten Software-Komponenten verwendet.
Es wurde auf handelsüblichen Computer mit Internetanbindung entwickelt.
Aus den Forderungen geht hervor, dass für die Umsetzung keine zusätzlichen Software-Komponenten erkauft wurden.
Die eingesetzten Software-Komponenten sind nicht kostenpflichtig und frei verfügbar.


### 4.2 Abnahmebedingungen
> Bedingungen des Auftraggebers für die Abnahme, wogegen?, wie?, welche Unterlagen

Für die Abnahme des Kunden sind eine Dokumentation und eine Anleitung, zur Bedienung des Programms, unablässlich.
Die Dokumentation umfasst die geleistete Arbeit und die umgesetzten Funktionen.
In der Dokumentation müssen zusätzlich die Anforderungen und die Probleme festgehalten sein.
Die Anleitung zur Bedienung des Programms, muss die Einrichtung des Bots und die Bedienung der Funktionalitäten des Programms umfassen.

### 4.3 Fertige und zugekaufte Komponenten
> z. B. Standardsoftware, wiederverwendete eigene Software, Software des Auftraggebers, Betriebssysteme, ...

Für die Entwickung wurden keine zusätzlichen Komponenten gekauft.
Die zur Enwticklung verwendeten Komponenten sind kostenlose Lösungen und für den Nutzer frei zugänglich.
Die verwendeten Software-Komponenten sind unter "4.1 Anforderungen an die Realisierung" aufgeführt.
Die Hardware-Anforderungen sind auf einen handelsüblichen Computer mit Internetanbindung beschränkt.
Durch das Betriebssystem wird keine Einschränkung erzielt.

### 4.4 Lieferbedingungen
> z.B. Lieferplan mit Terminen, Form der Lieferungen, geforderte Dokumentation

Die Lieferungen werden in Form von regelmäßigen Lieferungen durchgeführt.
Der aktuelle Stand der software ist durchgängig auf dem angegebenen Repository auf "GitHub" für die Nutzer verfügbar.
Sofern die Nutzer den Stand kontrollieren wollen, besteht jederzeit die Möglichkeit die Software herunterzuladen.
Andernfalls wird mit Abschluss des Projekts, das Endprodukt mit allen vereinbarten Komponenten an die Kunden ausgelifert.
Der endgültig angestrebte Lieferzeitpunkt ist auf den 13.06.2018 angesetzt.

### 4.5 Gewährleistung

Unter den Bedingungen, dass dies ein nicht kommerzielles Projekt für eine Universität ist, entfällt jegliche Garantie und Gewährleistung.
Für die Software wird keine Wartung oder Fehlerbehebung nach Auslieferung durchgeführt.
Die Fehler, die während der Entwicklung auftreten, werden behoben und die Software wird, mit dem Stand zum Zeitpunkt der Auslieferung, ausgeliefert.
Es werden nach der Auslieferung keine Funktionen nachgeliefert oder das Produkt aktualisiert.
Für die Fehlerfreie Funktionsfähigkeit wird nach Auslieferung nicht gesorgt, ebenso wenig wie für die Funtkionsfähigkeit der Software mit anderen Version der benutzen Software-Komponenten.
Auch die Funktionsfähigkeit für das soziale Netzwerk "Twitter" wird für zukünftige Versionen nicht gewährleistet.
Der ausgelieferte Stand entspricht dem gewährleisteten Stand der Software.
Da dies ein Forschungsprojekt ist, entfällt jegliche Gewährleistung und Wartung.

## 5. Durchführbarkeitsuntersuchungen
> Markt- und Kundenanalyse, Durchführbarkeitsanalyse,...

Beim ersten Ansatz wurde als soziales Netzwerk "FaceBook" angestrebt.
Bei der Abstimmung der umsetzbaren Funktionalität gegenüber den Anforderungen wurde festgestellt, dass die Umsetzung nahezu unmöglich ist.
Durch die strengen Richtlinien von "FaceBook" werden die meisten Funktionen für ein externes Programm gesperrt.
Um die Funktionen umsetzen zu können, würde ein enormer Mehraufwand notwendig werden und die Zukunftsfähigkeit wird stark eingeschränkt.
Die Umsetung ist abhängig von der momentanen Version von "FaceBook" und den damit eingeführten Richtlinien.
Die Richtlinien haben in den letzen Monaten immer mehr und mehr Funktionen von "FaceBook" für den externen Gebrauch gesperrt und mit der momentanen Debatte (Stand: 18.04.2018) werden weitere Funktionen gesperrt und gesperrt werden.
Durch die eingeschränkte Funktionalität können den Kunden nicht die geforderten Anforderungen garantiert werden.
Um dem Kunden das beste Gesamtergebnis zu gewährlsieten wird auf die soziale Plattform "Twitter" gewechselt.
Die Kunden sind  nicht explizit an ein soziales Netzwerk gebunden, da der Fokus auf der Interaktion mit anderen Nutzern in einem beliebigen sozialen Netzwerk liegt.
Bei genauerer Analyse der Funktionalitäten gegenüber den Anforderungen hat sich "Twitter" als beste Alternative heraus kristallisiert.
Das Projekt wird auf das soziale Netzwerk "Twitter" umgestellt und die bisherige Arbeit wird überarbeitet und an die Gegebenheiten von "Twitter" angepasst.

## 6. Bewertung der Anforderungen
> Falls bei der Beschreibung der funktionalen Eigenschaften des Produkts noch nicht erfolgt: Klassifizierung, Priorisierung, Auswahl (Paketierung) mit Auswahlbegründungen

## 7. Verpflichtungen des Auftaggebers
> z.B.: gestellte Hardware / Software, Schulung von Entwicklern oder von Auftraggeberpersonal, Ansprechpartner, zur Verfügung stellen von Räumen, Rechenzentrum, Reaktionszeiten des Auftraggebers auf Anfragen

Der Auftraggeber verpflichtet sich, mit den aufkommenden Anforderungen zeitnah zu den Entwicklern zu kommen.
Die Auftraggeber unterliegen der Verantwortung, das Projekt mit ihren Wünschen voranzutreiben.
Die gewünschten Anforderungen werden an die Entwickler weitergetragen und von den Entwicklern in den "User Requirements Specification" niedergeschrieben.
Die Auftraggeber verpflichten sich, die in den "User Requirements Specification" nidergeschriebenen Anforderungen, duchzulesen und zu akzeptieren.