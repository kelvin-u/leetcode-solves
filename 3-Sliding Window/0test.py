s1 = "ab"
s2 = "eidbaooo"

# two hashmaps and check if they are equal

s1_charSet = {}
s2_charSet = {}

# hash map of s1 and s2
for i in range(len(s1)):
    s1_charSet[s1[i]] = s1_charSet.get(s1[i], 0) + 1
    s2_charSet[s2[i]] = s2_charSet.get(s2[i], 0) + 1
    
# check if they are equal before sliding the window
if s1_charSet == s2_charSet:
    print('true')

# sliding window through s2 to check if s1 exists in s2
l = 0 
 
for r in range(len(s1), len(s2)):
    s2_charSet[s2[r]] = s2_charSet.get(s2[r], 0) + 1
    s2_charSet[s2[l]] -= 1
    
    print(s2_charSet)
    if s2_charSet[s2[l]] == 0:
        del s2_charSet[s2[l]]
    l += 1
    
    if s1_charSet == s2_charSet:
        print('true')

    


