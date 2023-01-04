class Board(object):
    def __init__(self, values = []) -> None:
        self.values = values
        self.N = 9
        self.n = 3
    
    def enterBoard(self):
        i = 0
        print("\nEnter the numbers in each row without any gap and 0 for spaces\n")
        while (i < self.N):
            row = input("Row " + str(i) + ": ")
            if len(row) != self.N:
                print("Invalid Row Length, try again")
            else:
                try:
                    self.values.append([int(x) for x in row])
                    i += 1
                except ValueError:
                    print("Invalid Value, try again")

    def isValid(self, pos, inp):
        fixedRow, fixedCol = pos[0], pos[1]

        # checking for duplicates in the particular row
        for col_num in range(self.N):
            if self.values[fixedRow][col_num] == inp:
                return False

        # checking for duplicates in the particular column
        for row_num in range(self.N):
            if self.values[row_num][fixedCol] == inp:
                return False
        
        # checking the sub Matrix (n x n)
        subMatrix_X = (fixedCol // self.n) * self.n
        subMatrix_Y = (fixedRow // self.n) * self.n

        for rowOffset in range(self.n):
            for colOffset in range(self.n):
                if self.values[subMatrix_Y + rowOffset][subMatrix_X + colOffset] == inp:
                    return False
        
        return True
    
    def solve(self) -> bool:
        for row_num in range(self.N):
            for col_num in range(self.N):
                if self.values[row_num][col_num] == 0:
                    for inp in range(1, 10):
                        if self.isValid((row_num, col_num), inp):
                            self.values[row_num][col_num] = inp
                            if (self.solve()):
                                return True
                            else:
                                self.values[row_num][col_num] = 0
                            
                    return False
        
        return True
    
    def __repr__(self) -> str:
        printString = ''
        for row_num in range(self.N):
            if row_num % self.n == 0:
                printString += '+' + "-"*23 + '+\n'

            for col_num in range(self.N):
                if col_num % self.n == 0:
                    printString += "| " 
                if col_num == 8:
                    printString += str(self.values[row_num][col_num]) + " |\n"
                else:
                    printString += str(self.values[row_num][col_num]) + " "
        printString+= '+' + "-"*23 + '+\n'
        return printString

def main():
    try:
        myBoard = Board()
        if myBoard.values == []:
            myBoard.enterBoard()
        print("\n Given Board: \n")
        print(myBoard)
        print("\n" + "*"*30)
        if myBoard.solve():
            print("\n Found a solution : \n")
            print(myBoard)
            print()
        else:
            print("The board is not solvable")
    
    except KeyboardInterrupt:
        print("\n\n------Exiting the Sudoku Solver------\n")
        exit()

main()