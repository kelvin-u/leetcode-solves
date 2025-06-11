s = "A man, a plan, a canal: Panama"
# "amanaplanacanalpanama" -> true


def isPalindrome(s):
    # two pointers
    l = 0
    r = len(s) - 1

    while l < r:
        # case 1 left pointer is NOT at a alpha numeric char (a-z) (0-9) move it till it is
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        # case 2 not the same
        while s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


print(isPalindrome(s))
