from pathlib import Path


def transcribe_with_fast_whisper(video_path):
    """Transcribe video using Faster Whisper"""
    try:
        from faster_whisper import WhisperModel

        model = WhisperModel("base", device="cpu", compute_type="auto")

        segments, _ = model.transcribe(video_path)
        transcript = " ".join([segment.text for segment in segments])
        transcript_path = str(Path(video_path).with_suffix('.txt'))

        with open(transcript_path, 'w', encoding='utf-8') as f:
            f.write(transcript)

        return True

    except ImportError:
        print("ImportError")
        return False
    except Exception as e:
        print(f"Fast transcription error: {e}")
        return False


transcribe_with_fast_whisper("video.mp4")
