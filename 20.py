#20.	Keep only numbers divisible by 3.
tuple_nums = (1,2,3,4,5,6,7,8,9)
divisible_3 = filter(lambda x : x % 3 == 0, tuple_nums)
print(tuple(divisible_3))