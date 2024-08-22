import random

components = ['🪨', '📃', '✂️']

# User starts the game
ch = input("Start Game (Y/N) : ")
if ch.lower() == 'y':
    ch = 1
else:
    ch = 0

while ch == 1:
    sys_option = random.choice(components)
    print("--'🪨' Rock '📃' Paper '✂️' Scissors--")
    print("---Game Started---")
    print(f"My turn: {sys_option}")
    
    user_option = input("Choose your option:\n'🪨' - R\n'📃' - P\n'✂️' - S\nYour Turn: ").upper()
    if user_option == 'R':
        user_option = '🪨'
    elif user_option == 'P':
        user_option = '📃'
    elif user_option == 'S':
        user_option = '✂️'
    else:
        print("Invalid choice, please try again.")
        continue
    
    # Checking user input
    if (sys_option == '✂️' and user_option == '🪨') or \
       (sys_option == '📃' and user_option == '✂️') or \
       (sys_option == '🪨' and user_option == '📃'):
        print("Congrats, You Won!")
    elif sys_option == user_option:
        print("It's a Draw!")
    else:
        print("You Lose the Game.")
    
    # Asking to exit or continue the game
    ch = input("Do You Want to continue (Y/N) : ").lower()
    if ch == 'y':
        ch = 1
    else:
        ch = 0

# Rules of the Game
'''
🪨 wins against ✂️
✂️ wins against 📃
📃 wins against 🪨
'''
