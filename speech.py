import os
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

    audio = AudioSegment.from_mp3("output.mp3")
    play(audio)

    os.remove("output.mp3")  # Delete the audio file