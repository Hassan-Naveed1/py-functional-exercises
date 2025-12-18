#50. From a list of numbers, select values greater than 10, square them, and calculate their total sum
from functools import reduce
nums = [12,10,9,9,10,20,50,15]
values_greater_10 = reduce(lambda sum , x: sum + x,
                           map(lambda x : x ** 2,
                               filter(lambda x :x > 10,nums)))
print(values_greater_10)
