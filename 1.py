#1.	Given a tuple of numbers, use map() to double every value.
nums = (1,2,3,4,5,6,7,8,9,10)
double_nums = map(lambda x : x * 2, nums)
print(tuple(double_nums))