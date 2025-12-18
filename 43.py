#43.	Filter even numbers, square them, and find the total sum.
from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]
filter_even = reduce(lambda sum, x : sum + x,
                     map(lambda x : x ** 2, 
                         filter(lambda x : x % 2 == 0, nums)) )
print(filter_even)