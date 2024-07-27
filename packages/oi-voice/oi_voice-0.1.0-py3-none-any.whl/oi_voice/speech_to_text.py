from faster_whisper import WhisperModel

def transcribe_audio(audio_file_path):
    try:
        model = WhisperModel("medium")  # or "large" for better quality
    except Exception as e:
        raise Exception(f"Failed to load Whisper model: {e}")
    segments, info = model.transcribe(audio_file_path)
    return " ".join([segment.text for segment in segments])
