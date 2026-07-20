
import whisper
model = whisper.load_model("base")
result = model.transcribe("temp_audio.wav")
print("Transcribed text:", repr(result["text"]))

