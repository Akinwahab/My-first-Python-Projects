
import random
import re
import time
#create a board for the game
class Board:
    def __init__(self, dimension_size, num_bombs):
        self.dimension_size = dimension_size
        self.num_bombs = num_bombs
        
        # lets create a board
        self.board = self.make_new_board()  
        self.assign_values_to_board()


        # initialize a set to keep track of uncovered locations
        # we'll save the locations as tuples (row, col)
        self.dug = set() 
        #intialize a set to flag locations
        self.flags = set()
 
    def assign_values_to_board(self):
        # iterate through the board and assign values to each square
        for r in range(self.dimension_size):
            for c in range(self.dimension_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
        
    def get_num_neighboring_bombs(self, row, col):
        # check all neighboring squares and count how many bombs are there
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dimension_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dimension_size, col + 2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def make_new_board(self):
        board= [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]
        #[
         #   [None, None, None],
        #  [None, None, None],
            # [None, None, None]
        #] here is how the board looks like

        # plant bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dimension_size ** 2 - 1)
            row = loc // self.dimension_size
            col = loc % self.dimension_size
            
            if board[row][col] == "*":
                # bomb already planted here
                continue
            board[row][col] = "*"
            bombs_planted += 1
        return board

    def dig(self, row, col):
        # dig at the location
        # return True if dug successfully, False if dug a bomb
        self.dug.add((row, col))
        if (row, col) in self.flags:
            return True

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True
        
        # dig recursively
        for r in range(max(0, row - 1), min(self.dimension_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dimension_size, col + 2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        
        return True
    def toggle_flag(self, row, col):
        if (row, col) in self.dug:
            return False  # can't flag a dug cell

        if (row, col) in self.flags:
            self.flags.remove((row, col))
        else:
            self.flags.add((row, col))
        return True

    def __str__(self):
        # create a string representation of the board
        visible_board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]
        
        for r in range(self.dimension_size):
            for c in range(self.dimension_size):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                elif (r, c) in self.flags:
                    visible_board[r][c] = "F"
                else:
                    visible_board[r][c] = "·"

        string_rep = ""

        # Column header
        string_rep += "    " + "   ".join(f"{i}" for i in range(self.dimension_size)) + "\n"
        string_rep += "   ┌" + "───┬" * (self.dimension_size - 1) + "───┐\n"

        for r in range(self.dimension_size):
            row_str = f"{r:>2} │ " + " │ ".join(visible_board[r]) + " │\n"
            string_rep += row_str
            if r < self.dimension_size - 1:
                string_rep += "   ├" + "───┼" * (self.dimension_size - 1) + "───┤\n"
            else:
                string_rep += "   └" + "───┴" * (self.dimension_size - 1) + "───┘\n"

        string_rep += "\nN.B:\n"
        string_rep += "* = Bomb   · = Hidden   F = Flagged   Numbers = Nearby Bombs\n"


        return string_rep
# play game
def play(dimension_size=10, num_bombs=10):
    while True:
        # Step 1: Create the board and plant bombs
        board = Board(dimension_size, num_bombs)

        # step2 : show user the board and ask where they want to dig
        # step3a: if they dig a bomb, show game over
        # step3b: if location is safe, dig recursively until each quare is at least near a bomb
        # step4: if all safe squares are dug, show victory
        safe = True
        print("\n🎮 Welcome to MINESWEEPER 🎮\n")
        print(f"Board Size: {dimension_size}x{dimension_size} | Bombs: {num_bombs}\n")
        start_time = time.time()

        while len(board.dug) < board.dimension_size ** 2 - board.num_bombs:
            print(board)
            user_input = input("📍 Enter command (e.g., d 3,4 to dig, f 3,4 to flag): ").strip().lower()

            try:
                match = re.match(r"([df])\s*(\d+),\s*(\d+)", user_input)
                if not match:
                    print("⚠️ Invalid format. Use: d 3,4 or f 3,4\n")
                    continue

                action, row, col = match.groups()
                row, col = int(row), int(col)

                if row < 0 or row >= board.dimension_size or col < 0 or col >= board.dimension_size:
                    print("🚫 Invalid location. Try again.\n")
                    continue

                if action == 'f':
                    success = board.toggle_flag(row, col)
                    if not success:
                        print("🚫 You can't flag a revealed cell.\n")
                    continue  # skip digging
            except:
                print("⚠️ Invalid input format. Please enter as row,col (e.g., 3,4)\n")
                continue

            safe = board.dig(row, col)
            if not safe:
                print("\n💥 BOOM! You hit a bomb. Game Over.\n")
                break

        if safe:
            print("\n🎉 Congratulations! You cleared the board.\n")

        # reveal the full board after game ends
        board.dug = {(r, c) for r in range(board.dimension_size) for c in range(board.dimension_size)}
        print("🧩 Final Board:")
        print(board)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"⏱️ Time taken: {elapsed_time:.2f} seconds\n")
        # Ask to play again
        again = input("\n🔁 Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thanks for playing. Goodbye!\n")
            break

if __name__ == "__main__":
    play()