import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#La funcion .load() sirve para cargar las imagenes, no las muestra solo las carga.
alvinHead = pygame.image.load("assets/fotoSFCabeza.png")
alvinChest = pygame.image.load("assets/torsoSF.png")
alvinLeftArm = pygame.image.load("assets/brazoIzquierdoSF.png")
alvinRightArm = pygame.image.load("assets/brazoDerechoSF.png")
alvinLeftLeg = pygame.image.load("assets/piernaIzquierdaSF.png")
alvinRightLeg = pygame.image.load("assets/piernaDerechSF.png")

alvinHeadScale=pygame.transform.scale(alvinHead,(100,100))
alvinChestScale=pygame.transform.scale(alvinHead,(100,100))
alvinLeftArmScale=pygame.transform.scale(alvinHead,(100,100))
alvinRightArmScale=pygame.transform.scale(alvinHead,(100,100))
alvinLeftLegScale=pygame.transform.scale(alvinHead,(100,100))
alvinRightLegScale=pygame.transform.scale(alvinHead,(100,100))


"""#¿Cómo las coordenadas?
# Las coordenadas en la pantalla inician en la esquina superior izquierda y se extienden en el eje de las x, es decir,
# por el largo de la pantalla, y en el eje de las Y's se extiende hacia abajo con valores positivos, por eso le sumamos o restamos
# reciben la coordenada incial de la cabeza. Para el resto de las extremidades se les posiciona sumandole o restandole
# cantidades a los iniciales para que apareza el dibujo correctamente.
# Basicamente es como tener el cuadrante I del plano cartesiano pero al revez y con el eje (0,0) en la esquina superior izquierda."""

# Funciones para dibujar cada pieza
def draw_head(surface, x, y):
    surface.blit(alvinHead, (x - alvinHead.get_width() // 2, y))


def draw_chest(surface, x, y):
    surface.blit(alvinChest, (x - alvinChest.get_width() // 2, y + alvinHead.get_height()))


def draw_left_arm(surface, x, y):
    chest_y = y + alvinHead.get_height()
    arm_y = chest_y + 20  # pequeño ajuste
    surface.blit(alvinLeftArm, (x - alvinChest.get_width() // 2 - alvinLeftArm.get_width() + 10, arm_y))


def draw_right_arm(surface, x, y):
    chest_y = y + alvinHead.get_height()
    arm_y = chest_y + 20  # mismo ajuste
    surface.blit(alvinRightArm, (x + alvinChest.get_width() // 2 - 10, arm_y))


def draw_left_leg(surface, x, y):
    chest_y = y + alvinHead.get_height()
    leg_y = chest_y + alvinChest.get_height() - 10
    surface.blit(alvinLeftLeg, (x - 25, leg_y))


def draw_right_leg(surface, x, y):
    chest_y = y + alvinHead.get_height()
    leg_y = chest_y + alvinChest.get_height() - 10
    surface.blit(alvinRightLeg, (x + 5, leg_y))

def draw_doll(SCREEN, doll_x, doll_y, wrong_count):
    if wrong_count <= 5:
        draw_head(SCREEN, doll_x, doll_y)
    if wrong_count <= 4:
        draw_chest(SCREEN, doll_x, doll_y)
    if wrong_count <= 3:
        draw_left_arm(SCREEN, doll_x, doll_y)
    if wrong_count <= 2:
        draw_right_arm(SCREEN, doll_x, doll_y)
    if wrong_count <= 1:
        draw_left_leg(SCREEN, doll_x, doll_y)
    if wrong_count <= 0:
        draw_right_leg(SCREEN, doll_x, doll_y)
