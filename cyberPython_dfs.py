import random
import copy
import box_world as box_world
import pygame
from path_search import dfs as dfs_path_search
from queue import LifoQueue
from searches import PriorityQueue
import utility as utility

TOTAL = box_world.WIDTH * box_world.HEIGHT

#checks that the coordinate is within the bounds of the game grid 
def valid_coord(coord, coords):
    (x, y) = coord
    if x < 0 or x >= box_world.WIDTH:
        return False
    if y < 0 or y >= box_world.HEIGHT:
        return False

    for _coord in coords:
        (_x, _y) = _coord
        if x == _x and y == _y:
            return False
    return True

#random coordinates for the apple (food) on the game grid that the snake hasn't occupied.
def get_apple_coord(snake_coords):
    apple = (random.randint(0, box_world.WIDTH - 1), random.randint(0, box_world.HEIGHT - 1))
    while not valid_coord(apple, snake_coords):
        apple = (random.randint(0, box_world.WIDTH - 1), random.randint(0, box_world.HEIGHT - 1))
    return apple

#move the snake in the direction of the new coordinate
def move(snake_coords, n_coord, apple, draw=False):
    snake_coords.insert(0, n_coord)
    tail = None
    if not utility.cell_equal(n_coord, apple):
        score = 0
        tail = snake_coords.pop()
    else:
        score = 1

    if draw:
        if tail:
            box_world.draw_cells([tail, apple], box_world.COLOR.BG_COLOR.value)
        # draw the head
        box_world.draw_cell(snake_coords[0], box_world.COLOR.GREEN.value)
        # draw the body
        box_world.draw_cell_line(snake_coords[1:], box_world.COLOR.DARK_GRAY.value, box_world.COLOR.DARK_GREEN.value)

    return score

#simulate a run of the snake from its current position to the apple following the given path
def virtual_run(snake_coords, apple, path):
    _snake_coords = copy.deepcopy(snake_coords)
    _apple = copy.deepcopy(apple)
    _path = copy.deepcopy(path)

    for _n_coord in _path:
        move(_snake_coords, _n_coord, _apple)

    if len(_snake_coords) == TOTAL:
        return True

    if utility.cell_equal(_snake_coords[0], _apple):
        __path = dfs_path_search.cal(_snake_coords[0], _snake_coords[-1], _snake_coords[:-1]) 
        return __path is not None
    else:
        return True

#the snake move in a direction that gets it closer to the apple
def wander(snake_coords, apple):
    adjs = utility.adj(snake_coords[0], obstacles=snake_coords[:-1])
    stack = LifoQueue()

    for adj in adjs:
        path = dfs_path_search.cal(adj, snake_coords[-2], [adj] + snake_coords[:-2])
        if path:
            stack.put(adj)

    if not stack.empty():
        return stack.get()
    else:
        return None

#calculates the next coordinate for the snake to move to. It first tries to find a path to the apple using DFS search.
def next_coord(snake_coords, apple):
    path = dfs_path_search.cal(snake_coords[0], apple, snake_coords[:-1])

    if path:
        if virtual_run(snake_coords, apple, path):
            return path[0]  
        else:
            return wander(snake_coords, apple)
    else:
        return wander(snake_coords, apple)


def run_game():
    # Initialize pygame's font module
    pygame.font.init()
    snake_coords = [(1, 2), (1, 1)]
    apple = get_apple_coord(snake_coords)
    score = 0

    box_world.draw_background()
    box_world.draw_grid()
    box_world.draw_cell_line(snake_coords, box_world.COLOR.DARK_GRAY.value, box_world.COLOR.DARK_GREEN.value)
    box_world.draw_cell(apple, box_world.COLOR.RED.value)
    box_world.update()

    while True:
        n_coord = next_coord(snake_coords, apple)
        if not n_coord:
            print("The snake is stuck. Try again. Game over")
            return

        score += move(snake_coords, n_coord, apple, draw=True)
        # Render score
        score_surface = box_world.font.render('Score: {}'.format(score), True, (255, 255, 255))
        # Position of score, change it according to your requirements
        score_position = (box_world.WINDOW_WIDTH - score_surface.get_width(), 0)
        # Draw score onto screen
        box_world.screen.blit(score_surface, score_position)

        if not valid_coord(snake_coords[0], snake_coords[1:]):
            print("Game Over!")
            valid_coord(snake_coords[0], snake_coords[1:])
            return
        if len(snake_coords) == TOTAL:
            print("Nobody beats the cyber python: the ultimate AIpple eater.")
            box_world.draw_grid()
            game_over_font = pygame.font.Font('freesansbold.ttf', 50)
            game_over_surface = game_over_font.render('Game Over', True, (255, 255, 255))
            game_over_position = ((box_world.WINDOW_WIDTH - game_over_surface.get_width()) // 2, box_world.WINDOW_HEIGHT // 2 - game_over_surface.get_height())
            box_world.screen.blit(game_over_surface, game_over_position)

            win_surface = box_world.font.render('Nobody beats the cyber python: the ultimate AIpple eater.', True, (255, 255, 255))
            win_position = ((box_world.WINDOW_WIDTH - win_surface.get_width()) // 2, box_world.WINDOW_HEIGHT // 2)
            box_world.screen.blit(win_surface, win_position)

            box_world.update()
            pygame.time.delay(3000)
            return
        
        if utility.cell_equal(n_coord, apple):
            apple = get_apple_coord(snake_coords)

        box_world.draw_cell(apple, box_world.COLOR.RED.value)
        box_world.draw_grid()
        pygame.display.update()

def main():
    global TOTAL

    box_world.init("Cyber python: DFS search", 15, 13)
    box_world.draw_grid()
    box_world.update()

    TOTAL = box_world.WIDTH * box_world.HEIGHT
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                run_game()

if __name__ == "__main__":
    main()
