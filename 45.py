#45.	Filter prices above 100, apply 20% tax, and calculate final total cost.
from functools import reduce
nums = [120,101,99,89,10,20,50,150]
prices_above_100_20_tax = reduce(lambda total, x : total + x,
                                 map(lambda x : x + (x*0.20),
                                     filter(lambda x: x > 100, nums)))
print(prices_above_100_20_tax)