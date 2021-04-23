import random
import math


# we have two player game

# player class is the base lass for the other two classes
class Player:
    def __init__(self,letter):
        self.letter = letter        #letter can be x or o

    def get_move(self,game):        #we want all player to get their next move given a game
        pass


# computer player
class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square


# human player
class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8):')
            # we are going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, then we say its invalid
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True     # if these are successful, then yay!!
            except ValueError:
                print('Invalid square. Try again.')

        return val


# this is the genius class where computer never loses, we may have a tie but the he never loses
# for this we will have minmax algorithm where computer will maximize his chance of wining and minimize chance of user wining
# for this we will have to check every possible outcome at a given state
# utility function = 1 *(no. of squares left after making + 1) if X win
# utility function = -1 *(no. of squares left after making + 1) if O win
# utility function = 0 * 1 (if no one wins i.e tie)


# genius computer who never loses
class GeniusComputerPlayer(Player):

    def __init__(self,letter):
        super().__init__(letter)


    def get_move(self,game):
        if len(game.available_moves())==9:
            square = random.choice(game.available_moves())      #randomly choses one

        else:

            #get the square on the basis of minimax algorithm
            square = self.minimax(game,self.letter)['position']

        return square


    def minimax(self,state,player):
        max_player = self.letter    #yourself
        other_player = 'O' if player=='X' else 'X'

        #base case
        #check if the previous move is winner
        if state.current_winner == other_player:
            # we should return its position and score because we need to keep track of score and compare them for optimal solution

            return {'position': None, 'score': 1*(state.empty_squares() + 1) if other_player==max_player
                    else -1*(state.empty_squares() + 1)}

        elif not state.empty_squares(): # no empty squares
            return {'position': None,'score' : 0}


        if player==max_player:
            best = {'position': None,'score' : -math.inf}   #each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}    #each score should minimize

        for possible_move in state.available_moves():

            # step 1: make a move, try that spot
            state.make_move(possible_move,player)

            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state,other_player)   # now, we alternate players


            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move       # otherwise this will get messed up

            # step 4: update the dictionary if necessary
            if player == max_player:        #maximize max_player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:                           #minimize other_player
                if sim_score['score'] < best['score']:
                    best= sim_score

        return best

