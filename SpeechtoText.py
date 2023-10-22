import os
import openai
from pydub import AudioSegment

# Setting the paths for ffmpeg and ffprobe
AudioSegment.converter = r"C:\\Users\\Owner\\OneDrive\Documents\\ffmpeg-2023-10-18-git-e7a6bba51a-full_build\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\\Users\\Owner\\OneDrive\Documents\\ffmpeg-2023-10-18-git-e7a6bba51a-full_build\\bin\\ffprobe.exe"

# Setting OpenAI API key
openai_api_key = 'Use your own API, thank you'
openai.api_key = openai_api_key

# Source and destination directories
source_directory = r'C:\\Users\\Owner\\OneDrive\\Documents\\2023-2024\\GF AI\\Recordings'
destination_directory = r'C:\\Users\\Owner\\OneDrive\\Documents\\2023-2024\\GF AI\\Text'

# Iterating over the MP3 files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".mp3"):
        mp3_path = os.path.join(source_directory, filename)

        # Transcribing the audio using Whisper API
        with open(mp3_path, 'rb') as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)

        # Writing the transcription to the destination directory
        text_path = os.path.join(destination_directory, filename.replace('.mp3', '.txt'))
        with open(text_path, 'w') as text_file:
            text_file.write(transcript['text'])

        print(f"Transcribed {filename} and saved to {text_path}")

print("All files processed.")
