def feedDog(hunger_level, biscuit_size):
    satiDog = 0
    leastHung = min(hunger_level) # sorting algorithm, if using heap sort, the time complexity is O(nlogn)
    leastBis = min(biscuit_size)
    while hunger_level and biscuit_size:
        if leastHung > leastBis:
            biscuit_size.remove(leastBis)    
        else:
            biscuit_size.remove(leastBis)    
            hunger_level.remove(leastHung)
            satiDog = satiDog + 1    
        
        if hunger_level:
            leastHung = min(hunger_level)
        if biscuit_size:
            leastBis = min(biscuit_size)        
    
    return satiDog

print(feedDog([1, 2, 3], [1, 1]))
