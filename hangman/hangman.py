import random
import string
import time
from words import word as word_list

LIVES = 6  # Number of lives for the player
# ASCII stages of hangman drawing
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========""",
]


def get_valid_word():  # Selects a valid word from the word list
    """Selects a random word from the word list that does not contain hyphens or spaces."""
    selected_word = random.choice(word_list)
    while "-" in selected_word or " " in selected_word:
        selected_word = random.choice(word_list)
    return selected_word.upper()


def hangman_round():  # Plays a single round of Hangman
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = LIVES

    print("\n🎮 New Round! Try to guess the word!")
    time.sleep(1)

    while len(word_letters) > 0 and lives > 0:
        print(HANGMAN_PICS[6 - lives])

        word_display = [letter if letter in used_letters else "_" for letter in word]
        print("\n💡 Word: ", " ".join(word_display))
        print("🔤 Used letters:", " ".join(sorted(used_letters)))
        print(f"Lives: {'❤️ ' * lives + '🖤 ' * (6 - lives)} ({lives} left)\n")

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"✅ Naam! '{user_letter}' is in the word.\n")
            else:
                lives -= 1
                print(f"❌ Naah! '{user_letter}' is not in the word.\n")
            time.sleep(1.2)
        elif user_letter in used_letters:
            print("⚠️ You already used that letter. Try another.\n")
            time.sleep(1)
        else:
            print("🚫 Invalid input. Please enter a letter from A-Z.\n")
            time.sleep(1)

    print(HANGMAN_PICS[6 - lives])
    time.sleep(1)

    if lives == 0:
        print(f"💀 Game Over! The word was: {word}\n")
    else:
        print(f"🎉 Congratulations! You guessed the word: {word}\n")

    time.sleep(2)
    return lives > 0


def play_hangman():
    wins = 0
    losses = 0

    print("🧠 Welcome to Hangman!")
    time.sleep(1)
    print("Guess the word correctly before you run out of lives.\n")
    time.sleep(1)

    while True:
        result = hangman_round()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"📊 Score: ✅ Wins = {wins} | ❌ Losses = {losses}")
        time.sleep(1)

        play_again = input("🔁 Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("\n👋 Thanks for playing Hangman!")
            time.sleep(1)
            print(f"🏁 Final Score: ✅ {wins} wins | ❌ {losses} losses")
            break
        else:
            print("🔄 Starting new round...\n")
            time.sleep(1)


play_hangman()
