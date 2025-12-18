#40. Select marks greater than or equal to 50 and convert each of them into the string "Pass"

grades = [30,51,69,29,70,99,100,41,50,78,98]
passing_grades = map(lambda x : "Pass", filter(lambda x : x >= 50,grades) )
print(tuple(passing_grades))