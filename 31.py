#31.	From a tuple, select numbers less than 10 and then add 5 to them.
nums = (9,2,4,10,200,30,31,25,16,19)
less_than_10 = map(lambda x : x + 5, filter(lambda x : x < 10, nums))
print(tuple(less_than_10))