def isValid(s: str) -> bool:
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    map = {c: o for o, c in zip(opening, closing)}

    n = len(s)
    if n % 2 == 1: #odd length of parenthese will always have one missing pair at least
        return False

    stack = []

    i  = 0
    while i < n:
        if not stack and s[i] in closing: #stack is empty but current bracket is closing
            return False
        
        if s[i] in opening:
            stack.append(s[i])
        else:
            popped = stack.pop()
            if popped != map[s[i]]:
                return False

        i += 1
    
    return not stack

values = ["()", "()[]{}", "(]", "([])", "([)]"]
ans = [isValid(val) for val in values]
print(ans)