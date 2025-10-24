A program for counting the possible combinations that solve the Soma cube

![soma_indexing](soma_index.png "Indexing used in the program")

S3 permutation:  
```
x = (x & 0xfebaa0a1)
  | ((x & 0x00000400) << 2)
  | ((x & 0x00000100) << 3)
  | ((x & 0x00000010) << 6)
  | ((x & 0x00004002) << 8)
  | ((x & 0x00000800) << 13)
  | rol(x & 0x01000004, 16)
  | ((x & 0x00040000) >> 12)
  | ((x & 0x00001000) >> 8)
  | ((x & 0x00400200) >> 6)
  | ((x & 0x00000040) >> 4)
  | ((x & 0x00010008) >> 2);
```

y rotation :
```
0 > 6 > 8 > 2
1 > 3 > 7 > 5
9 > 15 > 17 > 11
10 > 12 > 16 > 14
18 > 24 > 26 > 20
19 > 21 > 25 > 23
-----------------
x = (x & 0xf8402010)
  | ((x & 0x01088442) << 2)
  | ((x & 0x00201008) << 4)
  | ((x & 0x00040201) << 6)
  | ((x & 0x04020100) >> 6)
  | ((x & 0x00804020) >> 4)
  | ((x & 0x02110884) >> 2);
```

Link to [code generator for a bitwise permutation](https://programming.sirrida.de/calcperm.php)  
Link to [bitwise rotation in Python](https://www.falatic.com/index.php/108/python-and-bitwise-rotation)


