
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
background_sound.set_volume(0.2)

def play_correct_sound():
    sound_correct.play()