#32.	Filter even numbers and then square them.
nums = (1,2,3,4,5,6,7,8,9,10)
square_nums = filter(lambda x : x % 2 == 0, map(lambda x : x ** 2, nums))
print(tuple(square_nums))