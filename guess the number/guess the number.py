#2- Guess the Number Game: Create a game where the computer randomly selects a number
#  and the user has to guess it. Include features like a number of attempts or a hint system.

import random
print("welcome to guess the number")
while True:
    try:
      range_of_num = int(input("please pick the range of the number\n"))
    except:
      print("invalid input please select a number")
    else:
         break
while True:
    try:
      number_of_attempts = int(input("please pick the number of attempts\n"))
    except:
      print("invalid input please select a number")
    else:
         break
      
attempt_number = 0
comp_choice = random.randint(1,range_of_num)

while True:
    player_choice = int(input("what is your guess\n"))
    if player_choice > comp_choice:
        print("WRONG! your number was bigger than the answer, Try again")
        attempt_number += 1
        
    elif player_choice < comp_choice:
        print("WRONG! your number was smaller than the answer, Try again")
        attempt_number += 1
    
    elif player_choice == comp_choice:
          print("CORRECTTT!!!, you won")
          attempt_number += 1
          print(f"number of attempts: {attempt_number}")
          break
    else:
          print("wrong input please enter a number")

    if attempt_number >= number_of_attempts:
        print("Oops you are out of guesses, hard luck")
        break
    
    

