import time
import sys
import cowsay
from pyfiglet import Figlet
import random
import re
import json
from colorama import Fore, Style, Back

figlet = Figlet()
figlet_fonts = figlet.getFonts()


class Quiz:
    def __init__(self, filename, username):
        self.filename = filename
        self.questions = []
        self.score = 0
        self.total_questions = 10
        self.letters = ["A", "B", "C", "D", "E"]
        self.username = username
        self.subject = filename.replace(".json", "").capitalize()

    def load_questions(self):
        try:
            with open(self.filename, "r") as file:
                PQ = json.load(file)
                self.questions = PQ["questions"]
            random.shuffle(self.questions)
            self.questions = self.questions[: self.total_questions]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load questions: {e}")
            sys.exit()

    def show_question(self, question, index):
        print(f"\nQuestion {index + 1}: {question['question']}")
        for i, option in enumerate(question["options"]):
            print(f"{self.letters[i]}. {option}")

    def get_user_choice(self):
        valid_inputs = {letter: idx for idx, letter in enumerate(self.letters)}
        while True:
            choice = input("Enter your answer (A–E): ").strip().upper()
            if choice in valid_inputs:
                return valid_inputs[choice]
            else:
                print("❗ Invalid choice. Please enter A, B, C, D, or E.")

    def check_answer(self, choice_index, question):
        selected = question["options"][choice_index]
        correct = question["correct_answer"]
        if selected == correct:
            print("✅ Correct!")
            return True
        else:
            print(f"❌ Wrong. Correct answer is: {correct}")
            return False

    @staticmethod
    def save_score(name, subject, score):
        record = {"name": name, "subject": subject, "score": score}
        with open("score_log.json", "a") as file:
            file.write(json.dumps(record) + "\n")

    @staticmethod
    def show_user_history(name):
        try:
            with open("score_log.json", "r") as file:
                lines = file.readlines()
                history = []
                for line in lines:
                    try:
                        entry = json.loads(line)
                        if entry["name"] == name:
                            history.append(entry)
                    except json.JSONDecodeError:
                        continue
                if history:
                    print(f"\n📜 Previous Scores for {name}:")
                    for h in history:
                        print(f" - {h['subject']}: {h['score']}/10")
        except FileNotFoundError:
            return

    def run(self):
        self.load_questions()
        figlet.setFont(font="block")
        print(figlet.renderText("\n🎓 Starting the Quiz!\n"))
        time.sleep(1)
        start_time = time.time()
        for i, question in enumerate(self.questions):
            self.show_question(question, i)
            choice = self.get_user_choice()
            if self.check_answer(choice, question):
                self.score += 1
        end_time = time.time()
        duration = end_time - start_time
        print(f"⏱️ You completed the quiz in {duration:.2f} seconds.")
        print("*" * 30)
        print("-" * 40)
        print(
            Fore.YELLOW
            + f"🎯 Final Score: {self.score}/{self.total_questions}"
            + Style.RESET_ALL
        )
        print(f"📊 Percentage: {(self.score /self.total_questions) * 100:.2f}%")
        if self.score >= 9:
            msg = "🏆 Excellent!"
        elif self.score >= 6:
            msg = "👍 Good job!"
        else:
            msg = "📘 Keep practicing!. You can do better"
        print(Fore.BLUE + msg + Style.RESET_ALL)
        cowsay.dragon(f"Well done, {self.username}!")
        self.save_score(self.username, self.subject, self.score)


def main():
    print(Fore.CYAN + "Welcome!" + Style.RESET_ALL)
    time.sleep(0.3)
    print(Fore.GREEN + intro("Assalamu Aliakum") + Style.RESET_ALL)
    time.sleep(0.5)
    name = input("What's ur Full name? ").strip().title()
    parts = name.split()
    first = parts[0] if parts else "Friend"
    print(f"Welcome, {first}")
    print("\n")
    time.sleep(0.8)
    Age = input("How old are you? ").strip()
    try:
        birth_year = 2025 - int(age(Age))
        print(f"I got you, {first}. You were born in {birth_year}")
    except ValueError:
        print("Oops! Couldn't figure out your age.")
    time.sleep(0.5)
    print(Fore.MAGENTA + "YUP!, I  am very smart 🤗" + Style.RESET_ALL)
    print("\n")
    time.sleep(0.8)
    Nationality = input("What's ur Nationality? ").strip().title()
    print(f"Glad to know u are a , {Nationality}")
    print("\n")
    time.sleep(0.8)
    Buddy = buddy_check(input("Are you Akinwahab's buddy, yes/no ").strip().casefold())
    print("\n")
    about_you = {"Name": name, "Age": Age, "Nationality": Nationality, "Buddy": Buddy}
    time.sleep(0.8)
    for key, value in about_you.items():
        print(f"{key}: {value}")
    while True:
        Ready = input("\nReady to take the quiz? (yes/no): ").strip().casefold()
        Quiz.show_user_history(first)
        if Ready == "yes":
            subject_file = select_subject()
            countdown()
            quiz = Quiz(subject_file, first)
            quiz.run()
        else:
            print("\n👋 Thanks for playing! Stay curious 🌟")
            break
    print("©Akinwahab")


def intro(A):
    fonts = ["barbwire", "block", "contessa", "larry3d"]
    figlet.setFont(font=random.choice(fonts))
    return figlet.renderText(A)


def age(x):
    age = re.search(r"([0-9][0-9]?[0-9]?)", x)
    if not age:
        raise ValueError("Missing Age")
    else:
        return age.group(1)


def buddy_check(B):
    if B == "yes":
        print(
            Fore.WHITE + "💯💯💯, I trust you know he is very amazing" + Style.RESET_ALL
        )
        return "Akinwahab's Buddy"

    else:
        print(Fore.RED + "I am so sad 😭, Well no problems." + Style.RESET_ALL)
        return "Not a buddy"


def select_subject():
    subjects = {
        "1": "math.json",
        "2": "english.json",
        "3": "physics.json",
        "4": "chemistry.json",
        "5": "biology.json",
    }

    print("📚 Choose a subject to begin:\n")
    print("1. Mathematics")
    print("2. English")
    print("3. Physics")
    print("4. Chemistry")
    print("5. Biology\n")

    while True:
        choice = input("Select a subject (1–5): ").strip()
        if choice in subjects:
            return subjects[choice]
        else:
            print("❗ Invalid selection. Please choose a number from 1 to 5.")


def countdown(seconds=3):
    print("\n🕒 Get ready!")
    for i in range(seconds, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)
    print("🚀 Go!\n")


if __name__ == "__main__":
    main()
