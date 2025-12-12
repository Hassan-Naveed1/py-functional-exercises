#28.	Keep only students who scored above 60.
student_grades = [50,60,70,100,30,50,60,70,61,59]
greater_then_60 = filter(lambda x : x > 60, student_grades)
print(tuple(greater_then_60))