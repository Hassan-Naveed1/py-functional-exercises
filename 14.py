#14.Convert a list of numbers into their last digits using map().
numbers = [123, 45, 678, 92411]
num_last = map(lambda x : x % 10 , numbers)
print(tuple(num_last))