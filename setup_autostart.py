import os
from pathlib import Path

SERVICE_NAME = "aari.service"


SERVICE_TEMPLATE = """[Unit]
Description=Aari Host Service
After=network.target

[Service]
Type=simple
ExecStart={python} {script} listen
WorkingDirectory={workdir}
Restart=on-failure

[Install]
WantedBy=default.target
"""


def generate_service_text(python_path: str = None, script_path: str = None) -> str:
    """Return the systemd service file content."""
    python_path = python_path or os.path.realpath(os.sys.executable)
    script_path = script_path or os.path.join(Path(__file__).resolve().parent, "cli.py")
    workdir = Path(script_path).resolve().parent
    return SERVICE_TEMPLATE.format(python=python_path, script=script_path, workdir=workdir)


def install_service(user_dir: Path = None) -> Path:
    """Install the service file for the current user."""
    user_dir = user_dir or Path.home() / ".config" / "systemd" / "user"
    user_dir.mkdir(parents=True, exist_ok=True)
    service_path = user_dir / SERVICE_NAME
    service_path.write_text(generate_service_text())
    return service_path


if __name__ == "__main__":  # pragma: no cover - manual use
    path = install_service()
    print(f"Service installed at {path}")
    print("Enable it with: systemctl --user enable aari.service && systemctl --user start aari.service")
