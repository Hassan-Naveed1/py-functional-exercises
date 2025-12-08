#12.	Multiply every number in a list by its index using map().
nums = (1,2,3,4,5,6,7,8,9,10)
multiply_tuple = map(lambda pair : pair[0] * pair[1], enumerate(nums))
print(tuple(multiply_tuple))

