def does_match(bracket1,bracket2):
    if (bracket1 == '[' and bracket2 == ']') or (bracket1 == '(' and bracket2 == ')') or (bracket1 == '{' and bracket2 == '}') or (bracket1 == '<' and bracket2 == '>'):
        return True
    else:
        return False

def isopen(bracket):
    if bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<':
        return True
    else:
        return False


s = "<[({)]>"
mylist = []
for item in s:
    if isopen(item):
        mylist.append(item)
        print(mylist)
    else:
        if len(mylist) == 0:  
            print("unbalanced")
            exit(0)
        else:
            x = mylist.pop()
            if does_match(x,item):
                print(mylist)
            else:
                print("unbalanced")
                exit(0)
                
if len(mylist) == 0:
    print("balanced")
else:
    print("unbalanced")

