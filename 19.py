#19.	Filter out all negative numbers from a list.
nums = [1,2,-1,-100,2,4,5,7,-100,-50]
only_negative = filter(lambda x : x < 0, nums)
print(tuple(only_negative))