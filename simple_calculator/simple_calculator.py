i = 0
mylist = [0]
result = input("write the equation you wish to calculate: ")
for item in result:
    if item.isdigit():
        if isinstance(mylist[-1], str):
            mylist.append(int(item))
        else:
            mylist[-1] = mylist[-1] * 10 + int(item)

            
    elif item == " ":
        continue
    else:
        mylist.append(item)
    
while i in range(len(mylist)):
    if mylist[i] not in ['*','/']:
        i += 1
    elif mylist[i] == '*':
        mylist[i] = mylist[i - 1] * mylist[i+1]
        mylist.pop(i-1)
        mylist.pop(i)
    elif mylist[i] == '/':
        mylist[i] = mylist[i - 1] / mylist[i+1]
        mylist.pop(i-1)
        mylist.pop(i)
    

i = 1
if mylist[i] == '+':
    mylist[i] = mylist[i - 1] + mylist[i+1]
    mylist.pop(i-1)
    mylist.pop(i)
elif mylist[i] == '-':
    mylist[i] = mylist[i - 1] - mylist[i+1]
    mylist.pop(i-1)
    mylist.pop(i)

result = mylist[0]
print(result)


