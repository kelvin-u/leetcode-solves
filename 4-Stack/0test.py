temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

result = [0] * len(temperatures)
stack = []

for i, temp in enumerate(temperatures):
    while stack and temperatures[stack[-1]] < temp:
        index = stack.pop()
        result[index] = i - index

    stack.append(i)