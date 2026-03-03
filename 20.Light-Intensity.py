# InfoSys SP Coding Qn #1
'''
There are N street lamps, each has an intensity value.

You are also given a number K.
We check lamps sequentially from left to right.

If the difference between current lamp and previous lamp’s intensity
abs(intensity[i] - intensity[i-1]) <= K
→ Both can stay ON (current lamp becomes ACTIVE).

If the difference is greater than K
→ The current lamp will overpower, and only it remains active, meaning previous active lamps get deactivated.

Finally, return the total glow after processing all lamps.

Stepwise:

- 4 → active

- 5 (|5-4| <= 2) → active → [4,5]

- 7 (|7-5| <= 2) → active → [4,5,7]

- 12 (|12-7| > 2) → overpower → [12]

- 10 (|10-12| <= 2) → active → [12,10]

👉 Final output: [12, 10] = 12 + 10 = 22
'''

def finalGlow(lamps, k):
    active = [lamps[0]]  # first lamp always active

    for i in range(1, len(lamps)):
        if abs(lamps[i] - active[-1]) <= k:
            active.append(lamps[i])
        else:
            active = [lamps[i]]
    
    # return total glow (sum of active intensities)
    return sum(active)


# Example
lamps = [4, 5, 7, 12, 10]

k = 2
print(finalGlow(lamps, k))  # Output: 22 (12+10)