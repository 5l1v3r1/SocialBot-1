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
Die Bots sollen die grundlegensten Aktionen, bestehend aus "Tweeten", "Liken", "Kommentieren", "Folgen", "Re-Tweeten" und "Direkte Nachrichten senden" automatisiert durchführen.
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

### 2.5 Vorgaben zu Hardware und Software

Das Programm soll Betriebssystem unabhängig sein, auf OpenSource-Software basieren und keine Kosten verursachen.
Das Programm wird mit Python 3.6.3 entwickelt.

### 2.6 Anforderungsquellen / Zielgruppen

Das Hauptziel ist die Auswertung der sozialen Interaktionen zwischen dem Bot und der Umwelt.
Die Hauptnutzer werden durch Studentinnen und Studenten der Universität Basel dargstellt.
Die Hauptnutzer beziehen die Daten für ihre Analyse aus der Auswertung der Daten zu den Interaktionen des Bots.
Die Studienrichtung der Studentinnen und Studenten sind die Sozialwissenschaften.
Weitere Zielgruppen können in Zukunft hinzukommen und müssen nicht explizit aufgeführt werden.
Das Programm soll unabhängig vom Nutzer funktionieren und eine einfach Handhbung garantieren.

## 3. Detailierte Beschreibung der Anforderung (Leistungsmerkmale)

### 3.1 Lieferumfang

Zu der Lieferung gehört ein Programm mit allen zugehörigen Komponenten, eine Dokumentation der implementierten Funktionen und eine Einweisung in die Funktionen der Software.
Die Komponenten des Programms bestehen aus der Benutzeroberfläche, dem Programmteil für die Abwicklung der Funktionen und dem austauschbaren Algorithmus.
Die Dokumentation des Vorgehens und des Ablaufs des Projekts werden in Form eines oder mehrerer Dokumente geliefert.
Und des weiteren wird eine einfache Einleitung für die Verwendung des Programms geliefert.

### 3.2 Abläufe (Szenarien) von Interaktionen mit der Umgebung
> Typische Abläufe z.B. mit Anwendungsfall-Diagrammen darstellen.

### 3.3 Geforderte Funktionen des Produkts
> Das Produkt wird aus funktionaler Sicht anhand von Anwendungsfällen (Use Cases) beschrieben. Jeder Anwendungsfall wird in Form einer Tabelle spezifiziert:

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

### 3.5 Schnittstellen des gewünschten System
> Beschreibung der Benutzerschnittstellen; Beschreibung der Schnittstellen zu anderen Soft- und Hardwaresystemen. Zu berücksichtigende Normen

### 3.6 Zu berücksichtigende Normen

### 3.7 Qualitätsanforderungen / sonstige Entwicklerorientierte Anforderungen

Spezifikation von Anforderungen hinsichtlich Performance, Ressourcen, Safety (Schutz und Sicherheit), Datensicherheit, Portabilität, Reliability, Wartung, Wiederverwendung, Usability, Serviceability

## 4. Vorgaben des Auftraggebers an die Projektabwicklung

### 4.1 Anforderungen an die Realisierung
> z. B. Angaben über zu verwendende Software, Hardware, Entwicklungsmethode, Termine, Ausbaustufen, zugekaufte Produkte

### 4.2 Abnahmebedingungen
> Bedingungen des Auftraggebers für die Abnahme, wogegen?, wie?, welche Unterlagen

### 4.3 Fertige und zugekaufte Komponenten
> z. B. Standardsoftware, wiederverwendete eigene Software, Software des Auftraggebers, Betriebssysteme, ...

### 4.4 Lieferbedingungen
> z.B. Lieferplan mit Terminen, Form der Lieferungen, geforderte Dokumentation

### 4.5 Gewährleistung

Da dies ein Forschungsprojekt ist, entfällt jegliche Gewährleistung und Wartung

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

