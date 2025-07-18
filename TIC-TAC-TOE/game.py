from player import Human_Player, Random_Computer_Player, GeniusComputerPlayer
from colorama import init, Fore, Style
import time
import os

init(autoreset=True)  # Automatically resets styles

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        print("\n" + "-" * 13)
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            formatted_row = "| " + " | ".join([self._colorize(letter) for letter in row]) + " |"
            print(formatted_row)
            print("-" * 13)

    def _colorize(self, letter):
        if letter == "X":
            return Fore.RED + letter + Style.RESET_ALL
        elif letter == "O":
            return Fore.BLUE + letter + Style.RESET_ALL
        else:
            return " "

    @staticmethod
    def print_board_nums():
        print("\nPosition Guide:")
        print("-" * 13)
        for row in [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]:
            print("| " + " | ".join(row) + " |")
            print("-" * 13)

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        col = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diag1]):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"
    while game.empty_squares():
        player = x_player if letter == "X" else o_player

        if "Computer" in player.__class__.__name__:
            print(Fore.YELLOW + "Computer is thinking", end="")
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            print()

        square = player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"\n{Fore.GREEN}{letter} makes a move to square {square}")
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(Fore.MAGENTA + f"🏆 {letter} WINS THE GAME! 🏆\n")
                return letter

            letter = "O" if letter == "X" else "X"

    if print_game:
        print(Fore.CYAN + "🤝 It's a TIE!\n")
    return "tie"


def run_game(x_player, o_player):
    x_score, o_score, ties = 0, 0, 0

    while True:
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=True)

        if result == "X":
            x_score += 1
        elif result == "O":
            o_score += 1
        else:
            ties += 1

        print(Fore.YELLOW + "\n📊 SCOREBOARD:")
        print(Fore.RED + f"X - {x_score}  ", end="")
        print(Fore.BLUE + f"O - {o_score}  ", end="")
        print(Fore.CYAN + f"Ties - {ties}\n")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print(Fore.GREEN + "Thanks for playing! 👋")
            break
        os.system("cls" if os.name == "nt" else "clear")


def play_pvp():
    x_player = Human_Player("X")
    o_player = Human_Player("O")
    run_game(x_player, o_player)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.MAGENTA + """
████████╗██╗ ██████╗       ████████╗██╗ ██████╗      ████████╗ ██████╗ ██████╗ 
╚══██╔══╝██║██╔════╝       ╚══██╔══╝██║██╔═══██╗      ╚══██╔══╝██╔═══██╗██╔══██╗
   ██║   ██║██║     █████╗   ██║   ██║██║   ██║█████╗   ██║   ██║   ██║██████╔╝
   ██║   ██║██║     ╚════╝   ██║   ██║██║   ██║╚════╝   ██║   ██║   ██║██╔═══╝ 
   ██║   ██║╚██████╗        ██║   ██║╚██████╔╝        ██║   ╚██████╔╝██║     
   ╚═╝   ╚═╝ ╚═════╝        ╚═╝   ╚═╝ ╚═════╝         ╚═╝    ╚═════╝ ╚═╝     
    """)
    print(Fore.GREEN + "Welcome to the Ultimate Tic Tac Toe Challenge!\n")
    print("Choose a mode:")
    print("1 - Human vs Random Computer 🤖")
    print("2 - Human vs Human 👥")
    print("3 - Human vs Genius AI 🧠")

    mode = input("Enter 1, 2 or 3: ").strip()

    if mode == "1":
        x_player = Human_Player("X")
        o_player = Random_Computer_Player("O")
        run_game(x_player, o_player)
    elif mode == "2":
        play_pvp()
    elif mode == "3":
        x_player = Human_Player("X")
        o_player = GeniusComputerPlayer("O")
        run_game(x_player, o_player)
    else:
        print(Fore.RED + "Invalid input. Please restart and try again.")
        exit(1)