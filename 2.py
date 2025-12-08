#2.	Add 3 to every number in a list using map().
nums = [3,6,9,12,15,18,21,24,27,30]
nums_3 = map(lambda x:x+3, nums)
print(tuple(nums_3))