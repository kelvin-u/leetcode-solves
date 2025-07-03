s1 = "ab"
s2 = "eeidbaooo"

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_charCount = {}
    s2_charCount = {}

    for i in range(len(s1)):
        s1_charCount[s1[i]] = s1_charCount.get(s1[i], 0) + 1
        s2_charCount[s2[i]] = s2_charCount.get(s2[i], 0) + 1

    if s1_charCount == s2_charCount:
        return True

    l = 0
    for r in range(len(s1), len(s2)):
        s2_charCount[s2[r]] = 1 + s2_charCount.get(s2[r], 0)
        s2_charCount[s2[l]] -= 1

        if s2_charCount[s2[l]] == 0:
            del s2_charCount[s2[l]]

        l += 1

        if s1_charCount == s2_charCount:
            return True

    return False