# aarulon.1

Aarulon (Aari) is a modular assistant that runs entirely on your local machine. It aims to be a playful companion that works without any internet connection. This base version uses German as the default language. Additional languages can easily be added.

This project includes the following minimal modules:

- `start.sh` – start script
- `aari.py` – main controller with a simple speech test via `pyttsx3`
- `aari_listen.py` – offline speech recognition with `vosk`
- `systemcheck.py` – helper functions for system checks
- `aari_config.json` – example configuration
- `install_aari.py` – simple cross‑platform installer

Start Aari with `./start.sh <command>` or run `install_aari.py` for automatic installation of the required Python packages.

## Dependencies

All required packages are listed in `requirements.txt`:

* `pyttsx3` for speech output
* `vosk` and `sounddevice` for offline speech recognition
* a suitable Vosk model inside the `model` folder
* `pyaudio` to check audio devices

## Installation

Run the installation script first to install dependencies and start Aari:

```bash
python3 install_aari.py
```

The script automatically installs all packages from `requirements.txt`.

## Usage

After installation you can start the command line tool:

```bash
./start.sh <command>
```

Or directly via Python:

```bash
python3 cli.py <command>
```

Available commands are `self-check`, `system-data`, `listen`, and `say <text>`.

## Robot Fish Control
With `robotfish.py` Aari can control a robot fish. The function `control_robot_fish()` only accepts the signature `4789` and prints the command in dry-run mode.

## Configuration

The file `aari_config.json` contains basic settings:

```json
{
    "name": "Aarulon",
    "signature": "4789",
    "language": "de",
    "parents": ["Raphael", "Kathrin"]
}
```

- `name` determines the internal name of the assistant.
- `signature` is a unique value you can freely choose.
- `language` sets the language. The defaults `de`, `berndeutsch`, and `en` are defined in `messages.py`.
- `parents` lists people considered as reference persons.

Adjusting this file lets you easily rename Aari or switch to another language.

## Localization

All message texts are stored in `messages.py`. You can add more languages there. After adding a language, set its code in the configuration under `language` to start Aari with that localization.

## Autostart service

`setup_autostart.py` creates a systemd unit so Aari starts automatically when the user logs in. It writes `~/.config/systemd/user/aari.service`.

```bash
python3 setup_autostart.py
systemctl --user enable aari.service
systemctl --user start aari.service
```

## Simple HTTP server

`aari_server.py` provides a small HTTP server on port 4789. `GET /say?text=<TEXT>&signature=4789` will let Aari speak the text. A `GET /ping` returns `pong`. Requests with an invalid signature receive `403`.
