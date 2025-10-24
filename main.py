from soma import *

def fits(grid, pos):
    if (grid & pos) == 0:
        return True
    return False

def assemble(grid, p_ind, pieces, previous_calls):
    p = pieces[p_ind]
    ret = 0
    if (grid, p_ind) not in previous_calls:
        for pos in all_positions[p]:
            if fits(grid, pos):
                if p_ind == len(pieces) - 1:
                    return 1
                else:
                    ret += assemble(grid + pos, p_ind + 1, pieces, previous_calls)
    else:
        previous_calls.add((grid, p_ind))
    return ret

print("Soma cube solution found :", assemble(0, 0, ["W", "Nb", "Na", "T", "S", "L", "l"], set()))