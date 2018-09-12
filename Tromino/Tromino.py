from PIL import Image, ImageDraw

class TrominoSolver:

    def getCenter(self, startX, endX, startY, endY):
        return ((startX + endX) // 2, (startY + endY) // 2)

    def isWithinBounds(self, tileX, tileY, startX, startY, endX, endY):
        return (startX <= tileX <= endX) and (startY <= tileY <= endY)

    def placeTile(self, tileMap, x, y, n):
        tileMap[x][y] = n

    def placeTiles(self, tileMap, x1, y1, x2, y2, x3, y3, n):
        self.placeTile(tileMap, x1, y1, n)
        self.placeTile(tileMap, x2, y2, n)
        self.placeTile(tileMap, x3, y3, n)

    def solve(self, n, tileMap, startX, endX, startY, endY, tileX, tileY):
        cX, cY = self.getCenter(startX, endX, startY, endY)

        firstX, firstY = cX, cY
        secondX, secondY = cX+1, cY
        thirdX, thirdY = cX, cY+1
        fourthX, fourthY = cX+1, cY+1

        if tileX <= cX:
            if tileY <= cY:
                self.placeTiles(tileMap, cX, cY+1, cX+1, cY+1, cX+1, cY, n)
                firstX, firstY = tileX, tileY
            else:
                self.placeTiles(tileMap, cX, cY, cX+1, cY, cX+1, cY+1, n)
                secondX, secondY = tileX, tileY
        else:
            if tileY <= cY:
                self.placeTiles(tileMap, cX, cY, cX, cY+1, cX+1, cY+1, n)
                thirdX, thirdY = tileX, tileY
            else:
                self.placeTiles(tileMap, cX, cY, cX+1, cY, cX, cY+1, n)
                fourthX, fourthY = tileX, tileY

        if n==1:
            return
        else:
            self.solve(n-1, tileMap, startX, cX, startY, cY, firstX, firstY)
            self.solve(n-1, tileMap, startX, cX, cY, endY, secondX, secondY)
            self.solve(n-1, tileMap, cX, endX, startY, cY, thirdX, thirdY)
            self.solve(n-1, tileMap, cX, endX, cY, endY, fourthX, fourthY)

    def solveTromino(self, n, tileX, tileY):
        size = 2**n
        if not self.isWithinBounds(tileX, tileY, 0, 0, size-1, size-1):
            print("Invalid tile coordinates...")
        else:
            tileMap = [['x' if i==tileX and j==tileY else '0' for j in range(size)] for i in range(size)]
            self.printMap(tileMap)
            self.solve(n, tileMap, 0, size-1, 0, size-1, tileX, tileY)
            self.printMap(tileMap)

    def printMap(self, tileMap):
        size = len(tileMap)
        print()
        for i in range(size):
            for j in range(size):
                print("%s" % tileMap[i][j], end=" ")
            print()
        print()

#####################################################################################################

class GraphicTrominoSolver:

    OUTLINE = (0,0,0)
    TILE_FILL = (255,0,0)
    FILL = (253,200,77)

    TILESIZE = 16

    def __init__(self):
        self.tileSize = self.TILESIZE
  
    def getCenter(self, startX, endX, startY, endY):
        return ((startX + endX) // 2, (startY + endY) // 2)

    def isWithinBounds(self, tileX, tileY, startX, startY, endX, endY):
        return (startX <= tileX <= endX) and (startY <= tileY <= endY)

    def gPos(self,x,y):
        return (x * self.tileSize, y * self.tileSize)

    def graphicSolve(self, n, startX, endX, startY, endY, tileX, tileY, img):
        draw = ImageDraw.Draw(img, "RGB")
        cX, cY = self.getCenter(startX, endX, startY, endY)

        firstX, firstY = cX, cY
        secondX, secondY = cX+1, cY
        thirdX, thirdY = cX, cY+1
        fourthX, fourthY = cX+1, cY+1

        if tileX <= cX:
            if tileY <= cY:
                draw.polygon([self.gPos(cX,cY+1), self.gPos(cX,cY+2), self.gPos(cX+2,cY+2), self.gPos(cX+2,cY), self.gPos(cX+1,cY), self.gPos(cX+1,cY+1)], outline=self.OUTLINE, fill=self.FILL)
                firstX, firstY = tileX, tileY
            else:
                draw.polygon([self.gPos(cX,cY), self.gPos(cX+2,cY), self.gPos(cX+2,cY+2), self.gPos(cX+1,cY+2), self.gPos(cX+1,cY+1), self.gPos(cX,cY+1)], outline=self.OUTLINE, fill=self.FILL)
                secondX, secondY = tileX, tileY
        else:
            if tileY <= cY:
                draw.polygon([self.gPos(cX,cY), self.gPos(cX+1,cY), self.gPos(cX+1,cY+1), self.gPos(cX+2,cY+1), self.gPos(cX+2,cY+2), self.gPos(cX,cY+2)], outline=self.OUTLINE, fill=self.FILL)
                thirdX, thirdY = tileX, tileY
            else:
                draw.polygon([self.gPos(cX,cY), self.gPos(cX+2,cY), self.gPos(cX+2,cY+1), self.gPos(cX+1,cY+1), self.gPos(cX+1,cY+2), self.gPos(cX,cY+2)], outline=self.OUTLINE, fill=self.FILL)
                fourthX, fourthY = tileX, tileY

        if n==1:
            return
        else:
            self.graphicSolve(n-1, startX, cX, startY, cY, firstX, firstY, img)
            self.graphicSolve(n-1, startX, cX, cY, endY, secondX, secondY, img)
            self.graphicSolve(n-1, cX, endX, startY, cY, thirdX, thirdY, img)
            self.graphicSolve(n-1, cX, endX, cY, endY, fourthX, fourthY, img)

    def createSolutionImage(self, n, tileX, tileY, imageSize):
        size = 2**n
        if not self.isWithinBounds(tileX, tileY, 0, 0, size-1, size-1):
            print("Invalid tile coordinates...")
        elif imageSize < 0 or not (imageSize % 2 == 0):
            print("Invalid image size parameter (must be greater than 0 and a power of 2).")
        else:
            tileSize = (imageSize+1) // size
            img = Image.new("RGB", (imageSize+1, imageSize+1))
            draw = ImageDraw.Draw(img)
            draw.rectangle([self.gPos(tileX, tileY), self.gPos(tileX+1, tileY+1)], fill=self.TILE_FILL)
            self.graphicSolve(n, 0, size-1, 0, size-1, tileX, tileY, img)
            return img