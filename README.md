# kingdroid
Following are the services you can use

`from kingdroid.tts import TTS `<br>
ms=TTS() <br>
ms.speak('text to speak')<br>
ms.get_voices()<br>
ms.get_language()<br>
ms.get_engines()<br>
ms.get_duration()<br>
ms.get_available_languages()<br>
ms.get_default_voice()<br>
ms.get_max_input_length()<br>
ms.get_default_engine()<br>
ms.set_voice(voice)<br>
ms.set_pitch(pitch)<br>
ms.set_language(loc)<br>
ms.set_speech_rate(rate)<br>
ms.is_speaking()<br>
ms.is_language_available(loc)<br>


Note:- This will only work in android
