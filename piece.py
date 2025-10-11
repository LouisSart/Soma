import numpy as np

# Defining each piece in an arbitrary orientation
# by storing the x, y, z coordinates of each cubelet
W =  np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0]])
S =  np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [2, 1, 0]])
L =  np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 2, 0]])
l =  np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
T =  np.array([[0, 0, 0], [0, 1, 0], [1, 1, 0], [0, 2, 0]])
Na = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 0, 1]])
Nb = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 0, 1]])

def is_canonical(piece):
    # A piece is canonically positioned if every
    # cubelet is in the (x>=0, y>=0, z>=0) portion of the 3D space
    # and at least one of its cubelets has coordinate x = 0
    # and at least one of its cubelets has coordinate y = 0
    # and at least one of its cubelets has coordinate z = 0

    all_positive = all(p >= 0 for p in piece.flat)
    one_zero = any(p == 0 for p in piece[:, 0]) and\
        any(p == 0 for p in piece[:, 1]) and\
        any(p == 0 for p in piece[:, 2])

    return one_zero and all_positive

# Rotation matrices
Mx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
My = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
Mz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

def rotate(piece, axis):
    assert(axis < 3)
    if axis == 0:
        M = Mx
    elif axis == 1:
        M = My
    else:
        M = Mz
    for i, cube in enumerate(piece):
        piece[i] = M @ cube

def translate(piece, axis, d):
    piece[:, axis] += d

def make_canonical(piece):
    dx = np.min(piece[:, 0])
    translate(piece, 0, -dx)
    dy = np.min(piece[:, 1])
    translate(piece, 1, -dy)
    dz = np.min(piece[:, 2])
    translate(piece, 2, -dz)

def is_inside_cube(piece):
    for cube in piece:
        for c in cube:
            if c < 0 or c > 27:
                return False
    return True

if __name__ == "__main__":

    u = [1, 0, 0]
    v = [0, 1, 0]
    w = [0, 0, 1]

    assert np.array_equal(u, Mx @ Mx @ Mx @ Mx @ u)
    assert np.array_equal(v, Mx @ Mx @ Mx @ Mx @ v)
    assert np.array_equal(w, Mx @ Mx @ Mx @ Mx @ w)

    assert np.array_equal(u, My @ My @ My @ My @ u)
    assert np.array_equal(v, My @ My @ My @ My @ v)
    assert np.array_equal(w, My @ My @ My @ My @ w)

    assert np.array_equal(u, Mz @ Mz @ Mz @ Mz @ u)
    assert np.array_equal(v, Mz @ Mz @ Mz @ Mz @ v)
    assert np.array_equal(w, Mz @ Mz @ Mz @ Mz @ w)

    bad =  np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [2, 0, 0]])
    assert not is_canonical(bad)
    assert is_canonical(W)
    assert is_canonical(S)
    assert is_canonical(L)
    assert is_canonical(l)
    assert is_canonical(T)
    assert is_canonical(Na)
    assert is_canonical(Nb)

    rotate(W, 0)
    assert not is_canonical(W)
    rotate(S, 0)
    rotate(S, 0)
    assert not is_canonical(S)
    rotate(Na, 1)
    assert not is_canonical(Na)
    rotate(L, 2)
    assert not is_canonical(L)
    rotate(l, 0)
    rotate(l, 0)
    assert not is_canonical(l)
    rotate(Nb, 0)
    assert not is_canonical(Nb)
    rotate(T, 2)
    assert not is_canonical(T)

    for p in (W, S, L, l, T, Na, Nb):
        for axis in range(3):
            rotate(p, axis)
            make_canonical(p)
            assert is_canonical(p)
