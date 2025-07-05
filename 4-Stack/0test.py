temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

n = len(temperatures)
stack = []

res = [0] * n
for i, temp in enumerate(temperatures):
    while stack and temperatures(stack[-1]):
        index = stack.pop()
        res[index] = i - index
    stack.append(i)
