import streamlit as st
import speech_recognition as sr

st.title("Live Voice to Text Converter")

r = sr.Recognizer()

# Create a function to record audio from the user's microphone
def record_audio():
    with sr.Microphone() as source:
        st.write("Recording started. Speak now!")
        audio_data = r.record(source, duration=5)
        st.write("Recording stopped. Processing audio...")
        text = r.recognize_google(audio_data)
        st.write(f"Transcription: {text}")
        
# Add a button to the app that the user can click to start recording audio
if st.button("Record Audio"):
    record_audio()
