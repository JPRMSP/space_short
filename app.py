import streamlit as st
from gtts import gTTS
from PIL import Image
import numpy as np
from scipy.io.wavfile import write
import time
import os

st.set_page_config(page_title="Nolan Space Short", page_icon="🌌", layout="centered")

# -------------------------------
# Generate a soft ambient background tone
# -------------------------------
def generate_background_music(filename="background.wav", duration=60, freq=220):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = 0.3 * np.sin(2 * np.pi * freq * t)  # soft hum
    stereo_wave = np.stack([wave, wave], axis=1)
    write(filename, sample_rate, stereo_wave.astype(np.float32))

if not os.path.exists("background.wav"):
    generate_background_music()

# -------------------------------
# Nolan-style narration
# -------------------------------
script_text = """
They told me space is empty, but they were wrong.
Out here, every breath is borrowed, every second earned.
When gravity no longer holds you, you realize the only thing pulling you forward is your will.
Dreams aren't made on solid ground. They're forged in the silence between stars.
Keep going. Even the stars began in darkness.
"""

if not os.path.exists("narration.mp3"):
    tts = gTTS(script_text)
    tts.save("narration.mp3")

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🌌 Christopher Nolan – Space Motivation Short")

# Load images
images = [
    "01_space_empty.png",
    "02_training.png",
    "03_sunrise.png",
    "04_tear.png",
    "05_nebula.png"
]

# Combine both audio tracks in UI
st.audio("background.wav")
st.audio("narration.mp3")

# -------------------------------
# Slideshow
# -------------------------------
st.subheader("🚀 Visual Journey")
for img in images:
    image = Image.open(img)
    st.image(image, use_container_width=True)
    time.sleep(3)

st.success("✨ The stars are waiting. Keep going.")
