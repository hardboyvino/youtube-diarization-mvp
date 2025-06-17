"""CLI smoke test for Day 1."""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_cli_invocable() -> None:
    """`python -m diarizer` exits 0 and prints version string."""
    result = subprocess.run(
        [sys.executable, "-m", "diarizer"],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
    )
    assert result.returncode == 0
    assert "stub" in result.stdout.lower()
