from soma import *

def fits(grid, pos):
    if (grid & pos) == 0:
        return True
    return False

def assemble(grid, p_ind, pieces):
    p = pieces[p_ind]
    for pos in all_positions[p]:
        if fits(grid, pos):
            if p_ind == len(pieces) - 1:
                return True
            else:
                if assemble(grid + pos, p_ind + 1, pieces):
                    return True
    return False

print("Soma cube solution found :", assemble(0, 0, ["W", "Nb", "Na", "T", "S", "L", "l"]))