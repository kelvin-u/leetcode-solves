s = "ABABAA"
k = 2

l = 0 
length = 0 
charSet = {}

for r in range(len(s)):
    charSet[s[r]] = charSet.get(s[r], 0) + 1

    while (r-l+1) - max(charSet.values()) > k:
        charSet[s[l]] -= 1
        l += 1

    length = max(length, r - l + 1)