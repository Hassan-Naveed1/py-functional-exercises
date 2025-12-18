#38.	Select numbers ending in 0 and multiply them by 10.
numbers = [200,35,350,19,21,20,210,410,0]
numbers_ending_0 = map(lambda x : x * 10, filter(lambda x: x % 10 == 0, numbers))
print(tuple(numbers_ending_0))