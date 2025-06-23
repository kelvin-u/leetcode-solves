s = "pwwkew"

def lengthOfLongestSubstring(str):
    longestSet = set()
    
    l = 0
    result = 0
    
    for r in range(len(str)):
        # if in substring
        while str[r] in longestSet:
            longestSet.remove(str[l]) # remove from the left
            l += 1
        longestSet.add(str[r])
        result = max(result,r-l+1)
    return result

lengthOfLongestSubstring(s)