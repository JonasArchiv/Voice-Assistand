import threading
from playsound import playsound


class Audio:
    def __init__(self, file_path):
        self.file_path = file_path
        self.playing = threading.Event()
        self.thread = threading.Thread(target=self.play_audio, args=(file_path,), daemon=True)

    def play_audio(self, file_path):
        playsound(file_path)

    def play(self):
        if not self.thread.is_alive():
            self.playing.set()
            self.thread.start()

    def stop(self):
        if self.thread.is_alive():
            self.playing.clear()


# Usage:
player = AudioPlayer('audiofile.mp3')
player.play()
