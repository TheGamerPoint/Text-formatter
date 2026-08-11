# This autoclicker belongs to TheGamerPoint
# https://github.com/TheGamerPoint/Text-formatter
# If you have any bugs you want to report DM thegamerpoint on discord user id: 1076614414276493362

# Don't edit below this line unless you know what your doing
import keyboard, os

def clear():
    print(" ")
    print("Press enter to clear: ")
    keyboard.wait('enter')
    os.system('cls')

def enter():
    print("Press enter to continue")
    keyboard.wait('enter')

while True:
    print("1. Upper-case")
    print("2. Lower-case")
    print("3. Title-case")
    print("4. Sentence-case")
    print("5. Close")
    print(" ")
    raw = input("Enter a number: ").strip()

    if not raw:
        os.system('cls')
        continue

    try:
        number = int(raw)
        os.system('cls')
    except ValueError:
        print("Please enter a whole number (no letters or decimals).")
        enter()
        os.system("cls")
        continue

    if number < 1 or number > 5:
        print("Please enter a number from 1 to 5!")
        enter()
        os.system("cls")
        continue
    if number == 5:
        raise SystemExit("Closing program")
    text = input("Enter text: ")
    print(" ")
    

    if number == 1:
        print(text.upper())
        clear()
    elif number == 2:
        print(text.lower())
        clear()
    elif number == 3:
        print(text.title())
        clear()
    elif number == 4:
        result = ""
        capitalize_next = True

        for char in text:
            if capitalize_next and char.isalpha():
                result += char.upper()
                capitalize_next = False
            else:
                result += char

            if char in ".!?":
                capitalize_next = True
        print(result)
        clear()
