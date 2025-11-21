import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#La funcion .load() sirve para cargar las imagenes, no las muestra solo las carga.
alvinHead = pygame.image.load("assets/fotoSFCabeza.png")
alvinChest = pygame.image.load("assets/torsoSF.png")
alvinLeftArm = pygame.image.load("assets/brazoIzquierdoSF.png")
alvinRightArm = pygame.image.load("assets/brazoDerechoSF.png")
alvinLeftLeg = pygame.image.load("assets/piernaIzquierdaSF.png")
alvinRightLeg = pygame.image.load("assets/piernaDerechaSF.png")
rope = pygame.image.load("assets/sogaSF.png")

ropeScale=pygame.transform.scale(rope,(125,400))
alvinHeadScale=pygame.transform.scale(alvinHead,(100,100))
alvinChestScale=pygame.transform.scale(alvinChest,(177,100))
alvinLeftArmScale=pygame.transform.scale(alvinLeftArm,(100,150))
alvinRightArmScale=pygame.transform.scale(alvinRightArm,(100,150))
alvinLeftLegScale=pygame.transform.scale(alvinLeftLeg,(100,200))
alvinRightLegScale=pygame.transform.scale(alvinRightLeg,(100,200))


"""#¿Cómo las coordenadas?
# Las coordenadas en la pantalla inician en la esquina superior izquierda y se extienden en el eje de las x, es decir,
# por el largo de la pantalla, y en el eje de las Y's se extiende hacia abajo con valores positivos, por eso le sumamos o restamos
# reciben la coordenada incial de la cabeza. Para el resto de las extremidades se les posiciona sumandole o restandole
# cantidades a los iniciales para que apareza el dibujo correctamente.
# Basicamente es como tener el cuadrante I del plano cartesiano pero al revez y con el eje (0,0) en la esquina superior izquierda."""

# Funciones para dibujar cada pieza
def draw_rope(surface, x, y):
    surface.blit(ropeScale, ((x + 8) - ropeScale.get_width() // 2, y-280))

def draw_head(surface, x, y):
    surface.blit(alvinHeadScale, (x - alvinHeadScale.get_width() // 2, y))


def draw_chest(surface, x, y):
    surface.blit(alvinChestScale, (x - alvinChestScale.get_width() // 2, y + alvinChestScale.get_height()))


def draw_left_arm(surface, x, y):
    chest_y = y + alvinHeadScale.get_height()
    arm_y = chest_y + 1  # pequeño ajuste
    surface.blit(alvinRightArmScale, (x - alvinChestScale.get_width() // 2 - alvinRightArmScale.get_width() + 10, arm_y))


def draw_right_arm(surface, x, y):
    chest_y = y + alvinHeadScale.get_height()
    arm_y = chest_y - 5  # mismo ajuste
    surface.blit(alvinLeftArmScale, (x + alvinChestScale.get_width() // 2 - 10, arm_y))


def draw_left_leg(surface, x, y):
    chest_y = y + alvinHeadScale.get_height()
    leg_y = chest_y + alvinChestScale.get_height() - 5
    surface.blit(alvinRightLegScale, (x - 105, leg_y))


def draw_right_leg(surface, x, y):
    chest_y = y + alvinHeadScale.get_height()
    leg_y = chest_y + alvinChestScale.get_height() - 5
    surface.blit(alvinLeftLegScale, (x - 5, leg_y))

def draw_doll(SCREEN, doll_x, doll_y, wrong_count):
    draw_rope(SCREEN, doll_x, doll_y)
    if wrong_count <= 5:
        draw_head(SCREEN, doll_x, doll_y)
    if wrong_count <= 4:
        draw_chest(SCREEN, doll_x, doll_y)
    if wrong_count <= 3:
        draw_right_arm(SCREEN, doll_x, doll_y)
    if wrong_count <= 2:
        draw_left_arm(SCREEN, doll_x, doll_y)
    if wrong_count <= 1:
        draw_left_leg(SCREEN, doll_x, doll_y)
    if wrong_count <= 0:
        draw_right_leg(SCREEN, doll_x, doll_y)
