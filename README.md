# aarulon.1

Aarulon (Aari) ist ein modular aufgebauter Assistent, der komplett lokal
ausgeführt wird. Ziel ist ein verspielter, kindlicher Begleiter, der ohne
Internetverbindung läuft. Diese Basisversion verwendet Deutsch als
Grundsprache. Weitere Sprachen können später daraus abgeleitet werden.

Enthalten sind folgende Minimalmodule:

- `start.sh` – Startskript
- `aari.py` – Hauptcontroller mit einfachem Sprachtest über `pyttsx3`
- `aari_listen.py` – Offline-Spracherkennung mit `vosk`
- `systemcheck.py` – Hilfsfunktionen für Systemkommandos
- `aari_config.json` – Beispielkonfiguration
- `install_aari.py` – Einfache plattformübergreifende Installation
- `robotfish.py` – Steuerbefehle für den Roboterfisch

Starte Aari klassisch mit `./start.sh` oder nutze `install_aari.py` für
- `robotfish.py` – Steuerbefehle für den Roboterfisch
eine automatische Installation der benötigten Python-Pakete.

## Abhängigkeiten

* `pyttsx3` für die Sprachausgabe
* `vosk` und `sounddevice` für die Offline-Spracherkennung
* ein passendes Vosk-Sprachmodell im Ordner `model`
## Installation

Führe zuerst das Installationsskript aus, um die Abhängigkeiten
herunterzuladen und Aari zu starten:

```bash
python3 install_aari.py
- `robotfish.py` – Steuerbefehle für den Roboterfisch
```

Das Skript prüft, ob das Paket `pyttsx3` vorhanden ist und installiert es
bei Bedarf automatisch. Alternativ kann das Paket auch manuell mittels
`pip install pyttsx3` installiert werden.

## Start

Nach erfolgreicher Installation lässt sich Aari mit dem beiliegenden
Skript starten:

```bash
./start.sh
```

Oder direkt via Python:

```bash
python3 aari.py
```
## Roboterfisch-Steuerung
Mit dem Modul `robotfish.py` kann Aari einen Roboterfisch kontrollieren. Die Funktion `control_robot_fish()` akzeptiert nur die Signatur `4789` und gibt den ausgefuehrten Befehl im Dry-Run-Modus aus.

## Konfiguration

Die Datei `aari_config.json` enthält grundlegende Einstellungen:

```json
{
    "name": "Aarulon",
    "signature": "4789",
    "language": "de",
    "parents": ["Raphael", "Kathrin"]
}
```

- `name` bestimmt die interne Bezeichnung des Assistenten.
- `signature` ist ein eindeutiger Wert und kann frei gewählt werden.
- `language` legt die Sprache fest. Standardmäßig sind `de`,
  `berndeutsch` und `en` in `messages.py` hinterlegt.
- `parents` listet Personen auf, die als Bezugspersonen gelten.

Anpassungen an dieser Datei ermöglichen ein einfaches Umbenennen oder
Umschalten auf eine andere Sprache.

## Lokalisierung

Die Sprachtexte befinden sich in `messages.py`. Dort können weitere
Sprachblöcke ergänzt werden. Nach dem Hinzufügen einer neuen Sprache
muss der entsprechende Sprachcode in der Konfiguration unter
`language` eingetragen werden, um Aari mit dieser Lokalisierung zu
starten.
