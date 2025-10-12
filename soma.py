from piece import *

# The space for the Soma cube is a 3x3x3
# 3D grid. An (i, j, k) position is occupied 
# if a cubie is located at (i, j, k). A given 
# piece arrangement is then stored as a bit 
# array of size 3x3x3 = 27

def piece_to_int(piece):
    ret = 0
    for cube in piece:
        x, y, z = cube
        ind = 3 * (3 * z + y) + x
        assert(ind < 27)
        ret += 2 ** ind
    return int(ret)

def gen_canonicals(piece):
    dup_tracker = set()
    ret = []
    for xrot in range(4):
        for yrot in range(4):
            for zrot in range(4):
                assert(is_canonical(piece))
                ind = piece_to_int(piece)
                if ind not in dup_tracker:
                    ret.append(np.copy(piece))
                    dup_tracker.add(ind)
                rotate(piece, 2)
                make_canonical(piece)
            rotate(piece, 1)
            make_canonical(piece)
        rotate(piece, 0)
        make_canonical(piece)
    return ret

def make_all_positions(piece):
    # Generate all integers corresponding to every legal position
    # of a piece in the grid
    assert(is_canonical(piece))
    ret = list()
    dup_tracker = set()

    for cano in gen_canonicals(piece):
        c0 = np.copy(cano)
        for dx in range(3):
            c1 = np.copy(c0)
            for dy in range(3):
                c2 = np.copy(c1)
                for dz in range(3):
                    if is_inside_cube(c2):
                        ind = piece_to_int(c2)
                        if ind not in dup_tracker:
                            ret.append(np.copy(c2))
                            dup_tracker.add(ind)
                    translate(c2, 2, 1)
                translate(c1, 1, 1)
            translate(c0, 0, 1)
    return ret

all_positions = {name : list(piece_to_int(p) for p in make_all_positions(piece)) \
                 for name, piece in pieces.items()}

if __name__ == "__main__":
    W_cano = gen_canonicals(W)
    l_cano = gen_canonicals(l)
    S_cano = gen_canonicals(S)
    L_cano = gen_canonicals(L)
    T_cano = gen_canonicals(T)
    Na_cano = gen_canonicals(Na)
    Nb_cano = gen_canonicals(Nb)
    assert(len(Na_cano) == len(Nb_cano) == 12)
    assert(len(T_cano) == 12)
    assert(len(l_cano) == 12)
    assert(len(L_cano) == 24)
    assert(len(S_cano) == 12)

    W_pos = make_all_positions(W)
    S_pos = make_all_positions(S)
    l_pos = make_all_positions(l)
    Na_pos = make_all_positions(Na)
    assert(len(W_pos) == 64)
    assert(len(S_pos) == len(S_cano) * 6)
    assert(len(l_pos) == len(l_cano) * 12)

    assert(len(all_positions["W"]) == len(W_pos))
    assert(len(all_positions["S"]) == len(S_pos))
    assert(len(all_positions["l"]) == len(l_pos))
    assert(len(all_positions["Na"]) == len(Na_pos))