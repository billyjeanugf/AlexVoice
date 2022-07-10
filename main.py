from stt import *
from tts import speak

for text in listen():
    if "привет" in text:
        speak("привет")
