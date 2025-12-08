#6.	Add 10 to every odd-indexed position value using map().
list = [1,2,3,4,5,6,7,8,9,10]
odd_indexed_10 = map(lambda pair: pair[1] + 10 if pair[0] % 2 != 0 else pair[1], enumerate(list))
print(tuple(odd_indexed_10))