s = "([])"

def isValid(self, s: str) -> bool:
    stack = []
    bracket_map = {"(": ")", "[": "]", "{": "}"}

    for bracket in s:
        if bracket in bracket_map:
            stack.append(bracket)
        else:
            if not stack:
                return False
            # stack is empty
            top = stack.pop()
            if bracket_map[top] != bracket:
                return False
    return len(stack) == 0
