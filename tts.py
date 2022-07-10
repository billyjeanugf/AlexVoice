#импорты
import pyttsx3

#говорить
def speak(speech):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_id = 'com.apple.speech.synthesis.voice.yuri'
    engine.setProperty('voice', voice_id)
    engine.say(speech)
    engine.runAndWait()

