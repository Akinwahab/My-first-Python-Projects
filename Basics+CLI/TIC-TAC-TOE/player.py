import random
import math
from typing import Optional


class Player :
    def __init__(self, letter):
        #letter is X or O
        self.letter = letter

    # we want all players to get their move given a game
    def get_move(self, game) -> Optional[int]: 
        pass

class Random_Computer_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        # Get a random valid move
        square = random.choice(game.available_moves())
        return square

class Human_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        valid_square = False
        val = 0
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # we try to cast it to an integer, if invalid we say it's invalid
            # if that spot is not available , we say it's invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if we get here, the square is valid
            except ValueError:
                print("Invalid square. Try again.")
                
        return val            
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game) -> int:
        if len(game.available_moves()) == 9:
            # Pick randomly if it's the first move
            square = random.choice(game.available_moves())
        else:
            # Use minimax to find the best move
            result = self.minimax(game, self.letter)
            square = result["position"]
        return square
    def minimax(self, state, player):          
        max_player = self.letter  
        other_player = "O" if player == "X" else "X"

        # Base case: check for a previous winner
        if state.current_winner == other_player:
            return {
                "position": None,
                "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }

        elif not state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  
        else:
            best = {"position": None, "score": math.inf}

        for possible_move in state.available_moves():
            # Make the move
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Recursion

            # Undo move
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move

            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best