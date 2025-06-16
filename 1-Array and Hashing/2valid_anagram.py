# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

s = "anagram"
t = "nagaram"


def isAnagram(s, t):
    letter_count = {}
    for char in s:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    for char in t:
        if char in letter_count:
            letter_count[char] -= 1
        else:
            letter_count[char] = 1

    for value in letter_count.values():
        if value != 0:
            return False
    return True

print(isAnagram(s, t))
