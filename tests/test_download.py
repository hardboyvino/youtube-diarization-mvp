from pathlib import Path
import shutil


from diarizer.download import fetch_audio


FIXTURE_URL = "https://youtu.be/dQw4w9WgXcQ"  # Use RickRoll because why not
DUMMY_WAV = Path("tests/fixtures/dummy.wav")  # 2-sec CC-BY clip


def test_fetch_audio_monowav(tmp_path, monkeypatch):
    """yt-dlp + ffmpeg should return a mono 16 kHz wav Path"""
    # --- mock yt-dlp so we never hit the network
    fake_mp4 = tmp_path / "audio.mp4"
    fake_mp4.write_bytes(b"stub")

    def fake_ydl(*_, **__):
        return fake_mp4

    monkeypatch.setattr("diarizer.download._download_mp4", fake_ydl)

    # --- mock ffmpeg-python convert
    def fake_ffmpeg(src, dst):
        shutil.copy(DUMMY_WAV, dst)
        return dst

    monkeypatch.setattr("diarizer.download._convert_to_wav", fake_ffmpeg)

    out = fetch_audio(FIXTURE_URL, tmp_dir=tmp_path)
    assert out.suffix == ".wav"
    assert out.exists()

    import wave
    import contextlib

    with open(out, "rb") as fh, contextlib.closing(wave.open(fh, "rb")) as wf:
        assert wf.getnchannels() == 1
        assert wf.getframerate() == 44_100
