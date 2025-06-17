"""
Helpers to download YouTube audio and convert to mono 16kHz WAV
"""

from __future__ import annotations
from pathlib import Path

from yt_dlp import YoutubeDL
import ffmpeg


def _download_mp4(url, out_dir):
    """Return path to best-audio MP4 in out_dir"""
    out_path = out_dir / "%(title)s.%(ext)s"
    ydl_opts = {
        "format": "ba[ext=m4a]/bestaudio/best",
        "outtmpl": str(out_path),
        "quiet": True,
        "noprogress": True,
        "nocheckcertificate": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return Path(ydl.prepare_filename(info))


def _convert_to_wav(src, dst):
    """fmmpeg-python one-liner to mono 16 kHz WAV"""
    (
        ffmpeg.input(str(src))
        .output(str(dst), ac=1, ar="16k", format="wav", loglevel="error")
        .overwrite_output()
        .run()
    )
    return dst


def fetch_audio(url, *, tmp_dir):
    """Public helper that returns Path to cleaned WAV inside `tmp_dir`"""
    mp4 = _download_mp4(url, tmp_dir)
    wav = tmp_dir / (mp4.stem + ".wav")
    return _convert_to_wav(mp4, wav)
