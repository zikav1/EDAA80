
# function for calculating average temp without sum() and len()
def calculate_avg_temp(t_list: list[float]) -> float:
    
    # Keep track of the total temperature and days per month 
    total_temp = 0
    days_per_month = 0
    
    for temp in t_list:
        days_per_month += 1
        total_temp += temp
    
    return total_temp / days_per_month




def when_is_spring(t_list: list[float]) -> int:
    first_found = False  # Keep track if we have found the first positive temperature day
    n = 0  # Count how many consecutive days with positive temperatures we have found
    index = -1  # Store the index of the first positive temperature day

    for i, temp in enumerate(t_list):
        if temp > 0:
            if not first_found:
                first_found = True
                index = i
                n = 1
            else:
                n += 1
        else:
            first_found = False
            n = 0
            index = -1

        
        if n == 7:
            return index
    return -1

             
                
    
    
    
    
    
    