s = "ADOBECODEBANC"
t = "aaaab"


def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""

    t_charCount = {}
    s_window = {}

    # t charcount

    for i in range(len(t)):
        t_charCount[t[i]] = t_charCount.get(t[i], 0) + 1

    have = 0
    need = len(t_charCount)
    res, resLen = [-1, -1], float("infinity")

    l = 0

    for r in range(len(s)):
        s_window[s[r]] = s_window.get(s[r], 0) + 1

        if s[r] in t_charCount and s_window[s[r]] == t_charCount[s[r]]:
            have += 1

        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            # pop from the left of our window
            s_window[s[l]] -= 1
            if s[l] in t_charCount and s_window[s[l]] < t_charCount[s[l]]:
                have -= 1
            l += 1
        l, r = res
    return s[l : r + 1] if resLen != float("infinity") else ""


print(minWindow(s, t))
