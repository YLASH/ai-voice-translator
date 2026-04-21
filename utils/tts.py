import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # 預設聲音 George，之後可以換

def text_to_speech(text, output_dir="static"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        # "model_id": "eleven_monolingual_v1",
        "model_id":"eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    res = requests.post(url, json=data, headers=headers)

    if res.status_code != 200:
        raise Exception(f"ElevenLabs error: {res.status_code} - {res.text}")

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "wb") as f:
        f.write(res.content)

    return filename