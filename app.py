import streamlit as st
from PIL import Image
from gtts import gTTS
import time
import tempfile
from pydub import AudioSegment
from pydub.generators import Sine

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Echoes Beyond the Stars", layout="wide")
st.title("🎬 Echoes Beyond the Stars — A Nolan-Inspired Space Short")

# ---------- SCENES (PNG IMAGES) ----------
scenes = [
    {"file": "01_space_empty.png", "caption": "They told me space is empty… but they were wrong.", "duration": 5},
    {"file": "02_training.png", "caption": "Out here, every breath is borrowed… every second, earned. But emptiness teaches purpose.", "duration": 8},
    {"file": "03_sunrise.png", "caption": "When gravity no longer holds you… you realize — the only thing pulling you forward is your will.", "duration": 8},
    {"file": "04_tear.png", "caption": "Dreams aren’t made on solid ground. They’re forged in the silence between stars.", "duration": 8},
    {"file": "05_nebula.png", "caption": "If you ever feel lost in the dark… look up. The universe isn’t infinite — it’s inviting you to begin again.", "duration": 10}
]

# ---------- FUNCTION: GENERATE AMBIENT MUSIC ----------
def generate_ambient_music(duration_ms=60000):
    """Creates subtle Nolan-style ambient tones."""
    base = Sine(220).to_audio_segment(duration=duration_ms).apply_gain(-20)
    layer = Sine(440).to_audio_segment(duration=duration_ms).apply_gain(-25)
    hum = Sine(110).to_audio_segment(duration=duration_ms).apply_gain(-30)
    return base.overlay(layer).overlay(hum).fade_in(2000).fade_out(2000)

# Generate temporary ambient background
music = generate_ambient_music(60000)
temp_music = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
music.export(temp_music.name, format="mp3")

# ---------- PLAY BACKGROUND MUSIC ----------
st.audio(temp_music.name, format="audio/mp3")

# ---------- SLIDESHOW ----------
placeholder = st.empty()
for scene in scenes:
    # Display image
    img = Image.open(scene["file"])
    placeholder.image(img, use_container_width=True)

    # Display caption
    st.markdown(f"### _{scene['caption']}_")

    # Generate and play narration
    tts = gTTS(text=scene["caption"], lang='en', slow=False)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")
        time.sleep(scene["duration"])

# ---------- ENDING ----------
st.markdown("### 🌌 *Keep going. Even the stars began in darkness.*")
