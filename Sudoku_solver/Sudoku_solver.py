import time
# Optional: install colorama with `pip install colorama` for colored output
try:
    from colorama import init, Fore, Style
    init(autoreset=True)  # Automatically reset color after each print
except ImportError:
    Fore = Style = None  # Fallback if colorama isn't installed


def find_empty_square(puzzle):
    """
    Find an empty square in the Sudoku puzzle.-> rep with " "
    Returns a tuple (row, col) of the first empty square found, or (None, None) if no empty squares exist.
    """
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == " ":  # Assuming " " represents an empty square
                return (r, c)
    return (None, None)  # (None, None) if no empty square is found

def is_valid(puzzle, guess, row, col):
    """
    Check if a guess is valid in the Sudoku puzzle.
    Returns True if the guess is valid else False.
    A guess is valid if it does not violate Sudoku rules:
    - The number is not already in the same row, column, or 3x3 subgrid.
    """
    guess = str(guess)
    # Check row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Check column
    col_vals = [puzzle[r][col] for r in range(9)]
    if guess in col_vals:
        return False

    # Check 3x3 subgrid
    # find where row starts and column starts
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def print_board(puzzle):
    print()
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(Fore.CYAN + "-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(Fore.CYAN + "|", end=" ")

            val = puzzle[i][j]
            if val == " ":
                print(Fore.LIGHTBLACK_EX + ".", end=" ")
            else:
                print(Fore.YELLOW + val, end=" ")
        print()
    print()

def get_user_board():
    print(Fore.CYAN + "\n📋 Paste your full Sudoku board (one row at a time).")
    print(Fore.CYAN + "→ Use digits 1–9 for known values.")
    print(Fore.CYAN + "→ Use " + Fore.RED + "dot (.) only" + Fore.CYAN + " for empty cells.")
    print(Fore.CYAN + "→ Each row must be exactly 9 characters.\n")

    board = []

    while len(board) < 9:
        line = input(Fore.GREEN + f"Row {len(board)+1}: ").strip()

        # Validate input
        if len(line) != 9:
            print(Fore.RED + "❌ Row must be exactly 9 characters.")
            continue
        if not all(c in "123456789." for c in line):
            print(Fore.RED + "❌ Invalid characters. Use only digits 1–9 or dots (.) for blanks.")
            continue

        # Convert to board format
        row = [c if c != "." else " " for c in line]
        board.append(row)

    print(Fore.GREEN + "\n✅ Sudoku input complete!\n")
    return board

def solve_sodoku(puzzle):
    """
    Solve a Sudoku puzzle using backtracking algorithm.
    Puzzle is a list of lists, where each inner list represents a row in the Sudoku grid.
    Returns a solved Sudoku grid by mutating the list  or None if no solution exists.
    """

    # choose some empty square to make a quess
    row, col = find_empty_square(puzzle)

    if (row, col) == (None, None):  # If no empty square is found, the puzzle is solved
        return True

    # Try numbers 1-9 in the empty square
    for guess in range(1, 10):  # range(1, 10) represents numbers 1 to 9
        # Check if the guess is valid
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = str(guess)
            # Recursively try to solve the rest of the puzzle
            if solve_sodoku(puzzle):
                return True

            # If the guess didn't lead to a solution, reset the square and try the next number
            puzzle[row][col] = " "
    return False  # If no valid guess leads to a solution, return False. ie puzzle unsolvable


if __name__ == "__main__":
    print(Fore.MAGENTA + Style.BRIGHT + "\n🎯 WELCOME TO THE AKIN SUDOKU SOLVER 9000 🎯\n")
    time.sleep(1)

    board = get_user_board()
    print(Fore.BLUE + "🧩 Here's your Sudoku board:\n")
    print_board(board)
    time.sleep(1)

    print(Fore.YELLOW + "⏳ Solving your puzzle...\n")
    time.sleep(2)

    if solve_sodoku(board):
        print(Fore.GREEN + Style.BRIGHT + "🎉 Sudoku Solved Successfully!\n")
        print_board(board)
    else:
        print(Fore.RED + Style.BRIGHT + "❗ Sorry, no solution exists for this puzzle.\n")