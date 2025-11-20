
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

elif evento.key == pygame.K_RETURN:
    enter_sound.play()
    
if letra in secret_word:
    sound_correct.play()
    
else: 
    errors += 1
    sound_incorrect.play()

if win:
    winning_sound.play
    victory_animation(screen)
    
if errors == max_errors:
    losing_sound.play()
    losing_animation(screen)
    
def victory_animation(screen):
    font = pygame.font.Font(None, 80)
    text = font.render("¡YOU WON", True, (0, 255, 9))
    y = 600
    
    for i in range(60):
        screen.fill((0,0,0))
        screen.blit(text, (200,y))
        y -= 5
        pygame.display.update()
        pygame.time.delay(30)
        
def losing_animation(screen):
    font  = pygame.font.Font(None, 80)
    text = font.render("YOU LOST!", True, (255, 0, 0))
    
    for i in range(30):
        screen.fill((i*8, 0, 0))
        screen.blit(text, (200,250))
        pygame.display.update()
        pygame.time.delay(40)
        

