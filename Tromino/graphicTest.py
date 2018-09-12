from Tromino import GraphicTrominoSolver

n = 5
tileX = 20
tileY = 20
imageSize = 512
gSolver = GraphicTrominoSolver()
img = gSolver.createSolutionImage(n, tileX, tileY, imageSize)
img.save("tromino.png")