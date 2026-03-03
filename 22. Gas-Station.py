#Accenture Coding Qn.
'''
You are given two arrays:

-> fuel[i] → amount of fuel available at petrol pump i

-> cost[i] → fuel required to travel from pump i to (i + 1)

The pumps are arranged in a circular manner.
Return the starting petrol pump index from where the car can complete the circular tour.

If it is not possible, return -1.
'''

def canCompleteCircuit(fuel, cost):
    total_tank = 0
    curr_tank = 0
    start_index = 0

    for i in range(len(fuel)):
        total_tank += fuel[i] - cost[i]
        curr_tank += fuel[i] - cost[i]

        # If current tank becomes negative
        if curr_tank < 0:
            start_index = i + 1
            curr_tank = 0

    return start_index if total_tank >= 0 else -1


# Example
fuel = [4, 6, 7, 4]
cost = [6, 5, 3, 5]
print(canCompleteCircuit(fuel, cost))