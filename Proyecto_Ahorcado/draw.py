# hangman_doll.py
import pygame

BLACK = (0, 0, 0)

def draw_head(surface, x, y):
    pygame.draw.circle(surface, BLACK, (x, y), 30, 3)

def draw_body(surface, x, y):
    pygame.draw.line(surface, BLACK, (x, y + 30), (x, y + 110), 4)

def draw_left_arm(surface, x, y):
    pygame.draw.line(surface, BLACK, (x, y + 50), (x - 40, y + 20), 4)

def draw_right_arm(surface, x, y):
    pygame.draw.line(surface, BLACK, (x, y + 50), (x + 40, y + 20), 4)

def draw_left_leg(surface, x, y):
    pygame.draw.line(surface, BLACK, (x, y + 110), (x - 30, y + 170), 4)

def draw_right_leg(surface, x, y):
    pygame.draw.line(surface, BLACK, (x, y + 110), (x + 30, y + 170), 4)



