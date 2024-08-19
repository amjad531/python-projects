#  SOLOUTION 1:

# x = int(input("what is the number which you want to calculate its factorial?\n"))
# s = 1
# if x == 0:
#     print("the answer is 1")
# else:
#     for i in range(1, x + 1):
#         s *= i
#     print(f"the answer is {s}")



#SOLOUTION 2:

def calculate_factorial():
    num = int(input("what is the number for which you want to calculate the factorial?\n"))

    i = 1
    if num == 0 or num == 1:
        print("the answer is 1")
    else:
        for _ in range(0,num):
            i *= num
            num -= 1
        print(f"the answer is {i}")
calculate_factorial()



    

