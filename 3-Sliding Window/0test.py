s1 = "ab"
s2 = "eidbaooo"

# two hashmaps and if they are equal we good

s1_charMap = {}
s2_charMap = {}

# build hashmap for the length in s1
for i in range(len(s1)):
    s1_charMap[s1[i]] = s1_charMap.get(s1[i], 0) + 1
    s2_charMap[s2[i]] = s2_charMap.get(s2[i], 0) + 1

l = 0

if s1_charMap == s2_charMap:
    print('done1')

for r in range(len(s1), len(s2)):
    s2_charMap[s2[r]] = s2_charMap.get(s2[r], 0) + 1
    s2_charMap[s2[l]] -= 1

    if s2_charMap[s2[l]] == 0:
        del s2_charMap[s2[l]]
    l += 1

    if s1_charMap == s2_charMap:
        print('done1')
print('not done')


