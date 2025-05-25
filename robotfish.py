"""Control utilities for the robot fish."""

import subprocess

ALLOWED_SIGNATURE = "4789"


def control_robot_fish(action: str, signature: str, dry_run: bool = True) -> bool:
    """Send a command to the robot fish.

    Parameters
    ----------
    action:
        The command to send, e.g. "left", "right", "forward", "stop".
    signature:
        Signature identifying the user. Only signature '4789' is allowed.
    dry_run:
        If ``True``, the command is printed instead of executed.

    Returns
    -------
    bool
        ``True`` on success, ``False`` otherwise.

    Raises
    ------
    PermissionError
        If the provided signature is not authorized.
    """
    if str(signature) != ALLOWED_SIGNATURE:
        raise PermissionError("Unauthorized signature")

    command = f"robotfish --action {action}"

    if dry_run:
        print(f"[Aari] {command}")
        return True
    try:
        subprocess.check_call(command.split())
        return True
    except Exception as exc:  # pragma: no cover - system dependent
        print(f"[Aari] Robot fish command failed: {exc}")
        return False
