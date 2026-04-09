import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-Base",
    device_map="cpu"
)

wavs, sr = model.generate_voice_clone(
    text="This is a cloned voice test.",
    language="English",
    ref_audio="data/speaker.wav",
    ref_text="This is the original voice sample."
)

sf.write("clone.wav", wavs[0], sr)