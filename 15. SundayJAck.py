def count_sundays(start_day, total_days):
    days = ["mon""tue""wed""thu""fri""sat""sun"]
    
    # Map start day to its index
    start_index = days.index(start_day.lower())
    
    # Calculate days until the first Sunday
    # If it's Sunday (index 6), first Sunday is day 1. 
    # If Monday (0), first Sunday is day 7.
    days_to_first_sunday = (6 - start_index)
    if days_to_first_sunday < 0:
        days_to_first_sunday += 7
        
    first_sunday = days_to_first_sunday + 1
    
    if first_sunday > total_days:
        return 0
        
    # Count how many Sundays fit in the total days
    count = 1 + (total_days - first_sunday) // 7
    return count

# Test cases
print(count_sundays("wed", 31)) # Output: 4
print(count_sundays("sun", 29)) # Output: 5
