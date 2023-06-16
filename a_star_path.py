from path_search.a_star import cal
import box_world as box_world
import pygame

if __name__ == "__main__":
    box_world.init("Research HD: A* path finding")
    box_world.draw_background()
    box_world.draw_grid()

    start = (8, 9)
    end = (21, 5)
    obstacles = []
    #obstacles for the snake
    for x in range(4, 10):
        obstacles.append((x, 3))
    for x in range(4, 13):
        obstacles.append((x, 12))
    for y in range(2, 14):
        obstacles.append((10, y))
    for y in range(0, 7):
        obstacles.append((17, y))
    for y in range(2, 17):
        obstacles.append((14, y))

    box_world.draw_cell(start, box_world.COLOR.GREEN.value)
    box_world.draw_cell(end, box_world.COLOR.RED.value)
    box_world.draw_cells(obstacles, box_world.COLOR.WHITE.value)
    box_world.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                path = cal(start, end, obstacles, show_details=True)
                box_world.draw_cell_line(path[:-1], box_world.COLOR.DARK_GRAY.value, box_world.COLOR.DARK_GREEN.value)
                box_world.update()