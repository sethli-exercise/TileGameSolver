import sys
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


class MapOfMoves:
    def __init__(self):
        self.states = {}

    def setMoves(self, key: str, moves: Moves):
        self.states[key] = moves

    def getMoves(self, key: str):
        return self.states.get(key)

    def toStr(self) -> str:
        str = ""
        for key,val in self.states.items():
            str += key + ": " + val.toStr() + "\n"
        return str

    def getLen(self) -> int:
        return len(self.states)

    def keyExists(self, key: str) -> bool:
        return key in self.states

class Solver:
    END_STATE = "111,111,111,"

    def __init__(self, board: Board):
        self.boardInstance = board
        # visitedStates will be used by the object to keep track of how it got to what board state
        self.visitedStates = None


        #Map<String, Moves> visitedStates = new HashMap<>();


    def printStates(self):
        print(self.visitedStates.toStr())
        print("{} states found".format(self.visitedStates.getLen()))

    def printSolution(self):
        endState = self.visitedStates.getMoves(Solver.END_STATE)
        if endState is not None:
            print(endState.toStr())
        else:
            print("no solution found")

    # will solve the board by modeling the problem as a graph problem
    # at each point in the graph it can make 4 choices (move up, down, left, right)
    # if it makes a choice that results in a state it has already seen it will stop and reassess
    def solveBoard(self) -> None:
        self.visitedStates = MapOfMoves()
        self.depthLimit = sys.maxsize

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
        seenState = self.visitedStates.keyExists(strState)

        ################################################################################
        # unoptimized solution without memoization
        # if seenState and self.visitedStates.getMoves(strState).moveNum > moves.moveNum:
        #     self.visitedStates.setMoves(strState, moves)
        # if not seenState:
        #     self.visitedStates.setMoves(strState, moves)
        # if moves.moveNum > 8:
        #     return
        ################################################################################

        if seenState and self.visitedStates.getMoves(strState).moveNum > moves.moveNum:
            self.visitedStates.setMoves(strState, moves)
        elif not seenState:
            self.visitedStates.setMoves(strState, moves)
        else: # I have been in this state before with less moves no reason to continue
            return
        # a solution has been found
        if strState == Solver.END_STATE:
            self.depthLimit = moves.moveNum
            return
        if moves.moveNum >= self.depthLimit:
            return

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