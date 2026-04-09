import torch
from qwen_tts import Qwen3TTSModel

from src.pipeline import run_pipeline

# ✅ Use voice cloning model (IMPORTANT)
model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-0.6B-Base",
    device_map="cpu"
)

TEXT = """
"Hello. नमस्ते. Hola. Bonjour."
"""

run_pipeline(model, TEXT)


from src.speaker_cache import save_prompt, load_prompt

# Create prompt once
prompt = model.create_voice_clone_prompt(
    ref_audio="data/speaker.wav",
    ref_text="This is the reference speaker voice."
)

save_prompt(prompt)