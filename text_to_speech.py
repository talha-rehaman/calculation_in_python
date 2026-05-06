import os
import wave
import struct
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-tts",
    contents="Hello! I am Talha Rehman, a passionate software developer with expertise in Python and JavaScript. I love creating innovative solutions and exploring new technologies.",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Aoede"
                )
            )
        )
    )
)

# Raw audio data lo
audio_data = response.candidates[0].content.parts[0].inline_data.data

# ✅ Proper WAV file banao headers ke saath
def save_as_wav(audio_bytes, filename="output.wav",
                sample_rate=24000, channels=1, sampwidth=2):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_bytes)
    print(f"✅ Audio saved: {filename}")

save_as_wav(audio_data)
