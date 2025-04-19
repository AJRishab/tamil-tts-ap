import streamlit as st
from gtts import gTTS
import tempfile

# Set page config
st.set_page_config(page_title="Tamil TTS", layout="centered")

# Page title
st.title("🗣️ Tamil Text to Speech Converter")

# Text input box (visible immediately)
tamil_text = st.text_area("Type your Tamil text here 👇", height=150)

# Button to trigger conversion
if st.button("🔊 Convert to Speech"):
    if tamil_text.strip() == "":
        st.warning("Please enter some Tamil text.")
    else:
        # Convert to speech
        tts = gTTS(tamil_text, lang='ta')

        # Save to a temporary MP3 file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tts.save(tmp_file.name)
            st.audio(tmp_file.name, format="audio/mp3")
            st.success("✅ Speech generated!")
