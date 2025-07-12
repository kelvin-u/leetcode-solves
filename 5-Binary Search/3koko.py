import math
piles = [3, 6, 7, 11]
h = 8


def minEatingSpeed(piles, h) -> int:
    l = 1
    r = max(piles)
    result = r

    while l <= r:
        k = (l + r) // 2

        total_time = 0 

        for p in piles:
            total_time += math.ceil(p/k)

            if total_time <= h:
                result = k 
                r = k - 1
            else:
                l = k + 1
    return result
        
