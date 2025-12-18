#36.	Select temperatures below 0 and convert them to Fahrenheit.
temperatures = [10,20,30,40,50,-2,-5,-7,-11,20]
temperatures_below0 = map(lambda x : (x * 9/5) + 32, filter(lambda x : x < 0 , temperatures))
print(tuple(temperatures_below0))