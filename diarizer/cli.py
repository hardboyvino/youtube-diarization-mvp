"""
Command line entry for `python -m diarizer`.
Day 1: just prints version and exists 0.
"""

from __future__ import annotations

import sys
from rich.console import Console

from . import __version__

console = Console()


def main() -> None:
    """Run the stub CLI"""
    console.print(f"[bold green]YouTube Diarizer v{__version__} (stub)[/]")
    sys.exit(0)


if __name__ == "__main__":
    main()
