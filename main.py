from solver import Solver
from board import Board
import datetime
# import solver

def main():
    b = Board(3,3,[1,1])
    s = Solver(b)
    print("Solving, be patient...")
    startTime = datetime.datetime.now()
    print(startTime.time())
    s.solveBoard()
    s.printStates()
    # print(s.solveBoard())
    s.printSolution()
    endTime = datetime.datetime.now()
    diff = endTime - startTime
    print(endTime.time())
    print(diff)

main()
