# voice_interface.py
import speech_recognition as sr
from memory_logger import memory_logger

def activate_voice_interface():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Voice Interface Activated. Speak something...")

    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        memory_logger.log_event(f"Voice command received: {command}")

    except sr.UnknownValueError:
        print("❌ Voice not recognized.")
        memory_logger.log_event("Voice recognition failed.")
    except sr.RequestError as e:
        print(f"❌ Could not request results: {e}")
        memory_logger.log_event(f"Voice recognition request error: {e}")
