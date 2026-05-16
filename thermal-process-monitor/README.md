# thermal-process-monitor

Bewerberprojekt zur Simulation einer industriellen Prozessüberwachung.

Das Programm verarbeitet synthetische Sensordaten einer technischen Anlage, prüft Grenzwerte, erkennt Alarme und erstellt einen Prozessbericht. Zusätzlich enthält das Projekt eine kleine C++-Komponente zur Grenzwertprüfung.

## Bewerbungskontext

Das Projekt passt besonders zu technischer Informatik, Maschinenbau, Mechatronik und industrieller Softwareentwicklung.

Passende Themen:

- Sensordatenanalyse
- Prozessüberwachung
- Grenzwertprüfung
- Alarmlogik
- technische Kennzahlen
- Berichtserstellung
- Python und C++ Grundlagen

## Tech Stack

- Python 3.11
- pandas
- numpy
- pytest
- GitHub Actions
- C++

## Funktionen

- Sensordaten aus CSV laden
- Daten validieren
- Temperatur, Druck und Durchfluss prüfen
- Wärmeübertragungsrate berechnen
- Anlagenwirkungsgrad berechnen
- Alarme zusammenfassen
- Prozessbericht erzeugen
- Tests ausführen

## Projektstruktur

```text
thermal-process-monitor/
├── main.py
├── src/
├── tests/
├── data/
├── docs/
├── cpp/
├── reports/
├── requirements.txt
└── .github/workflows/python-ci.yml
```

## Start

```bash
pip install -r requirements.txt
python main.py
```

Der Bericht wird lokal unter `reports/process_report.txt` erzeugt.

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

## Hinweis

Alle Daten sind synthetisch. Das Projekt ist ein Bewerberprojekt und kein produktives industrielles Überwachungssystem.
