#49.	Filter temperatures above 25, convert to Fahrenheit, and find average.
from functools import reduce
temperatures = [10,20,15,26,30,35,41,42,16,18,4]
temps_f = map(lambda x : (x* 9/5) +32,
              filter(lambda x: x > 25, temperatures))



total = reduce(lambda a,b : a+b, temps_f)

print("The total of the list in farenheit is: ",total)

count = 0
for x in temperatures:
    if x > 25:
        count = count + 1

average = total / count 
print(average)