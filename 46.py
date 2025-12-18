#46.	Select salaries below 30,000, add a 50,000 bonus, and find total payroll.
from functools import reduce
salaries = [28000,21000,32000,40000,50000,15000,18000]
salaries_below_30 = reduce(lambda total, x : total + x ,
                           map(lambda x : x + 5000, 
                               filter(lambda x : x < 30000, salaries)))
print(salaries_below_30)