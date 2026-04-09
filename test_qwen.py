import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice",  # use smaller first
    device_map="cpu",
    dtype=torch.float32,
    attn_implementation="eager"   # 🔥 IMPORTANT FIX
)

wavs, sr = model.generate_custom_voice(
    text="Hello, this is a test.",
    language="English",
    speaker="Ryan"
)

sf.write("output.wav", wavs[0], sr)
print("Done")