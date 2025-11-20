import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_head(surface, x, y):
    pygame.draw.circle(surface, WHITE, (x, y), 30, 3)

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