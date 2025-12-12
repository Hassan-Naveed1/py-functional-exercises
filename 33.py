#33.	Filter odd numbers and then cube them.
nums = (1,2,3,4,5,6,7,8,9,10)
filter_odd_nums = map(lambda x : x ** 3, filter(lambda x : x % 2 != 0, nums))
print(tuple(filter_odd_nums))