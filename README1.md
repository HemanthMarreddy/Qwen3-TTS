FULL PROFESSIONAL README (COPY THIS)
# Qwen3-TTS Multilingual Voice Cloning & Streaming Pipeline

## 📌 Overview
This project implements a **Qwen3-TTS based text-to-speech system** with:

- Chunk-based streaming inference
- Multilingual speech generation
- Voice synthesis using predefined voices
- Performance evaluation (Latency & RTF)

The system is designed to simulate a production-ready pipeline for future multilingual voice cloning systems.

---

## 🧠 Architecture

Text → Chunking → TTS Model → Audio Output → Metrics

---

## ⚙️ Features

- ✅ Chunk-based streaming
- ✅ Multilingual support
- ✅ Predefined voice synthesis
- ✅ Latency measurement
- ✅ Real-Time Factor (RTF) calculation
- 🔄 Voice cloning (optional extension) #use other instead of 0.6B in model

---

## 📁 Project Structure


Qwen3-TTS/
│
├── src/
│ ├── streaming.py
│ ├── metrics.py
│ ├── pipeline.py
│
├── data/
│ └── speaker.wav
│
├── output/
│
├── main.py
├── test_qwen.py
├── requirements.txt
├── README.md


---

## 🚀 Setup Instructions

### 1. Clone Repository
git clone https://github.com/QwenLM/Qwen3-TTS
cd Qwen3-TTS

2. Create Virtual Environment
py -3.11 -m venv .venv
.venv\Scripts\activate

3. Install Dependencies
pip install -U qwen-tts
pip install librosa soundfile sox

4. Install System Dependencies
FFmpeg

Download and add to PATH:

https://ffmpeg.org/
SoX

Download and add to PATH:

http://sox.sourceforge.net/
5. Run Test Script
python test_qwen.py
6. Run Main Pipeline
python main.py

🧪 Testing
Test Cases:
English text
Long text (streaming)
Multilingual input
Different speaker voices

📊 Metrics
Latency: Total processing time

RTF (Real-Time Factor):

RTF = Processing Time / Audio Duration

⚠️ Known Issues
Hugging Face may return HTTP 503 (temporary issue)
FlashAttention not supported on Windows
Large models require high RAM

🧠 Key Learnings
Model-function compatibility is critical
Streaming improves real-time performance
Predefined vs cloned voices differ significantly

🚀 Future Work
Voice cloning using Base model
GCP deployment
Real-time API serving
Benchmarking vs other TTS models

Outputs: we acheived chunk_.. wav audio file along with metrics like leatency, RTF, aduio duration in he output..

Now we are adding moe like voiceclonning, caching, multilingual...  