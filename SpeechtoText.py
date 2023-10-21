import os
import openai
import soundfile as sf
from pydub import AudioSegment

AudioSegment.converter = r"C:\Users\eblak\Downloads\ffmpeg-6.0-full_build\bin\ffmpeg.exe"
AudioSegment.ffprobe   = r"C:\Users\eblak\Downloads\ffmpeg-6.0-full_build\bin\ffprobe.exe"


# Set OpenAI API key
openai_api_key = ''
openai.api_key = openai_api_key

# Source and destination directories
source_directory = r'C:\Users\eblak\OneDrive\Documents\2023-2024\GF AI\Recordings'
destination_directory = r'C:\Users\eblak\OneDrive\Documents\2023-2024\GF AI\Text'

# Iterate over the MP3 files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".mp3"):
        # Read the MP3 file and convert it to WAV
        mp3_path = os.path.join(source_directory, filename)
        audio = AudioSegment.from_mp3(mp3_path)
        wav_path = mp3_path.replace('.mp3', '.wav')
        audio.export(wav_path, format='wav')

        # Read the WAV file
        with open(wav_path, 'rb') as audio_file:
            data, samplerate = sf.read(audio_file)

        # Use Whisper API to transcribe the audio
        response = openai.Whisper.asr.create(
            audio=data,
            model="whisper-large-13",
            sample_rate=samplerate,
        )

        # Write the transcription to the destination directory
        text_path = os.path.join(destination_directory, filename.replace('.mp3', '.txt'))
        with open(text_path, 'w') as text_file:
            text_file.write(response.data['text'])

        print(f"Transcribed {filename} and saved to {text_path}")

print("All files processed.")


