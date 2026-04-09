import time
import soundfile as sf
import librosa
import os

from src.streaming import split_text
from src.metrics import print_metrics


def run_pipeline(model, text):
    os.makedirs("output", exist_ok=True)

    chunks = list(split_text(text))
    total_audio_duration = 0

    start_total = time.time()

    for i, chunk in enumerate(chunks):
        print(f"\nProcessing chunk {i}...")

        start = time.time()

        # ✅ Correct function for CustomVoice model
        wavs, sr = model.generate_voice_clone(
            text=chunk,
            language="English",
            ref_audio="data/speaker.wav",
            ref_text="This is the reference speaker voice."
        )

        file_path = f"output/chunkks_{i}.wav"
        sf.write(file_path, wavs[0], sr)

        # Calculate duration
        audio, sr = librosa.load(file_path, sr=16000)
        duration = len(audio) / sr
        total_audio_duration += duration

        print(f"Chunk {i} latency: {time.time() - start:.2f}s")

    total_time = time.time() - start_total

    print_metrics(total_time, total_audio_duration)