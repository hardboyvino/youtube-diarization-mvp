from __future__ import annotations
import shutil
import tempfile
from pathlib import Path
import atexit
import signal


class TempWorkspace:
    """Context manager that auto-nukes its folder even on Ctrl-C"""

    def __enter__(self):
        self.path = Path(tempfile.mkdtemp(prefix="diarizer_"))
        # Register final cleanup
        atexit.register(self.cleanup)
        # Trap SIGINT so Ctrl-C also deletes
        signal.signal(signal.SIGINT, self._sigint)
        return self.path

    def _sigint(self, *_):
        self.cleanup()
        raise KeyboardInterrupt

    def cleanup(self):
        if getattr(self, "path", None) and self.path.exists():
            shutil.rmtree(self.path, ignore_errors=True)

    def __exit__(self, exc_type, exc, tb):
        self.cleanup()
