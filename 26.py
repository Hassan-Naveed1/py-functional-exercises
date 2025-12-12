#26.	Keep only values between 10 and 20 (inclusive).
nums = (20,10,30,40,15,30,11,19,21,9,8,20)
between_10_20 = filter(lambda x : x >= 10 and x <= 20,nums)
print(tuple(between_10_20))