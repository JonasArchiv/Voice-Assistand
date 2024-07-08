import speech_recognition as sr
from gtts import gTTS
import os
import playsound


filename = "audio\\output.mp3"


def from_microphone():
    speech_engine = sr.Recognizer()
    with sr.Microphone() as micro:
        print("Recording...")
        audio = speech_engine.record(micro, duration=5)
        print("Recognition...")
        microtext = speech_engine.recognize_google(audio, language="de-DE")
        return microtext


def speak(text):
    tts = gTTS(text=text, lang="de")
    if os.path.exists(filename):
        os.remove(filename)
    tts.save(filename)
    playsound.playsound(filename)


def del_output():
    if os.path.exists(filename):
        os.remove(filename)
