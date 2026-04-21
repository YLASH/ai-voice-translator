import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from utils.transcribe import transcribe
from utils.translate import translate
from utils.tts import text_to_speech

app = Flask(__name__)
UPLOAD_FOLDER = "static"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400

    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    # 存暫存檔
    temp_path = os.path.join(UPLOAD_FOLDER, f"temp_{file.filename}")
    file.save(temp_path)

    try:
        # 1. 語音轉文字
        transcription = transcribe(temp_path)
        original_text = transcription["text"]
        detected_lang = transcription["language"]

        # 2. 翻譯
        target_lang =  request.form.get("target_lang", "English")
        translated_text = translate(original_text, target_lang)

        # 3. 文字轉語音
        audio_filename = text_to_speech(translated_text)

        return jsonify({
            "original": original_text,
            "detected_language": detected_lang,
            "translated": translated_text,
            "audio_url": f"/static/{audio_filename}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        # 清理暫存檔
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.route("/static/<filename>")
def serve_audio(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)