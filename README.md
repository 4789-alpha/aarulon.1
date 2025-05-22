# aarulon.1

Aarulon (Aari) ist ein modular aufgebauter Assistent, der komplett lokal
ausgeführt wird. Ziel ist ein verspielter, kindlicher Begleiter, der ohne
Internetverbindung läuft. Diese Basisversion verwendet Deutsch als
Grundsprache. Weitere Sprachen können später daraus abgeleitet werden.

Enthalten sind folgende Minimalmodule:

- `start.sh` – Startskript
- `aari.py` – Hauptcontroller mit einfachem Sprachtest über `pyttsx3`
- `aari_listen.py` – Platzhalter für zukünftige Spracherkennung
- `systemcheck.py` – Hilfsfunktionen für Systemkommandos
- `aari_config.json` – Beispielkonfiguration
- `install_aari.py` – Einfache plattformübergreifende Installation

Starte Aari klassisch mit `./start.sh` oder nutze `install_aari.py` für
eine automatische Installation der benötigten Python-Pakete.
