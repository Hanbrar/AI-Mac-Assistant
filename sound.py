from pydub import AudioSegment
from pydub.playback import play

def playwakemp3():
    mp3_file = AudioSegment.from_file("wake_mp3.mp3", format="mp3")
    play(mp3_file)
