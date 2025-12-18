#42.	Select numbers less than 10, add 5 to them, and find their product.
from functools import reduce
nums = [10,5,2,3,9,1,0,6,8,10,20]
nums_less_10 = reduce(lambda product, x : product * x,
                      map(lambda x : x + 5,
                          filter(lambda x : x < 10,nums) ))
print(nums_less_10)