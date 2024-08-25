import random

print("--- 🛠️ Password Generator ---")  # Displaying the title
user_mode = input("🔍 Select Mode (Simple - S or Advanced - A): ").lower()  # Asking user to select mode
password = ''

if user_mode == 's':
    print("----🟢 Simple mode selected ----")  # Simple mode selected
    user_input = int(input("🔢 How many characters for the password? : "))  # Asking for password length
    char_gen = "1 2 3 4 5 6 7 8 9 0 a b c d e f b h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * () < , > ~ ` / * - + "
    sec_seq = char_gen.split(" ")  # Splitting characters into a list
    for i in range(user_input):
        password += random.choice(sec_seq)  # Randomly selecting characters
    else:
        print(f"🔑 Your password: {password}")  # Displaying the generated password
        print("🤐 Keep it secret and secure!")  # Reminder to keep the password secret

elif user_mode == 'a':
    print("----🔴 Advanced mode selected ----")  # Advanced mode selected
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    small_char = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    capital_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', ',', '>', '~', '', '/', '*', '-', '+']
    
    # Asking for the number of each type of character
    print("🧮 Let's Set Up Your Password")
    user_num = int(input("How many numbers in the password? : "))
    user_small_char = int(input("How many lowercase letters in the password? : "))
    user_capital_char = int(input("How many uppercase letters in the password? : "))
    user_special_char = int(input("How many special characters in the password? : "))
    
    # Generating the password
    print("🎲 Password generation started")
    for i in range(user_num):
        password += str(random.choice(num))
    for i in range(user_small_char):
        password += random.choice(small_char)
    for i in range(user_capital_char):
        password += random.choice(capital_char)
    for i in range(user_special_char):
        password += random.choice(special_char)
    
    # Shuffling the password to ensure randomness
    npass = list(password)
    random.shuffle(npass)
    par_pass = "".join(npass)
    
    print(f"🔑 Your strong password: {par_pass}")  # Displaying the generated password
    print("🤐 Keep it secret and secure!")  # Reminder to keep the password secret
