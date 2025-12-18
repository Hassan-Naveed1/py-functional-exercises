#37.	Filter multiples of 4 and then subtract 1 from each.
numbers = [20,5,4,40,30,20,10]
multiples_of_4 = map(lambda x : x - 1 , filter(lambda x : x % 4 == 0,numbers))
print(tuple(multiples_of_4))