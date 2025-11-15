
import pygame
pygame.init()
pygame.mixer.init()

ANCHO, ALTO = 800, 600

FUENTE_MEDIA = pygame.font.SysFont(None, 32)
FUENTE_GRANDE = pygame.font.SysFont(None, 48)
sound_correct = pygame.mixer.Sound("sounds/correct.sound.wav")
sound_incorrect = pygame.mixer.Sound("sounds/incorrect.sound.wav")
winning_sound = pygame.mixer.Sound("sounds/winning.sound.wav")
losing_sound = pygame.mixer.Sound("sounds/losing.sound.wav")
enter_sound = pygame.mixer.Sound("sounds/enter.sound.wav")
background_sound = pygame.mixer.Sound("sounds/background.music.wav")
background_sound.play(-1)

sound_incorrect.play()
pygame.time.delay(1000)

import os

ruta = os.path.join(os.path.expanduser("~"), "Desktop", "mi_archivo.wav")

with open(ruta, "wb") as f:
    f.write(b"contenido_del_wav")
