LETTER_LIST = ['a','b','c','d','e'] 
import json
def load_json(file_directory):
    with open(file_directory,'r') as f:
        mylist = json.load(f)
        return mylist

def print_total_points(mylist):
    total_points = 0
    for item in mylist:
        total_points += item["question_points"]
        
    print(f"the total points are: {total_points}")

def return_total_points(mylist):
    all_points = 0
    for item in mylist:
        all_points += item["question_points"]
    return all_points

def print_dicts(mylist):
    i = 1
    for dict in mylist:
        print('\n')
        print(f"quizz{i}:\n")
        i += 1 
        for key,value in dict.items():
            if key == "answers":
                for key2,value2 in dict["answers"].items():
                    print(f"{key2}: {value2}")
            else:
                print(f"{key}: {value}")

def view(mylist,index=None):
    if index is None:
        print_dicts(mylist)
            
    else:
        print_dicts(mylist[index])
    print("\n")    
    print_total_points(mylist)
    
def filling_dicts(mylist,index = -1):
    total_points = 0
    player_question = input("please enter the question:\n")
    mylist[index]["question"] = player_question

    player_answer_count = int(input("how many answers do you want?\n"))

    letter_player_list = []
    for num in range(player_answer_count):
        letter_player_list.append(LETTER_LIST[num])

    mylist[index]["answers"] = {}
    print("what are the answers?")
    for i in range(player_answer_count):
        player_answer = input(f"{letter_player_list[i]}: ")
        mylist[index]["answers"][letter_player_list[i]] = player_answer

            

    player_correct_answer = input(f"what is the correct answer?({letter_player_list})\n")
    mylist[index]["correct_answer"] = player_correct_answer

    question_points = int(input("how many points do you want to assign to this question?\n"))

    mylist[index]["question_points"] = question_points
    total_points += question_points
    
    view(mylist)
    

def update_question_in_file(mylist,question_directory):
    with open(question_directory,'w') as f:
        json.dump(mylist,f,indent = 4)

def admin_quizz_edit(mylist):
    while True:
        player_choice = input("do you want to add,edit,remove or view a question?\n")

        if player_choice == "add":
            mylist.append({})
            filling_dicts(mylist)
            update_question_in_file(mylist,'questions.json')

        elif player_choice == "edit":
            view(mylist)
            player_input = int(input("which question do you want to edit?\n"))
            edited_quizz_index = player_input - 1
            mylist[edited_quizz_index] = {}
            filling_dicts(edited_quizz_index)
            update_question_in_file(mylist,'questions.json')

        elif player_choice == "remove":
            view(mylist)
            player_input = int(input("which quizz do you want to remove?\n"))
            removed_list = player_input - 1
            mylist.pop(removed_list)
            update_question_in_file(mylist,'questions.json')

        elif player_choice == "view":
            view(mylist)
            
        else:
            break




def get_questions():
    mylist = load_json('questions.json')
    for dict in mylist:
        for key,value in list(dict.items())[:2]:
                if key == "answers":
                    for key,value in dict["answers"].items():
                        print(f"{key}: {value}")
                else:
                    print(key)
                    print(value)
        print("\n")
     



def game_logic(mylist):
    players_points = 0
    print("welcome to Quizzes")
    print_total_points(mylist)
    for item in mylist:
        letter_player_list = []
        print(item["question"])
        for key,value in item["answers"].items():
            print(f"{key}: {value}")
            letter_player_list.append(key)
        player_answer = input(f"please choose your answer, {letter_player_list}\n")
        if player_answer == item["correct_answer"]:
            players_points += item["question_points"]
    print(f"Game over you scored {players_points} out of {return_total_points(mylist)}")
