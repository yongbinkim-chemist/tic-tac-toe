import time
from __player import HumanPlayer, Lv1CPU, Lv2CPU, Lv3CPU

class TicTacToe:

    def __init__(self,describe=True):
        self.board = [' ' for _ in range(9)]
        if describe:
            self.manual()

    def available_place(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def print_board(self):
        for i in range(3):
            print('| ' + ' | '.join(self.board[3*i:3*i+3]) + ' |')

    def winner(self,stone):
        for i in range(3):
            # check row
            if self.board[i*3:i*3+3].count(stone) == 3:
                return True
            # check column
            if [self.board[i+c*3] for c in range(3)].count(stone) == 3:
                return True
        # check diagonal
        if [self.board[0],self.board[4],self.board[8]].count(stone) == 3:
            return True
        # check off-diagonal
        if [self.board[2],self.board[4],self.board[6]].count(stone) == 3:
            return True
        return False

    @staticmethod
    def manual():
        print("#"*58)
        print("#\t\t\tTIC-TAC-TOE\t\t\t #")
        print("#"*58)
        board = [str(i) for i in range(9)]
        for i in range(3):
            print('\t\t'+' '*7+'| '+' | '.join(board[3*i:3*i+3])+' |')
        print("Tic-tac-toe is a game  for  two  players  who  take  turns")
        print("making the spaces in a three-by-three grid with  X  or  O.")
        print("The player who succeeds in placing three  of  their  marks")
        print("in a horizontal, vertical, or diagonal row is the  winner.")
        print("It is a solved game, with a forced draw assuming best play") 
        print("from both players.\n")

    @staticmethod
    def gameLevel():
        ValidLv = False
        Level = None
        diff = {1:"Easy",2:"Medium",3:"Hard"}
        while not ValidLv:
            x = input("Set the game difficulty. 1:Easy 2:Medium 3:Hard --> ")
            Level = int(x)
            try:
                if Level < 1 or Level > 3:
                    raise IndexError
                ValidLv = True
                print(f"{diff[Level]} mode has been selected.\n")
            except IndexError:
                print(f"difficulty {Level} is not available. Try (1-3)")
        return Level

    @staticmethod
    def gamePlay():
        ValidIdx = False
        pick = None
        player = {1:"Human",2:"CPU"}
        while not ValidIdx:
            x = input("Who would you like to play first? 1:Human 2:CPU --> ")
            pick = int(x)
            try:
                if pick < 1 or pick > 2:
                    raise IndexError
                ValidIdx = True
                print(f"{player[pick]} will play the first.\n")
            except IndexError:
                print(f"{pick} is not valid player. Try 1 or 2")
        return pick

def play(game,player1,player2,display=True):

    turn = 0
    winner = False
    while game.available_place():
        if turn % 2 == 0:
            move = player1.getMove(game)
            name = player1.name
            stone = player1.stone
        else:
            move = player2.getMove(game)
            name = player2.name
            stone = player2.stone
        print(f"{name} places {stone} at position {move}.")
        game.board[move] = stone
        if display:
            game.print_board()
        if game.winner(stone):
            print(f"{name} wins!!")
            winner = True
            break
        turn += 1
        time.sleep(0.5)

    if not winner:
        print("It is a tie!")

if __name__ == "__main__":

    game = TicTacToe()
    Level = game.gameLevel()
    player = game.gamePlay()
    human = HumanPlayer(stone='O')
    if Level == 1:
        cpu = Lv1CPU(stone='X')
    elif Level == 2:
        cpu = Lv2CPU(stone='X')
    else:
        cpu = Lv3CPU(stone='X')
    
    if player == 1:
        play(game,human,cpu,display=True)
    else:
        play(game,cpu,human,display=True)
