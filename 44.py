#44.	Select odd numbers, multiply each by 3, and find the total.
from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]
odd_nums = reduce(lambda total, x : total + x ,
                  map(lambda x : x * 3,
                      filter(lambda x : x % 2 != 0, nums)))

print(odd_nums)