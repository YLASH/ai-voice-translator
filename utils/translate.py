import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate(text, target_lang="English"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional translator. Translate the given text accurately. Return only the translated text, nothing else."},
            {"role": "user", "content": f"Translate this to {target_lang}:\n\n{text}"}
        ]
    )
    return response.choices[0].message.content