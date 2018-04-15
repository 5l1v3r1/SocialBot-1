# User Requirement Specification

## 1. Einleitung

In diesem Dokument werden die User Requirements für das Projekt "Social Life eines Bots" festgehalten.
Bei dem Projekt handelt es sich um die Erstellung eines Bots für die Soziale Internetseite "FaceBook".
Die Bots sollen automatisiert bestimmte Funktionen ausführen und dabei beobachtet werden können.
Die Anforderungen an diese Bots werden im Folgenden genauer dokumentiert.

### 1.1 Zweck des Dokuments

In diesem Dokument werden die User Requirements für den Kundenauftrag festgelegt. 
Die Kundenansprüche werden festgehalten, um einen Überblick zu erschaffen und den Umfang des Projekts zu definieren.


### 1.2 Gültigkeit des Dokuments

Erstellung des Dokuments: 11.04.2018

### 1.3 Begriffsbestimmung und Abkürzungen

--

### 1.4 Zusammenhang mit anderen Dokumenten

--

## 2. Allgemeine Beschreibung des gewünschten Systems

Der Bot sollen automatisiert auf bestimmte Ereignisse mit vorgefertigte Aktionen reagieren.
Der Bot soll für die Soziale Netzwerk "FaceBook" erstellt werden.
Der Bot soll die einfachen Aktionen dieses Sozialen Netzwerks ausführen, wie "Liken", "Kommentieren" und "Posten".
Die Aktivitäten des Bots sollen in einem Log festgehalten werden und später nachsehbar sein.

### 2.1 Zweck des gewünschten Systems

Der Zweck des Projekts besteht aus der Beobachtung des sozialen Aspekts eines Bots in einem Sozialen Netzwerk.
Die Interaktion des Bots mit Seiten, anderen Nutzern und eventuell anderen Bots soll beobachtet werden.
Die Interaktion mit anderen Nutzern in Form von Menschen steht im Mittelpunkt der Beobachtung.
Flexibilität des Bots ist wichtig, um möglichst unterschiedliche Interaktionen zu fördern und umfangreiche Reaktionen zu erreichen.

### 2.2 Überblick über die geforderte Funktionalität

Als Forderung an die Funktionalität ist die Erstellung unterschiedlicher Bots gesetzt.
Die Bots sollen einen "Post" anhand einem vorgefertigten Text erstellen und veröffentlichen.
Ein "Like" auf bestimmte, vorher definierte "Posts" soll vom Bot gegeben werden können.
Der Bot soll unter bestimmten "Posts" einen festgelegten Text in Form eines "Kommentars" kommentieren können.
Jede Aktivität des Bots soll in einem Aktivitäten-Log festgehalten werden.
Beim Festhalten der Aktivität ist auch auf Reaktionen anderer Nutzer dauf die Aktion des Bots zu achten.
Die Reaktion anderer Nutzer muss abgespeichert werden und mit der entsprechenden Aktion des Bots in Verbindung gebracht werden können.
Die gespeicherten Aktivitäten des Bots müssen auslesbar und anzeigbar sein, um die Aktionen und Reaktionen auszuwerten.
Der Algorithmus für die Aktivitäten des Bots soll austauschbar gehalten werden, muss folglich in einer austauschbaren Weise vorlegen.
Der ünbrige Teil, ohne Algorithmus muss mit jeder Form von Algorithmus im selben Format arbeiten können.
Die Einstellung des Bots, über den Algorithmus, muss Flexibilität bieten.
Die Möglichkeit muss bestehen, jeden Bot unterschieldlich einzustellen, um andere Aktionen und Reaktion anderer Nutzer hervor zu bringen.
Als weitere Aktivitäten für den Bot stehen die Handhabung von "Freundschaftsanfragen" und von "Persönlichen Nachrichten", sowie das "Teilen".
Die weiteren Aktivitäten stellen zusätzliche Anforderungen dar, die es in Zukunft umzusetzen gilt.
Bei der Erstbearbeitung liegt der Fokus nicht auf der bearbeitung der zusätzlichen Aktivitäten.

### 2.3 Abgrenzung und Einbettung des gewünschten Systems

Die bevorzugten Betriebssysteme werden in erster Linie durch Windows und in zweiter Linie durch MacOS dargstellt.
Des weiteren soll die Software "OpenSource" gehalten werden, aufgrund der Konstitutionellen Voraussetzungen.
Das Endprodukt soll keine Lizenz-EIngrenzungen erhalten und für alle Nutzer in vollem Umfang zur Verfügung stehen.
Das Endprodukt wird nur zur nicht kommerziellen Nutzung verwendet.

### 2.4 Allgemeine Einschränkungen

Die Software muss das Verhalten des Bots kapseln, damit zukünftig Nutzer leichter das Verhalten verändern können.

### 2.5 Vorgaben zu Hardware und Software

Grundsätzlich wird die Software mit Python 3.6.3 entwickelt. Durch die Plattformunabhängigkeit von Python, spielt die Wahl des Betriebssystems keine Rolle.

### 2.6 Anforderungsquellen / Zielgruppen

Die Nutzer werden durch Studentinnen und Studenten dargstellt, die eine Auswertung mit dem Endprodukt tätigen wollen.
Die Studienrichtung richtet sich in erster Weise auf die Sozialwissenschaften.
Weitere Zielgruppen können in Zukunft hinzukommen und müssen nicht explizit aufgeführt werden.

## 3. Detailierte Beschreibung der Anforderung (Leistungsmerkmale)

### 3.1 Lieferumfang

Die Software liefert einen automatisierte Konto erstellung auf Facebook und sie wird in der Lage sein auf Beiträge zu reagieren, die entsprechend auf der Oberfläche konfiguriert werden können.

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

