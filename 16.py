#16.	From a tuple of numbers, keep only values less than 10.
numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
filtered_tuple = filter(lambda x : x < 10, numbers)
print(tuple(filtered_tuple))