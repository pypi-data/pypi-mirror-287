"""Support executing the CLI by doing `python -m ensurepython`."""
from __future__ import annotations

from ensurepython.cli import cli

if __name__ == "__main__":
    raise SystemExit(cli())
