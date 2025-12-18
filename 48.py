#48.	Select values divisible by 5, double them, and calculate total product.
from functools import reduce
values = [5,6,7,8,9,10,15,20,21,22,15,30]
values_divisible5 = reduce(lambda total, x : total + x,
                           map(lambda x : x + x,
                               filter(lambda x : x % 5 == 0, values)))
print(values_divisible5)