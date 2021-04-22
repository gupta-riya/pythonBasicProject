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