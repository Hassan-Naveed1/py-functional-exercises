#8.	Convert a list of integers to strings using map().
list_integers = [1,2,3,4,5,6,7,8,9,10]
list_string = map(lambda x: str(x),list_integers)
print(tuple(list_string))