# thermal-process-monitor

![Thermal Process Monitor CI](https://github.com/JojoMab/JojoMab/actions/workflows/thermal-process-monitor-ci.yml/badge.svg)

Bewerberprojekt zur Simulation einer industriellen Prozessüberwachung.

Das Programm verarbeitet synthetische Sensordaten einer technischen Anlage, prüft Grenzwerte, erkennt kritische Betriebszustände und erstellt einen verständlichen Prozessbericht. Ergänzend enthält das Projekt eine kleine, eigenständige C++-Grenzwertprüfung als Zusatzübung in systemnaher Syntax.

## Bewerbungskontext

Das Projekt eignet sich besonders für Bewerbungen in den Bereichen technische Informatik, Mechatronik, Maschinenbau-nahe Softwareentwicklung und industrielle Datenanalyse.

| Studienrichtung | Relevanz |
|---|---|
| Technische Informatik | Sensorauswertung, Alarmlogik, Prozessüberwachung |
| Maschinenbau | Temperatur, Druck, Durchfluss und Anlagenbewertung |
| Mechatronik | Verbindung von Messdaten, Steuerungslogik und Software |
| Data Science / KI-Grundlagen | Strukturierte Datenanalyse, Kennzahlen und einfache Auswertung |

Passende Unternehmen und Branchen:

- ASMPT
- Linde Engineering
- MTU Aero Engines
- Siemens Energy
- Automatisierungstechnik
- Anlagenbau
- industrielle Softwareentwicklung

## Tech Stack

- Python 3.11
- pandas
- numpy
- pytest
- GitHub Actions
- C++ Grundlagen

## Funktionen

- Sensordaten aus CSV laden
- Daten auf Vollständigkeit und Plausibilität prüfen
- Temperatur, Druck und Durchfluss analysieren
- Grenzwertverletzungen erkennen
- Wärmeübertragungsrate berechnen
- vereinfachten Anlagenwirkungsgrad bestimmen
- Alarme zusammenfassen und bewerten
- Prozessbericht als TXT-Datei erstellen
- automatisierte Tests ausführen
- separate C++-Grenzwertprüfung nutzen

## Projektstruktur

```text
thermal-process-monitor/
├── main.py
├── src/
│   ├── sensor_reader.py
│   ├── process_calculator.py
│   ├── alarm_handler.py
│   └── report_generator.py
├── tests/
│   ├── test_calculator.py
│   └── test_alarm.py
├── data/
│   └── sensor_readings.csv
├── docs/
│   ├── application_fit.md
│   └── example_report.txt
├── cpp/
│   └── threshold_checker.cpp
├── reports/
│   └── .gitkeep
└── requirements.txt
```

## Schnellstart

```bash
pip install -r requirements.txt
python main.py
```

Der Bericht wird lokal unter folgendem Pfad erzeugt:

```text
reports/process_report.txt
```

## Tests

```bash
pytest tests/ -v
```

Lokaler Teststatus: `7 passed`.

## C++-Komponente

```bash
g++ -o threshold_checker cpp/threshold_checker.cpp
./threshold_checker 180.5 8.2 12.1
```

Beispielausgabe:

```text
OK
```

Bei Grenzwertüberschreitung:

```bash
./threshold_checker 251.0 8.2 12.1
```

```text
ALARM - Temperatur ueberschreitet Grenzwert
```

## Beispielausgabe

```text
Lade Sensordaten... 50 Messpunkte geladen.
Prüfe Grenzwerte...

Temperatur-Alarme:  5
Druck-Alarme:       3
Durchfluss-Alarme:  0
Alarmrate:          16.0 %

Bericht gespeichert: reports/process_report.txt
Bewertung: Erhöhte Alarmrate. Überprüfung empfohlen.
```

## Lernziele

- Strukturierung eines Python-Projekts
- Verarbeitung technischer CSV-Messdaten
- Umsetzung einer einfachen industriellen Überwachungslogik
- Berechnung technischer Kennzahlen
- Schreiben automatisierter Tests
- Nutzung von GitHub Actions
- Python-Hauptlogik plus separate C++-Grundlagenübung
- verständliche technische Dokumentation

## Hinweis

Alle Daten sind synthetisch. Das Projekt ist ein Bewerberprojekt und kein produktives industrielles Überwachungssystem.
