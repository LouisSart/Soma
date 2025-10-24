A program for counting the possible combinations that solve the Soma cube

run with `python3 main.py`

![soma_indexing](soma_index.png "Indexing used in the program")

UBR3 permutation: Rotation of a 120° angle around an axis that passes through cubelets 0 and 26
```
2 > 18 > 6
24 > 8 > 11
1 > 9 > 3
22 > 16 > 14
21 > 7 > 11
19 > 15 > 5
10 > 12 > 4
23 > 25 > 17
```

y rotation : 90° rotation around a vertical axis that passes through the center of the cube
```
0 > 6 > 8 > 2
1 > 3 > 7 > 5
9 > 15 > 17 > 11
10 > 12 > 16 > 14
18 > 24 > 26 > 20
19 > 21 > 25 > 23
```

S2 rotation: 180° rotation around an axis that passes through cubelets 10, 13 and 16
```
3 <> 23
7 <> 25
5 <> 21
1 <> 19
22 <> 4
0 <> 20
2 <> 18
6 <> 26
8 <> 24
12 <> 14
9 <> 11
15 <> 17
```


Link to [code generator for a bitwise permutation](https://programming.sirrida.de/calcperm.php)  
Link to [bitwise rotation in Python](https://www.falatic.com/index.php/108/python-and-bitwise-rotation)


