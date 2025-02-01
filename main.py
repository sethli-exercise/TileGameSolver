from solver import Solver
from board import Board
# import solver

def main():
    b = Board(3,3,[1,1])
    s = Solver(b)
    print("Solving, be patient...")
    s.solveBoard()
    s.printStates()
    # print(s.solveBoard())
    s.printSolution()

main()
