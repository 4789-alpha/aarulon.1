# aarulon.1

Aarulon (Aari) ist ein modular aufgebauter Assistent, der komplett lokal
ausgeführt wird. Ziel ist ein digitaler Begleiter, der symbolisch ein
35-jähriges "Ich" repräsentiert und ohne Internetverbindung läuft. Diese
Basisversion verwendet Deutsch als
Grundsprache. Weitere Sprachen können später daraus abgeleitet werden.

Enthalten sind folgende Minimalmodule:

- `start.sh` – Startskript
- `aari.py` – Hauptcontroller mit einfachem Sprachtest über `pyttsx3`
- `aari_listen.py` – Offline-Spracherkennung mit `vosk`
- `systemcheck.py` – Hilfsfunktionen für Systemkommandos
- `aari_config.json` – Beispielkonfiguration
- `install_aari.py` – Einfache plattformübergreifende Installation

Starte Aari klassisch mit `./start.sh <befehl>` oder nutze `install_aari.py`
für eine automatische Installation der benötigten Python-Pakete.

## Abhängigkeiten

Alle benötigten Pakete sind in `requirements.txt` aufgelistet:

* `pyttsx3` für die Sprachausgabe
* `vosk` und `sounddevice` für die Offline-Spracherkennung
* ein passendes Vosk-Sprachmodell im Ordner `model`
## Installation

Führe zuerst das Installationsskript aus, um die Abhängigkeiten
zu installieren und Aari zu starten:

```bash
python3 install_aari.py
```

Das Skript installiert automatisch alle Pakete aus `requirements.txt`.

## Start

Nach erfolgreicher Installation kann das Kommandozeilen-Werkzeug
gestartet werden:

```bash
./start.sh <befehl>
```

Oder direkt via Python:

```bash
python3 cli.py <befehl>
```

Verfügbare Befehle sind `self-check`, `system-data`, `listen` und
`say <text>`.
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
