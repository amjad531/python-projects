import random
small_letters = "abcdefghijklmnopqrstuvwxyz"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_letters = "!@#$%^&*_-+=/?.><,`~"
numbers = "0123456789"
password = ""
players_list = []

len_of_password = input("choose the length of your password: (1-9)\n")
small_letters_choice = input("do you want the password to contain small_letters? y/n\n")
capital_letters_choice = input("do you want the password to contain capital_letters? y/n\n")
special_letters_choice = input("do you want the password to contain special_letters y/n\n")
numbers_choice = input("do you want the password to contain numbers? y/n\n")


if small_letters_choice == 'y':
    players_list.append(small_letters)


if capital_letters_choice == 'y':
    players_list.append(capital_letters)


if special_letters_choice == 'y':
    players_list.append(special_letters)

if numbers_choice == 'y':
    players_list.append(numbers)

if len(players_list) == 0:
    print("sorry, you have to include at least one time of charachters ")
else:
    for num in range(int(len_of_password)):  
        random_number = random.randint(0, len(players_list) - 1)
        character_type = players_list[random_number]
        random_number_letter = random.randint(0, len(character_type) - 1)
        character = character_type[random_number_letter]
        password += character
        num += 1
print(password)

    

 
