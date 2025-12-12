#29. Keep only numbers that are multiples of 5.
nums = [5,10,15,11,24,25,20,30,39,50,100,109]
num_divisible_5 = filter(lambda x : x % 5 == 0, nums)
print(tuple(num_divisible_5))