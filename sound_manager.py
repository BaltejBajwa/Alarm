import pygame

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sound.mp3")
    pygame.mixer.music.play()
