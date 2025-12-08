#4.	Square every number in a tuple using map().
numbers = (2,4,6,8,10,12)
squared_tuple = map(lambda x:x * x, numbers)
print(tuple(squared_tuple))
