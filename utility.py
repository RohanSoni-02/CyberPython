import box_world

#checks if two cells are the same
def cell_equal(cell1: tuple[int, int], cell2: tuple[int, int]):
    if cell1 and not cell2:
        return False

    if not cell1 and cell2:
        return False

    if not cell1 and not cell2:
        return True

    (x1, y1) = cell1
    (x2, y2) = cell2

    return x1 == x2 and y1 == y2

#generate a unique identifier for a cell
def cal_cell_id(cell):
    (x, y) = cell
    return f"({x},{y})"

#check if two cells are adjacent on the grid
def is_adjacent(cell1, cell2):
    (x1, y1) = cell1
    (x2, y2) = cell2
    if x1 == x2 and abs(y1 - y2) == 1:
        return True
    if y1 == y2 and abs(x1 - x2) == 1:
        return True
    return False

#check if a cell is valid 
def valid_cell(mark={}, obstacles=[]):
    def valid(cell):
        (x, y) = cell
        if x < 0 or x >= box_world.WIDTH:
            return False
        if y < 0 or y >= box_world.HEIGHT:
            return False
        if cal_cell_id(cell) in mark.keys():
            return False
        for obstacle in obstacles:
            if cell_equal(cell, obstacle):
                return False
        return True

    return valid

#cell which is not yet visited, not an obstacle, and within the grid boundaries 
def adj(cell, mark={}, obstacles=[]):
    (x, y) = cell
    cells = [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y)
    ]
    return filter(valid_cell(mark, obstacles), cells)

#the path from the start to the destination cell by following the parent pointers
def cal_path(mark, cell_id):
    path = []
    cell = mark[cell_id]

    while cell:
        path.append(cell)
        parent_id = cal_cell_id(cell)
        if parent_id in mark.keys():
            cell = mark[parent_id]
        else:
            break

    path.reverse()
    return path

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

if __name__ == "__main__":
    assert cell_equal(None, None)
    assert not cell_equal(None, (1, 2))
    assert not cell_equal((1, 2), None)
    assert not cell_equal((1, 2), (3, 4))
    assert cell_equal((1, 2), (1, 2))

    print(cal_cell_id((1, 2)))

