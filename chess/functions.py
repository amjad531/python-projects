class bcolors:
    GRAY = '\033[90m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

def print_colored_text(text, color,end):
    print(color + text + bcolors.ENDC, end = end)

myboard = {
    "a": ['!','w_R','w_P','O','O','O','O','b_P','b_R'],
    "b": ['!','w_N','w_P','O','O','O','O','b_P','b_N'],
    "c": ['!','w_B','w_P','O','O','O','O','b_P','b_B'],
    "d": ['!','w_Q','w_P','O','O','O','O','b_P','b_Q'],
    "e": ['!','w_K','w_P','O','O','O','O','b_P','b_K'],
    "f": ['!','w_B','w_P','O','O','O','O','b_P','b_B'],
    "g": ['!','w_N','w_P','O','O','O','O','b_P','b_N'],
    "h": ['!','w_R','w_P','O','O','O','O','b_P','b_R']
}

def print_board(board = myboard):
    print("-" * 73)
    for i in range(1,9):
        print("|",end = "\t")
        for key in board.keys():
            if board[key][i][0] == 'w':
                print_colored_text(board[key][i][-1], bcolors.WHITE,"\t")
            elif board[key][i][0] == 'b':
                print_colored_text(board[key][i][-1],bcolors.GRAY,"\t")
            else:
                print_colored_text(board[key][i],bcolors.BLUE, end = "\t")
        print(f"| {i}")
    print("-" * 73)
    print(end ="\t")
    for key in board.keys():
        print(key, end = "\t")

        


        



