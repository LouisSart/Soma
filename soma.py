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
        ind = 3 * (3 * x + y) + z
        assert(ind < 27)
        ret += 2 ** ind
    return ret

def gen_canonicals(piece):
    dup_tracker = set()
    ret = []
    for xrot in range(4):
        for yrot in range(4):
            for zrot in range(4):
                print(xrot, yrot, zrot)
                ind = piece_to_int(piece)
            # if ind not in dup_tracker:
            #     dup_tracker.add(ind)
                ret.append(np.copy(piece))
                rotate(piece, 2)
                make_canonical(piece)
            rotate(piece, 1)
            make_canonical(piece)
        rotate(piece, 0)
        make_canonical(piece)
    return ret

# def make_all_positions(piece):
#     # Generate all integers corresponding to every legal position
#     # of a piece in the grid
#     ret = set()

#     for cano in gen_canonicals(piece):
#         for dx in range(3):
#             p0 = np.copy(piece)
#             for dy in range(3):
#                 p1 = np.copy(p0)
#                 for dz in range(3):
#                     p2 = np.copy(p1)
#                     translate(p2, 1, dz)
#                     if is_inside_cube(p2):
#                         ret.add(p2)
#                 translate(p1, 1, 1)
#             translate(p0, 0, 1)

if __name__ == "__main__":
    gen_canonicals(l)
    # for p in gen_canonicals(l):
    #     print(piece_to_int(p))
