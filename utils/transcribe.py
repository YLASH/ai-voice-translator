import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LANGUAGE_NAMES = {
    "en": "English",
    "zh": "Chinese",
    "ja": "Japanese",
    "ko": "Korean",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "th": "Thai",
    "vi": "Vietnamese",
    "id": "Indonesian",
}

def transcribe(audio_path):
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="verbose_json"
        )

    lang_code = transcript.language or "unknown"
    lang_name = LANGUAGE_NAMES.get(lang_code, lang_code.upper())

    return {
        "text": transcript.text,
        "language": lang_name
    }