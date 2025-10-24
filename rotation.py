# Rotate grid state on the bit level


def rol(n, d):  
    return ((n << d) % (1 << 32)) | (n >> (32 - d))


def S3(x):
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
    

if __name__ == "__main__":
    a = 1010548
    print(bin(a))
    b = a
    b = S3(b)
    b = S3(b)
    b = S3(b)
    print(bin(b))