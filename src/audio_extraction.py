<<<<<<< HEAD
import ffmpeg
import sys
from pathlib import Path

input_video = sys.argv[1] if len(sys.argv) > 1 else "sample.mp4"
output_audio = Path(input_video).stem + "_audio.wav"

(
    ffmpeg
    .input(input_video)
    .output(str(output_audio), ac=1, ar='16k') # one channel
    .overwrite_output()
    .run(quiet=False)
)

print(f"Audio extracted successfully → {output_audio}")
=======
import ffmpeg
import sys
from pathlib import Path

input_video = sys.argv[1] if len(sys.argv) > 1 else "sample.mp4"
output_audio = Path(input_video).stem + "_audio.wav"

(
    ffmpeg
    .input(input_video)
    .output(str(output_audio), ac=1, ar='16k')
    .overwrite_output()
    .run(quiet=False)
)

print(f"Audio extracted successfully → {output_audio}")
>>>>>>> 1f657a2 (Add audio extraction and speech-to-text modules)
