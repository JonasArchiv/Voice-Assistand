import pygame
import time


def play_audio_old(file_path):
    pygame.mixer.init()

    pygame.mixer.music.load(file_path)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)
