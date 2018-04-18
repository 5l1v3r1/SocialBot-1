# User Requirement Specification

## 1. Einleitung

In diesem Dokument werden die User Requirements für das Projekt "Social Life eines Bots" festgehalten.
Bei dem Projekt handelt es sich um die Erstellung eines Bots für die Soziale Internetseite "FaceBook".
Die Bots sollen automatisiert bestimmte Funktionen ausführen und dabei beobachtet werden können.
Die Anforderungen an diese Bots werden im Folgenden genauer dokumentiert.

### 1.1 Zweck des Dokuments

In diesem Dokument werden die User Requirements für den Kundenauftrag festgelegt. 
Die Kundenansprüche werden festgehalten, um einen Überblick zu erschaffen und den Umfang des Projekts zu definieren.
Die Anforderungen definieren die zu erledigende Arbeit und definieren den Umfang, der geleistet werden muss.

### 1.2 Gültigkeit des Dokuments

Erstellung des Dokuments: 11.04.2018

### 1.3 Begriffsbestimmung und Abkürzungen

--

### 1.4 Zusammenhang mit anderen Dokumenten

--

## 2. Allgemeine Beschreibung des gewünschten Systems

Das Projekt besteht aus der Erstellung von Bots für das soziale Netzwerk "FaceBook".
Die soziale Plattform "FaceBook" ist eine Internetseite, auf der Personen miteinander kommunizieren und Ereignisse teilen können.
Die Personen haben ein eigenes Profil und können über mehrere Möglichkeiten mit anderen Nutzern in Kontakt treten.
Zu den wichtigsten Aktionen der Interaktion zwischen Nutzern zählen "Posten", "Liken", "Kommentieren", "Nachrichten schreiben", "Teilen" und "Freundschaftsanfragen schicken". 
Die Bots sollen die wichtigsten Aktionen automatisiert ausführen und auf vordefinierte Ereignisse automatisiert reagieren.
Die Aktionen und Reaktionen auf Ereignisse und die Ereignisse sollen im Vorfeld definiert werden.
Der Nutzer kann die Aktionen, Reaktionen und Ereignisse selbst definieren und umändern.
Die priorisierten Aktionen bestehen aus "Posten", "Kommentieren" und "Liken". 
Jede Aktion und Reaktion, samt allen zugehörigen Parametern sollen in einem Log festgehalten werden.
Das Log muss die Aktionen des Bots enthalten und die Reaktion anderer Nutzer auf die Aktion.
Die Aktionen des Bots sollen jederzeit im Log einsehbar sein.

### 2.1 Zweck des gewünschten Systems

Der Zweck des Projekts besteht aus der Beobachtung des sozialen Aspekts eines Bots in einem Sozialen Netzwerk.
Die Interaktion des Bots mit Seiten, anderen Nutzern und eventuell anderen Bots soll beobachtet werden.
Die Interaktion mit anderen Nutzern in Form von Menschen steht im Mittelpunkt der Beobachtung.
Flexibilität des Bots ist wichtig, um möglichst unterschiedliche Interaktionen zu fördern und umfangreiche Reaktionen zu erreichen.
Der Bot soll unterschiedliche Aktionen und Reaktionen durchführen. 
Dabei sollen verschiedene soziale Einstellungen und die Reaktionen von anderen Nutzern auf die Aktionen beobachtet werden.
Die Interaktion zwischen dem Bot und den Nutzern soll, abhängig von der sozialen Einstellung, verschiedene Reaktionen hervorrufen.
Die verschiedenen Reaktionen der Nutzer auf den Bot, sollen festgehalten werden, um den sozialen Aspekt des Bots beobachten zu können.
Aus den erfassten Daten soll das soziale Leben des Bots beurteilt werden und anschließend in die Studie der Kunden übernommen werden. 

### 2.2 Überblick über die geforderte Funktionalität

Als Forderung an die Funktionalität ist die Erstellung unterschiedlicher Bots gesetzt.
Die Bots sollen die einfachsten Aktionen, bestehend aus "Posten", "Liken" und "Kommentieren", automatisiert durchführen.
Die Bots sollen einen "Post" anhand einem vorgefertigten Text erstellen und veröffentlichen können, ein "Like" auf bestimmte, vorher definierte "Posts" geben können und unter ausgewählten "Posts" einen festgelegten Text in Form eines "Kommentars" kommentieren können.
Jede Aktivität des Bots soll in einem Aktivitäten-Log festgehalten werden.
Beim Festhalten der Aktivität liegt der Fokus darauf die Aktivität des Bots mit den Reaktionen der anderen Nutzer auf die Aktivität festzuhalten.
Die Reaktionen anderer Nutzer muss abgespeichert werden und mit der entsprechenden Aktion des Bots in Verbindung gebracht werden können.
Die gespeicherten Aktionen des Bots und die Reaktionen anderer Nutzer müssen anschaulich angezeigt werden, um die Interaktion auswerten zu können.
Der Algorithmus für die Aktivitäten des Bots soll austauschbar sein.
Der Algorithmus des Bots muss in einer gesonderten Form gehalten werden, um in Zukunft eine reibunglose Einbindung eines neuen Algorithmus zu gewährleisten.
Der Programmteil ohne Algorithmus muss mit jeder Form von Algorithmus, der Daten im selben Format nutzt, arbeiten können.
Die Einstellung des Bots, über den Algorithmus, muss Flexibilität bieten.
Die Möglichkeit muss bestehen, jeden Bot unterschieldlich einzustellen, um andere Aktionen und Reaktion anderer Nutzer hervor zu bringen.
Die sozialen Einstellungen des Bots müssen konfigurierbar sein und bei jedem Bot anders einstellbar sein.
Als weitere Aktivitäten für den Bot stehen die Handhabung von "Freundschaftsanfragen" und von "Persönlichen Nachrichten", sowie das "Teilen".
Die weiteren Aktivitäten stellen zusätzliche Anforderungen dar, deren Umsetzung in Zukunft bearbeitet werden kann.
Bei der ersten Bearbeitung des Projekts liegt der Fokus auf der Erstellung eines Bots und der Einbindung einfacher Aktionen.

### 2.3 Abgrenzung und Einbettung des gewünschten Systems

Das Projekt soll ein einfach zu handhabendes Programm hervorbringen, dass ausgeführt werden muss und alle wichtigen Funktionalitäten und Daten in einem Fenster vereint.
Das Programm soll Betriebssystem unabhängig agieren, um eine Plattform unabhängige Arbeitsweise zu gewährleisten.
Die bevorzugten Betriebssysteme werden in erster Linie durch Windows und in zweiter Linie durch MacOS dargstellt.
Des weiteren soll die Software "OpenSource" gehalten werden, aufgrund der Konstitutionellen Voraussetzungen.
Das Endprodukt soll keine Lizenz-Eingrenzungen erhalten und für alle Nutzer in vollem Umfang zur Verfügung stehen.
Das Endprodukt wird auschließlich nur zur nicht kommerziellen Nutzung verwendet.
Die Anbindung an das soziale Netzwerk "FaceBook" soll vom Programm intern gelöst werden.

### 2.4 Allgemeine Einschränkungen

Die Software muss das Verhalten des Bots kapseln, damit zukünftig Nutzer leichter das Verhalten verändern können.
Eine Einschränkung der Funktionalität durch die Richtlinien von "FaceBook" ist, je nach Stand der Richtlinien, möglich.
Die automatische Erstellung eines Accounts für die Bots ist, aufgrund der momentanen Richtlinien von "FaceBook" Stand(16.04.2018), unmöglich.

### 2.5 Vorgaben zu Hardware und Software

Grundsätzlich wird die Software mit Python 3.6.3 entwickelt. 
Durch die Plattformunabhängigkeit von Python, spielt die Wahl des Betriebssystems keine Rolle.

### 2.6 Anforderungsquellen / Zielgruppen

Das Hauptziel ist die Auswertung der sozialen Interaktionen zwischen dem Bot und der Umwelt.
Die Hauptnutzer werden durch Studentinnen und Studenten der Universität Basel dargstellt.
Die Hauptnutzer beziehen die Daten für ihre Analyse aus der Auswertung der Daten zu den Interaktionen des Bots.
Die Studienrichtung der Studentinnen und Studenten sind die Sozialwissenschaften.
Weitere Zielgruppen können in Zukunft hinzukommen und müssen nicht explizit aufgeführt werden.
Das Programm soll unabhängig vom Nutzer funktionieren und eine einfach handhbung garantieren.

## 3. Detailierte Beschreibung der Anforderung (Leistungsmerkmale)

### 3.1 Lieferumfang
Zu der Lieferung gehört ein Programm mit allen zugehörigen Komponenten, eine Dokumentation der implementierten Funktionen und eine Einweisung in die Funktionen der Software.
Die Software liefert die Möglichkeit einen Bot für "FaceBook" zu erstellen und die Möglichkeit das Verhalten des Bots auf der Oberfläche zu konfigurieren.

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

## 6. Bewertung der Anforderungen
> Falls bei der Beschreibung der funktionalen Eigenschaften des Produkts noch nicht erfolgt: Klassifizierung, Priorisierung, Auswahl (Paketierung) mit Auswahlbegründungen

## 7. Verpflichtungen des Auftaggebers
> z.B.: gestellte Hardware / Software, Schulung von Entwicklern oder von Auftraggeberpersonal, Ansprechpartner, zur Verfügung stellen von Räumen, Rechenzentrum, Reaktionszeiten des Auftraggebers auf Anfragen

