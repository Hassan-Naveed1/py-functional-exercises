#39.	Filter values between 5 and 15 and then double them.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
filter_between = map(lambda x : x + x ,filter(lambda x : x > 5 and x < 15, numbers))
print(tuple(filter_between))