s = "ABABAA"
k = 2


def characterReplacement(s, k):
    l = 0
    length = 0
    charCount = {}
    
    for r in range(len(s)):
        # frequency count of the string
        charCount[s[r]] = charCount.get(s[r], 0) + 1

        # while the window size - the highest count char > k we need to adjust the window
        while (r - l + 1) - max(charCount.values()) > k:
            # remove the frequency from the left then update the pointer
            charCount[s[l]] -= 1
            l += 1
        length = max(length, r - l + 1)

    return length

print(characterReplacement(s, k))
