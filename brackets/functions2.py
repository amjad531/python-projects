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

def reverse(bracket):
    if bracket == '(':
        return ')'
    elif bracket == '[':
        return ']'
    elif bracket == '{':
        return '}'
    elif bracket == '<':
        return '>'
        

