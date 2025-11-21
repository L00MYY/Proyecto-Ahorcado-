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

background_sound.set_volume(0.1)
enter_sound.set_volume(1.0)
sound_correct.set_volume(1.0)
sound_incorrect.set_volume(1.0)
winning_sound.set_volume(1.0)
losing_sound.set_volume(1.0)

def play_correct_sound():
    sound_correct.play()

def play_incorrect_sound():
    sound_incorrect.play()
    
def play_winning_sound():
    winning_sound.play()
    
def play_losing_sound():
    losing_sound.play()
    
def play_enter_sound():
    enter_sound.play()