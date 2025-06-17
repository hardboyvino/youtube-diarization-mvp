"""
Makes `python -m diarizer` work.

Simply delegates to diarizer.cli.main()
"""

from .cli import main

if __name__ == "__main__":
    main()
