from soma import *

def fits(grid, pos):
    if (grid & pos) == 0:
        return True
    return False

def assemble(grid, pieces_left):
    p = pieces_left[-1]
    for pos in all_positions[p]:
        if fits(grid, pos):
            if len(pieces_left) == 1:
                return True
            else:
                if assemble(grid + pos, pieces_left[:-1]):
                    return True
    return False

print("Soma cube solution found :", assemble(0, ["l", "L", "S", "T", "Na", "Nb", "W"]))