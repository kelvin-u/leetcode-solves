s = "abcabcbb"

l = 0
charSet = set()
result = 0

for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[r])
        l += 1
    charSet.add(s[r])
    result = max(result, r-l+1)
print(result)

