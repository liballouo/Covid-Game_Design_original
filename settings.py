import pygame

# screen size
WIN_WIDTH, WIN_HEIGHT = 1200, 700

LV_BTN_WIDTH, LV_BTN_HEIGHT = 150, 155
TOWER_WIDTH, TOWER_HEIGHT = 200, 210
TOWER_X, TOWER_Y = 130, 330
MANA_X, MANA_Y, MANA_W = 350, 50, 500
# frame rate
FPS = 60
# enemy path
PATH_E = (lambda y: [(1050, y), (1000, y), (950, y), (900, y), (850, y), (800, y), (750, y),
                     (700, y), (650, y), (600, y), (550, y), (500, y), (450, y), (400, y),
                     (350, y), (300, y), (250, y)])
# player path
PATH_P = (lambda y: [(200, y), (250, y), (300, y), (350, y), (400, y), (450, y),
                     (500, y), (550, y), (600, y), (650, y), (700, y), (750, y),
                     (800, y), (850, y), (900, y), (950, y)])
# base
BASE = pygame.Rect(430, 90, 195, 130)

