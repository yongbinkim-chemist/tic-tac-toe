import random

class Player:
    def __init__(self, stone):
        self.stone = stone

class HumanPlayer(Player):
    ''' choose move manually '''
    def __init__(self,stone='O'):
        super().__init__(stone)
        self.name = 'Human'

    def getMove(self,game):
        isValid = False
        move = None
        while not isValid:
            x = input(f"{self.name} player's turn. Choose one of the following {game.available_place()}: ")
            move = int(x)
            try:
                if move < 0 or move > 8:
                    raise IndexError
                if move not in game.available_place():
                    raise ValueError
                isValid = True
            except IndexError:
                print(f"{x} is out of range. Try (0-9).")
            except ValueError:
                print(f"{x} if occupied. Try again.")
        return move

class Lv1CPU(Player):
    ''' choose move 100% random'''
    def __init__(self,stone='X'):
        super().__init__(stone)
        self.name = 'CPU'

    def getMove(self,game):
        move = random.choice(game.available_place())
        return move

def minimax(curr_state,player,opponent,turn,alpha,beta):
    '''
    Player wants to maximize its winning probability
                    minimize opponent's winning probability
    WANT TO FIND THE SOLUTION with LESS NUMBER of PLAYS
    MINIMAX WITH ALPHA-BETA PRUNING
    '''
    available_place = curr_state.available_place()
    
    if not available_place:
        return (0,True) # draw game
    if curr_state.winner(player):
        return (+1*(9-turn),True) # less plays = higher in cost
    if curr_state.winner(opponent):
        return (-1*(9-turn),True) # less plays = lower in cost

    if turn % 2 == 0: # Maximize
        MAX,POSITION = float('-inf'),None
        for move in available_place:
            curr_state.board[move] = player
            cost,_ = minimax(curr_state,player,opponent,turn+1,alpha,beta)
            curr_state.board[move] = ' '
            if cost > MAX:
                MAX = cost
                POSITION = move
            if cost > alpha:
                alpha = cost
            if cost >= beta: # do not need to check further
                return (MAX,POSITION)
        return (MAX,POSITION)
    else: # Minimize
        MIN,POSITION = float('inf'),None
        for move in available_place:
            curr_state.board[move] = opponent
            cost,_ = minimax(curr_state,player,opponent,turn+1,alpha,beta)
            curr_state.board[move] = ' '
            if cost < MIN:
                MIN = cost
                POSITION = move
            if cost < beta:
                beta = cost
            if cost <= alpha: # do not need to check further
                return (MIN,POSITION)
        return (MIN,POSITION)

class Lv2CPU(Player):
    ''' choose move 50% random / 50% minimax'''
    def __init__(self,stone='X'):
        super().__init__(stone)
        self.name = 'CPU'

    def getMove(self,game):
        if len(game.available_place()) == 9:
            # CPU plays the first
            move = random.choice(game.available_place())
        else:
            if random.choice([0,1]):
                player_stone = self.stone
                opponent_stone = 'O' if player_stone == 'X' else 'X'
                _,move = minimax(game,player_stone,opponent_stone,0,float('-inf'),float('inf'))
            else:
                move = random.choice(game.available_place())
        return move

class Lv3CPU(Player):
    ''' choose move 100% minimax'''
    def __init__(self,stone='X'):
        super().__init__(stone)
        self.name = 'CPU'

    def getMove(self,game):
        if len(game.available_place()) == 9:
            # CPU plays the first
            move = random.choice(game.available_place())
        else:
            player_stone = self.stone
            opponent_stone = 'O' if player_stone == 'X' else 'X'
            _,move = minimax(game,player_stone,opponent_stone,0,float('-inf'),float('inf'))
        return move
