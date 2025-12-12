#17.	Keep only even numbers from a list using filter().
numbers = [1,2,3,4,5,6,7,8,9,10]
only_even = filter(lambda x : x % 2 == 0, numbers)
print(tuple(only_even))