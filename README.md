# 🎙️ AI Voice Translator

A full-stack AI pipeline that transcribes audio, translates it, and generates speech output.

Built with OpenAI Whisper, GPT-4o-mini, and ElevenLabs TTS.

---

## ✨ Features

- 📁 Upload audio files (.mp3 / .wav / .m4a)
- 🎙️ Record audio directly in the browser
- 🔍 Auto-detect source language
- 🌐 Translate to 8 languages (English, Traditional Chinese, Japanese, Korean, Spanish, French, German, Thai)
- 🔊 Generate natural speech output via ElevenLabs
- 📋 Copy original or translated text with one click
- ⬇️ Download translated audio as .mp3
- ⚡ Simple, clean web UI

---

## 🏗️ Architecture
```
Audio Input (Upload / Browser Recording)
↓
Speech-to-Text (OpenAI Whisper)
↓
Translation (GPT-4o-mini)
↓
Text-to-Speech (ElevenLabs)
↓
Audio Output
```
---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Speech-to-Text | OpenAI Whisper API |
| Translation | OpenAI GPT-4o-mini |
| Text-to-Speech | ElevenLabs API |
| Frontend | HTML, CSS, JavaScript |

---

## 🚀 Setup

**1. Clone the repo**
```bash
git clone https://github.com/YLASH/ai-voice-translator.git
cd ai-voice-translator
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install flask openai requests python-dotenv httpx==0.27.0
```

**4. Add API keys**

Create a `.env` file:
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key

**5. Run**
```bash
python app.py
```

Open `http://localhost:5000`

---

## 📂 Project Structure
```
ai-voice-translator/
├── utils/
│   ├── transcribe.py     # Whisper STT
│   ├── translate.py      # GPT translation
│   └── tts.py            # ElevenLabs TTS
├── templates/
│   └── index.html        # Web UI
├── static/               # Audio output files
├── app.py                # Flask API
├── .env                  # API keys (not committed)
└── README.md
```

---

## 🗺️ Roadmap

- [x] Audio file upload
- [x] Browser recording
- [x] Auto language detection
- [x] Multi-language translation
- [x] TTS audio output
- [x] Copy text to clipboard
- [x] Download translated audio
- [ ] Translation history
- [ ] Voice selection
- [ ] Streaming real-time transcription
- [ ] Zoom integration
