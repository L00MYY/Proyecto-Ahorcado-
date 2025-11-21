import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#La funcion .load() sirve para cargar las imagenes, no las muestra solo las carga.
alvinHead = pygame.image.load("assets/fotoSFCabeza.png")

#¿Cómo las coordenadas?
# Las coordenadas en la pantalla inician en la esquina superior izquierda y se extienden en el eje de las x, es decir,
# por el largo de la pantalla, y en el eje de las Y's se extiende hacia abajo con valores positivos, por eso le sumamos o restamos
# reciben la coordenada incial de la cabeza. Para el resto de las extremidades se les posiciona sumandole o restandole
# cantidades a los iniciales para que apareza el dibujo correctamente.
# Basicamente es como tener el cuadrante I del plano cartesiano pero alrevez y con el eje (0,0) en la esquina superior izquierda.

def draw_head(surface, x, y):
    #pygame.draw.circle(surface, WHITE, (x, y), 30, 3)
   surface.blit(alvinHead,
             (x - alvinHead.get_width() // 2,
              y - alvinHead.get_height() // 2))

def draw_body(surface, x, y):
    pygame.draw.line(surface, WHITE, (x, y + 30), (x, y + 110), 4)

def draw_left_arm(surface, x, y):
    pygame.draw.line(surface, WHITE, (x, y + 50), (x - 40, y + 20), 4)

def draw_right_arm(surface, x, y):
    pygame.draw.line(surface, WHITE, (x, y + 50), (x + 40, y + 20), 4)

def draw_left_leg(surface, x, y):
    pygame.draw.line(surface, WHITE, (x, y + 110), (x - 30, y + 170), 4)

def draw_right_leg(surface, x, y):
    pygame.draw.line(surface, WHITE, (x, y + 110), (x + 30, y + 170), 4)

def draw_doll(SCREEN, doll_x, doll_y, wrong_count):
    if wrong_count <= 5:
        draw_head(SCREEN, doll_x, doll_y)
    if wrong_count <= 4:
        draw_body(SCREEN, doll_x, doll_y)
    if wrong_count <= 3:
        draw_left_arm(SCREEN, doll_x, doll_y)
    if wrong_count <= 2:
        draw_right_arm(SCREEN, doll_x, doll_y)
    if wrong_count <= 1:
        draw_left_leg(SCREEN, doll_x, doll_y)
    if wrong_count <= 0:
        draw_right_leg(SCREEN, doll_x, doll_y)
