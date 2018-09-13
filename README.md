# Tromino-tiling-problem-solver-in-Python
This is a solver of the tromino tiling problem, based on [Golomb's tromino theorem](https://en.wikipedia.org/wiki/Tromino#Rep-tiling_and_Golomb's_tromino_theorem), made in Python.

## Tromino.py

The `Tromino.py` file contains two classes, `TrominoSolver` and `GraphicTrominoSolver`, each of them providing the solution,
based of depth first recursion, for a tromino tiling problem. It uses the [Pillow](https://pillow.readthedocs.io/en/5.2.x/) library for image creation.

### TrominoSolver

An example case of the `TrominoSolver` class is listed below:
```
from Tromino import TrominoSolver

n = 3
tileX = 1
tileY = 2
solver = TrominoSolver()
solver.solveTromino(n, tileX, tileY)
```

The output will be:
```
0 0 0 0 0 0 0 0 
0 0 x 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


1 1 1 1 1 1 1 1 
1 2 x 1 1 2 2 1 
1 2 2 1 1 1 2 1 
1 1 1 1 3 1 1 1 
1 1 1 3 3 1 1 1 
1 2 1 1 1 1 2 1 
1 2 2 1 1 2 2 1 
1 1 1 1 1 1 1 1 
```

### GraphicTrominoSolver

For the `GraphicTrominoSolver` class, there is the following example:
```
from Tromino import GraphicTrominoSolver

n = 5
tileX = 20
tileY = 20
imageSize = 512
gSolver = GraphicTrominoSolver()
img = gSolver.createSolutionImage(n, tileX, tileY, imageSize)
img.save("tromino.png")
```

Output:

![alt-text](https://github.com/VasilisG/Tromino-tiling-problem-solver-in-Python/blob/master/tromino.png)
