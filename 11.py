#11.	Add 5 to only the first 10 elements of a tuple using map().
tuple_num = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
add_5_first_10 = map(lambda pair: pair[1] + 5 if pair[0] < 10 else pair[1], enumerate(tuple_num))
result = tuple(add_5_first_10)
print(result)