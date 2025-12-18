#41.	Filter numbers greater than 10, double them, and find their total sum.
from functools import reduce
nums = [10,20,30,40,5,6,7,10,11,12,15,16]

filter_nums = reduce(lambda total, x : total + x, 
    map(lambda x : x + x,
        filter(lambda x : x > 10, nums) 
    )
)

print(filter_nums)