def isValid(Parentheses:str) -> bool :
    stack = []
    for s in Parentheses :
        if s == "(" :
            stack.append(")")
        elif s == "{" :
            stack.append("}")
        elif s == "[" :
            stack.append("]")
        elif s not in stack or stack.pop() != s :
            return False
    return not stack