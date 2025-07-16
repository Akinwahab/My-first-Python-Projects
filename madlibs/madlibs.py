import time
import random


def Eid_madlib():
    adjective1 = input("Enter an adjective: ")
    family_member = input("Enter a family member: ")
    clothing = input("Enter a type of clothing: ")
    mosque_name = input("Enter a mosque name: ")
    number = input("Enter a number: ")
    gift = input("Enter a gift: ")
    snack = input("Enter a snack: ")
    drink = input("Enter a drink: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")
    islamic_phrase = input("Enter an Islamic phrase (e.g., Takbir): ")

    madlib = f"""
    🎉 Eid Celebration 🎉

    Eid morning was so {adjective1}! I woke up early and hugged my {family_member}, then wore my best {clothing}. 
    We went to {mosque_name} to pray the Eid salah with {number} other people.

    After salah, everyone said "{islamic_phrase}" loudly! I got a {gift} from my uncle and ate {snack} with {drink}.

    Later in the day, we visited {place} to celebrate more. I felt so {emotion} and thankful for the blessings of Eid.
    """

    print(madlib)


def Hajj_Madlib():
    transport = input("Enter a mode of transportation: ")
    adjective1 = input("Enter an adjective: ")
    emotion1 = input("Enter an emotion: ")
    ritual = input("Enter a ritual of Hajj (e.g., Tawaf): ")
    animal = input("Enter an animal: ")
    dua = input("Enter a dua/request: ")
    item = input("Enter an item you would pack: ")
    food = input("Enter a type of food: ")
    adjective2 = input("Enter another adjective: ")
    emotion2 = input("Enter another emotion: ")

    madlib = f"""
    🕋 Journey to Makkah 🕋

    I traveled to Makkah by {transport}. The journey was long but very {adjective1}. 
    I felt so {emotion1} when I first saw the Kaaba.

    We performed {ritual}, and saw people from all over the world—even someone walking with a {animal}!

    I made dua for {dua}, and thanked Allah for the chance to be here. I packed my {item}, ate some {food}, 
    and prepared for the next day of worship. It was truly a {adjective2} journey that made me feel {emotion2}.
    """

    print(madlib)


def Ramadan_madlib():
    time = input("Enter a time (e.g., 4:30am): ")
    family_member = input("Enter a family member: ")
    food_item = input("Enter a food item: ")
    drink = input("Enter a drink: ")
    islamic_phrase = input("Enter an Islamic phrase (e.g., Bismillah): ")
    snack = input("Enter a snack: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    surah_name = input("Enter the name of a Surah: ")
    type_of_dhikr = input("Enter a type of dhikr (e.g., tasbih): ")
    fruit = input("Enter a fruit: ")
    main_dish = input("Enter a main dish: ")
    dessert = input("Enter a dessert: ")
    dua = input("Enter a dua or something you would ask Allah for: ")

    madlib = f"""
    🌙 Ramadan Adventure 🌙

    During the blessed month of Ramadan, I wake up at {time} to eat suhoor with my {family_member}. 
    We had {food_item} and {drink}. I made niyyah to fast and said “{islamic_phrase}”.

    At school, my classmates were eating {snack}, but I stayed strong. I kept my mouth {adjective1} and 
    my heart {adjective2}. I spent my break reading Surah {surah_name} and making {type_of_dhikr}.

    At iftar, we broke our fast with {fruit}, then ate {main_dish} and enjoyed some {dessert}. 
    Before bed, I made this dua: "{dua}".
    """

    print(madlib)


def Masjid_madlib():
    adjective1 = input("Enter an adjective: ")
    day_of_the_week = input("Enter a day of the week: ")
    family_member = input("Enter a family member: ")
    piece_of_clothing = input("Enter a piece of clothing: ")
    fav_obj = input("Enter an object: ")
    person_name = input("Enter a person's name: ")
    number = input("Enter a number: ")
    name_of_salah = input("Enter the name of a salah: ")
    title_of_islamic_figure = input("Enter the title of an Islamic figure: ")
    islamic_topic = input("Enter an Islamic topic: ")
    adjective2 = input("Enter another adjective: ")
    surah_name = input("Enter the name of a Surah: ")
    beverage = input("Enter a beverage: ")
    food_item = input("Enter a food item: ")
    emotion = input("Enter an emotion: ")
    adjective3 = input("Enter another adjective: ")

    madlib = f"""
    🕌 A Day in the Masjid 🕌

    Today, I woke up feeling very {adjective1} because it was {day_of_the_week}—the day I go to the masjid 
    with my {family_member}. I wore my favorite {piece_of_clothing} and grabbed my {fav_obj} before heading out.

    At the masjid, I met my friend {person_name}. We performed {number} rak’ahs of {name_of_salah}, and 
    afterwards, we listened to the {title_of_islamic_figure} give a {adjective2} khutbah about {islamic_topic}.

    After salah, we ate {food_item}, drank {beverage}, and recited Surah {surah_name} together. 
    I felt so {emotion} and thankful to Allah for such a {adjective3} day.
    """
    print(madlib)


def main():
    madlibs = [Ramadan_madlib, Eid_madlib, Hajj_Madlib, Masjid_madlib]
    print("Welcome to the Islamic Madlib Generator!")
    print("Choose a madlib to create:")
    for i, madlib in enumerate(madlibs, 1):
        print(f"{i}. {madlib.__name__}")
    print("Press Enter to randomly pick a madlib.")
    print("Type 'exit' to quit the program.")
    choice = input("Enter the number of your choice: ")
    if choice.lower() == "exit":
        print("Thank you for using the Islamic Madlib Generator! Goodbye!")
        return
    elif choice == "":
        madlib = random.choice(madlibs)
        print(f"\nGenerating your random madlib: {madlib.__name__}...\n")
        time.sleep(1)
        madlib()
    elif choice.isdigit() and 1 <= int(choice) <= len(madlibs):
        print(f"\nGenerating your {madlibs[int(choice) - 1].__name__}...\n")
        time.sleep(1)
        madlibs[int(choice) - 1]()
    else:
        print("Invalid choice. Please run the program again and select a valid option.")
while True:
    main()
    again = input("\nWould you like to try another Madlib? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! See you next time insha’Allah!")
        break

if __name__ == "__main__":
    main()
