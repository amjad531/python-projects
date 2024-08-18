my_str = "welcomeemoclew"
# mylist1 = []
# mylist2 = []
# if len(my_str) % 2 != 0:
#     print("False")
# else:
#     mid_index = int(len(my_str) / 2)
#     for letter in my_str[:mid_index]:
#         mylist1.append(letter)
#     for letter in my_str[mid_index:]:
#         mylist2.append(letter)
#     mylist2.reverse()
#     print(mylist1)
#     print(mylist2)

#     if mylist1 == mylist2:
#         print("True")
#     else:
#         print("False")
if len(my_str) % 2 != 0:
    print("False")
else:
    mid_index = len(my_str) // 2
    mylist1 = list(my_str[:mid_index])
    mylist2 = list(my_str[mid_index:])
    mylist2.reverse()
    if mylist1 == mylist2:
        print("True")
    else:
        print("False")

