s = "ABABAA"
k = 2


def characterReplacement(s, k):
    l = 0
    length = 0
    charCount = {}
    
    for r in range(len(s)):
        charCount[s[r]] = charCount.get(s[r], 0) + 1

        while (r - l + 1) - max(charCount.values()) > k:
            charCount[s[l]] -= 1
            l += 1
        length = max(length, r - l + 1)

    return length

print(characterReplacement(s, k))
