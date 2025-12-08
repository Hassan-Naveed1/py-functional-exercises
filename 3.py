#3.	Convert a list of temperatures from Celsius to Fahrenheit using map().
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = map(lambda x:x * 9/5 + 32, celsius_temps)
print(tuple(fahrenheit_temps))