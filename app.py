import streamlit as st
from gtts import gTTS
from PIL import Image
import numpy as np
import wave
import struct
import time
import os

# -------------------------------------------------------
# Streamlit Page Setup
# -------------------------------------------------------
st.set_page_config(page_title="Nolan Space Short", page_icon="🌌", layout="centered")

st.title("🌌 Christopher Nolan – Space Motivation Short")
st.write("A 1-minute cinematic journey through space and self-discovery.")

# -------------------------------------------------------
# Generate a Soft Ambient Background Tone (no external libs)
# -------------------------------------------------------
def generate_background_music(filename="background.wav", duration=60, freq=220):
    """Generate a low-frequency ambient hum using numpy and wave."""
    sample_rate = 44100
    amplitude = 16000
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave_data = amplitude * np.sin(2 * np.pi * freq * t)

    with wave.open(filename, "w") as f:
        f.setnchannels(1)          # mono
        f.setsampwidth(2)          # 16-bit samples
        f.setframerate(sample_rate)
        for s in wave_data:
            f.writeframes(struct.pack('<h', int(s)))

# Generate ambient music once
if not os.path.exists("background.wav"):
    generate_background_music()

# -------------------------------------------------------
# Nolan-style Narration Script
# -------------------------------------------------------
script_text = """
They told me space is empty, but they were wrong.
Out here, every breath is borrowed, every second earned.
When gravity no longer holds you, you realize the only thing pulling you forward is your will.
Dreams aren't made on solid ground. They're forged in the silence between stars.
Keep going. Even the stars began in darkness.
"""

# Generate narration (voice) if not already saved
if not os.path.exists("narration.mp3"):
    tts = gTTS(script_text)
    tts.save("narration.mp3")

# -------------------------------------------------------
# Audio Controls
# -------------------------------------------------------
st.subheader("🎧 Listen to the Soundscape")
st.audio("background.wav")
st.audio("narration.mp3")

# -------------------------------------------------------
# Display the Slideshow
# -------------------------------------------------------
st.subheader("🚀 Visual Journey")

images = [
    "01_space_empty.png",
    "02_training.png",
    "03_sunrise.png",
    "04_tear.png",
    "05_nebula.png"
]

for img in images:
    if os.path.exists(img):
        image = Image.open(img)
        st.image(image, use_column_width=True)
        time.sleep(3)
    else:
        st.warning(f"⚠️ Image not found: {img}")

st.success("✨ The stars are waiting. Keep going.")
