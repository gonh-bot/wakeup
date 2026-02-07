# core/audio.py

import pygame
from core.config import ALARM_SOUND

pygame.mixer.init()

def play_alarm():
    pygame.mixer.music.load(ALARM_SOUND)
    pygame.mixer.music.play()
