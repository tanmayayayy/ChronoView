<<<<<<< HEAD
import whisper
import sys

audio_file = sys.argv[1] if len(sys.argv) > 1 else "sample_audio.wav"

model = whisper.load_model("base")
result = model.transcribe(audio_file)

print("===== Transcript =====")
print(result["text"])
=======
import whisper
import sys

audio_file = sys.argv[1] if len(sys.argv) > 1 else "sample_audio.wav"

model = whisper.load_model("base")
result = model.transcribe(audio_file)

print("===== Transcript =====")
print(result["text"])
>>>>>>> 1f657a2 (Add audio extraction and speech-to-text modules)
