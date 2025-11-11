import streamlit as st
from gtts import gTTS
from PIL import Image
import pygame
import time
import os

# Initialize Pygame mixer for background sound
pygame.mixer.init()

# Function to generate background tone dynamically
def generate_background_music(duration=60):
    freq = 220  # Base tone frequency
    sample_rate = 44100
    sound = pygame.sndarray.make_sound(
        (4096 * pygame.surfarray.pixels3d(pygame.Surface((1, 1)))).astype('int16')
    )
    sound.play(-1)
    time.sleep(duration)
    sound.stop()

# Voice narration text (Nolan-style)
script_text = """
They told me space is empty, but they were wrong.
Out here, every breath is borrowed, every second earned.
When gravity no longer holds you, you realize the only thing pulling you forward is your will.
Dreams aren't made on solid ground. They're forged in the silence between stars.
Keep going. Even the stars began in darkness.
"""

# Generate narration
if not os.path.exists("narration.mp3"):
    tts = gTTS(script_text)
    tts.save("narration.mp3")

# Streamlit UI
st.title("🌌 Christopher Nolan - Space Motivation Short")

# Load images in sequence
images = [
    "01_space_empty.png",
    "02_training.png",
    "03_sunrise.png",
    "04_tear.png",
    "05_nebula.png"
]

# Play audio controls
st.audio("narration.mp3")

# Display slideshow
for img in images:
    image = Image.open(img)
    st.image(image, use_container_width=True)
    time.sleep(3)

st.success("🚀 End of Nolan-inspired space short!")
