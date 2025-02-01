from copy import deepcopy

from board import Board

class Moves:
    def __init__(self, moveNum: int=0, moveList: list=[]):
        self.moveNum = moveNum
        self.moveList = moveList

    def addMove(self, move: str) -> list:
        ml = deepcopy(self.moveList)
        ml.append(move)
        return ml

    def toStr(self) -> str:
        return "{}: {}".format(self.moveNum,self.moveList)

class Solver:
    END_STATE = "111,111,111,"

    def __init__(self, board: Board):
        self.boardInstance = board
        # visitedStates will be used by the object to keep track of how it got to what board state
        self.visitedStates = None

    def printStates(self):
        for key,val in self.visitedStates.items():
            print(key, ": ", val.toStr())

    def printSolution(self):
        endState = self.visitedStates.get(Solver.END_STATE)
        if endState is not None:
            print(endState.toStr())
        else:
            print("no solution found")

    # will solve the board by modeling the problem as a graph problem
    # at each point in the graph it can make 4 choices (move up, down, left, right)
    # if it makes a choice that results in a state it has already seen it will stop and reassess
    def solveBoard(self) -> None:
        self.visitedStates = {}

        # init the prev states with the initial state
        # board -> [number of steps, [list of steps]]
        # self.visitedStates[self.board] = [0, []]

        self.solveBoardRec(self.boardInstance, Moves(0,[]))

        # return self.visitedStates[Solver.END_STATE].moveList
        # return self.visitedStates

        # return "could not find solution"

    def solveBoardRec(self, currBoard: Board, moves: Moves):

        strState = currBoard.toStr()
        # board states are represented as strings and this is how it is compared
        seenState = strState in self.visitedStates

        if seenState and self.visitedStates[strState].moveNum > moves.moveNum:
            self.visitedStates[strState] = moves
        elif not seenState:
            self.visitedStates[strState] = moves
        else: # I have been in this state before with less moves no reason to continue
            return

        # a solution has been found
        if strState == Solver.END_STATE:

            return

        # currBoardCpy = deepcopy(currBoard)

        # go up
        self.solveBoardRec(
            deepcopy(currBoard).moveUp(),
            Moves(
                moves.moveNum + 1,
                moves.addMove("u")
            )
        )

        # go down
        self.solveBoardRec(
            deepcopy(currBoard).moveDown(),
            Moves(
                moves.moveNum + 1,
                moves.addMove("d")
            )
        )

        # go right
        self.solveBoardRec(
            deepcopy(currBoard).moveRight(),
            Moves(
                moves.moveNum + 1,
                moves.addMove("r")
            )
        )

        # go left
        self.solveBoardRec(
            deepcopy(currBoard).moveLeft(),
            Moves(
                moves.moveNum + 1,
                moves.addMove("l")
            )
        )

        return