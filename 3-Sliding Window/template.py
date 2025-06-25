"""
A generic template for dynamic sliding window finding max window length
"""


def longest_window(s, condition):
    l = 0
    max_length = 0
    result = None

    for r in range(s):
        # Expand the window
        # Add s[r] to the current window logic

        # Shrink the window if the condition is violated
        while not condition():
            # Shrink the window from the left
            # Remove nums[l] from the current window logic
            s[l] -= 1
            l += 1

        # Update the result if the current window is larger
        max_length = max(max_length, l - r + 1)

    return result
