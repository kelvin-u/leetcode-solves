s = "pwwkew"

def lengthOfLongestSubstring(s):
    longestSet = set()
    
    l = 0
    result = 0
    
    for r in range(len(s)):
        # if in substring
        while s[r] in longestSet:
            longestSet.remove(s[l]) # remove from the left
            l += 1
        longestSet.add(s[r])
        result = max(result,r-l+1)
    return result

lengthOfLongestSubstring(s)