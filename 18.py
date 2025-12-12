#18.	Keep only odd numbers from a tuple.
numbers = (1,2,3,4,5,6,7,8,9,10)
odd_only = filter(lambda x : x % 2 != 0, numbers)
print(tuple(odd_only))