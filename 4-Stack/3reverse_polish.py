tokens = ["2","1","-","3","*"]
output = 9

def evalRPN(self, tokens) -> int:
    stack = []
    
    for num in tokens:
        if num == "+":
            stack.append((stack.pop() + stack.pop()))
        elif num == "-":
            a = (stack.pop()), b = (stack.pop())
            stack.append(b-a)
        elif num == "*":
            stack.append(stack.pop() * stack.pop())
        elif num == "/":
            a = stack.pop(), b = stack.pop()
            stack.append(b/a)
        else:
            stack.append(int(num))
    return stack[0]