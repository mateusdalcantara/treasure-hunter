print(r"""
        /\____;;___
       | /         /
       `. ())oo() .
        |\(%()*^^()^
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
    %%%%
""")
print("Welcome to the treasure hunter game!")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go? "
                "Type  'left' or 'right'.").lower()

if choice1 == "right":
    choice2 = input("You've come to a lake. "
                    "You need to across this lake. "
                    "Type \"wait\" to wait for a boat or "
                    "\"swim\" to swim across.").lower()
    if choice2 == "wait":
        choice3 = input("You across the lake safe. When you arrive, you decided to keep walk toward the flores,"
              "there you found a house with 3 doors. One is blue, one is yellow and one red."
              " Which door you choose to open?").lower()

        if choice3 == "blue":
            print("It's a room full of magic water, you got drowned. Game Over.")
        elif choice3 == "yellow":
            print("It's a room with fungus, you got a bad sick! Game over.")
        elif choice3 == "red":
            print("Well done! You found a chest full of gold coin!")
        else:
            print("You give up, your choice. Game over.")

    else:
        print("You got attacked by a crocodile. Game over.")
else:
    print("You fell in to a hole and broke your pinky... Ouch. Game over")