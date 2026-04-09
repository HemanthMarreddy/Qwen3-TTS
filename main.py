import torch
from qwen_tts import Qwen3TTSModel

from src.pipeline import run_pipeline

# ✅ Use CustomVoice model (IMPORTANT)
model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice",
    device_map="cpu"
)

TEXT = """
This is a demonstration of chunk based streaming using Qwen3 TTS model.
We are testing latency, real time factor, and multilingual capability.
"""

run_pipeline(model, TEXT)