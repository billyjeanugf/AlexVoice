from stt import *
from tts import speak
from config import *

for text in listen():
    if text == alias:
        speak("привет")
    else:
        speak("нахуй пошел")
