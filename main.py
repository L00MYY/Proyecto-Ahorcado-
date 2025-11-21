import pygame
import sys
from game import hangman_game
from sound import play_correct_sound

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (52, 152, 219)

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego: Ahorcado")

font_small = pygame.font.Font(None, 24)
font_medium = pygame.font.Font(None, 36)
font_large = pygame.font.Font(None, 50)
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2


def draw_text_centered(text, font, color, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (center_x, y)
    screen.blit(textobj, textrect)
    return textrect


def draw_loading_screen():
    screen.fill(BLACK)
    
    title = "I N I C I A N D O   E L  J U E G O"
    draw_text_centered("=" * 30, font_small, WHITE, 50)
    draw_text_centered(title, font_large, YELLOW, 80)
    draw_text_centered("=" * 30, font_small, WHITE, 110)
    
    draw_text_centered("CARGANDO DATOS...", font_medium, WHITE, 180)
    
    bar_width = 300
    bar_height = 20
    bar_x = (SCREEN_WIDTH - bar_width) // 2
    bar_y = 220
    
    pygame.draw.rect(screen, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
    pygame.draw.rect(screen, GREEN, (bar_x, bar_y, bar_width, bar_height))
    draw_text_centered("100%", font_small, GREEN, bar_y + bar_height + 20)

    draw_text_centered("Carga Completa. Haz clic para continuar.", font_medium, WHITE, 300)
    
    pygame.display.flip()


def main_menu_simple():
    
    draw_loading_screen()
    
    waiting_for_start = True
    while waiting_for_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting_for_start = False
    
    
    options = [
        ("1", "Abrir el programa", "RUN"),
        ("2", "Acerca de", "ABOUT"),
        ("3", "Salir", "QUIT")
    ]
    
    button_rects = []
    
    y_start = 130
    padding = 40
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 
                for rect, target in button_rects:
                    if rect.collidepoint(mouse_pos):
                        if target == "QUIT":
                            running = False
                        elif target == "RUN":
                            #EJECUTAMOS
                            hangman_game(screen)
                        elif target == "OPTIONS":
                            draw_text_centered("Mostrando opciones... (Clic para volver)", font_medium, YELLOW, center_y)
                            pygame.display.flip()
                            wait_for_click()
                        elif target == "ABOUT":
                            draw_text_centered("Información: Yo. (Clic para volver)", font_medium, YELLOW, center_y)
                            pygame.display.flip()
                            wait_for_click()
        screen.fill(BLACK)

        menu_title = "M E N U   P R I N C I P A L"
        draw_text_centered("=" * 25, font_small, WHITE, 30)
        draw_text_centered(menu_title, font_large, BLUE, 60)
        draw_text_centered("-" * 25, font_small, WHITE, 90)

        button_rects = [] 
        
        for i, (num, text, target) in enumerate(options):
            full_text = f"[{num}] - {text}"
            
            rect = draw_text_centered(full_text, font_medium, WHITE, y_start + i * padding)
            button_rects.append((rect, target))
            
        draw_text_centered("-" * 20, font_small, WHITE, y_start + len(options) * padding)

        draw_text_centered("Haz clic en una opción.", font_small, WHITE, SCREEN_HEIGHT - 30)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def wait_for_click():
    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                wait = False

if __name__ == "__main__":
    main_menu_simple()