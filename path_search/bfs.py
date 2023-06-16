import box_world
from queue import Queue
import utility

#implements the BFS algorithm
def cal(start, end, obstacles=[], show_details=False):
    if utility.cell_equal(start, end):
        return []

    if utility.is_adjacent(start, end):
        return [end]
    
    #BFS algorithm by creating a queue
    queue = Queue()
    queue.put(start)

    #A dictionary mark to keep track of visited cells and their predecessors 
    mark = {utility.cal_cell_id(start): None}

    while not queue.empty():
        cell = queue.get()

        adjs = utility.adj(cell, mark, obstacles)
        for adj in adjs:
            if utility.cal_cell_id(adj) in mark.keys():
                continue

            mark[utility.cal_cell_id(adj)] = cell
            queue.put(adj)

            if utility.cell_equal(adj, end):
                path = utility.cal_path(mark, utility.cal_cell_id(adj))
                return path[1:] + [end]

            if show_details:
                box_world.draw_cell(adj, box_world.COLOR.DARK_GREEN.value)
                box_world.update()

    return None

