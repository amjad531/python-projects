players_points = 0
total_points = 0
mylist = [
    {
        "question": "What is 1+1",
        "answer":{
            'a':"6",
            'b':"5",
            'c':"2",
            'd':"3",
        },
        "correct_answer":'c',
        "question_points": 100

    },
    {
        "question": "What is 11+11",
        "answer":{
            'a':"66",
            'b':"55",
            'c':"33",
            'd':"22",
        },
        "correct_answer":'d',
        "question_points": 200
    },
    {
        "question": "What is 9+9",
        "answer":{
            'a':"18",
            'b':"3",
            'c':"4",
            'd':"35",
        },
        "correct_answer":'a',
        "question_points": 300
    }     
]
for dict in mylist:
    answer_list = []
    total_points += dict["question_points"]
    print(dict["question"])
    for key in dict["answer"].keys():
        print(f"{key}: {dict["answer"][key]}")
        answer_list.append(key)
    answer_list = ",".join(answer_list)
    player_answer = input(f"Choose your answer: {answer_list}\n")
    if player_answer == dict["correct_answer"]:
        players_points += dict["question_points"]

print(f"you scored {players_points} out of {total_points}")
print("thanks for playing")
