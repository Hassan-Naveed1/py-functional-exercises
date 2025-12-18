#47.	Filter student marks below 40, add 5 grace marks to each, and calculate the total.
from functools import reduce
marks = [35,45,51,60,75,89,95,90,25,31]
marks_below_40 = reduce(lambda total, x : total + x,
                        map(lambda x : x + 5,
                            filter(lambda x : x < 40,marks)))
print(marks_below_40)