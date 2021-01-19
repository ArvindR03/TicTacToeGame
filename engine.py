class Board:

    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


    def checkSpace(self, coords):
        row, col = coords
        if 0 <= row <= 2 and 0 <= col <= 2:
            if self.board[row][col] == 0:
                return True
            else:
                return False
        else:
            return False


    def checkTurns(self):
        turns = 0
        for row in self.board:
            for item in row:
                if item != 0:
                    turns += 1
        return turns


    def noughtTurn(self, coords):
        if self.checkSpace(coords):
            row, col = coords
            self.board[row][col] = 'O'
        else:
            pass



    def crossTurn(self, coords):
        if self.checkSpace(coords):
            row, col = coords
            self.board[row][col] = 'X'
        else:
            pass


    def checkWin(self):
        ret = 0

        if self.checkTurns() == 9:
            ret = 'd'
        for index in range(3):
            if self.board[0][index] == self.board[1][index] and self.board[2][index] == self.board[1][index]:
                ret = self.board[0][index]
            elif self.board[index][0] == self.board[index][1] and self.board[index][2] == self.board[index][1]:
                ret = self.board[index][0]
        if self.board[0][0] == self.board[1][1] and self.board[2][2] == self.board[1][1]:
            ret = self.board[0][0]
        elif self.board[0][2] == self.board[1][1] and self.board[2][0] == self.board[1][1]:
            ret = self.board[1][1]

        return ret


    def printBoard(self):
        print('   0 1 2')
        print('   -----')
        print(f'0| {self.board[0][0]} {self.board[0][1]} {self.board[0][2]}')
        print(f'1| {self.board[1][0]} {self.board[1][1]} {self.board[1][2]}')
        print(f'2| {self.board[2][0]} {self.board[2][1]} {self.board[2][2]}')


def main():
    user1 = input('Player 1 - noughts or crosses? (n/c): ')
    if user1 == 'n':
        user2 = 'c'
    elif user1 == 'c':
        user2 = 'n'
    else:
        print('Incorrect input.')
        quit()
    print('---------------------------------------START--------------------------------')
    board = Board()
    board.printBoard()
    print('----------------------------------------------------------------------------')
    win = 0

    while win != 'X' and win != 'O':
        moveMade1 = False
        while not moveMade1:
            print('PLAYER 1\'s turn: ')
            userx = int(input('Enter the x coordinate (0 - 2): '))
            usery = int(input('Enter the y coordinate (0 - 2): '))
            user_input = (usery, userx)
            if board.checkSpace(user_input):
                if user1 == 'n':
                    board.noughtTurn(user_input)
                elif user1 == 'c':
                    board.crossTurn(user_input)
                moveMade1 = True
                board.printBoard()
                print('----------------------------------------------------------------------------')
            else:
                print('Incorrect coordinates, try again.')
        win = board.checkWin()
        if win != 0:
            break

        moveMade2 = False
        while not moveMade2:
            print('PLAYER 2\'s turn: ')
            userx = int(input('Enter the x coordinate (0 - 2): '))
            usery = int(input('Enter the y coordinate (0 - 2): '))
            user_input = (usery, userx)
            if board.checkSpace(user_input):
                if user2 == 'n':
                    board.noughtTurn(user_input)
                elif user2 == 'c':
                    board.crossTurn(user_input)
                moveMade2 = True
                board.printBoard()
                print('----------------------------------------------------------------------------')
            else:
                print('Incorrect coordinates, try again.')
        win = board.checkWin()
        if win != 0:
            break

    if win == 'd':
        print('It\'s a draw!')
    elif (win == 'X' and user1 == 'c') or (win == 'O' and user1 == 'n'):
        print('Player 1 won!')
    else:
        print('Player 2 won!')


if __name__ == '__main__':
    main()