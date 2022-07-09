import pyttsx3

def speak(speech):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_id = 'com.apple.speech.synthesis.voice.yuri'
    engine.setProperty('voice', voice_id)
    engine.say(speech)
    engine.runAndWait()

#ладно
#в общем я наконец то разобрался с pyttsx3
#ты не сможешь запустить, тут id для маков
