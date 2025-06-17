"""
Command line entry for `python -m diarizer`.
Day 1: just prints version and exists 0.
"""

from __future__ import annotations

import sys
from rich.console import Console

from . import __version__
from .temp_utils import TempWorkspace
from .download import fetch_audio


console = Console()


def main() -> None:
    """Run the stub CLI"""
    console.print(f"[bold green]YouTube Diarizer v{__version__} (stub)[/]")
    sys.exit(0)

    if len(sys.argv) == 2:
        url = sys.argv[1]
        with TempWorkspace() as tmp:
            wav_path = fetch_audio(url, tmp_dir=tmp)
            console.print(f"[cyan]Download & converted:[/] {wav_path}")


if __name__ == "__main__":
    main()
