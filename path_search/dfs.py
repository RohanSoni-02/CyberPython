import box_world
from queue import LifoQueue
import utility

#represents a node in the search tree
class Node:
    def __init__(self, cell, parent=None):
        self._cell = cell #a point in the grid
        self._parent = parent # predescessor or the cell from which the above cell was reached

    @property
    def cell(self):
        return self._cell

    @property
    def parent(self):
        return self._parent

#implements the DFS algorithm    
def cal(start, end, obstacles=[], show_details=False):
    if utility.cell_equal(start, end):
        return []

    if utility.is_adjacent(start, end):
        return [end]

    #DFS algorithm by creating a LIFOqueue or Stack
    queue = LifoQueue()

    #A dictionary mark to keep track of visited cells and their predecessors
    mark = {}

    queue.put(Node(start))

    while not queue.empty():
        node = queue.get()
        cell = node.cell
        parent = node.parent

        if utility.cal_cell_id(cell) in mark.keys():
            continue

        mark[utility.cal_cell_id(cell)] = parent

        if show_details:
            box_world.draw_cell(cell, box_world.COLOR.DARK_GREEN.value)
            box_world.update()

        if utility.cell_equal(cell, end):
            path = utility.cal_path(mark, utility.cal_cell_id(end))
            return path[1:] + [end]

        adjs = utility.adj(cell, mark, obstacles)
        for adj in adjs:
            queue.put(Node(adj, cell))

    return None