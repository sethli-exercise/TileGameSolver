from tile import Tile

class Board:
    def __init__(self, boardHeight:int, boardWidth:int, startingPos:list):
        self.boardHeight = boardHeight
        self.boardWidth = boardWidth

        # first elem is the player's x coordinate
        # second elem is the player's y coordinate
        self.playerPos = startingPos

        # create a board of the given size starting with all black tiles (False)
        self.board = []
            # [[None] * self.boardHeight] * self.boardWidth
        for i in range(boardWidth):
            self.board.append([])
            for j in range(boardHeight):
                self.board[i].append(Tile())
                #print(i,j)
        # self.changeAdjacentTiles()
        #self.board[0][0].switchState()
        #self.board[1][0].switchState()
        self.board[1][1].switchState()
        #self.board[1][2].switchState()

    def switchTileRight(self):
        if self.playerPos[0] + 1 < self.boardWidth:
            self.board[self.playerPos[0] + 1][self.playerPos[1]].switchState()

    def switchTileUp(self):
        if self.playerPos[1] + 1 < self.boardHeight:
            self.board[self.playerPos[0]][self.playerPos[1] + 1].switchState()

    def switchTileLeft(self):
        if self.playerPos[0] - 1 > -1:
            self.board[self.playerPos[0] - 1][self.playerPos[1]].switchState()

    def switchTileDown(self):
        if self.playerPos[1] - 1 > -1:
            self.board[self.playerPos[0]][self.playerPos[1] - 1].switchState()

    # switches the state of the tiles orthogonally adjacent to the player
    def changeAdjacentTiles(self):
        self.board[self.playerPos[0]][self.playerPos[1]].switchState()

        self.switchTileRight()
        self.switchTileUp()
        self.switchTileLeft()
        self.switchTileDown()


    def allWhite(self) -> bool:
        for row in self.board:
            for tile in row:
                if not tile.state:
                    return False

        return True

    # moves the player one tile up and changes the state of the board accordingly
    def moveUp(self):
        # Check if the player can move up
        if self.playerPos[1] < self.boardHeight - 1:
            self.playerPos[1] += 1
            self.changeAdjacentTiles()
        return self

    # moves the player one tile down and changes the state of the board accordingly
    def moveDown(self):
        # Check if the player can move down
        if self.playerPos[1] > 0:
            self.playerPos[1] -= 1
            self.changeAdjacentTiles()
        return self

    # moves the player one tile left and changes the state of the board accordingly
    def moveLeft(self):
        # Check if the player can move left
        if self.playerPos[0] > 0:
            self.playerPos[0] -= 1
            self.changeAdjacentTiles()
        return self

    # moves the player one tile right and changes the state of the board accordingly
    def moveRight(self):
        # Check if the player can move right
        if self.playerPos[0] < self.boardWidth - 1:
            self.playerPos[0] += 1
            self.changeAdjacentTiles()
        return self

    def toStr(self) -> str:
        str = ""
        for j in range(self.boardHeight - 1, -1, -1):
            for i in range(self.boardWidth):
               if self.board[i][j].state:
                   str += "1"
               else:
                   str += "0"
            str += ","
        return str

        # # create a board of the given size starting with all black tiles (False)
        # self.board = [[None] * self.boardHeight] * self.boardWidth
        # for i in range(boardWidth):
        #     for j in range(boardHeight):
        #         self.board[i][j] = Tile()