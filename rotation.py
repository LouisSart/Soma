# Rotate grid state on the bit level


def rol(n, d):
    # Circular shift to the left by d places
    return ((n << d) % (1 << 32)) | (n >> (32 - d))


def UBR3(x):
  # Rotation of a 120° angle around an axis
  # that passes through cubelets 0 and 26

  return ((x & 0xfebaa0a1)) \
  | ((x & 0x00000400) << 2) \
  | ((x & 0x00000100) << 3) \
  | ((x & 0x00000010) << 6) \
  | ((x & 0x00004002) << 8) \
  | ((x & 0x00000800) << 13) \
  | rol(x & 0x01000004, 16) \
  | ((x & 0x00040000) >> 12) \
  | ((x & 0x00001000) >> 8) \
  | ((x & 0x00400200) >> 6) \
  | ((x & 0x00000040) >> 4) \
  | ((x & 0x00010008) >> 2)

def y(x):
    # 90° rotation around a vertical
    # axis that passes through the center of the cube
    return (x & 0xf8402010) \
  | ((x & 0x01088442) << 2) \
  | ((x & 0x00201008) << 4) \
  | ((x & 0x00040201) << 6) \
  | ((x & 0x04020100) >> 6) \
  | ((x & 0x00804020) >> 4) \
  | ((x & 0x02110884) >> 2)

def S2(x):
    # 180° rotation around an axis that passes through
    # cubelets 10, 13 and 16
    return (x & 0xf8012400) \
  | ((x & 0x00009200) << 2) \
  | ((x & 0x04900000) >> 20) \
  | ((x & 0x02480000) >> 18) \
  | rol(x & 0x01240124, 16) \
  | ((x & 0x00000092) << 18) \
  | ((x & 0x00000049) << 20) \
  | ((x & 0x00024800) >> 2)


def gen_all_rotations(x):
    ret = set()
    a = x
    for _ in range(3):
        a = UBR3(a)
        for _ in range(2):
            a = S2(a)
            for _ in range(4):
                a = y(a)
                ret.add(a)
    return ret

if __name__ == "__main__":
    a = 1401880478
    assert(len(bin(a)) - 2 < 32)

    b = a
    for _ in range(3):
        b = UBR3(b)
    assert(b == a)

    for _ in range(4):
        b = y(b)
    assert(b == a)

    for _ in range(2):
        b = S2(b)
    assert(b == a)

    s = gen_all_rotations(a)
    assert(len(s) == 24)