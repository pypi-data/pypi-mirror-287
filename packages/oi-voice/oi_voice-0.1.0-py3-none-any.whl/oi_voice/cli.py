import click
import open_interpreter
import pyaudio
import wave
from oi_voice.speech_to_text import transcribe_audio
from oi_voice.text_to_speech import text_to_speech
from pydub import AudioSegment
from pydub.playback import play

@click.command(help="Start a real-time voice conversation with Open Interpreter.")
def main():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    audio = pyaudio.PyAudio()

    while True:
        click.echo("Listening...")
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

        text = transcribe_audio(WAVE_OUTPUT_FILENAME)
        if text.lower() in ["exit", "quit", "stop"]:
            click.echo("Exiting conversation.")
            break

        response = open_interpreter.execute(text)
        audio_file = text_to_speech(response)
        audio_segment = AudioSegment.from_wav(audio_file)
        play(audio_segment)

    audio.terminate()

if __name__ == "__main__":
    main()
