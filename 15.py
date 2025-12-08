#15.	Convert a list of marks into pass/fail labels using map().
marks = [35, 70, 50, 20]
pass_fail = map(lambda x : "Pass" if x >= 50  else "Fail", marks)
print(tuple(pass_fail))