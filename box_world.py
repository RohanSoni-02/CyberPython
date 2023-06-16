import pygame
from enum import Enum

WIDTH = 24
HEIGHT = 18
CELL_SIZE = 40
WINDOW_WIDTH = WIDTH * CELL_SIZE
WINDOW_HEIGHT = HEIGHT * CELL_SIZE

screen = None
font = None

class COLOR(Enum):
    WHITE = (255, 255, 255)
    WATER = (35,137,218)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    DARK_GREEN = (0, 155, 0)
    DARK_GRAY = (40, 40, 40)
    BG_COLOR = (0, 0, 0)

#set up the game window
def init(title, width=24, height=18):
    global screen, font, WIDTH, HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT
    WIDTH = width
    HEIGHT = height
    WINDOW_WIDTH = WIDTH * CELL_SIZE
    WINDOW_HEIGHT = HEIGHT * CELL_SIZE

    pygame.init()
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 18)

#update the entire display
def update():
    pygame.display.update()

def draw_background():
    screen.fill(COLOR.BG_COLOR.value)

#draw a grid over the entire game window
def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, COLOR.DARK_GRAY.value, (x, 0), (x, WINDOW_HEIGHT))

    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, COLOR.DARK_GRAY.value, (0, y), (WINDOW_WIDTH, y))

    update()

#draw a cell at a specified location with a specified color
def draw_cell(cell, color=COLOR.GREEN.value):
    (x, y) = cell
    x = x * CELL_SIZE
    y = y * CELL_SIZE

    outer_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    padding_rect = pygame.Rect(x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4)
    inner_rect = pygame.Rect(x + 4, y + 4, CELL_SIZE - 8, CELL_SIZE - 8)

    pygame.draw.rect(screen, color, outer_rect)
    pygame.draw.rect(screen, COLOR.BG_COLOR.value, padding_rect)
    pygame.draw.rect(screen, color, inner_rect)

#draw a list of cells on the grid 
def draw_cells(cells, color=COLOR.GREEN.value):
    for cell in cells:
        draw_cell(cell, color)

#draw a list of cells on the grid
#draw lines between the center of each pair of adjacent cells
def draw_cell_line(cells, cell_color=COLOR.GREEN.value, line_color=COLOR.DARK_GREEN.value):
    if len(cells) < 1:
        return

    draw_cells(cells, cell_color)

    for i in range(1, len(cells)):
        (x1, y1) = cells[i - 1]
        (x2, y2) = cells[i]
        pygame.draw.line(screen, line_color,
                         ((x1 + .5) * CELL_SIZE, (y1 + .5) * CELL_SIZE),
                         ((x2 + .5) * CELL_SIZE, (y2 + .5) * CELL_SIZE),
                         6)
