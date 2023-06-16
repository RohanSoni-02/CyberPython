import box_world
from searches import PriorityQueue
import utility

class Node:
    def __init__(self, cell, g, h):
        self._cell = cell
        self._g = g  #cost to reach this cell from the start cell 
        self._h = h  #estimated cost from this cell to the end cell
        self._f = g + h #total estimated cost of the path through the node 

    #getter methods for cell, f, and g
    @property
    def cell(self):
        return self._cell

    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    #calculate the Manhattan distance (sum of the absolute differences in the x and y coordinates) between two cells
    @staticmethod
    def cal_h(cell1, cell2):
        (x1, y1) = cell1
        (x2, y2) = cell2
        return abs(x1 - x2) + abs(y1 - y2)
    
#implements the A* algorithm
def cal(start, end, obstacles=[], show_details=False):
    if utility.cell_equal(start, end):
        return []

    if utility.is_adjacent(start, end):
        return [end]

    queue = PriorityQueue()
    start_node = Node(start, 0, Node.cal_h(start, end))
    queue.put(start_node, start_node.f)
    mark = {utility.cal_cell_id(start): None} #dictionary that keeps track of the cells that have been visited

    while not queue.empty():
        node = queue.get()

        adjs = utility.adj(node.cell, mark, obstacles)
        for adj in adjs:
            if utility.cal_cell_id(adj) in mark.keys():
                continue

            mark[utility.cal_cell_id(adj)] = node.cell

            adj_node = Node(adj, node.g + 1, Node.cal_h(adj, end))
            queue.put(adj_node, adj_node.f)

            if utility.cell_equal(adj, end):
                path = utility.cal_path(mark, utility.cal_cell_id(adj))
                return path[1:] + [end]

            if show_details:
                box_world.draw_cell(adj, box_world.COLOR.DARK_GREEN.value)
                box_world.update()

    return None