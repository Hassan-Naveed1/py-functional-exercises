#34.	Select numbers greater than 20 and then divide them by 2.
nums = [5,10,15,20,25,30,21,22,23]
nums_greater_20 = filter(lambda x : x > 20 , map(lambda x : x + 2, nums))
print(tuple(nums_greater_20))