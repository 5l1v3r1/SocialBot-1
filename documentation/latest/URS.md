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

--

## 2. Allgemeine Beschreibung des gewünschten Systems

Das Projekt besteht aus der Erstellung von Bots für das soziale Netzwerk "Twitter".
Die soziale Plattform "Twitter" ist eine Internetseite, auf der Personen miteinander kommunizieren und Meinungen miteinander teilen können.
Die Personen haben ein eigenes Profil und können über mehrere Möglichkeiten mit anderen Nutzern in Kontakt treten.
Zu den wichtigsten Aktionen der Interaktion zwischen Nutzern zählen "Tweeten", "Liken", "Kommentieren", "Nachrichten schreiben", "Re-Tweeten" und "Folgen". 
Zu den ursprünglichen Anforderungen zählte die Anbindung an das soziale Netzwerk "FaceBook".
Die Aktionen bei "Twitter" haben Äquivalente Aktionen bei "FaceBook".
Das Äquivalent zu "Tweeten" ist "Posten", "Liken", "Kommentieren" und "Persönliche Nachrichten" werden in beiden sozialen Netzwerken gleich gehandhabt.
Das Äquivalent zu "Re-Tweeten" in "Twitter" ist "Teilen" in "FaceBook" und zu "Folgen" ist das Äquivalent eine "Freundschaft".
Die Bots sollen die wichtigsten Aktionen in "Twitter" automatisiert ausführen und auf vordefinierte "Tweets" automatisiert reagieren.
Der Nutzer kann die Aktionen, Reaktionen und die Stichwörter der "Tweetes" im Vorfeld selbst definieren und ändern.
In einem Log sollen alle Aktionen des Bots einsehbar sein.
Jeder "Tweet" des Bots, jede Reaktion auf einen "Tweet" und jegliche andere Aktivität des Bots soll im Log zusammen mit den Reaktionen anderer Nutzer beobachtbar sein.

### 2.1 Zweck des gewünschten Systems

Der Zweck des Projekts besteht aus der Beobachtung des sozialen Aspekts eines Bots in einem Sozialen Netzwerk.
Die Interaktion des Bots mit anderen Nutzern, eventuell auch dargestellt durch andere Bots, soll beobachtet werden.
Die Interaktion mit anderen Nutzern in Form von Menschen steht im Mittelpunkt der Beobachtung.
Besonders die Reaktionen der anderen Nutzer auf den Bot sind der Haupt Beobachtungsaspekt.
Flexibilität des Bots ist wichtig, um unterschiedliche soziale Einstellungen des Bots gewährleisten zu können und umfangreiche Reaktionen anderer Nutzer hervorzurufen.
Der Bot soll unterschiedliche Aktionen, abhängig von seinen im Vorfeld getätigten Einstellungen, ausführen und verschiedene Reaktionen bei den Nutzern hervorrufen.
Die Aktionen des Bots und die Reaktionen anderer Nutzer sollen im Log einsehbar sein.
Aus den erfassten Daten soll das soziale Leben des Bots beurteilt werden und anschließend in die Studie der Kunden übernommen werden. 

### 2.2 Überblick über die geforderte Funktionalität

Als Anforderung an die Funktionalität ist die Erstellung unterschiedlicher Bots gesetzt.
Ein Bot für das soziale Netzwerk soll, nicht automatisiert, erstellt werden können.
Die Bots sollen die grundlegensten Aktionen, bestehend aus "Tweeten", "Liken", "Kommentieren", "Nutzer Folgen", "Re-Tweeten" und "Direkte Nachrichten senden" automatisiert durchführen.
Die Bots sollen einen vorgefertigten Text "Tweeten" können, ein "Like" auf bestimmte, vorher definierte "Tweets" geben können und unter ausgewählten "Tweets" einen festgelegten Text in Form eines Kommentars "kommentieren" können.
Jede Aktivität des Bots und die Reaktionen anderer Nutzer sollen in einem Aktivitäten-Log festgehalten werden.
Die Reaktionen anderer Nutzer müssen abgespeichert werden und mit der entsprechenden Aktion des Bots in Verbindung gebracht werden können.
Die Daten aus dem Aktivitäten-Log sollen in einer Übersicht in der Nutzeroberfläche angezeigt werden.
Die Einstellungen für das Verhalten des Bots sollen vom Nutzer getätigt werden können.
Explizit sollen die Nutzer die Texte des Bots und die Stichwörter auf die der Bot reagieren soll einstellen können.
Der Algorithmus für die Zuordnung der Texte des Bots zu den Stichwörtern in Tweets soll austauschbar sein, um in Zukunft andere Relationen zuzulassen.
Standardmäßig soll eine 1-zu-1-Relation von den Texten des Bots zu Stichwörtern geschaffen werden.
Die Relation von Texten zu Stixhwörtern soll in Zukunft durch einen anderen Algorithmus austauschbar sein.
Der Algorithmus des Bots muss floglich in einer gesonderten Form gehalten werden, um in Zukunft eine reibunglose Einbindung eines neuen Algorithmus zu gewährleisten.
Die Benutzeroberfläche und die Funktionen des Bots sollen mit jedem Algorithmus, der Daten im selben Format verwendet, arbeiten können.
Die Einstellungen für das Verhalten des Bots sollen über die Stichwörter, auf die der Bot reagieren soll, in Verbindung mit den zugeordneten Texten, getätigt werden.
Außerdem können allgemeine Funktionen wie "Suchen" und "Streaming" zu einem Thema in der Benutzeroberfläche getätigt werden.

### 2.3 Abgrenzung und Einbettung des gewünschten Systems

Das Projekt soll ein einfach zu handhabendes Programm hervorbringen, dass ausgeführt werden muss.
Alle wichtigen Funktionalitäten und Daten sollen in der Benutzeroberfläche vereint werden.
Die Funktionalitäten sollen in der Benutzeroberfläche aufrufbar sein und die Daten sollen in einer Übersicht angezeigt werden.
Das Programm soll Betriebssystem unabhängig agieren, um eine Plattform unabhängige Arbeitsweise zu gewährleisten.
Als priorisierte Betriebssysteme werden Windows und MacOS angestrebt.
Des weiteren soll die Software "OpenSource" gehalten werden, aufgrund der Konstitutionellen Voraussetzungen. 
Die verwendete Software soll keine Kosten erzeugen und auf kostenloser Software basieren.
Das Endprodukt soll keine Lizenz-Eingrenzungen erhalten und für alle Nutzer in vollem Umfang zur Verfügung stehen.
Das Endprodukt wird auschließlich zur nicht kommerziellen Nutzung verwendet.
Die Anbindung an das soziale Netzwerk "Twitter" soll vom Programm intern gelöst werden.
Die Verbindung der Software Komponenten untereinander wird vom Programm intern gelöst.

### 2.4 Allgemeine Einschränkungen

Die Software soll das Verhalten des Bots in einer eigenen Datei halten, um das Verhalten in Zukunft austauschbar zu halten. 
Nutzer können durch die Kapselung die Datei mit dem Verhalten, in Zukunft, einfacher austauschen.
Der ursprüngliche Ansatz, den Bot für das soziale Netzwerk "FaceBook" zu entwerfen, wurde aufgrund der Richtlinien von "FaceBook" verworfen.
Die Richtlinien von "FaceBook" verhindern die Umsetzung der geforderten Funktionalitäten. (Siehe "5. Durchführbarkeitsuntersuchungen")
Die automatische Erstellung von Bots für "Twitter" ist nicht möglich und muss händisch durchgeführt werden.
Die Software muss auf OpenSource Software-Lösungen basieren, um Kosten zu vermeiden.

### 2.5 Vorgaben zu Hardware und Software

Das Programm soll Betriebssystem unabhängig sein, auf OpenSource-Software basieren und keine Kosten verursachen.
Das Programm wird mit Python 3.6.3 entwickelt.
Als weitere Software die zum Einsatz kommt wird die offiziele "Twitter" API als anbindung an das soziale Netzwerk "Twitter" verwendet.
Als Programmierumgebung wird "PyCharm" von "JetBrains" in der Version "PyCharm 2018.1.1 (Professional Edition) , Build #Py-181.4445.76".
Für den Datenaustausch wird "GitHub" verwendet.
Die Dateien zu diesem Projekt werden alle unter dem Repository "SocialBot" unter dem Link "https://github.com/weberval/SocialBot" gesammelt.
An die Hardware sind keine besonderen Anfordewrungen gestellt.
Die Grundlegenden Eigenschaften zum Ausführen des Bots sind vorausgesetzt.
Zu den grundlegenden Voraussetzungen zählen ein lauffähiger Computer mit Internet-Anbindung.
An den Nutzer sind die Anforderungen gestellt, mit dem Umgang von Software auf dem Computer Erfahrung zu haben.
Das Wissen um die Bedienung von "Twitter" wird als Anforderung gesetzt, um die Funktionalität des Programms verstehen zu können.

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
Als letztes wird bei Auslieferung eine Schrittweise ANleitung mitgeliefert, wie das Programm zu nutzen ist, für den vorgesehenen Zweck.
Die Einrichtung des Programms, sofern dies noch notwendig ist, die Erstellung eines "Twitter"-Accounts, die Aktivierung eines "Twitter"-Profils und eine Erklärung aller Funktionen, zusammen mit der jeweiligen Benutzung im Programm.

### 3.2 Abläufe (Szenarien) von Interaktionen mit der Umgebung
> Typische Abläufe z.B. mit Anwendungsfall-Diagrammen darstellen.

### 3.3 Geforderte Funktionen des Produkts
> Das Produkt wird aus funktionaler Sicht anhand von Anwendungsfällen (Use Cases) beschrieben. Jeder Anwendungsfall wird in Form einer Tabelle spezifiziert:

Die Funktionen des Produkts bestehen aus der Erstellung eines Bots, der Verwaltung eines Bots und dem Löschen eines Bots.
Zu den Funktionen des Bots zählen das "Tweeten", das "Re-Tweeten", das "Liken", das "Kommentieren", das "Folgen" und "Nachrichten schreiben".
Bot erstellen
Bot verwalten
Bot löschen
Tweeten
Re-Tweeten
Liken
Kommentieren
Folgen
Nachricht schreiben 

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

Das Programm baut auf einer inoffizielen "Phyton-Twitter"-API auf. 
Aufgrundlage dieser "Twitter-Phyton"-API wird die Anwendung aufgebaut.
Unser Programm erweitert jede Funktion der "Twitter-Phyton"-API, um das geforderte Log. 
Für jeden Bot wird ein neues Log angelegt, das für jeden Bot gespeichert wird.
Änderungen am Verhalten des Bots und ausgeführte Aktionen des Bots werden in das entsprechende Log des Bots eingetragen.
Das Log kann jederzeit im Programm angezeigt und ausgelesen werden.
Die Funktionen für den Nutzer werden in einem Nutzer Interface bereit gestellt.
Das Nutzer Interface stellt die meisten Funktionen für die Nutzer über Buttons zur Verfügung.
Die möglichen Funktionen, die über einen Button Klick ausführbar sind, beschränken sich auf "Bot erstellen", "Bot löschen", "Botverhalten anpassen", "Botprotokoll betrachten", und "Bot starten/stoppen".
Um einen neuen Bot anzulegen, wird die Funktion "Bot erstellen" über den entsprechenden Button ausgeführt.
Anschließend wird der Bot erstellt und das Verhalten für den Bot wird eingestellt.
Um einen bereits erstlellten Bot zu entfernen, wird über den Button "Bot löschen" die entsprechende Funktion ausgeführt.
Um die bereits erstellten Bots in ihrem Verhalten anzupassen, wird die Funktion, zum Verändern des Verhaltens, über den Button "Botverhalten anpassen" ausgeführt.
Um einen bereits erstellten Bot in Betrieb zu nehmen oder ihn anschließend wieder zu stoppen, wird der Button "Bot starten/stoppen" verwendet.
Der Button startet den ausgewählten Bot oder stoppt ihn wieder, sollte er bereits laufen.
Nachdem ein Bot in Betrieb genommen wurde und Aktionen ausgeführt wurden, kann das Log für den Bot angezeigt werden.
Das Log kann über den Button "Botprotokoll betrachten" angezeigt werden.

### 3.6 Zu berücksichtigende Normen

Für das Projekt sind keine Normen zu beachten. 
Die Nutzung der Software ist nur für die private Nutzung innerhalb der Universität Basel ausgelegt.
Die private Nutzung innerhalb einer Universität unterliegt keinen Normen.

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
Ein Product Backlog Item wird von einem Mitarbeiter oder von mehreren durch die gesamten Bearbeitungsschritte grführt.
Die einzelnen Bearbeitungsschritte sind auf eine bestimmte Anzahl an Items beschränkt, die sich maximal in diesem Schritt befinden dürfen.
Es können dynamisch neue Product Backlog Items in das Product Backlog hinzugefügt werden und die Aufgaben können dynamisch bearbeitet werden.
Es gibt keine zeitliche Vorgabe für die Bearbeitung eines Product Backlog Items, noch eine mindest Anforderung an der Anzahl die ein Mitarbeiter bearbeiten muss.
Insgesamt wird dadurch Agil entwickelt.
Als terminliche Vorgabe ist der Zeitraum des Semesters gesetzt.
Das Projekt soll vom ersten Vorlesungstermin bis zum letzte Vorlesungstermin laufen.
Als genauer Zeitraum ist 04.04.2018 bis 13.06.2018 gesetzt.

### 4.2 Abnahmebedingungen
> Bedingungen des Auftraggebers für die Abnahme, wogegen?, wie?, welche Unterlagen

Für die Abnahme des Kunden sind eine Dokumentation und eine Anleitung, zur Bedienung des Programms unablässlich.
Die Dokumentation umfasst die geleistete Arbeit und die umgesetzten Funktionen.
In der Dokumentation müssen zusätzlich die Anforderungen und die Probleme festgehalten sein.
Die Anleitung zur Bedienung des Programms, muss die Einrichtung des Bots und die Bedienung der Funktionalitäten des Programms umfassen.

### 4.3 Fertige und zugekaufte Komponenten
> z. B. Standardsoftware, wiederverwendete eigene Software, Software des Auftraggebers, Betriebssysteme, ...



### 4.4 Lieferbedingungen
> z.B. Lieferplan mit Terminen, Form der Lieferungen, geforderte Dokumentation



### 4.5 Gewährleistung

Unter den Bedingungen, dass dies ein nicht kommerzielles Projekt für eine Universität ist, entfällt jegliche Garantie und Gewährleistung.
Eine Wartung ist für die Software nicht vorgesehen.
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

