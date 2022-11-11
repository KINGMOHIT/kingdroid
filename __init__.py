from kivy.utils import platform

from kivy.logger import Logger
import webbrowser

from jnius import autoclass, cast, JavaException,PythonJavaClass,java_method
from android import activity
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
Locale = autoclass('java.util.Locale')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

mActivity = PythonActivity.mActivity
ArrayList = autoclass('java.util.ArrayList')
    

def text_to_speech(text, lang=Locale.US):
        tts = TextToSpeech(mActivity, None)
        tts.setLanguage(lang)
        tts.speak(str(text), TextToSpeech.QUEUE_FLUSH, None)