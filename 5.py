#5.	Convert all numbers in a list to their negative values using map().
list = [1,2,3,4,5,6,7,8,9,10]
negative_list = map(lambda x: -x, list)
print(tuple(negative_list))